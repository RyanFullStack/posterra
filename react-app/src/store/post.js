const GET_ALL_POSTS = 'posts/ALL'
const GET_SINGLE_POST = 'posts/ONE'

const actionGetSinglePost = (post) => ({
    type: GET_SINGLE_POST,
    post
})

const actionGetAllPosts = (posts) => ({
    type: GET_ALL_POSTS,
    posts
})

export const thunkGetSinglePost = (id) => async(dispatch) => {
    const res = await fetch(`/api/posts/${id}`)
    if (res.ok) {
        const data = await res.json()
        dispatch(actionGetSinglePost(data))
        return data
    } else {
        return res
    }
}

export const thunkGetAllPosts = (page, sort) => async (dispatch) => {
    const res = await fetch(`/api/posts/?page=${page}&sort=${sort}`)

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

export const thunkGetCommunityPosts = (id, sort, page) => async (dispatch) => {
    const res = await fetch(`/api/communities/${id}/posts?sort=${sort}&page=${page}`)

    if (res.ok) {
        const data = await res.json()
        dispatch(actionGetAllPosts(data))
        return data
    } else {
        return res
    }
}

export const thunkCreatePost = (data) => async (dispatch) => {
    const res = await fetch('/api/posts/new', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            post_title: data.post_title,
            post_body: data.post_body,
            created_by: data.created_by,
            community_id: data.community_id,
            ext_url: data.ext_url
        })
    })
    if (res.ok) {
        const data = await res.json();
        dispatch(thunkGetCommunityPosts(data.community_id, 'newest', 1))
        return data
    } else {
        return res
    }
}


export const thunkEditPost = (communityId, postId, data, location, page, sort) => async (dispatch) => {
    const res = await fetch(`/api/posts/${postId}/edit`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            post_title: data.post_title,
            post_body: data.post_body,
            created_by: data.created_by,
            community_id: communityId,
            ext_url: data.ext_url
        })
    })
    if (res.ok) {
        const data = await res.json();
        if (location === 'home') {
            dispatch(thunkGetAllPosts(page, sort))
        }
        if (location === 'post-info') {
            dispatch(thunkGetSinglePost(postId))
        }
        else {
            dispatch(thunkGetCommunityPosts(communityId, sort, page))
        }
        return data
    } else {
        return res
    }
}


export const thunkDeletePost = (post_id, community_id, location, sort, page) => async (dispatch) => {
    const res = await fetch(`/api/posts/${post_id}/delete`, {
        method: 'DELETE'
    })

    if (res.ok) {
        const data = await res.json();
        console.log(location)
        if (location === 'home') {
            dispatch(thunkGetAllPosts(page, sort))
        }
        else {
            dispatch(thunkGetCommunityPosts(community_id, sort, page))
        }
        return data
    } else {
        return res
    }
}

const initialState = { posts: null, singlePost: null }

export default function postReducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_POSTS:
            return { ...state, posts: action.posts }
        case GET_SINGLE_POST:
            return { ...state, singlePost: action.post }
        default:
            return state
    }
}
