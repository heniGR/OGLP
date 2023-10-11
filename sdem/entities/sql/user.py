from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import backref, relationship

from sdem.configs.entities.learner.learner import Learner as LearnerConfig
from sdem.configs.entities.user.fields.created_at import (
    CreatedAt as UserCreatedAtConfig,
)
from sdem.configs.entities.user.fields.email import Email as UserEmailConfig
from sdem.configs.entities.user.fields.id import Id as UserIdConfig
from sdem.configs.entities.user.fields.is_active import IsActive as USerIsActiveConfig
from sdem.configs.entities.user.fields.password_1hash import (
    PasswordHash as UserPasswordHashConfig,
)
from sdem.configs.entities.user.fields.phone_number import (
    PhoneNumber as UserPhoneNumberConfig,
)
from sdem.configs.entities.user.fields.user_type import UserType as UserTypeConfig
from sdem.configs.entities.user.fields.username import UserName as UserUsernameConfig
from sdem.configs.entities.user.user import User as UserConfig
from sdem.configs.entities.user_session.user_session import (
    UserSession as UserSessionConfig,
)
from sdem.configs.sql.sql_db_config import SQLDbConfig
from sdem.fields.created_at_field import CreatedAtSQLField
from sdem.fields.email_field import EmailSQLField
from sdem.fields.id_field import IdSQLField
from sdem.fields.is_active_field import IsActiveSQLField
from sdem.fields.password_1hash_field import PasswordHashSQLField
from sdem.fields.phone_number_field import PhoneNumberSQLField
from sdem.fields.user_type_field import UserTypeSQLField
from sdem.fields.username_field import UsernameSQLField


class User(SQLDbConfig.base):
    """
    user class represents a user SQL model used for exchanging data with SQL Database.
    This class inherits from SQLDbConfig.Base, which provides the base configuration for SQL database tables.

    Attributes:
        __tablename__ (str): The name of the database table for user objects.
      id (IdSQLField): The ID of the user.
        email (EmailSQLField): The type of payment for the user.
        created_at (CreatedAtSQLField): date of creation of the user.
        is_active (IsActiveSQLField): Indicates whether the user is active or no.
        phone_number (PhoneNumberSQLField): The phone number of the user.
        password_hash (PasswordHashSQLField): The password of the user.
        username (UsernameSQLField): The username of the user.
        user_type (UserTypeSQLField): The type of the user.
        user_sessions (lazy List[SQLUserSession]): List of related user_sessions.
        learner (lazy [SQLUserSession]): session of related learner.
    """

    __tablename__: str = UserConfig.table_name

    id = IdSQLField(
        UserIdConfig.sql_type,
        name=UserIdConfig.name,
        primary_key=UserIdConfig.primary_key,
        nullable=UserIdConfig.nullable,
    )
    email = EmailSQLField(
        UserEmailConfig.sql_type,
        name=UserEmailConfig.name,
        nullable=UserEmailConfig.nullable,
    )
    created_at = CreatedAtSQLField(
        UserCreatedAtConfig.sql_type,
        name=UserCreatedAtConfig.name,
        nullable=UserCreatedAtConfig.nullable,
        default=UserCreatedAtConfig.default,
    )
    is_active = IsActiveSQLField(
        USerIsActiveConfig.sql_type,
        name=USerIsActiveConfig.name,
        nullable=USerIsActiveConfig.nullable,
    )
    user_type = UserTypeSQLField(
        UserTypeConfig.sql_type,
        name=UserTypeConfig.name,
        nullable=UserTypeConfig.nullable,
    )

    username = UsernameSQLField(
        UserUsernameConfig.sql_type,
        name=UserUsernameConfig.name,
        nullable=UserUsernameConfig.nullable,
    )
    phone_number = PhoneNumberSQLField(
        UserPhoneNumberConfig.sql_type,
        name=UserPhoneNumberConfig.name,
        nullable=UserPhoneNumberConfig.nullable,
    )
    password_hash = PasswordHashSQLField(
        UserPasswordHashConfig.sql_type,
        name=UserPasswordHashConfig.name,
        nullable=UserPasswordHashConfig.nullable,
    )
    user_sessions = relationship(UserSessionConfig.model_name, backref=backref("user"))
    learner = relationship(LearnerConfig.model_name, uselist=False, backref="user")

    def __init__(
        self,
        id=None,
        created_at=None,
        is_active=is_active,
        user_type=None,
        username=None,
        phone_number=None,
        password_hash=None,
        email=None,
        user_sessions=None,
        learner=None,
    ):
        """
        Initialize a User object.

        Args:
           id (int, optional): The ID of the user.
        email (str, optional): The email of the user.
        created_at (date): date of creation of the user.
        is_active (bool, optional): Indicates whether the user is active or no.
        phone_number (str, optional): The phone number of the user.
        password_hash (str, optional): The password of the user.
        username (str, optional): The username of the user.
        user_type (UserTypes, optional): The type of the user.
        user_sessions (lazy List[SQLUserSession], optional): List of related user_sessions.
        learner (lazy [SQLUserSession], optional): session of related learner.
        """
        self.id = id
        self.created_at = created_at
        self.is_active = is_active
        self.user_type = user_type
        self.username = username
        self.phone_number = phone_number
        self.password_hash = password_hash
        self.email = email
        if user_sessions:
            self.user_sessions = user_sessions
        if learner:
            self.learner = learner

    def save(self):
        """
        Save the User object to the SQL database and return the ID.
        """
        session = SQLDbConfig.session_local()
        session.add(self)
        session.commit()
        session.refresh(self)  # Refresh the object to get the ID
        session.close()
        return self

    def delete(self):
        """
        Delete the User object from the SQL database.
        """
        session = SQLDbConfig.session_local()
        if session.query(User).filter_by(id=self.id).count() == 1:
            session.delete(self)
            session.commit()
        else:
            raise NoResultFound(
                "User with the given ID is not persisted in the database."
            )
        session.close()

    def refresh(self, fetch_user_sessions=None, fetch_learner=None):
        """
        Refresh the User object with the latest data from the database.
        fetch_user_sessions (List[SQLUserSession], optional): List of related UserSessions.
        fetch_learner (SQLUserSession, optional): Session of related learner.
        Raises:
            NoResultFound: If the User with the given ID does not exist.
        """
        session = SQLDbConfig.session_local()
        try:
            refreshed_user = session.query(User).filter_by(id=self.id).one()
            self.email = refreshed_user.email
            self.created_at = refreshed_user.created_at
            self.is_active = refreshed_user.is_active
            self.phone_number = refreshed_user.phone_number
            self.password_hash = refreshed_user.password_hash
            self.user_type = refreshed_user.user_type
            self.username = refreshed_user.username
            if fetch_user_sessions:
                self.user_sessions = refreshed_user.user_sessions
            if fetch_learner:
                self.learner = refreshed_user.learner
        except NoResultFound:
            raise NoResultFound("User with the given ID does not exist.")
        finally:
            session.close()

    def __str__(self):
        """
        Return a string representation of the user model.

        Returns:
            str: A string representation of the user model.
        """
        return (
            f"<User(id={self.id}, email={self.email}, username={self.username},"
            f" is_active={self.is_active}, phone_number={self.phone_number},user_type={self.user_type},"
            f" created_at={self.created_at}, password_hash={self.password_hash})>"
        )
