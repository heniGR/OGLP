from datetime import datetime

import pytest
from sqlalchemy.orm import sessionmaker

from sdem.configs.sql.sql_db_config import SQLDbConfig
from sdem.entities.sql.learner import Learner as SQLLearner  # noqa
from sdem.entities.sql.user import User as SQLUser  # noqa
from sdem.entities.sql.user_session import UserSession as SQLUserSession


# Assuming you have a function that creates an SQLAlchemy session
@pytest.fixture
def db_session():
    SQLDbConfig.create_tables()
    Session = sessionmaker(bind=SQLDbConfig.engine)
    session = Session()
    yield session
    session.close()


def test_create_user_session(db_session):
    # Create a new UserSession object with the desired attributes
    created_at = datetime.now()
    user_session = SQLUserSession(
        secret_key="testingSecret",
        created_at=created_at,
        user_id=2,
    )
    db_session.add(user_session)
    db_session.commit()

    # Add more assertions as needed


def test_update_user_session(db_session):
    user_session = db_session.query(SQLUserSession).get(1)
    user_session.secret_key = "updated_secret_key_here"
    db_session.commit()

    updated_user_session = db_session.query(SQLUserSession).get(1)
    assert updated_user_session is not None
    assert updated_user_session.secret_key == "updated_secret_key_here"


def test_retrieve_user_session(db_session):
    existing_user_session = db_session.query(SQLUserSession).get(1)
    assert existing_user_session is not None
    assert existing_user_session.secret_key == "updated_secret_key_here"


def test_delete_user_session(db_session):
    existing_user_session = db_session.query(SQLUserSession).get(1)
    db_session.delete(existing_user_session)
    db_session.commit()


if __name__ == "__main__":
    pytest.main()
