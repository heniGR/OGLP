from sqlalchemy import ForeignKey
from sqlalchemy.exc import NoResultFound

from sdem.configs.entities.learner.fields.first_name import (
    FirstName as LearnerFirstNameConfig,
)
from sdem.configs.entities.learner.fields.id import Id as LearnerIdConfig
from sdem.configs.entities.learner.fields.last_name import (
    LastName as LearnerLastNameConfig,
)
from sdem.configs.entities.learner.fields.type import Type as LearnerTypeConfig
from sdem.configs.entities.learner.fields.user_id import UserId as UserIdConfig
from sdem.configs.entities.learner.learner import Learner as LearnerConfig
from sdem.configs.sql.sql_db_config import SQLDbConfig
from sdem.fields.first_name_field import FirstNameSQLField
from sdem.fields.foreign_key_field import ForeignKeySQLField
from sdem.fields.id_field import IdSQLField
from sdem.fields.last_name_field import LastNameSQLField
from sdem.fields.type_field import TypeSQLField


class Learner(SQLDbConfig.base):
    """
    Learner class represents a learner SQL model used for exchanging data with SQL Database.
    This class inherits from SQLDbConfig.Base, which provides the base configuration for SQL database tables.

    Attributes:
        __tablename__ (str): The name of the database table for Learner objects.
        id (IdSQLField): The unique identifier for the learner.
        first_name (FirstNameSQLField, optional): The first name of the learner.
        last_name (LastNameSQLField, optional): The last name of the learner.
        type (TypeSQLField, optional): The type of the learner.
        user_id (ForeignKeySQLField): The foreign key of the user and the user_session.
        user (lazy SQLUser): The relationship between the user_session and the user.
    """

    __tablename__: str = LearnerConfig.table_name

    id = IdSQLField(
        LearnerIdConfig.sql_type,
        name=LearnerIdConfig.name,
        primary_key=LearnerIdConfig.primary_key,
        nullable=LearnerIdConfig.nullable,
    )
    first_name = FirstNameSQLField(
        LearnerFirstNameConfig.sql_type,
        name=LearnerFirstNameConfig.name,
        nullable=LearnerFirstNameConfig.nullable,
    )
    last_name = LastNameSQLField(
        LearnerLastNameConfig.sql_type,
        name=LearnerLastNameConfig.name,
        nullable=LearnerLastNameConfig.nullable,
    )
    type = TypeSQLField(
        LearnerTypeConfig.sql_type,
        name=LearnerTypeConfig.name,
        nullable=LearnerTypeConfig.nullable,
    )
    user_id = ForeignKeySQLField(
        UserIdConfig.sql_type,
        ForeignKey(UserIdConfig.foreign_key, ondelete=UserIdConfig.ondelete),
        nullable=UserIdConfig.nullable,
        unique=UserIdConfig.unique,
    )

    def __init__(
        self,
        first_name=None,
        last_name=None,
        type=None,
        id=None,
        user=None,
        user_id=None,
    ):
        """
        Initialize a Learner object.

        Args:
            id (int, optional): The unique identifier for the learner.
            first_name (str, optional): The first name of the learner.
            last_name (str, optional): The last name of the learner.
            type (int, optional): The type of the learner.
            user_id (ForeignKeySQLField, optional): The foreign key of the user and the user_session.
            user (lazy SQLUser, optional): The relationship between the user_session and the user.
        """
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.type = type
        self.user_id = user_id
        if user:
            self.user = user

    def save(self):
        """
        Save the Learner object to the SQL database and return the ID.
        """
        session = SQLDbConfig.session_local()
        session.add(self)
        session.commit()
        session.refresh(self)  # Refresh the object to get the ID
        session.close()
        return self

    def delete(self):
        """
        Delete the Learner object from the SQL database.
        """
        session = SQLDbConfig.session_local()
        session.delete(self)
        session.commit()
        session.close()

    def refresh(self, fetch_user=False):
        """
        Refresh the Learner object with the latest data from the database.

        Raises:
            NoResultFound: If the Learner with the given ID does not exist.
        """
        session = SQLDbConfig.session_local()
        try:
            refreshed_learner = session.query(Learner).filter_by(id=self.id).one()
            self.first_name = refreshed_learner.first_name
            self.last_name = refreshed_learner.last_name
            self.type = refreshed_learner.type
            self.user_id = refreshed_learner.user_id
            if fetch_user:
                self.user = refreshed_learner.user
        except NoResultFound:
            raise NoResultFound("Learner with the given ID does not exist.")
        finally:
            session.close()

    def __str__(self):
        """
        Return a string representation of the Learner object.

        Returns:
            str: A string representation of the Learner object, including its ID, first name, last name type and userID.
        """
        return (
            f"<Learner(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, type={self.type},"
            f" user_id={self.user_id})>"
        )
