/* eslint-disable no-unused-vars */
import React, { useState } from 'react';
import './SignUp.css';
import axios from 'axios';
function SignUp() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirm_password, setConfirmPassword] = useState('');
  const [error, setError] = useState('');

  function validate_password(){
    if(password !== confirm_password){
      setError("Passwords do not match");
    }else{
      setError("");
      return true;
    }
  }

  
  function signupHandler(e) {
    e.preventDefault();
    console.log('Signup clicked');
    console.log(username, email, password, confirm_password);
    
    //to avoid backend call
    if(!validate_password()){
      return;
    }
    console.log('calling backend serives');
    axios.post('http://localhost:8000/signup', { "username": username, "email": email, "password": password })
        .then((res) => {
          if(res.data.status !== "ok") {
            setError(res.data.detail);
          }
          else{
            console.log(res.data);
          }
        })
        .catch((err) => {
            const errMsg = err.response.data.detail;
            console.log(errMsg);
            setError(errMsg);
      
        });
}
    
  return (
      <form action='submit' className='SignUp'>
      <label htmlFor='signup_username'>UserName</label>
      <input type='text' id = "signup_email" placeholder='Enter Username' onChange={(e) => setUsername(e.target.value)}/>
      <label htmlFor='signup_email'>Email</label>
      <input type='text' id = "signup_email" placeholder='Enter Email' onChange={(e) => setEmail(e.target.value)}/>
      <label htmlFor='signup_password'>Password</label>
      <input type='password' id = "signup_password" placeholder='Enter Password' onChange={(e) => setPassword(e.target.value)}/>
      <label htmlFor='confirm_password'>Confirm Password</label>
      <input type='password' id = "signup_confirm_password" placeholder='Enter Password Again' onChange={(e) => setConfirmPassword(e.target.value)}/>
      <p id='signup_error'>{error}</p>
      <button id='signup_btn' type='submit' onClick={(e) => signupHandler(e)}>Sign Up</button>
      </form>
  )
}

export default SignUp