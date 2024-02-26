from typing import Dict

from fastapi import FastAPI

taskapi: FastAPI = FastAPI(
    title="TaskAPI",
    description="A FastAPI extension to easily retrieve Celery tasks status"
)

@taskapi.get("/greeting")
def greeting(name: str) -> Dict[str, str]:

    response: Dict[str, str] = {
        "greeting": f"Hello, {name}!",
    }
    
    return response