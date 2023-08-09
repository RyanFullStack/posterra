const GET_ALL_COMMUNITIES = 'communities/ALL'
const GET_SINGLE_COMMUNITY = 'communities/GET'

const actionGetAllCommunities = (communities) => ({
    type: GET_ALL_COMMUNITIES,
    communities
})

const actionGetSingleCommunity = (community) => ({
    type: GET_SINGLE_COMMUNITY,
    community
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

export const thunkGetSingleCommunity = (id) => async (dispatch) => {
    const res = await fetch(`/api/communities/${id}`)

    if (res.ok) {
        const data = await res.json()
        dispatch(actionGetSingleCommunity(data))
        return data
    } else {
        return res
    }
}

const initialState = { communities: null, singleCommunity: null }

export default function communityReducer(state = initialState, action) {
    switch(action.type) {
        case GET_ALL_COMMUNITIES:
            return { ...state, communities: action.communities}
        case GET_SINGLE_COMMUNITY:
            return { ...state, singleCommunity: action.community}
        default:
            return state
    }
}
