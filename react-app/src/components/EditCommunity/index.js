import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom';
import { thunkEditCommunity, thunkGetAllCommunities, thunkGetSingleCommunity } from '../../store/community';


function EditCommunity() {
    const dispatch = useDispatch()
    const history = useHistory()
    const community = useSelector(state => state.communities.singleCommunity)
    const currentUser = useSelector(state => state.session.user);
    const [name, setName] = useState()
    const [description, setDescription] = useState()
    const [logo_pic, setLogoPic] = useState()
    const [banner_pic, setBannerPic] = useState('')
    const [loaded, setLoaded] = useState(false)
    const [errors, setErrors] = useState({});
    const { communityId } = useParams()

    useEffect(() => {
        const data = async() => {
            const res = await dispatch(thunkGetSingleCommunity(communityId))
            const comm = await res
            setName(comm?.name)
            setDescription(comm?.description)
            setLogoPic(comm?.logo_pic)
            setBannerPic(comm?.banner_pic)
            setLoaded(true)
        }
        data()
    }, [dispatch, communityId])

    const validateData = () => {
        const errorObj = {};

        if (!name) errorObj.name = "Field is required."
        if (name && (name.length > 50 || name.length < 2)) errorObj.name = 'Must be between 2 and 50 characters.'

        if (description && description.length > 255) errorObj.description = 'Must be less than 255 characters.'

        if (Object.keys(errorObj).length > 0) return errorObj
        else return false
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        const newErrors = validateData();

        if (newErrors) return setErrors(newErrors)

        const data = {
            name,
            description,
            logo_pic,
            banner_pic,
            created_by: currentUser.id
        }
        console.log(data)
        const response = await dispatch(thunkEditCommunity(communityId, data))
        dispatch(thunkGetAllCommunities())
        history.push(`/communities/${response.id}`)
    }

    if (!currentUser) return <h2>Must be logged in to edit!</h2>

    if (community?.message) return <h2>Community not found!</h2>

    if (!loaded) return <h2>Loading...</h2>

    if (currentUser?.id !== community?.created_by) return <h2>Not your Community!</h2>

    return (
        <div>
            <form className='form-container' method='post' onSubmit={handleSubmit}>
                <h1>Edit your Community</h1>
                {errors.serverErrors && <p className='errors'>{errors.serverErrors}</p>}
                <label htmlFor='name'>Name{errors.name && <span className='errors'>: {errors.name}</span>}</label>
                <input
                    name='name'
                    value={name}
                    type="text"
                    onChange={(e) => setName(e.target.value)}
                    placeholder='community name'
                />
                <label htmlFor='description'>Description{errors.description && <span className='errors'>: {errors.description}</span>}</label>
                <input
                    name='description'
                    type="text"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    placeholder='description'
                />
                <label htmlFor='logo_pic'>Logo</label>
                <input
                    name='logo_pic'
                    type="text"
                    value={logo_pic}
                    onChange={(e) => setLogoPic(e.target.value)}
                    placeholder='logo'
                />
                <label htmlFor='banner_pic'>Banner Picture</label>
                <input
                    name='banner_pic'
                    type="text"
                    value={banner_pic}
                    onChange={(e) => setBannerPic(e.target.value)}
                    placeholder='banner pic'
                />
                <button className="form-button" type='submit'>Confirm Edits</button>
            </form>
        </div>
    )
}

export default EditCommunity;
