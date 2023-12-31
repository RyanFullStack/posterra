import React from 'react';
import { useModal } from '../../context/Modal';
import '../Navigation/Navigation.css'

function OpenModalButton({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose // optional: callback function that will be called once the modal is closed
}) {
  const { setModalContent, setOnModalClose } = useModal();

  const onClick = () => {
    if (onModalClose) setOnModalClose(onModalClose);
    setModalContent(modalComponent);
    if (onButtonClick) onButtonClick();
  };

  if (buttonText === 'Delete Post') {
    return (
      <div onClick={onClick} className='post-modify-buttons'>Delete Post</div>
    )
  }

  if (buttonText === 'Delete') {
    return (
      <div onClick={onClick} className='post-modify-buttons'>Delete</div>
    )
  }

  return (
    <button onClick={onClick} id={(buttonText === 'Log In' || buttonText === 'Sign Up')  ? 'nav-button' : 'deletepost'} >{buttonText}</button>
  );
}

export default OpenModalButton;
