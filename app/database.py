from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config import DB_URL

BASE: DeclarativeMeta = declarative_base()
ENGINE = create_engine(DB_URL, echo=True)
SESSION = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
