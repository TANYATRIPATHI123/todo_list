from fastapi import APIRouter

#router = FastAPI()
router = APIRouter(tags = ["greets"])
@router.get('/')
def greet() :
    return 'Hello'

@router.get('/greet/{name}')
def greetByName(name: str) :
    return f'Hello {name}'
