import { useSelector, useDispatch } from 'react-redux'
import { useHistory } from 'react-router-dom'
import './communityinfo.css'
import { thunkDeleteCommunity } from '../../store/community';


function CommunityInfo() {
    const community = useSelector(state => state.communities.singleCommunity)
    const sessionUser = useSelector((state) => state.session.user);
    const owner = community?.owner
    const dispatch = useDispatch()
    const history = useHistory()

    if (!owner || !community) return <h2>Loading...</h2>

    const handleDelete = async () => {
        if (window.confirm('Are You Sure? Cannot be undone')) {
            await dispatch(thunkDeleteCommunity(community.id))
            history.push('/')
        }
    }

    return (
        <div className="community-info-container">
            <div className='community-info-contents'>
                <p>{community?.name}</p>
                <p>{community?.description}</p>
                <p>Created by: u/{owner?.username}</p>
                {sessionUser?.id === owner.id ? <button onClick={handleDelete}>DELETE COMMUNITY</button> : null}
            </div>
        </div>
    )
}

export default CommunityInfo;
