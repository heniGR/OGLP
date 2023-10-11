from abc import ABC, abstractmethod

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class SQLDbConfig(ABC):
    """
    Abstract base class representing the configuration for SQL database connection.

    This class provides methods and attributes for establishing and managing a connection to a SQL database.

    Attributes:
        sqlalchemy_database_url (str): The SQLAlchemy database URL.
        engine (Engine): The SQLAlchemy engine for connecting to the database.
        session_local (sessionmaker): The sessionmaker for creating local sessions.
        base (DeclarativeMeta): The base class for declarative models.
    """

    # TODO Make it env secure params
    sqlalchemy_database_url = (
        "postgresql://lab2301:xftekko@localhost:5432/lab2301_test_db"
    )
    engine = create_engine(sqlalchemy_database_url)
    session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)
    base = declarative_base()

    @classmethod
    def create_tables(cls):
        """
        Create all tables defined in the SQLAlchemy models.
        """
        cls.base.metadata.create_all(cls.engine)

    @abstractmethod
    def abstract_method(self):
        """
        An abstract method that should be implemented by subclasses.
        """
        pass
