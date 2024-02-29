import uuid

from typing import Any
from typing import Dict
from typing import List
from typing import Callable

from fastapi import APIRouter

def retrieve_task_id() -> Dict[str, uuid.UUID]:
    return {"task_id": uuid.uuid4()}

class TaskAPIRouter(APIRouter):
    def __init__(
        self,
        prefix: str = "/taskapi",
        tags: str = ["tasks"],
    ) -> None:
        super().__init__(
            prefix=prefix,
            tags=tags,
        )

        self.add_api_route("", retrieve_task_id, tags=["GET"], description="some description")

