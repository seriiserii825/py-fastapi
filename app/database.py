from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"
DB_PASSWORD = "serii1981"
DB_NAME = "postgres"

# generate url for alcemy database connection
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# create engine
engine = create_async_engine(DATABASE_URL, echo=True)

# create session maker
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# create base class
class Base(DeclarativeBase):
    pass
