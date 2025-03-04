import React from 'react'
import {Link} from 'react-router-dom'
import './Error.css'
function Error() {
  return (
    <div>
      <h1>This page could not be found!</h1>
      <Link to="/">Click here to go back to the Home</Link>
    </div>
  )
}

export default Error