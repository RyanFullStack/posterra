import { useParams, useHistory } from "react-router-dom";
import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { thunkGetSinglePost } from "../../store/post";
import CommentContainer from "../Comment";
import PostContainer from "../Post";
import Loading from "../Loading";
import '../Comment/comment.css'

function PostInfo() {
    const { postId } = useParams()
    const [loaded, setLoaded] = useState(false)
    const [found, setFound] = useState(false)
    const [comments, setComments] = useState([])
    const dispatch = useDispatch()
    const history = useHistory()

    const post = useSelector(state => state.posts.singlePost)


    useEffect(() => {
        const data = async () => {
            const res = await dispatch(thunkGetSinglePost(postId))
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
        const data = async () => {
            const res = await fetch(`/api/comments/${postId}`)
            const com = await res.json()
            if (com.comments) {
                setComments(com.comments)
            } else setComments([])
        }
        data()
    }, [postId])

    if (!loaded) return <Loading />
    if (!found) return <h2><center>Post not found!</center></h2>

    const handleRedirect = () => {
        history.push(`/communities/${post.community.id}`)
    }

    return (
        <div className="community-container">
            <div className="post-main-container">
                <PostContainer post={post} location='post-info'/>
                <div className="comments-container">
                    {comments.map(comment => {
                        return (
                            <CommentContainer comment={comment} key={comment.id}/>
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
