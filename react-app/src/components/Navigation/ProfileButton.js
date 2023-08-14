import React, { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { logout } from "../../store/session";
import './Navigation.css'

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const sessionUser = useSelector((state) => state.session.user);
  const ulRef = useRef();
  const history = useHistory()

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
    history.push('/')
  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");

  // const closeMenu = () => setShowMenu(false);


  return (
    <>
      <button id='user-menu' onClick={openMenu}>
        <div className="logged-in-user">
          <div id='user'>
            <img id='logged-in-pic' src={sessionUser?.profile_pic} alt='User Profile Pic' />
            <b>{sessionUser?.username}</b>
          </div>
          <div id='fasdown'>
            <i className="fa-solid fa-chevron-down"></i>
          </div>
        </div>
      </button>
      <div className={ulClassName} ref={ulRef}>
        {user ? (
          <>
            <p>Hey, {user.username.toLowerCase().split('')[0].toUpperCase() + user.username.toLowerCase().slice(1)}</p>
            <small>{user.email}</small>
            <p>
              <button id='log-out-button' onClick={handleLogout}>Log Out</button>
            </p>
          </>
        ) : null}
      </div>
    </>
  );
}

export default ProfileButton;
