import { useEffect, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import OpenModalButton from '../OpenModalButton'
import ConfirmDeleteModal from '../ConfirmDeleteModal'
import { thunkDeleteComment, thunkEditComment } from '../../store/comment'
import { thunkGetSinglePost } from '../../store/post'

function CommentContainer({ comment }) {
    const [votes] = useState(comment.votes || null)
    const [userVote, setUserVote] = useState(null)
    const [upvote, setUpvote] = useState('')
    const [downvote, setDownvote] = useState('')
    const [voteCount, setVoteCount] = useState('')
    const [totalVotes, setTotalVotes] = useState(comment.numvotes || 0)
    const [editMode, setEditMode] = useState(false)
    const [userComment, setUserComment] = useState(comment.comment_body)
    const sessionUser = useSelector((state) => state.session.user);
    const [errors, setErrors] = useState({})
    const dispatch = useDispatch()

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

    const handleEdit = () => {
        setEditMode(true)
        return
    }

    const handleCancel = () => {
        setEditMode(false)
        setUserComment(comment.comment_body)
        return
    }

    const handleSubmit = async() => {

        if (sessionUser.id <= 14 && comment.id <= 200) {
            window.alert('Demo User cant edit exisiting comment. Please create your own.')
        } else {
            if (userComment.length < 1) {
                setErrors({ 'length': 'Must be at least 1 character' })
                return
            }
            const data = {
                'created_by': sessionUser.id,
                'post_id': parseInt(comment.post_id),
                'comment_body': userComment
            }
            const res = await dispatch(thunkEditComment(comment.id, data))
            setEditMode(false)

            if (res.errors) {
                setErrors(res.errors)
                return
            }
            return
    }
}

    const handleDelete = async() => {
        if (sessionUser.id <= 14 && comment.id <= 200) {
            window.alert('Demo User cant delete exisiting comment. Please create your own.')
        } else {
            await dispatch(thunkDeleteComment(comment.id, comment.post_id))
            await dispatch(thunkGetSinglePost(comment.post_id))
    }
}


    return (
        <div className="single-comment">
            <div className='comment-by'><img id='posted-by-small-pic' src={comment.owner.profile_pic} alt='User Profile Pic' />
            {comment.owner.username}
            <span id='post-info'>{dispTime} {comment.edited ? ' *edited' : null}</span>
            </div>

            {editMode ?
            <>
            <textarea id='comment-input-edit' value={userComment} placeholder='Share your thoughts...' onChange={e => setUserComment(e.target.value)}></textarea>
            <div id='comment-length-edit'>{userComment.length > 255 ? <span className="red">{userComment.length} / 255</span> : <span>{userComment.length} / 255</span>}{errors.length && <span className='errors'>{errors.length}</span>}
            </div>
            <div id='comment-button-container'>
                <button id='add-comment-button' onClick={handleCancel}>Cancel</button>&nbsp;
                <button id='add-comment-button' onClick={handleSubmit} disabled={userComment.length > 255 || !userComment.length || userComment === comment.comment_body}>Confirm Edit</button>
            </div></> :
            <div className="comment-body-content" id='break-word'>{comment.comment_body}</div>

            }


            <div className='comment-votes'>
                <div className={`vote-arrow-container vote-up ${upvote}`} onClick={handleUpvote}><i className="fa-solid fa-arrow-up" /></div>
                <span className={voteCount}><small>{totalVotes}</small></span>
                <div className={`vote-arrow-container vote-down ${downvote}`} onClick={handleDownvote}><i className="fa-solid fa-arrow-down" /></div>

                {sessionUser?.id === comment.created_by ?
                        <>
                            <div onClick={handleEdit} className='post-modify-buttons'>Edit</div>|
                            <OpenModalButton buttonText={'Delete'} modalComponent={<ConfirmDeleteModal title={'Are you sure? Cannot be undone.'} confirmFunc={handleDelete} />} />

                        </>
                        : null}
            </div>
        </div>
    )
}

export default CommentContainer;
