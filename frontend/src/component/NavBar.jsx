import React from 'react'
import './NavBar.css';
import {Link} from 'react-router-dom'
function NavBar() {
  return (
    <div className="NavBar">
      <div className="logo">Logo</div>
        <Link to ="/"> Home page</Link>
        <Link to="/about"> About page</Link>
        <Link to="/login">Login</Link>
        <Link to="/signup">SignUp</Link>
    </div>
  )
}

export default NavBar