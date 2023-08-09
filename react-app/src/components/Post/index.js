import './post.css'

function PostContainer({ post }) {

    const title = post.post_title
    const body = post.post_body
    const link = post.ext_url
    const edited = post.edited
    const created = post.created_at
    const updated = post.updated_at
    let shortLink = ''

    if (link?.length > 40) {
        shortLink = link.slice(0, 40) + '...'
    }

    return (
        <div key={post.id} className="post-container">
            <div>{title}</div>
            <div>{body}</div>
            {link?.toLowerCase().endsWith('.jpg') || link?.toLowerCase().endsWith('.jpeg') || link?.toLowerCase().endsWith('.png')
            ? <img src={link}></img> : <div><a href={link} target='_blank'>{shortLink ? shortLink : link}</a></div>
        }
        </div>
    )
}

export default PostContainer;
