from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from asyncpg import connect

from config import (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DATABASE
)


async def create_database(
    user: str,
    password: str,
    host: str,
    port: str,
    name_database: str
):
    connection = await connect(
        user = user,
        password = password,
        host = host,
        port = port    
    )

    # with connection as 