import { useDispatch } from 'react-redux';
import { useState, useEffect } from 'react';
import { getUserInfo } from '../../store/post';
import './post.css'

function PostContainer({ post }) {
    const [owner, setOwner] = useState()
    const dispatch = useDispatch()
    const title = post?.post_title
    const body = post?.post_body
    const link = post?.ext_url
    const edited = post?.edited
    const created = post?.created_at
    const created_by = post?.created_by
    let shortLink = ''

    if (link?.length > 40) {
        shortLink = link.slice(0, 40) + '...'
    }

    useEffect(() => {
        const data = async() => {
            const res = await dispatch(getUserInfo(created_by))
            const user = await res
            setOwner(user)
        }
        data()
        //eslint-disable-next-line
    }, [dispatch])

    return (
        <div key={post.id} className="post-container">
            <div>{title} by u/{owner?.username} {edited ? '*edited': null} at {created}</div>
            <div>{body}</div>
            {link?.toLowerCase().endsWith('.jpg') || link?.toLowerCase().endsWith('.jpeg') || link?.toLowerCase().endsWith('.png')
            ? <img src={link} alt={title}></img> : <div><a href={link} target='_blank' rel="noreferrer">{shortLink ? shortLink : link}</a></div>
        }
        </div>
    )
}

export default PostContainer;
