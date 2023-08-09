import { useSelector } from 'react-redux'
import './communityinfo.css'


function CommunityInfo() {
    const community = useSelector(state => state.communities.singleCommunity)
    const owner = community?.owner

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
