#installed uvicorn and fastAPI

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import greet, todos

app = FastAPI() #instance of fast API
origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST","DELETE"],
    allow_headers=["*"],
)

#Middleware
app.include_router(greet.router)
app.include_router(todos.router)


