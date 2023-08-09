import { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { thunkCreatePost } from '../../store/post';
import { thunkGetAllCommunities } from '../../store/community';

function PostForm() {
    const [loaded, setLoaded] = useState(false);
    const dispatch = useDispatch()
    const history = useHistory()
    const [title, setTitle] = useState('')
    const [body, setBody] = useState('')
    const [ext_url, setExtUrl] = useState('')
    const [communityId, setCommunityId] = useState('1')
    const [errors, setErrors] = useState({});
    const currentUser = useSelector(state => state.session.user);
    const allCommunities = useSelector((state) => state.communities.communities);

    useEffect(() => {
		const data = async () => {
			await dispatch(thunkGetAllCommunities());
            setLoaded(true);
		};
		data();
	}, [dispatch]);

    if (!loaded) return <h2>Loading...</h2>;



    const validateData = () => {
        const errorObj = {};

        if (!title) errorObj.title = "Field is required."
        if (title && (title.length > 255 || title.length < 10)) errorObj.title = 'Must be between 10 and 255 characters.'

        if (body && body.length > 1000) errorObj.body = 'Must be less than 1000 characters.'

        if (Object.keys(errorObj).length > 0) return errorObj
        else return false
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        const newErrors = validateData();

        if (newErrors) return setErrors(newErrors)

        const data = {
            post_title: title,
            post_body: body,
            created_by: currentUser.id,
            community_id: communityId,
            ext_url
        }

        console.log('********', data)

        const response = await dispatch(thunkCreatePost(data))

        if (response.errors) {
            const serverErrors = {}
            serverErrors.serverErrors = response.errors
            setErrors(serverErrors)
        } else {
            history.push(`/communities/${communityId}`)
        }
    }

    const handleChange = (e) => {
		setCommunityId(e.target.value)
	}

    if (!currentUser) return <h2>Must be logged in to create anything!</h2>

    return (
        <div>
            <form className='form-container' method='post' onSubmit={handleSubmit}>
                <h1>Create a new Post</h1>
                {errors.serverErrors && <p className='errors'>{errors.serverErrors}</p>}
                <select onChange={handleChange} value={communityId}>
					{allCommunities.communities.map((community) => (
						<option value={community.id} key={community.id}>
							{community.name}
						</option>
					))}
				</select>
                <label htmlFor='title'>Post Title{errors.title && <span className='errors'>: {errors.title}</span>}</label>
                <input
                    name='title'
                    value={title}
                    type="text"
                    onChange={(e) => setTitle(e.target.value)}
                    placeholder='title'
                />
                <label htmlFor='body'>Post Body{errors.body && <span className='errors'>: {errors.body}</span>}</label>
                <input
                    name='body'
                    type="text"
                    value={body}
                    onChange={(e) => setBody(e.target.value)}
                    placeholder='body'
                />
                <label htmlFor='ext_url'>Image URL/External Link</label>
                <input
                    name='ext_url'
                    type="text"
                    value={ext_url}
                    onChange={(e) => setExtUrl(e.target.value)}
                    placeholder='Image URL/External Link'
                />
                <button className="form-button" type='submit'>Create New Post</button>
            </form>
        </div>
    )
}

export default PostForm;
