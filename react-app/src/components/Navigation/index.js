import React, { useState, useEffect } from 'react';
import { NavLink, useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import ProfileButton from './ProfileButton';
import OpenModalButton from '../OpenModalButton';
import LoginFormModal from '../LoginFormModal';
import SignupFormModal from '../SignupFormModal';
import { thunkGetAllCommunities } from '../../store/community';
import './Navigation.css';

function Navigation({ isLoaded }) {
	const [loaded, setLoaded] = useState(false);
	const [selectedCommunity, setSelectedCommunity] = useState('none');
	const sessionUser = useSelector((state) => state.session.user);
	const allCommunities = useSelector((state) => state.communities.communities);
	const dispatch = useDispatch();
	const history = useHistory();

	useEffect(() => {
		const data = async () => {
			await dispatch(thunkGetAllCommunities());
			setLoaded(true);
		};
		data();
	}, [dispatch]);

	if (!loaded) return <h2>Loading...</h2>;

	const changeCommunity = (e) => {
		setSelectedCommunity(e.target.value);
		history.push(`/communities/${e.target.value}`);
	};

	const resetDropdown = () => {
		setSelectedCommunity('none');
	};

	return (
		<div>
			<NavLink exact to="/" onClick={resetDropdown}>
				Posterra
			</NavLink>

			<div>
				{isLoaded && sessionUser && <ProfileButton user={sessionUser} />}
			</div>

			<div>
				<select onChange={changeCommunity} value={selectedCommunity}>
					<option value="none" disabled hidden>
						Choose a community...
					</option>
					{allCommunities.communities.map((community) => (
						<option value={community.id} key={community.id}>
							{community.name}
						</option>
					))}
				</select>
			</div>

			{!sessionUser && (
				<div>
					<OpenModalButton
						buttonText="Log In"
						modalComponent={<LoginFormModal />}
					/>

					<OpenModalButton
						buttonText="Sign Up"
						modalComponent={<SignupFormModal />}
					/>
				</div>
			)}
		</div>
	);
}

export default Navigation;
