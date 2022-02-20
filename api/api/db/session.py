from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm.session import sessionmaker
from core.config import settings

ASYNC_POSTGRES_URL = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
    settings.POSTGRESQL_USER,
    settings.POSTGRESQL_PASSWORD,
    settings.POSTGRESQL_HOST,
    settings.POSTGRESQL_PORT,
    settings.POSTGRESQL_DB
)

engine = create_async_engine(ASYNC_POSTGRES_URL)

db_session = sessionmaker(bind=engine, class_=AsyncSession)


def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
