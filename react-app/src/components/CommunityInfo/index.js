import { useSelector, useDispatch } from 'react-redux'
import { useHistory } from 'react-router-dom'
import { thunkDeleteCommunity } from '../../store/community';
import OpenModalButton from "../OpenModalButton";
import ConfirmDeleteModal from "../ConfirmDeleteModal"
import './communityinfo.css'


function CommunityInfo() {
    const community = useSelector(state => state.communities.singleCommunity)
    const sessionUser = useSelector((state) => state.session.user);
    const owner = community?.owner
    const dispatch = useDispatch()
    const history = useHistory()

    if (!owner || !community) return <h2>Loading...</h2>

    const handleDelete = async () => {
        if (community.id <= 16 && sessionUser.id <= 14) {
            window.alert('Demo User cant delete exisiting community. Please create your own.')
        } else {
            await dispatch(thunkDeleteCommunity(community.id))
            history.push('/')
        }
    }

    const handleEdit = async () => {
        history.push(`/communities/${community.id}/edit`)
    }

    return (
        <div className="community-info-container">
            {community.banner_pic ? <img id='community-info-banner-pic' src={community.banner_pic} alt='community banner pic' /> : null}
            <div className='community-info-contents'>
                <div id='break-word'>
                    <b>{community?.name}</b><br />
                    <img id='community-info-pic' src={community?.logo_pic} alt={community?.name} />
                    <p>{community?.description}</p>
                    <small>Created by: {<img id='posted-by-small-pic' src={owner.profile_pic} alt='User Profile Pic'/>} u/{owner?.username}</small>
                </div>
                <p></p>
                {sessionUser?.id === owner.id ? <button id='editcomm' onClick={handleEdit}>Edit Community</button> : null}
                {sessionUser?.id === owner.id ? <OpenModalButton buttonText={'Delete Community'} modalComponent={<ConfirmDeleteModal title={'Are you sure? Cannot be undone.'} confirmFunc={handleDelete} />} /> : null}
            </div>
        </div>
    )
}

export default CommunityInfo;
