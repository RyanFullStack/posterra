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
                {allPosts.posts.map(post => {
                    if (sessionUser?.id !== post.owner.id) {
                    return (
                        <PostContainer post={post} key={post.id} />
                    )
                    } else return null;
                })}
            </div>
            <div className="home-info-container">
                <div className="home-info-contents">
                    <p>HOME</p>
                    <p>Posts from around the world...</p>
                    <button onClick={() => history.push('/posts/new')}>Create a post</button><br />
                    <button onClick={() => history.push('/communities/new')}>Create a community</button>
                </div>
            </div>
        </div>
    )
}

export default HomePage;
