import { useSelector, useDispatch } from 'react-redux'
import { thunkDeletePost } from '../../store/post'
import './post.css'

function PostContainer({ post }) {
    const title = post?.post_title
    const body = post?.post_body
    const link = post?.ext_url
    const edited = post?.edited
    const created = post?.created_at
    const owner = post?.owner
    const community = post?.community
    const sessionUser = useSelector((state) => state.session.user);
    const dispatch = useDispatch()

    let shortLink = ''

    if (link?.length > 40) {
        shortLink = link.slice(0, 40) + '...'
    }

    const handleDelete = async () => {
        if (window.confirm('Are You Sure? Cannot be undone')) {
            await dispatch(thunkDeletePost(post.id, community.id))
        }
    }

    const handleEdit = async () => {
        if (window.confirm('Coming soon')) {
            return
        }
    }

    return (
        <div key={post.id} className="post-container">
            <div>{title} by u/{owner.username} in p/{community.name} {edited ? '*edited': null} at {created}</div>
            <div>{body}</div>
            {link?.toLowerCase().endsWith('.jpg') || link?.toLowerCase().endsWith('.jpeg') || link?.toLowerCase().endsWith('.png')
            ? <img src={link} alt={title}></img> : <div><a href={link} target='_blank' rel="noreferrer">{shortLink ? shortLink : link}</a></div>}
            {sessionUser?.id === owner.id ? <button onClick={handleEdit}>Edit Post</button> : null}
            {sessionUser?.id === owner.id ? <button onClick={handleDelete}>Delete Post</button> : null}
        </div>
    )
}

export default PostContainer;
