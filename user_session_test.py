from datetime import datetime

from sqlalchemy.exc import NoResultFound  # noqa

from sdem.configs.sql.sql_db_config import SQLDbConfig
from sdem.entities.sql.learner import Learner as SQLLearner  # noqa
from sdem.entities.sql.user import User as SQLUser  # noqa
from sdem.entities.sql.user_session import UserSession as SQLUserSession

# Init SQL Config & Create Tables
SQLDbConfig.create_tables()

# Create a new UserSession object with the desired attributes
created_at = datetime.now()
user_session = SQLUserSession(
    secret_key="secret_key_here",
    created_at=created_at,
    user_id=1,
)

print("\nSQL Insert")
# Save the UserSession object to the database
user_session.save()

# Print the retrieved UserSession object
print(user_session)

# Updating some values
user_session.secret_key = "updated_secret_key_here"

print("\nSQL Update")
# Save the UserSession object to the database
user_session.save()

# Print the retrieved UserSession object
print(user_session)

print("\nSQL Retrieve")
existing_user_session = SQLUserSession(id=1)
existing_user_session.refresh()
print(existing_user_session)

print("\nVerify User relation")
existing_user_session.refresh(fetch_user=True)
print(existing_user_session.user)
