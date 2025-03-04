from fastapi import APIRouter, HTTPException, status
import database, utils
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


@router.get('/signin')
def sign_in(payload: dict):
    print(payload)
    conn = database.get_db()
    cursor = conn.cursor()
    try:
        email = payload['email']
        #username = payload['username']
        password = payload['password']
        hashed_password = utils.encode(password)
        query = f"select * from auth where email = '{email}' "

    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST
                            , str(e))

    finally:
        cursor.close()
        conn.close()

@router.get('/signout')
def sign_out():
    pass
