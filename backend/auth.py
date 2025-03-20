import uuid
from fastapi import APIRouter, HTTPException, Response, status
import database, utils
import datetime
router = APIRouter(tags = ["auth"])


@router.post('/signup')
def sign_up(payload: dict):
    print(payload)
    conn = database.get_db()
    cursor = conn.cursor()
    try:
        username = payload['username']
        email = payload['email']
        password = payload['password']
        hashed_password = utils.encode(password)
        query = f"select * from auth where email = '{email}' "
        cursor.execute(query)
        user_record_from_db = cursor.fetchone()
        if user_record_from_db: #user record is found
            raise Exception(f"user with {email} already exist, please sign in")
        else:
            query = f"insert into auth (user, email, password) values ('{username}','{email}', '{hashed_password}')"
            cursor.execute(query)
            conn.commit()
            return {"status": "ok", "data": 'user signed up successfully'}
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST
                            , str(e))

    finally:
        cursor.close()
        conn.close()


@router.post('/signin')
def sign_in(user_data: dict, response : Response):
  print(user_data)
  conn = database.get_db()
  cursor = conn.cursor()
  try:
    email = user_data['email']
    password = user_data['password']
    query = f"select * from auth where email = '{email}'"
    print(query)
    cursor.execute(query)
    user_record_from_db = cursor.fetchone() 
    if not user_record_from_db: # user record is not found, report error
      raise Exception(f"user with {email} doesnt exists, please signup first")
    else: # user record is found, proceed with sign in
      print(user_record_from_db)
      if not utils.verify_password(password, user_record_from_db[2]): # user entered wrong password
        raise Exception(f"incorrect username or password. Please try again")
      else: # user record found and passwords match
        query = "insert into user_sessions(email, session_token, created_at, expiry) values (%s,%s,%s,%s)"
        session_token = utils.generate_session_token()
        created_at = datetime.now()
        expiry = datetime.now() + datetime.timedelta(minutes = 3)
        cursor.execute(query, [email,session_token,created_at,expiry])
        conn.commit
        response.set_cookie('session_token', session_token)
        return {"status": "ok", "data": 'user logged in successfully'}

  except Exception as e:
    raise HTTPException(status.HTTP_400_BAD_REQUEST
                       ,str(e))
  finally:
    cursor.close()
    conn.close()  

@router.get('/signout')
def sign_out():
    pass
