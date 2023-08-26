import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { thunkGetSingleCommunity } from "../../store/community";
import { thunkGetCommunityPosts } from "../../store/post";
import PostContainer from "../Post";
import CommunityInfo from "../CommunityInfo";
import Loading from "../Loading";
import './community.css'

function Community() {
    const { communityId } = useParams()
    const [loaded, setLoaded] = useState(false)
    const [found, setFound] = useState(false)
    const dispatch = useDispatch()
    const communityPosts = useSelector(state => state.posts.posts)

    useEffect(() => {
        const data = async () => {
            const res = await dispatch(thunkGetSingleCommunity(communityId))
            await dispatch(thunkGetCommunityPosts(communityId))
            setLoaded(true)
            const isFound = await res
            if (isFound.message) {
                setFound(false)
            } else {
                setFound(true)
            }
        }
        data()

        return function () {
            setLoaded(false)
            setFound(false)
        }
    }, [dispatch, communityId])


    if (!loaded) return <Loading />
    if (!found) return <h2><center>Community not found!</center></h2>


    return (
        <div className="community-container">
            <div className="post-main-container">
                {communityPosts.posts.map(post => {
                    return (
                        <PostContainer post={post} key={post.id} />
                    )
                })}
            </div>
            <CommunityInfo />
        </div>
    )
}

export default Community;
