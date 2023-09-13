const GET_ALL_COMMENTS = 'comments/ALL'

const actionGetAllComments = (comments) => ({
    type: GET_ALL_COMMENTS,
    comments
})


export const thunkAddComment = (data) => async(dispatch) => {
    const res = await fetch(`/api/comments/${data.post_id}/new`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            created_by: data.created_by,
            post_id: data.post_id,
            comment_body: data.comment_body
        })
    })
    if (res.ok) {
        const data = await res.json()
        dispatch(thunkGetAllComments(data.post_id))
        return data
    } else {
        return res
    }
}

export const thunkGetAllComments = (id) => async(dispatch) => {
    const res = await fetch(`/api/comments/${id}`)
    if (res.ok) {
        const data = await res.json()
        dispatch(actionGetAllComments(data.comments))
        return data
    } else {
        return res
    }
}

const initialState = { allComments: null }

export default function commentReducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_COMMENTS:
            return {...state, allComments: action.comments}
        default:
            return state
    }
}
