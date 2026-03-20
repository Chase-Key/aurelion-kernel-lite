"""
AgentOps Console — database setup.
SQLite by default. Swap DATABASE_URL to postgres:// for Railway.
"""
import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Use absolute path so the DB is always next to this file, regardless of cwd.
# This matters for the MCP server which VS Code starts from the workspace root.
_DEFAULT_DB = f"sqlite:///{Path(__file__).parent / 'agentops.db'}"
DATABASE_URL = os.getenv("DATABASE_URL", _DEFAULT_DB)

_connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=_connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
