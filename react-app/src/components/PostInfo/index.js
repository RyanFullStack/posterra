import { useParams, useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { thunkGetSingleCommunity } from "../../store/community";
import { thunkGetCommunityPosts, thunkGetSinglePost } from "../../store/post";
import PostContainer from "../Post";
import CommunityInfo from "../CommunityInfo";
import Loading from "../Loading";

function PostInfo() {
    const { postId } = useParams()
    const [loaded, setLoaded] = useState(false)
    const [found, setFound] = useState(false)
    const dispatch = useDispatch()

    useEffect(() => {
        const data = async() => {
            const res = await dispatch(thunkGetSinglePost(postId))
            setLoaded(true)
            if (res.id) {
            setFound(true)
            }
        }
        data()

        return function() {
            setLoaded(false)
            setFound(false)
        }
    }, [dispatch])

    if (!loaded) return <Loading />
    if (!found) return <h2><center>Post not found!</center></h2>

    return (
        'POST'
    )
}

export default PostInfo;
