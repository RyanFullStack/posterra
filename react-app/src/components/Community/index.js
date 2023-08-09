import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { thunkGetSingleCommunity } from "../../store/community";
import { thunkGetCommunityPosts } from "../../store/post";
import PostContainer from "../Post";
import './community.css'

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

        return function () {
            setLoaded(false)
        }
    }, [dispatch, communityId])


    if (!loaded) return <h2>Loading...</h2>

    return (
        <div className="community-container">
            <h2>{community?.name}</h2>

            <div className="post-main-container">
                {communityPosts.posts.map(post => {
                    return (
                        <PostContainer post={post} key={post.id}/>
                    )
                })}
            </div>
        </div>
    )
}

export default Community;
