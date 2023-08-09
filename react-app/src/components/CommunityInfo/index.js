import { useSelector, useDispatch } from 'react-redux';
import { useState, useEffect } from 'react';
import { getUserInfo } from '../../store/post';
import './communityinfo.css'


function CommunityInfo() {
    const dispatch = useDispatch()
    const community = useSelector(state => state.communities.singleCommunity)
    const [owner, setOwner] = useState()

    useEffect(() => {
        const data = async() => {
            const res = await dispatch(getUserInfo(community.created_by))
            const user = await res
            setOwner(user)
        }
        data()
        //eslint-disable-next-line
    }, [dispatch])

    if (!owner || !community) return <h2>Loading...</h2>


    return (
        <div className="community-info-container">
            <div className='community-info-contents'>
                <p>{community?.name}</p>
                <p>{community?.description}</p>
                <p>Created by: u/{owner?.username}</p>
            </div>
        </div>
    )
}

export default CommunityInfo;
