from datetime import date

import pytest
from sqlalchemy.orm import sessionmaker

from sdem.configs.sql.sql_db_config import SQLDbConfig
from sdem.entities.sql.learner import Learner as SQLLearner  # noqa
from sdem.entities.sql.user import User as SQLUser
from sdem.entities.sql.user_session import UserSession as SQLUserSession  # noqa
from sdem.enums.user_type import UserTypes


# Assuming you have a function that creates an SQLAlchemy session
@pytest.fixture
def db_session():
    SQLDbConfig.create_tables()
    Session = sessionmaker(bind=SQLDbConfig.engine)
    session = Session()
    yield session
    session.close()


# Test your User operations
def test_create_user(db_session):
    # Create a new User object with the desired attributes
    user_sql = SQLUser(
        created_at=date(2023, 8, 1),
        email="test@example.com",
        username="testuser",
        is_active=True,
        phone_number="12345678",
        password_hash="hashed_password",
        user_type=UserTypes.SC,
    )
    db_session.add(user_sql)
    db_session.commit()

    # Retrieve the user from the database and check attributes
    retrieved_user = (
        db_session.query(SQLUser).filter_by(email="test@example.com").first()
    )
    assert retrieved_user is not None
    assert retrieved_user.username == "testuser"
    # Add more assertions as needed


def test_update_user(db_session):
    user_sql = db_session.query(SQLUser).get(1)
    user_sql.email = "updated_test@example.com"
    user_sql.is_active = False
    db_session.commit()

    updated_user = (
        db_session.query(SQLUser).filter_by(email="updated_test@example.com").first()
    )
    assert updated_user is not None
    assert updated_user.is_active == False


def test_retrieve_user_by_id(db_session):
    existing_user_sql = db_session.query(SQLUser).get(1)
    assert existing_user_sql is not None
    assert existing_user_sql.email == "updated_test@example.com"


def test_delete_user(db_session):
    existing_user_sql = db_session.query(SQLUser).get(11)
    db_session.delete(existing_user_sql)
    db_session.commit()


if __name__ == "__main__":
    pytest.main()
