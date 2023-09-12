import { useEffect, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { useHistory } from 'react-router-dom'
import { thunkDeletePost, thunkEditPost } from '../../store/post'
import OpenModalButton from "../OpenModalButton"
import ConfirmDeleteModal from "../ConfirmDeleteModal"
import isUrl from 'is-url'
import './post.css'

function PostContainer({ post, location, page, sort }) {
    const edited = post?.edited
    const created = post?.created_at
    const owner = post?.owner
    const community = post?.community
    const sessionUser = useSelector((state) => state.session.user);
    const dispatch = useDispatch()
    const [editMode, setEditMode] = useState(false)
    const [errors, setErrors] = useState({});
    const [title, setTitle] = useState(post?.post_title)
    const [body, setBody] = useState(post?.post_body)
    const [link, setLink] = useState(post?.ext_url)
    const [votes, setVotes] = useState()
    const [userVote, setUserVote] = useState(null)
    const [upvote, setUpvote] = useState('')
    const [downvote, setDownvote] = useState('')
    const [voteCount, setVoteCount] = useState('')
    const [totalVotes, setTotalVotes] = useState(post.numvotes || 0)
    const history = useHistory()

    const time = new Date(created)
    const dispTime = time.toLocaleTimeString("en-US", {
        weekday: 'short',
        day: 'numeric',
        month: 'short',
        year: 'numeric',
        hour: "numeric",
        minute: "numeric",
        hour12: true,
    })

    let shortLink = ''

    if (link?.length > 40) {
        shortLink = link.slice(0, 40) + '...'
    }

    useEffect(() => {
        const getVotes = async () => {
            const res = await fetch(`/api/votes/${post?.id}`)
            const data = await res.json()
            if (data.votes) {
                setVotes(data.votes)
            }
        }
        getVotes()
    }, [post])

    useEffect(() => {
        if (votes?.length) {
            const userVoteObj = votes.find(vote => vote?.user_id === sessionUser?.id);
            setUserVote(userVoteObj?.upvote);
        } else {
            setUserVote(null);
        }
        return function () {
            setUserVote(null)
        }
    }, [votes, sessionUser]);

    useEffect(() => {
        if (userVote) {
            setUpvote('red')
            setVoteCount('red')
            setDownvote('')
        }
        if (userVote === false) {
            setDownvote('blue')
            setVoteCount('blue')
            setUpvote('')
        }
        if (userVote === null) {
            setUpvote('')
            setDownvote('')
            setVoteCount('')
        }
        return function () {
            setUpvote('')
            setDownvote('')
            setVoteCount('')
        }
    }, [userVote, sessionUser])


    const handleDelete = async () => {
        if (sessionUser.id <= 14 && post.id <= 80) {
            window.alert('Demo User cant delete exisiting post. Please create your own.')
        } else {
            await dispatch(thunkDeletePost(post.id, community.id, location, sort, page))
        }
    }

    const handleEdit = async () => {
        setErrors({})
        setEditMode(true)
    }

    const handleCancel = async () => {
        setTitle(post?.post_title)
        setBody(post?.post_body)
        setLink(post?.ext_url)
        setEditMode(false)
    }


    const validateData = () => {
        const errorObj = {};

        if (!title) errorObj.title = "Title is required."
        if (title && title.trim().length === 0) errorObj.title = 'Title cannot be only whitespace'
        if (title && (title.length > 255 || title.length < 10)) errorObj.title = 'Must be between 10 and 255 characters.'

        if (body && body.length > 1000) errorObj.body = 'Must be less than 1000 characters.'

        if (link && !isUrl(link)) { errorObj.url = 'URL not valid!' } else { delete errorObj.url }

        if (Object.keys(errorObj).length > 0) return errorObj
        else return false
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (sessionUser.id <= 14 && post.id <= 80) {
            window.alert('Demo User cant edit exisiting post. Please create your own.')
        } else {

            const newErrors = validateData();

            if (newErrors) return setErrors(newErrors)

            const data = {
                post_title: title,
                post_body: body,
                created_by: sessionUser.id,
                community_id: community.id,
                ext_url: link
            }

            const response = await dispatch(thunkEditPost(community.id, post.id, data, location, page, sort))

            if (response.errors) {
                const serverErrors = {}
                serverErrors.serverErrors = response.errors
                setErrors(serverErrors)
            } else {
                setEditMode(false)
            }
        }
    }

    const handleUpvote = async () => {
        if (!sessionUser) {
            window.alert('Must be logged in to vote!')
            return
        }
        if (downvote) {
            await fetch(`/api/votes/${post.id}/deletevote`)
            await fetch(`/api/votes/${post.id}/addupvote`)
            setTotalVotes(prev => prev + 2)
            setUpvote('red')
            setDownvote('')
            setVoteCount('red')
            return
        }
        if (upvote) {
            await fetch(`/api/votes/${post.id}/deletevote`)
            setTotalVotes(prev => prev - 1)
            setUpvote('')
            setDownvote('')
            setVoteCount('')
        } else {
            await fetch(`/api/votes/${post.id}/addupvote`)
            setTotalVotes(prev => prev + 1)
            setUpvote('red')
            setDownvote('')
            setVoteCount('red')
        }
    }

    const handleDownvote = async () => {
        if (!sessionUser) {
            window.alert('Must be logged in to vote!')
            return
        }
        if (upvote) {
            await fetch(`/api/votes/${post.id}/deletevote`)
            await fetch(`/api/votes/${post.id}/adddownvote`)
            setTotalVotes(prev => prev - 2)
            setUpvote('')
            setDownvote('blue')
            setVoteCount('blue')
            return
        }
        if (downvote) {
            await fetch(`/api/votes/${post.id}/deletevote`)
            setTotalVotes(prev => prev + 1)
            setUpvote('')
            setDownvote('')
            setVoteCount('')
        } else {
            await fetch(`/api/votes/${post.id}/adddownvote`)
            setTotalVotes(prev => prev - 1)
            setUpvote('')
            setDownvote('blue')
            setVoteCount('blue')
        }
    }

    const handlePostRedirect = () => {
        history.push(`/posts/${post.id}`)
    }

    return (
        <div key={post.id} className="post-container">

            <div className='post-votes'>
                <div className={`vote-arrow-container vote-up ${upvote}`} onClick={handleUpvote}><i className="fa-solid fa-arrow-up" /></div>
                <span className={voteCount}><small>{totalVotes}</small></span>
                <div className={`vote-arrow-container vote-down ${downvote}`} onClick={handleDownvote}><i className="fa-solid fa-arrow-down" /></div>
            </div>


            <div className='post-content' onClick={handlePostRedirect}>
                {!editMode ? <>
                    <div className='posted-by-container'><small><a href={`/communities/${community.id}`}>{<img id='posted-by-small-pic' src={community.logo_pic} alt='Community Logo Pic' />} {community.name}</a> • <span id='post-info'>Posted by {<img id='posted-by-small-pic' src={owner.profile_pic} alt='User Profile Pic' />} u/{owner.username} on {dispTime} {edited ? '*edited' : null}</span></small></div>
                    <div id='break-word'>
                        <h4>{title}</h4>
                        <div><small>{body}</small></div>
                    </div></> :

                    <div className='edit-buttons'>
                        <label htmlFor='title'>Post Title{errors.title && <span className='errors'>: {errors.title}</span>}</label>
                        <input
                            className='create-form-select'
                            id='edit'
                            name='title'
                            value={title}
                            type="text"
                            onChange={(e) => setTitle(e.target.value)}
                            placeholder='title your post'
                        />
                        <label htmlFor='body'>Post Body{errors.body && <span className='errors'>: {errors.body}</span>}</label>
                        <textarea
                            id='post-input'
                            className='create-form-select'
                            name='body'
                            type="text"
                            value={body}
                            onChange={(e) => setBody(e.target.value)}
                            placeholder='post body...'
                        />
                        <label htmlFor='ext_url'>Image URL/External Link{errors.url && <span className='errors'>: {errors.url}</span>}</label>
                        <input
                            className='create-form-select'
                            id='edit'
                            name='ext_url'
                            type="text"
                            value={link}
                            onChange={(e) => setLink(e.target.value)}
                            placeholder='http://www.yourlink.com.jpg.jpeg.png.gif'
                        />
                    </div>}
                <div className='edit-buttons'>
                    {!editMode && (link?.toLowerCase().endsWith('.jpg') || link?.toLowerCase().endsWith('.jpeg') || link?.toLowerCase().endsWith('.png') || link?.toLowerCase().endsWith('.gif') || link?.toLowerCase().includes('drive.google'))
                        ? <div className='post-image'><img src={link} alt={title}></img></div> : <div><a href={link} target='_blank' rel="noreferrer">{shortLink ? shortLink : link}</a></div>}
                    <div className='edit-buttons' onClick={e=>{e.stopPropagation()}}>
                    {sessionUser?.id === owner.id && editMode ? <button id='editpost' onClick={handleSubmit}>Submit Changes</button> : null}
                    {sessionUser?.id === owner.id && editMode ? <button id='editpost' onClick={handleCancel}>Cancel</button> : null}
                    </div>
                </div>

                <div className='post-footer' onClick={e=>{e.stopPropagation()}}>
                    <div className='comments-display'><i className="fa-regular fa-message" />&nbsp;
                    <span onClick={handlePostRedirect}><small>{post.numcomments || 0} {post.numcomments === 1 ? 'Comment' : 'Comments'}</small></span></div>

                    {sessionUser?.id === owner.id ?
                        <>
                            |<div onClick={handleEdit} className='post-modify-buttons'>Edit Post</div>|
                            <OpenModalButton buttonText={'Delete Post'} modalComponent={<ConfirmDeleteModal title={'Are you sure? Cannot be undone.'} confirmFunc={handleDelete} />} />
                        </>
                        : null}
                </div>


            </div>
        </div>
    )
}

export default PostContainer;
