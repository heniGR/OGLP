import pytest
from sqlalchemy.orm import sessionmaker

from sdem.configs.sql.sql_db_config import SQLDbConfig
from sdem.entities.sql.learner import Learner as SQLLearner
from sdem.entities.sql.user import User as SQLUser  # noqa
from sdem.entities.sql.user_session import UserSession as SQLUserSession  # noqa


@pytest.fixture
def db_session():
    SQLDbConfig.create_tables()
    Session = sessionmaker(bind=SQLDbConfig.engine)
    session = Session()
    yield session
    session.close()


def test_create_learner(db_session):
    # Create a new SQLLearner object
    learner_sql = SQLLearner(first_name="baycii", last_name="labs", type=1, user_id=12)
    db_session.add(learner_sql)
    db_session.commit()

    # Verify the learner has been created
    assert learner_sql.id is not None


def test_update_learner(db_session):
    learner_sql = db_session.query(SQLLearner).get(5)
    learner_sql.first_name = "baycii updated"
    db_session.commit()

    # Verify the learner's first name has been updated
    assert learner_sql.first_name == "baycii updated"


def test_retrieve_learner(db_session):
    existing_learner_sql = db_session.query(SQLLearner).get(5)
    assert existing_learner_sql is not None
    assert existing_learner_sql.first_name == "baycii updated"


def test_verify_user_relation(db_session):
    existing_learner_sql = db_session.query(SQLLearner).get(5)
    existing_learner_sql.refresh(fetch_user=True)

    # Verify the associated user data
    assert existing_learner_sql.user is not None


def test_delete_learner(db_session):
    existing_learner_sql = db_session.query(SQLLearner).get(5)

    # Delete the learner
    db_session.delete(existing_learner_sql)
    db_session.commit()


if __name__ == "__main__":
    pytest.main()
