import React from "react";
import { useModal } from "../../context/Modal";

const ConfirmDeleteModal = ({ title, confirmFunc }) => {
  const { closeModal } = useModal();

  if (!title) return null;

  const handleClick = async () => {
    await confirmFunc();
    closeModal();
  };

  return (
    <div>
      <h1>{title}</h1>
      <div>
        <button onClick={handleClick}>
          Yes, Delete!
        </button>
        <button onClick={closeModal}>
          No, Back to safety!
        </button>
      </div>
    </div>
  );
};

export default ConfirmDeleteModal;
