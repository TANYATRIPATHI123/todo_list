import React from 'react'
import '../App.css';
import TodoItem from '../component/TodoItem';
import axios from 'axios';
import { useEffect, useState } from 'react';
//import Counter from './component/Counter';
import IonIcon from '@reacticons/ionicons';

function Todo() {
    const [isDeleted, setIsDeleted] = useState(false);
    //js goes here
    let [todosList, setTodosList] = useState([])
    useEffect (() => {
      axios.get('http://localhost:8000/api/v1/todos')  //axios invokation
                      .then((res)=> {
                        console.log(res.data);
                        setTodosList(res.data);
                      }
                    );
                  }
                  ,[isDeleted]);
  
    function deleteTodo(idx) {
      const todoItem = todosList[idx];
      console.log(`deleting todo item with idx = ${idx}`);
      console.log(`deleting todo item = ${todoItem}`)
      //console.log(todoItem.title);
      axios.delete(`http://localhost:8000/api/v1/delete-by-title/${todoItem.title}`)
      .then((res) => {
        console.log(res.data);
        todosList.splice(idx, 1);
        setTodosList(todosList);
      });
      
      setIsDeleted(true);
    }
    
    function addTodo(e) {
      e.preventDefault();  //
      //console.log(e);
      const todoItem = {'title' : e.target[0].value, 'desc' : e.target[1].value, 'status' : e.target[2].value}
      e.target[0].value = ""
      e.target[1].value = ""
      e.target[2].value = ""
      console.log('adding a new item')
      //todosList = [...todosList, todoItem];
      axios.post('http://localhost:8000/api/v1/todos', todoItem)  //axios invokation
                    .then((res)=> {
                      console.log(res.data);
                      setTodosList([...todosList, todoItem]);
                    }
                  );
      //console.log(todosList);
      //setTodosList([...todosList, todoItem]);
    };
    
    
    return (
      <div className="App">
        <form className = "Add_Todo" onSubmit={(e) => addTodo(e)}>
        <input name = "add_todo_input" id = "add_todo_title_input" placeholder='Add title'></input>
        <input name = "add_todo_input" id = "add_todo_desc_input" placeholder='Add description'></input>
        <input name = "add_todo_input" id = "add_todo_status_input" placeholder='Add status'></input>
        <button id = "add_todo_btn" type="submit">
          <IonIcon id = "add_todo_icon" name="add-circle"></IonIcon>
        </button>
        </form>
        <h1>Todos</h1>
        <button onClick={useEffect}>get Todos</button>
        {
          todosList.map((todo, idx) =>   //for looping through each item
            <TodoItem title={todo.title} desc={todo.desc} status={todo.status} idx ={idx}
            deleteTodo = {deleteTodo}/>
          )
        }
        
        {/* <TodoItem title="" desc="5:30" status="completed" createdAt="26/11/2024 7:50"/>
        <TodoItem title="Class end" desc="7:30" status="completed" createdAt="26/11/2024 7:50"/> */}
      {/* <Counter/> */}
      </div>
    );
}

export default Todo