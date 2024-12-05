import pytest

from src.engine import DATABASE_URL, engine

from alembic.config import Config
from alembic import command

from sqlalchemy.orm import sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session")
def apply_migrations():
    """Run Alembic migrations before tests."""
    alembic_cfg = Config("./alembic.ini")  # Path to your alembic.ini file
    alembic_cfg.set_main_option("sqlalchemy.url", DATABASE_URL)
    # Run migrations
    command.upgrade(alembic_cfg, "head")

    # Rollback migrations at the end of the session
    yield
    command.downgrade(alembic_cfg, "base")


@pytest.fixture
def db_session(apply_migrations):
    """Provide a database session for tests."""
    # Create a new database session
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()