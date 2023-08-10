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

    if (!loaded) return <h2>Loading...</h2>

    return (
        <div className="main-display-container">
            <div className="post-main-container">
                <div className="post-container">
                    <input placeholder="Create Post"></input>
                </div>
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
                        <p>Posterra Premium</p>
                        <p>The best posterra experience</p>
                        <button id='premium' onClick={() => window.alert('Coming Soon!')}>Try Now</button>
                    </div>
                </div>
                <div className="home-info-container">
                    <img id='home-earth' src='/earth.png' alt='earth'/>
                    <div className="home-info-contents">
                        <p>Posterra Home</p>
                        <p>Posts from around the world...</p>
                        <p>Your personal homepage. Come here to check in with your favorite communities.</p>
                        <button id='createpost' onClick={() => history.push('/posts/new')}>Create a post</button><br />
                        <button id='createcomm' onClick={() => history.push('/communities/new')}>Create a community</button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default HomePage;
