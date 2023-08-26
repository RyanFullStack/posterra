import { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useHistory, useLocation } from "react-router-dom";
import { thunkGetAllPosts } from "../../store/post";
import PostContainer from "../Post";
import Loading from '../Loading'
import './home.css'

function HomePage() {
    const [loaded, setLoaded] = useState(false)
    const dispatch = useDispatch()
    const history = useHistory()
    const allPosts = useSelector(state => state.posts.posts)
    const sessionUser = useSelector(state => state.session.user)

    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);
    const [currentPage, setCurrentPage] = useState(queryParams.get("page") || 1)
    const [currentSort, setCurrentSort] = useState(queryParams.get("sort") || 'best')

    useEffect(() => {
        const data = async () => {
            await dispatch(thunkGetAllPosts(currentPage, currentSort))
            setLoaded(true)
        }
        data()

        return function () {
            setLoaded(false)
        }
    }, [dispatch, currentPage, currentSort])

    const handlePost = () => {
        history.push('/posts/new')
    }

    if (!loaded) return <Loading />


    const handleBack = () => {
        if (currentPage > 1) {
            setCurrentPage(currentPage - 1)
        }
    }

    const handleNext = () => {
        if (currentPage > 0 && currentPage < allPosts.totalPages) {
            setCurrentPage(currentPage + 1)
        }
    }

    const handleBest = () => {
        setCurrentPage(1)
        setCurrentSort('best')
    }
    const handlePopular = () => {
        setCurrentPage(1)
        setCurrentSort('popular')
    }
    const handleNewest = () => {
        setCurrentPage(1)
        setCurrentSort('newest')
    }
    const handleOldest = () => {
        setCurrentPage(1)
        setCurrentSort('oldest')
    }
    const handleRandom = () => {
        dispatch(thunkGetAllPosts(1, 'random'))
        setCurrentPage(1)
        setCurrentSort('random')
    }

    return (
        <div className="main-display-container">
            <div className="post-main-container">
                {sessionUser ? <div className="post-container-fake">
                    <div className='post-input-container'>
                        <img id='post-profile-pic' src={sessionUser?.profile_pic} alt='User Profile Pic' />
                        <input id='create-post-input' onClick={handlePost} placeholder="Create Post"></input>
                    </div>
                </div> : null}
                <div className="post-order-by">
                    SORT BY |
                    <button onClick={handleBest} className='sort-button' disabled={currentSort === 'best'}>BEST</button> |
                    <button onClick={handlePopular} className='sort-button' disabled={currentSort === 'popular'}>POPULAR</button> |
                    <button onClick={handleNewest} className='sort-button' disabled={currentSort === 'newest'}>NEWEST</button> |
                    <button onClick={handleOldest} className='sort-button' disabled={currentSort === 'oldest'}>OLDEST</button> |
                    <button onClick={handleRandom} className='sort-button'>RANDOM</button>
                </div>
                {allPosts.posts.map(post => {
                    return <PostContainer post={post} key={post.id} location={'home'} page={currentPage} sort={currentSort} />
                })}
                <div className="location-buttons">
                    {currentPage > 1 ? <button className="next-previous" id='previous-button' onClick={handleBack}>Previous</button> : null}
                    {currentPage === allPosts.totalPages ? null : <button className="next-previous" onClick={handleNext}>Next</button>}
                </div>
            </div>
            <div className="sidebar">
                <div className="home-info">
                    <div className="home-info-contents">
                        <span id='heart-shield'><i className="fa-solid fa-shield-heart" /></span>
                        <small>Posterra Premium</small>
                        <p>The best posterra experience!</p>
                        <button id='premium' onClick={() => window.alert('Coming Soon!')}>Try Now</button>
                    </div>
                </div>
                <div className="sticky">
                    <div className="home-info-container">
                        <img id='home-earth' src='/earth.png' alt='earth' />
                        <div className="home-info-contents">
                            <b>Home</b><br />
                            <small>Posts from around the world...</small>
                            <p>Your personal homepage. Come here to check in with your favorite communities.</p>
                            {sessionUser ? <button id='createpost' onClick={() => history.push('/posts/new')}>Create post</button> : null}
                            {sessionUser ? <button id='createcomm' onClick={() => history.push('/communities/new')}>Create community</button> : null}
                        </div>
                    </div>
                    <div className="creator-info">
                        <div className="home-info">
                            <div className="home-info-contents">
                                <p><small>Created by: Ryan Erickson</small></p>
                                <p><a href='https://github.com/RyanFullStack' target='_blank' rel="noreferrer"><button id='premium'>Check out my GitHub</button></a></p>
                                <a href='https://www.linkedin.com/in/ryan-erickson-dev/' target='_blank' rel="noreferrer"><button id='createpost'>Connect with me on Linkedin</button></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default HomePage;
