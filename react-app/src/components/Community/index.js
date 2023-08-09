import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { thunkGetSingleCommunity } from "../../store/community";
import { thunkGetCommunityPosts } from "../../store/post";

function Community() {
    const { communityId } = useParams()
    const [loaded, setLoaded] = useState(false)
    const dispatch = useDispatch()
    const communityPosts = useSelector(state => state.posts.posts)
    const community = useSelector(state => state.communities.singleCommunity)

    useEffect(() => {
        const data = async () => {
            await dispatch(thunkGetSingleCommunity(communityId))
            await dispatch(thunkGetCommunityPosts(communityId))
            setLoaded(true)
        }
        data()

        return function() {
            setLoaded(false)
        }
    }, [dispatch, communityId])


    if (!loaded) return <h2>Loading...</h2>

    return (
        <div>
            <h2>{community?.name}</h2>

            <div>
                {communityPosts.posts.map(post => {
                    return (
                        <div key={post.id}>
                            {post.post_title}
                            {post.post_body}
                        </div>
                    )
                })}
            </div>
        </div>
    )
}

export default Community;
