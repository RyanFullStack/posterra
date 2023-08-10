import { useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { thunkDeletePost, thunkEditPost } from '../../store/post'
import OpenModalButton from "../OpenModalButton";
import ConfirmDeleteModal from "../ConfirmDeleteModal"
import './post.css'

function PostContainer({ post }) {
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

    let shortLink = ''

    if (link?.length > 40) {
        shortLink = link.slice(0, 40) + '...'
    }

    const handleDelete = async () => {
            await dispatch(thunkDeletePost(post.id, community.id))
    }

    const handleEdit = async () => {
        setEditMode(true)
    }

    const handleCancel = async () => {
        setEditMode(false)
    }

    const validateData = () => {
        const errorObj = {};

        if (!title) errorObj.title = "Field is required."
        if (title && (title.length > 255 || title.length < 10)) errorObj.title = 'Must be between 10 and 255 characters.'

        if (body && body.length > 1000) errorObj.body = 'Must be less than 1000 characters.'

        if (Object.keys(errorObj).length > 0) return errorObj
        else return false
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        const newErrors = validateData();

        if (newErrors) return setErrors(newErrors)

        const data = {
            post_title: title,
            post_body: body,
            created_by: sessionUser.id,
            community_id: community.id,
            ext_url: link
        }

        const response = await dispatch(thunkEditPost(community.id, post.id, data))

        if (response.errors) {
            const serverErrors = {}
            serverErrors.serverErrors = response.errors
            setErrors(serverErrors)
        } else {
            setEditMode(false)
        }
    }


    return (
        <div key={post.id} className="post-container">
            {!editMode ? <><div>{title} by u/{owner.username} in p/{community.name} {edited ? '*edited' : null} at {created}</div>
                <div>{body}</div></> :
                <>
                    <label htmlFor='title'>Post Title{errors.title && <span className='errors'>: {errors.title}</span>}</label>
                    <input
                        name='title'
                        value={title}
                        type="text"
                        onChange={(e) => setTitle(e.target.value)}
                        placeholder='title'
                    />
                    <label htmlFor='body'>Post Body{errors.body && <span className='errors'>: {errors.body}</span>}</label>
                    <input
                        name='body'
                        type="text"
                        value={body}
                        onChange={(e) => setBody(e.target.value)}
                        placeholder='body'
                    />
                    <label htmlFor='ext_url'>Image URL/External Link</label>
                    <input
                        name='ext_url'
                        type="text"
                        value={link}
                        onChange={(e) => setLink(e.target.value)}
                        placeholder='Image URL/External Link'
                    />
                </>
            }
            {!editMode && (link?.toLowerCase().endsWith('.jpg') || link?.toLowerCase().endsWith('.jpeg') || link?.toLowerCase().endsWith('.png'))
                ? <img src={link} alt={title}></img> : <div><a href={link} target='_blank' rel="noreferrer">{shortLink ? shortLink : link}</a></div>}
            {sessionUser?.id === owner.id && !editMode ? <button id='editpost' onClick={handleEdit}>Edit Post</button> : null}
            {sessionUser?.id === owner.id && editMode ? <button id='editpost' onClick={handleSubmit}>Submit Changes</button> : null}
            {sessionUser?.id === owner.id && editMode ? <button id='deletecomm' onClick={handleCancel}>Cancel</button> : null}
            {sessionUser?.id === owner.id ? <OpenModalButton buttonText={'Delete Post'} modalComponent={<ConfirmDeleteModal title={'Are you sure? Cannot be undone.'} confirmFunc={handleDelete}/>} /> : null}
        </div>
    )
}

export default PostContainer;
