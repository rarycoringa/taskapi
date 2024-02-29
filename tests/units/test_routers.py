from typing import List

from fastapi import FastAPI
from fastapi import APIRouter

from taskapi import TaskAPIRouter

class TestTaskAPIRouter:
    def test_class_is_api_router_subclass(self):
        assert issubclass(TaskAPIRouter, APIRouter)

    def test_instance_is_api_router_instance(self):
        assert isinstance(TaskAPIRouter(), APIRouter)

    def test_instance_can_be_included(self):
        api: FastAPI = FastAPI()
        router: TaskAPIRouter = TaskAPIRouter()

        api.include_router(router)

    def test_instantiate_with_default_values(self):
        router: TaskAPIRouter = TaskAPIRouter()

        assert router.prefix == "/taskapi"
        assert isinstance(router.tags, list)
        assert len(router.tags) > 0
        assert router.tags[0] == "tasks"

    def test_instantiate_with_custom_values(self):
        custom_prefix: str = "/dummyapi"
        custom_tags: List[str] = ["dummy_tag", "another_dummy_tag"]
        
        router: TaskAPIRouter = TaskAPIRouter(custom_prefix, custom_tags)

        assert router.prefix == custom_prefix
        assert isinstance(router.tags, list)
        assert len(router.tags) == len(custom_tags)
        assert router.tags == custom_tags
