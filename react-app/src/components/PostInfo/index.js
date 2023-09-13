import { useParams, useHistory } from "react-router-dom";
import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { thunkGetSinglePost } from "../../store/post";
import { thunkGetAllComments, thunkAddComment } from "../../store/comment";
import CommentContainer from "../Comment";
import PostContainer from "../Post";
import Loading from "../Loading";
import '../Comment/comment.css'

function PostInfo() {
    const { postId } = useParams()
    const [loaded, setLoaded] = useState(false)
    const [found, setFound] = useState(false)
    const [userComment, setUserComment] = useState('')
    const [errors, setErrors] = useState({})
    const dispatch = useDispatch()
    const history = useHistory()

    const post = useSelector(state => state.posts.singlePost)
    const currentUser = useSelector(state => state.session.user)
    const comments = useSelector(state => state.comments.allComments)


    useEffect(() => {
        const data = async () => {
            const res = await dispatch(thunkGetSinglePost(postId))
            await dispatch(thunkGetAllComments(postId))
            setLoaded(true)
            if (res.id) {
                setFound(true)
            }
        }
        data()

        return function () {
            setLoaded(false)
            setFound(false)
        }
    }, [dispatch, postId])

    useEffect(() => {
        if (userComment.length > 255) {
            setErrors({ 'length': 'Must be under 255 characters' })
        } else {
            setErrors({})
        }
        return function () {
            setErrors({})
        }
    }, [userComment])

    if (!loaded) return <Loading />
    if (!found) return <h2><center>Post not found!</center></h2>

    const handleRedirect = () => {
        history.push(`/communities/${post.community.id}`)
    }


    const handleAddComment = async () => {
        if (!currentUser) {
            window.alert('Must be logged in to comment!')
            return
        }
        if (userComment.length < 1) {
            setErrors({ 'length': 'Must be at least 1 character' })
            return
        }
        const data = {
            'created_by': currentUser.id,
            'post_id': parseInt(postId),
            'comment_body': userComment
        }
        const res = await dispatch(thunkAddComment(data))
        await dispatch(thunkGetSinglePost(postId))
        setUserComment('')

        if (res.errors) {
            setErrors(res.errors)
        }
    }


    return (
        <div className="community-container">
            <div className="post-main-container">
                <PostContainer post={post} location='post-info' />
                <div className="comments-container">
                    <div className="comment-box">
                        {currentUser ? `Comment as ${currentUser.username}` : 'Login to comment'}
                        <textarea id='comment-input' value={userComment} placeholder='Share your thoughts...' onChange={e => setUserComment(e.target.value)}></textarea>
                        <div id='comment-length'>{errors.length && <span className='errors'>{errors.length}</span>}{userComment.length} / 255
                        </div>
                        <div id='comment-button-container'>
                            <button id='add-comment-button' onClick={handleAddComment} disabled={userComment.length > 255 || !userComment.length}>Comment</button>
                        </div>
                    </div>
                    {comments.map(comment => {
                        return (
                            <CommentContainer comment={comment} key={comment.id} />
                        )
                    })}
                </div>
            </div>

            <div className="community-info-container pointer" onClick={handleRedirect}>
                {post.community.banner_pic ? <img id='community-info-banner-pic' src={post.community.banner_pic} alt='community banner pic' /> : null}
                <div className='community-info-contents'>
                    <div id='break-word'>
                        <b>{post.community?.name}</b><br />
                        <img id='community-info-pic' src={post.community?.logo_pic} alt={post.community?.name} />
                        <p>{post.community?.description}</p>
                        <small>Created by: {<img id='posted-by-small-pic' src={post.owner.profile_pic} alt='User Profile Pic' />} u/{post.community.owner?.username}</small>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default PostInfo;
