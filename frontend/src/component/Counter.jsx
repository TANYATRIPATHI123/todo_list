import React from 'react'
import {useState} from 'react';

function Counter() {
  console.log('Counter component rendering started');
  let [i,setI] = useState(0) ;
  function incrementI() {
    // document.getElementById("i_value").innerHTML = i;
     setI(i + 2);
  }
  //incrementI();         -- generated infinite loop
  return (
    <div>
        <p>hello from counter</p>
        {/* <p id="i_value">{i}</p> */}
        <p id>{i}</p>
        <button onClick={incrementI}>increment I</button>
    </div>
  )
}

export default Counter;