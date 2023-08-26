const GET_ALL_POSTS = 'posts/ALL'

const actionGetAllPosts = (posts) => ({
    type: GET_ALL_POSTS,
    posts
})

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
        dispatch(thunkGetCommunityPosts(data.community_id))
        return data
    } else {
        return res
    }
}


export const thunkEditPost = (communityId, postId, data) => async (dispatch) => {
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
        dispatch(thunkGetCommunityPosts(communityId))
        return data
    } else {
        return res
    }
}


export const thunkDeletePost = (post_id, community_id) => async (dispatch) => {
    const res = await fetch(`/api/posts/${post_id}/delete`, {
        method: 'DELETE'
    })
    if (res.ok) {
        const data = await res.json();
        dispatch(thunkGetCommunityPosts(community_id))
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
