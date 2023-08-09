import { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { thunkGetAllPosts } from "../../store/post";

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

        return function() {
            setLoaded(false)
        }
    }, [dispatch])

    if (!loaded) return <h2>Loading...</h2>

    return (
        <div>
            {allPosts.posts.map(post => {
                return (
                    <div key={post.id}>
                        {post.post_title}<br />
                        {post.post_body}
                    </div>
                )
            })}
        </div>
    )
}

export default HomePage;
