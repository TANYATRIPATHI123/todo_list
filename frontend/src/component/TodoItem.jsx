//rfce : react functional component export
import React from 'react';
import './TodoItem.css';
import IonIcon from '@reacticons/ionicons';

function TodoItem(props) { //JSON object is returned 
    let title = props.title || "default title";
    let description = props.desc;
    let status = props.status;
  return (
    <div className='TodoItem'>
      <div className='TodoItem__header'>
          <h2>title : {title}</h2>
          <button id='delete_todo_btn' onClick = {() => props.deleteTodo(props.idx)}>
            <IonIcon id = "delete_todo_icon" name="trash"></IonIcon>
          </button>
      </div>
      <p>description : {description}</p>
      <p>status : {status}</p>
    </div>
  )
}

export default TodoItem;