from litestar import get, post, route, Request
from pydantic import BaseModel


@get('/')
async def index() -> dict:
    None