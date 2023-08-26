import { useParams, useLocation } from "react-router-dom";
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

    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);
    const [currentSort, setCurrentSort] = useState(queryParams.get("sort") || 'best')

    useEffect(() => {
        const data = async () => {
            const res = await dispatch(thunkGetSingleCommunity(communityId))
            await dispatch(thunkGetCommunityPosts(communityId, currentSort))
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
    }, [dispatch, communityId, currentSort])


    if (!loaded) return <Loading />
    if (!found) return <h2><center>Community not found!</center></h2>

    const handleBest = () => {
        setCurrentSort('best')
    }
    const handlePopular = () => {
        setCurrentSort('popular')
    }
    const handleNewest = () => {
        setCurrentSort('newest')
    }
    const handleOldest = () => {
        setCurrentSort('oldest')
    }
    const handleRandom = () => {
        dispatch(thunkGetCommunityPosts(communityId, 'random'))
        setCurrentSort('random')
    }


    return (
        <div className="community-container">
            <div className="post-main-container">
                <div className="post-order-by">
                    SORT BY |
                    <button onClick={handleBest} className='sort-button' disabled={currentSort === 'best'}>BEST</button> |
                    <button onClick={handlePopular} className='sort-button' disabled={currentSort === 'popular'}>POPULAR</button> |
                    <button onClick={handleNewest} className='sort-button' disabled={currentSort === 'newest'}>NEWEST</button> |
                    <button onClick={handleOldest} className='sort-button' disabled={currentSort === 'oldest'}>OLDEST</button> |
                    <button onClick={handleRandom} className='sort-button'>RANDOM</button>
                </div>
                {communityPosts.posts.map(post => {
                    return (
                        <PostContainer post={post} key={post.id} sort={currentSort} location={'community'}/>
                    )
                })}
            </div>
            <CommunityInfo />
        </div>
    )
}

export default Community;
