const GET_ALL_POSTS = 'posts/ALL'

const actionGetAllPosts = (posts) => ({
    type: GET_ALL_POSTS,
    posts
})

export const thunkGetAllPosts = () => async (dispatch) => {
    const res = await fetch('/api/posts')

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
