const GET_ALL_COMMUNITIES = 'communities/ALL'

const actionGetAllCommunities = (communities) => ({
    type: GET_ALL_COMMUNITIES,
    communities
})

export const thunkGetAllCommunities = () => async (dispatch) => {
    const res = await fetch('/api/communities')

    if (res.ok) {
        const data = await res.json()
        dispatch(actionGetAllCommunities(data))
        return data
    } else {
        return res
    }
}

const initialState = { communities: null }

export default function communityReducer(state = initialState, action) {
    switch(action.type) {
        case GET_ALL_COMMUNITIES:
            return { ...state, communities: action.communities}
        default:
            return state
    }
}
