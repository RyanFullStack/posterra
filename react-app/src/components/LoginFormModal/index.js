import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(username, password));
    if (data) {
      setErrors(data);
    } else {
      closeModal()
    }
  };

  const handleDemo = async() => {
    await dispatch(login('dave', 'password'))
    closeModal()
  }

  return (
    <div className="modal">
      <h2>Log In</h2>
      <form onSubmit={handleSubmit}>
        <div className="errors">
          {errors.map((error, idx) => (
            <p key={idx}>{error}</p>
          ))}
        </div>
        <label>
          <p>Username</p>
          <p><input
            className='create-form-select'
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          /></p>
        </label>
        <label>
          <p>Password</p>
          <p><input
            className='create-form-select'
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          /></p>
        </label>
        <button id="login-button" type="submit">Log In</button><p></p>
        <button id='login-button' onClick={handleDemo}>Demo Login</button>
      </form>
    </div>
  );
}

export default LoginFormModal;
