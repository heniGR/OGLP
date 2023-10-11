# Import the necessary module or class
from sdem.configs.sql.sql_db_config import SQLDbConfig
from sdem.entities.sql.learner import Learner as SQLLearner
from sdem.entities.sql.user import User as SQLUser  # noqa
from sdem.entities.sql.user_session import UserSession as SQLUserSession  # noqa

# Init SQL Config & Create Tables in Postgres
SQLDbConfig.create_tables()

# Create a new SQLLearner object
learner_sql = SQLLearner(first_name="baycii", last_name="labs", type=1, user_id=1)
print("\nSQL Insert")
learner_sql.save()
print(learner_sql)

# Updating some values
learner_sql.first_name = "baycii updated"
print("\nSQL Update")
learner_sql.save()
print(learner_sql)

# Retrieving a SQL Learner object
print("\nSQL Retrieve")
existing_learner_sql = SQLLearner(id=1)
existing_learner_sql.refresh()
print(existing_learner_sql)

print("\nVerify User relation")
existing_learner_sql.refresh(fetch_user=True)
print(existing_learner_sql.user)
