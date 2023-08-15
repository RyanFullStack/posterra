import { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { thunkGetAllPosts } from "../../store/post";
import PostContainer from "../Post";
import './home.css'

function HomePage() {
    const [loaded, setLoaded] = useState(false)
    const dispatch = useDispatch()
    const history = useHistory()
    const allPosts = useSelector(state => state.posts.posts)
    const sessionUser = useSelector(state => state.session.user)

    useEffect(() => {
        const data = async () => {
            await dispatch(thunkGetAllPosts())
            setLoaded(true)
        }
        data()

        return function () {
            setLoaded(false)
        }
    }, [dispatch])

    const handlePost = () => {
        history.push('/posts/new')
    }

    if (!loaded) return <h2>Loading...</h2>

    return (
        <div className="main-display-container">
            <div className="post-main-container">
                {sessionUser ? <div className="post-container-fake">
                    <div className='post-input-container'>
                        <img id='post-profile-pic' src={sessionUser?.profile_pic} alt='User Profile Pic' />
                        <input id='create-post-input' onClick={handlePost} placeholder="Create Post"></input>
                    </div>
                </div> : null}
                {allPosts.posts.map(post => {
                    if (sessionUser?.id !== post.owner.id) {
                        return (
                            <PostContainer post={post} key={post.id} />
                        )
                    } else return null;
                })}
            </div>
            <div className="sidebar">
                <div className="home-info">
                    <div className="home-info-contents">
                        <small>Posterra Premium</small>
                        <p>The best posterra experience!</p>
                        <button id='premium' onClick={() => window.alert('Coming Soon!')}>Try Now</button>
                    </div>
                </div>
                <div className="sticky">
                    <div className="home-info-container">
                        <img id='home-earth' src='/earth.png' alt='earth' />
                        <div className="home-info-contents">
                            <b>Home</b><br />
                            <small>Posts from around the world...</small>
                            <p>Your personal homepage. Come here to check in with your favorite communities.</p>
                            {sessionUser ? <button id='createpost' onClick={() => history.push('/posts/new')}>Create post</button> : null}
                            {sessionUser ? <button id='createcomm' onClick={() => history.push('/communities/new')}>Create community</button> : null}
                        </div>
                    </div>
                    <div className="creator-info">
                        <div className="home-info">
                            <div className="home-info-contents">
                                <p><small>Created by: Ryan Erickson</small></p>
                                <p><a href='https://github.com/RyanFullStack' target='_blank' rel="noreferrer"><button id='premium'>Check out my GitHub</button></a></p>
                                <a href='https://www.linkedin.com/in/ryan-erickson-dev/' target='_blank' rel="noreferrer"><button id='createpost'>Connect with me on Linkedin</button></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default HomePage;
