import { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { thunkCreatePost } from '../../store/post';
import { thunkGetAllCommunities } from '../../store/community';
import './Postform.css'
import isUrl from 'is-url';

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


        if (!title) errorObj.title = "Title is required."
        if (title && title.trim().length === 0) errorObj.title = 'Title cannot be only whitespace'
        if (title && (title.length > 255 || title.length < 10)) errorObj.title = 'Must be between 10 and 255 characters.'

        if (body && body.length > 1000) errorObj.body = 'Must be less than 1000 characters.'

        if (ext_url && !isUrl(ext_url)) errorObj.url = 'URL not valid!'

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

        const response = await dispatch(thunkCreatePost(data, 'newest'))

        if (response.errors) {
            const serverErrors = {}
            serverErrors.serverErrors = response.errors
            setErrors(serverErrors)
        } else {
            history.push(`/communities/${communityId}/?sort=newest`)
        }
    }

    const handleChange = (e) => {
        setCommunityId(e.target.value)
    }

    if (!currentUser) return <h2>Must be logged in to create anything!</h2>

    return (
        <div className='create-form-container'>
            <div className='create-post-form'>
                <form className='form-container' method='post' onSubmit={handleSubmit}>
                    <h3>Create a post</h3>
                    {errors.serverErrors && <p className='errors'>{errors.serverErrors}</p>}
                    <div className='create-post-component'><small>* Indicates Required Field</small>
                        Choose a community*:
                        <select className='create-form-select' onChange={handleChange} value={communityId}>
                            {allCommunities.communities.map((community) => (
                                <option value={community.id} key={community.id}>
                                    {community.name}
                                </option>
                            ))}
                        </select>
                        <label htmlFor='title'>Post Title*{errors.title && <span className='errors'>: {errors.title}</span>}</label>
                        <input
                            className='create-form-select'
                            name='title'
                            value={title}
                            type="text"
                            onChange={(e) => setTitle(e.target.value)}
                            placeholder='title your post'
                        />
                        <label htmlFor='body'>Post Body{errors.body && <span className='errors'>: {errors.body}</span>}</label>
                        <textarea
                            className='create-form-select'
                            wrap='hard'
                            name='body'
                            type="textarea"
                            value={body}
                            onChange={(e) => setBody(e.target.value)}
                            placeholder='post body...'
                        />
                        <label htmlFor='ext_url'>Image URL/External Link{errors.url && <span className='errors'>: {errors.url}</span>}</label>
                        <input
                            className='create-form-select'
                            name='ext_url'
                            type="text"
                            value={ext_url}
                            onChange={(e) => setExtUrl(e.target.value)}
                            placeholder='http://www.yourlink.com.jpg.jpeg.png.gif'
                        />
                        <div id='post-button-align'>
                            <button id="post-form-button" type='submit'>Post</button>
                        </div>
                    </div>
                </form>
            </div>
            <div className='posting-rules'>
            <img id='home-earth' src='/earth.png' alt='earth' />
                <div id='rules'>
                <h5>Posting Rules:</h5>
                    <p>1. Remember the human</p>
                    <p>2. Behave like you would in real life</p>
                    <p>3. Look for the original source of content</p>
                </div>
            </div>
        </div>
    )
}

export default PostForm;
