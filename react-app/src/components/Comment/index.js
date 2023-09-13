import { useEffect, useState } from 'react'
import { useSelector } from 'react-redux'

function CommentContainer({ comment }) {
    const [votes] = useState(comment.votes || null)
    const [userVote, setUserVote] = useState(null)
    const [upvote, setUpvote] = useState('')
    const [downvote, setDownvote] = useState('')
    const [voteCount, setVoteCount] = useState('')
    const [totalVotes, setTotalVotes] = useState(comment.numvotes || 0)
    const sessionUser = useSelector((state) => state.session.user);

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

    const handleUpvote = async() => {
        if (!sessionUser) {
            window.alert('Must be logged in to vote!')
            return
        }
        if (downvote) {
            await fetch(`/api/votes/comments/${comment.id}/deletevote`)
            await fetch(`/api/votes/comments/${comment.id}/addupvote`)
            setTotalVotes(prev => prev + 2)
            setUpvote('red')
            setDownvote('')
            setVoteCount('red')
            return
        }
        if (upvote) {
            await fetch(`/api/votes/comments/${comment.id}/deletevote`)
            setTotalVotes(prev => prev - 1)
            setUpvote('')
            setDownvote('')
            setVoteCount('')
        } else {
            await fetch(`/api/votes/comments/${comment.id}/addupvote`)
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
            await fetch(`/api/votes/comments/${comment.id}/deletevote`)
            await fetch(`/api/votes/comments/${comment.id}/adddownvote`)
            setTotalVotes(prev => prev - 2)
            setUpvote('')
            setDownvote('blue')
            setVoteCount('blue')
            return
        }
        if (downvote) {
            await fetch(`/api/votes/comments/${comment.id}/deletevote`)
            setTotalVotes(prev => prev + 1)
            setUpvote('')
            setDownvote('')
            setVoteCount('')
        } else {
            await fetch(`/api/votes/comments/${comment.id}/adddownvote`)
            setTotalVotes(prev => prev - 1)
            setUpvote('')
            setDownvote('blue')
            setVoteCount('blue')
        }
    }


    return (
        <div className="single-comment">
            <div className='comment-by'><img id='posted-by-small-pic' src={comment.owner.profile_pic} alt='User Profile Pic' />
            {comment.owner.username}
            <span id='post-info'>{dispTime}</span>
            {comment.edited ? ' *edited' : null}
            </div>
            <div className="comment-body-content">{comment.comment_body}</div>
            <div className='post-votes'>
                <div className={`vote-arrow-container vote-up ${upvote}`} onClick={handleUpvote}><i className="fa-solid fa-arrow-up" /></div>
                <span className={voteCount}><small>{totalVotes}</small></span>
                <div className={`vote-arrow-container vote-down ${downvote}`} onClick={handleDownvote}><i className="fa-solid fa-arrow-down" /></div>
            </div>
        </div>
    )
}

export default CommentContainer;
