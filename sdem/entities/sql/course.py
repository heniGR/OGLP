from sqlalchemy.exc import NoResultFound

from sdem.configs.entities.course.fields.id import Id as CourseIdConfig
from sdem.configs.entities.course.fields.is_hidden import (
    IsHidden as CourseIsHiddenConfig,
)
from sdem.configs.entities.course.fields.name import Name as CourseNameConfig
from sdem.configs.entities.course.fields.order import Order as CourseOrderConfig
from sdem.configs.entities.course.fields.type import Type as CourseTypeConfig
from sdem.configs.sql.sql_db_config import SQLDbConfig
from sdem.fields.id_field import IdSQLField
from sdem.fields.is_hidden_field import IsHiddenSQLField
from sdem.fields.name_field import NameSQLField
from sdem.fields.order_field import OrderSQLField
from sdem.fields.type_field import TypeSQLField


class Course(SQLDbConfig.base):
    """
    Course class represents a course SQL model used for exchanging data with SQL Database.
    This class inherits from SQLDbConfig.base, which provides the base configuration for SQL database tables.

    Attributes:
        __tablename__ (str): The name of the database table for Course objects.
        id (IdSQLField): The unique identifier for the course.
        name (NameSQLField): The name of the course.
        type (TypeSQLField): The type of the course.
        order (OrderSQLField): The order of the course.
        is_hidden (IsHiddenSQLField): Indicates if the course is hidden or not.
    """

    __tablename__: str = str(__name__).lower()

    id = IdSQLField(
        CourseIdConfig.sql_type,
        name=CourseIdConfig.name,
        primary_key=CourseIdConfig.primary_key,
        nullable=CourseIdConfig.nullable,
    )
    name = NameSQLField(
        CourseNameConfig.sql_type,
        name=CourseNameConfig.name,
        nullable=CourseNameConfig.nullable,
    )
    type = TypeSQLField(
        CourseTypeConfig.sql_type,
        name=CourseTypeConfig.name,
        nullable=CourseTypeConfig.nullable,
    )
    order = OrderSQLField(
        CourseOrderConfig.sql_type,
        name=CourseOrderConfig.name,
        nullable=CourseOrderConfig.nullable,
    )
    is_hidden = IsHiddenSQLField(
        CourseIsHiddenConfig.sql_type,
        name=CourseIsHiddenConfig.name,
        nullable=CourseIsHiddenConfig.nullable,
    )

    def __init__(self, name=None, type=None, order=None, is_hidden=None, id=None):
        """
        Initialize a Course object.

        Args:
            id (int, optional): The unique identifier for the course.
            name (str, optional): The name of the course.
            type (int, optional): The type of the course.
            order (int, optional): The order of the course.
            is_hidden (bool, optional): Indicates if the course is hidden or not.
        """
        self.id = id
        self.name = name
        self.type = type
        self.order = order
        self.is_hidden = is_hidden

    def save(self):
        """
        Save the Course object to the SQL database and return the ID.
        """
        session = SQLDbConfig.session_local()
        session.add(self)
        session.commit()
        session.refresh(self)  # Refresh the object to get the ID
        session.close()
        return self

    def delete(self):
        """
        Delete the Course object from the SQL database.
        """
        session = SQLDbConfig.session_local()
        session.delete(self)
        session.commit()
        session.close()

    def refresh(self):
        """
        Refresh the Course object with the latest data from the database.

        Raises:
            NoResultFound: If the Course with the given ID does not exist.#
        """
        session = SQLDbConfig.session_local()
        try:
            refreshed_course = session.query(Course).filter_by(id=self.id).one()
            self.name = refreshed_course.name
            self.type = refreshed_course.type
            self.order = refreshed_course.order
            self.is_hidden = refreshed_course.is_hidden
        except NoResultFound:
            raise NoResultFound("Course with the given ID does not exist.")
        finally:
            session.close()

    def __str__(self):
        """
        Return a string representation of the Course object.

        Returns:
            str: A string representation of the Course object, including its ID, name, type, order, and is_hidden.
        """
        return (
            f"<Course(id={self.id}, name={self.name}, type={self.type}, order={self.order}, "
            f"is_hidden={self.is_hidden})>"
        )
