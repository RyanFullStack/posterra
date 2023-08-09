import { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { thunkGetAllPosts } from "../../store/post";
import PostContainer from "../Post";
import './home.css'

function HomePage() {
    const [loaded, setLoaded] = useState(false)
    const dispatch = useDispatch()
    const allPosts = useSelector(state => state.posts.posts)

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
                    return (
                        <PostContainer post={post} key={post.id} />
                    )
                })}
            </div>
            <div className="home-info-container">
                <div className="home-info-contents">
                    <p>HOME</p>
                    <p>Posts from around the world...</p>
                </div>
            </div>
        </div>
    )
}

export default HomePage;
