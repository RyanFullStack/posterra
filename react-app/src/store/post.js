const GET_ALL_POSTS = 'posts/ALL'

const actionGetAllPosts = (posts) => ({
    type: GET_ALL_POSTS,
    posts
})

export const thunkGetAllPosts = () => async (dispatch) => {
    const res = await fetch('/api/posts/')

    if (res.ok) {
        const data = await res.json()
        dispatch(actionGetAllPosts(data))
        return data
    } else {
        return res
    }
}

export const getUserInfo = (id) => async (dispatch) => {
    const res = await fetch(`/api/users/${id}`)

    if (res.ok) {
        const data = await res.json()
        return data
    } else {
        return res
    }
}

export const thunkGetCommunityPosts = (id) => async (dispatch) => {
    const res = await fetch(`/api/communities/${id}/posts`)

    if (res.ok) {
        const data = await res.json()
        dispatch(actionGetAllPosts(data))
        return data
    } else {
        return res
    }
}

const initialState = { posts: null }

export default function postReducer(state = initialState, action) {
    switch(action.type) {
        case GET_ALL_POSTS:
            return { ...state, posts: action.posts}
        default:
            return state
    }
}
