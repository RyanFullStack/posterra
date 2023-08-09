import { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { thunkCreateCommunity } from '../../store/community';

function CommunityForm() {
    const dispatch = useDispatch()
    const history = useHistory()
    const [name, setName] = useState('')
    const [description, setDescription] = useState('')
    const [errors, setErrors] = useState({});
    const currentUser = useSelector(state => state.session.user);



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
            created_by: currentUser.id,
        }

        const response = await dispatch(thunkCreateCommunity(data))

        if (response.errors) {
            const serverErrors = {}
            serverErrors.serverErrors = response.errors
            setErrors(serverErrors)
        } else {
            history.push('/')
        }
    }

    if (!currentUser) return <h2>Must be logged in to create anything!</h2>

    return (
        <div>
            <form className='form-container' method='post' onSubmit={handleSubmit}>
                <h1>Create a new Community</h1>
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
                <button className="form-button" type='submit'>Create New Comminuty</button>
            </form>
        </div>
    )
}

export default CommunityForm;
