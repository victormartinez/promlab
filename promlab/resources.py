from http import HTTPStatus
from typing import List

from fastapi import APIRouter

from promlab.telemetry.counter import http_requests_counter
from promlab.repository import users
from promlab.schema import User

router = APIRouter(tags=["users"])


@router.get("/users", status_code=HTTPStatus.OK, response_model=List[User])
async def list_users() -> None:
    http_requests_counter.inc()
    data = await users.list_users()
    return [User.model_validate(d) for d in data]
