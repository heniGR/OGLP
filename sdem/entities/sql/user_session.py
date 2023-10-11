from sqlalchemy import ForeignKey
from sqlalchemy.exc import NoResultFound

from sdem.configs.entities.user_session.fields.created_at import (
    CreatedAt as UserSessionCreatedAtConfig,
)
from sdem.configs.entities.user_session.fields.expiry_date import (
    ExpiryDate as UserSessionExpiryDateConfig,
)
from sdem.configs.entities.user_session.fields.id import Id as UserSessionIdConfig
from sdem.configs.entities.user_session.fields.secret_key import (
    SecretKey as UserSessionSecretKeyConfig,
)
from sdem.configs.entities.user_session.fields.user_id import UserId as UserIdConfig
from sdem.configs.entities.user_session.user_session import (
    UserSession as UserSessionConfig,
)
from sdem.configs.sql.sql_db_config import SQLDbConfig
from sdem.fields.created_at_field import CreatedAtSQLField
from sdem.fields.expiry_date_field import ExpiryDateSQLField
from sdem.fields.foreign_key_field import ForeignKeySQLField
from sdem.fields.id_field import IdSQLField
from sdem.fields.secret_key_field import SecretKeySQLField


class UserSession(SQLDbConfig.base):
    """
    user_session class represents a user_session SQL model used for exchanging data with SQL Database.
    This class inherits from SQLDbConfig.Base, which provides the base configuration for SQL database tables.

    Attributes:
        __tablename__ (str): The name of the database table for user_session objects.

          id (IdSQLField): The ID of the user_session.
          secret_key (SecretKeySQLField): secret key of the user_session.
          expiry_date (ExpiryDateSQLField): date of expiration of the user_session.
          created_at (CreatedAtSQLField): date of creation of the user_session.
          user_id (ForeignKeySQLField): The foreign key of the user and the user_session.
          user (lazy SQLUser): The relationship between the user_session and the user.


    """

    __tablename__: str = UserSessionConfig.table_name

    id = IdSQLField(
        UserSessionIdConfig.sql_type,
        name=UserSessionIdConfig.name,
        primary_key=UserSessionIdConfig.primary_key,
        nullable=UserSessionIdConfig.nullable,
    )
    secret_key = SecretKeySQLField(
        UserSessionSecretKeyConfig.sql_type,
        name=UserSessionSecretKeyConfig.name,
        nullable=UserSessionSecretKeyConfig.nullable,
    )
    created_at = CreatedAtSQLField(
        UserSessionCreatedAtConfig.sql_type,
        name=UserSessionCreatedAtConfig.name,
        nullable=UserSessionCreatedAtConfig.nullable,
        default=UserSessionCreatedAtConfig.default,
    )
    expiry_date = ExpiryDateSQLField(
        UserSessionExpiryDateConfig.sql_type,
        name=UserSessionExpiryDateConfig.name,
        nullable=UserSessionExpiryDateConfig.nullable,
        default=UserSessionExpiryDateConfig.default,
    )
    user_id = ForeignKeySQLField(
        UserIdConfig.sql_type,
        ForeignKey(UserIdConfig.foreign_key, ondelete=UserIdConfig.ondelete),
        nullable=UserIdConfig.nullable,
    )

    def __init__(
        self,
        id=None,
        secret_key=None,
        expiry_date=None,
        created_at=None,
        user=None,
        user_id=None,
    ):
        """
        Initialize a User_session object.

        Args:
          id (int, optional): The ID of the user_session.
          secret_key (str, optional): secret key of the user_session.
          expiry_date (date, optional): date of expiration of the user_session.
          created_at (date, optional): date of creation of the user_session.
          user_id (ForeignKeySQLField, optional): The foreign key of the user and the user_session.
          user (lazy SQLUser, optional): The relationship between the user_session and the user.


        """
        self.id = id
        self.secret_key = secret_key
        self.expiry_date = expiry_date
        self.created_at = created_at
        self.user_id = user_id
        if user:
            self.user = user

    def save(self):
        """
        Save the UserSession object to the SQL database and return the ID.
        """
        session = SQLDbConfig.session_local()
        session.add(self)
        session.commit()
        session.refresh(self)  # Refresh the object to get the ID
        session.close()
        return self

    def delete(self):
        """
        Delete the UserSession object from the SQL database.
        """
        session = SQLDbConfig.session_local()
        if session.query(UserSession).filter_by(id=self.id).count() == 1:
            session.delete(self)
            session.commit()
        else:
            raise NoResultFound(
                "User_session with the given ID is not persisted in the database."
            )
        session.close()

    def refresh(self, fetch_user=False):
        """
        Refresh the User_session object with the latest data from the database.
        Args:
            fetch_user (SQLUser, optional): The user object.

        Raises:
            NoResultFound: If the User_session with the given ID does not exist.
        """
        session = SQLDbConfig.session_local()
        try:
            refreshed_user_session = (
                session.query(UserSession).filter_by(id=self.id).one()
            )

            self.secret_key = refreshed_user_session.secret_key
            self.expiry_date = refreshed_user_session.expiry_date
            self.created_at = refreshed_user_session.created_at
            self.user_id = refreshed_user_session.user_id
            if fetch_user:
                self.user = refreshed_user_session.user

        except NoResultFound:
            raise NoResultFound("User_session with the given ID does not exist.")
        finally:
            session.close()

    def __str__(self):
        """
        Return a string representation of the user_session model.

        Returns:
            str: A string representation of the user_session model.
        """
        return (
            f"<User(id={self.id},"
            f" secret_key={self.secret_key}, expiry_date={self.expiry_date},created_at={self.created_at},"
            f" user_id={self.user_id})>"
        )
