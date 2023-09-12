function CommentContainer({ comment }) {

    console.log(comment)


    const time = new Date(comment.created_at)
    const dispTime = time.toLocaleTimeString("en-US", {
        weekday: 'short',
        day: 'numeric',
        month: 'short',
        year: 'numeric',
        hour: "numeric",
        minute: "numeric",
        hour12: true,
    })

    return (
        <div className="single-comment">
            <div className='comment-by'><img id='posted-by-small-pic' src={comment.owner.profile_pic} alt='User Profile Pic' />
            {comment.owner.username}
            <span id='post-info'>{dispTime}</span></div>
            <div className="comment-body-content">{comment.comment_body}</div>
        </div>
    )
}

export default CommentContainer;
