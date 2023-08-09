import './post.css'

function PostContainer({ post }) {
    const title = post?.post_title
    const body = post?.post_body
    const link = post?.ext_url
    const edited = post?.edited
    const created = post?.created_at
    const owner = post?.owner
    const community = post?.community

    let shortLink = ''

    if (link?.length > 40) {
        shortLink = link.slice(0, 40) + '...'
    }


    return (
        <div key={post.id} className="post-container">
            <div>{title} by u/{owner.username} in p/{community.name} {edited ? '*edited': null} at {created}</div>
            <div>{body}</div>
            {link?.toLowerCase().endsWith('.jpg') || link?.toLowerCase().endsWith('.jpeg') || link?.toLowerCase().endsWith('.png')
            ? <img src={link} alt={title}></img> : <div><a href={link} target='_blank' rel="noreferrer">{shortLink ? shortLink : link}</a></div>
        }
        </div>
    )
}

export default PostContainer;
