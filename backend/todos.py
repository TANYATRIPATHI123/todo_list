from fastapi import APIRouter,HTTPException,status, Query
from typing import List, Optional
import database

#router = FastAPI()
router = APIRouter(tags = ["todos"])
conn = database.get_db()


#read all todos
@router.get('/api/v1/todos', status_code=status.HTTP_200_OK) 
def get_all_todos(limit: Optional[int] = Query(10), offset:Optional[int] = Query(0)) -> List[dict]: 
 print(type(limit))
 start_idx = int(offset)
 end_idx = start_idx + int(limit)
 query = "select title, des, status from todo"
 cursor = conn.cursor() #for query execution
 cursor.execute(query)
 todos_from_db = cursor.fetchall() #list of tuples
 todos = [] #list of dictionary
 for todo in todos_from_db:
     todos.append({
         "title": todo[0],
         "desc": todo[1],
         "status": todo[2],
     })
 cursor.close()
 return todos[start_idx: end_idx]

#read todo by title
@router.get('/api/v1/todos/{title}', status_code=status.HTTP_200_OK)
def get_todo_by_title(title: str) -> dict:
    query = f"select title, des, status from todo where title = '{title}'"
    cursor = conn.cursor() #for query execution
    cursor.execute(query)
    todos_from_db = cursor.fetchall() #list of tuples
    todos = [0] #list of dictionary
    for todo in todos_from_db:
        todos.append({
            "title": todo[0],
            "desc": todo[1],
            "status": todo[2],
        })
    cursor.close()
    if len(todos) == 1:
      return todos
    else: 
      raise HTTPException(status.HTTP_400_BAD_REQUEST, f"todo not found with this {title}")

    
# get todo by status
@router.get('/api/v1/todos/status/{status}', status_code=status.HTTP_200_OK) 
def get_todos_by_status(status: str) -> List[dict]:
    query = f"select title, des, status from todo where status = '{status}'"
    cursor = conn.cursor() #for query execution
    cursor.execute(query)
    todos_from_db = cursor.fetchall() #list of tuples
    todos = [0] #list of dictionary
    for todo in todos_from_db:
        todos.append({
            "title": todo[0],
            "desc": todo[1],
            "status": todo[2],
        })
    cursor.close()
    if len(todos) == 1:
      return todos
    else: 
      raise HTTPException(status.HTTP_400_BAD_REQUEST, f"todo not found with this {status}")

# create a todo 
# enforcing title to be unique -> user defined constraint
@router.post('/api/v1/todos',status_code=status.HTTP_201_CREATED)
def create_todo(todo: dict) -> bool:
	query = f"select title,des,status from todo where title='{todo['title']}'"
	cursor = conn.cursor()
	cursor.execute(query)
	todos_from_db = cursor.fetchall() # list of tuples
	cursor.close()
	
	if (len(todos_from_db) > 0):
		message = f"todo with title {todo['title']} already exists."
		raise HTTPException(status.HTTP_409_CONFLICT,message)
	
	query = f"insert into todo(title,des,status) values('{todo['title']}','{todo['desc']}','{todo['status']}')"
	cursor = conn.cursor()
	cursor.execute(query)
	conn.commit()
	cursor.close()
	return True
    
@router.put('/api/v1/updateTodo', status_code=status.HTTP_200_OK)
def updateTodo(payload:dict) -> bool:
    query = f"update todo set des = '{payload['desc']}', status = '{payload['status']}' where title = '{payload['title']}' "
    conn = database.get_db()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    return True


#patch : only those fields that are needed,  put : all the fields are required
@router.delete('/api/v1/delete-by-title/{title}')
def deleteTodo(title: str) -> bool:
    query = f" delete from todo where title = '{title}';"
    conn = database.get_db()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    return True
