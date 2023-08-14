import React from "react";
import { useModal } from "../../context/Modal";
import './ConfirmDelete.css'

const ConfirmDeleteModal = ({ title, confirmFunc }) => {
  const { closeModal } = useModal();

  if (!title) return null;

  const handleClick = async () => {
    await confirmFunc();
    closeModal();
  };

  return (
    <div className='confirm-delete'>
      <h2>{title}</h2>
      <div className="confirm-buttons">
        <button id='confirm-button-delete' onClick={handleClick}>
          Yes, Delete!
        </button>
        <button id='confirm-button-keep' onClick={closeModal}>
          No, Back to safety!
        </button>
      </div>
    </div>
  );
};

export default ConfirmDeleteModal;
