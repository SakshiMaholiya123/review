from fastapi import FastAPI
from pydantic import BaseModel
from routes import  router

app=FastAPI()

app.include_router(router)