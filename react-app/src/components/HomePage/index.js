import { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { thunkGetAllPosts } from "../../store/post";
import { thunkGetAllCommunities } from "../../store/community";

function HomePage() {
    const [isLoaded, setIsLoaded] = useState(false)
    const dispatch = useDispatch()
    const allPosts = useSelector(state => state.posts.posts)
    const allCommunities = useSelector(state => state.communities.communities)

    useEffect(() => {
        const data = async () => {
            await dispatch(thunkGetAllPosts())
            await dispatch(thunkGetAllCommunities())
            setIsLoaded(true)
        }
        data()
    }, [dispatch])

    if (!isLoaded) return <h2>Loading...</h2>

    return (
        <>
        <div>
            {allCommunities.communities.map(community => {
                return (
                    <div key={community.id}>
                        {community.name}
                    </div>
                )
            })}
        </div>
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
        </>
    )
}

export default HomePage;
