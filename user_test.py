# Import the necessary modules
from datetime import date

from sqlalchemy.exc import NoResultFound  # noqa

from sdem.configs.sql.sql_db_config import SQLDbConfig
from sdem.entities.sql.learner import Learner as SQLLearner  # noqa
from sdem.entities.sql.user import User as SQLUser
from sdem.entities.sql.user_session import UserSession as SQLUserSession  # noqa
from sdem.enums.user_type import UserTypes

# Init SQL Config & Create Tables in Postgres
SQLDbConfig.create_tables()

# Create a new User object with the desired attributes
user_sql = SQLUser(
    created_at=date(2023, 8, 1),
    email="test2@example.com",
    username="heni",
    is_active=True,
    phone_number="12345678",
    password_hash="hashed_password3",
    user_type=UserTypes.SC,  # Use the UserTypes enum here
)

print("\nSQL Insert")
# Save the User object to the database
user_sql.save()

# Print the retrieved User object
print(user_sql)

# Updating some values
user_sql.email = "updated_test@example.com"
user_sql.is_active = False

print("\nSQL Update")
# Save the User object to the database
user_sql.save()

# Print the retrieved User object
print(user_sql)

print("\nSQL Retrieve")
existing_user_sql = SQLUser(id=1)
existing_user_sql.refresh()
print(existing_user_sql)

print("\nVerify Relations")
existing_user_sql.refresh(fetch_user_sessions=True, fetch_learner=True)


print("UserSessions:")
for US in existing_user_sql.user_sessions:
    print(US)
print("Learner:")
print(existing_user_sql.learner)
