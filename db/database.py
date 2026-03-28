from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from db.config import setting

async_engine = create_async_engine(
    url=setting.DATABASE_URL_aiosqlite,
    echo=True
)

session = async_sessionmaker(async_engine)


async def get_session() -> AsyncSession:
    async with session() as conn:
        yield conn


if __name__ == '__main__':
    ...
