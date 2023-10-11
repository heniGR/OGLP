from mongoengine import Document, DoesNotExist

from sdem.configs.entities.course.fields.id import Id as CourseIdConfig
from sdem.configs.entities.course.fields.markdown_content import MarkdownContent
from sdem.configs.no_sql.no_sql_db_config import MongoDbConfig
from sdem.fields.id_field import IdMongoField
from sdem.fields.markdown_content_field import MarkdownContentMongoField


class Course(Document):
    """
    Course document represents a course entity in MongoDB.

    Attributes:
        id (int): The ID of the course.
        markdown_content (str): The markdown content of the course.

    Meta:
        collection (str): The name of the MongoDB collection where the documents are stored.
        db_alias (str): The alias of the database used to save this document.
    """

    meta = {
        "collection": str(__name__).lower(),
        "db_alias": MongoDbConfig.db_name,
    }

    id = IdMongoField(
        db_field=CourseIdConfig.db_field,
        required=CourseIdConfig.required,
        primary_key=CourseIdConfig.primary_key,
    )
    markdown_content = MarkdownContentMongoField(
        db_field=MarkdownContent.db_field,
        required=MarkdownContent.required,
    )

    def __init__(self, id, markdown_content=None, **kwargs):
        """
        Initialize a Course document.

        Args:
            id (int): The ID of the course.
            markdown_content (str, optional): The markdown content of the course. Defaults to None.
            **kwargs: Additional keyword arguments for future flexibility.
        """
        super().__init__(**kwargs)
        self.id = id
        self.markdown_content = markdown_content

    def refresh(self):
        """
        Refresh the Course object with the latest data from the database.

        Raises:
            DoesNotExist: If the Course document with the object's ID does not exist.
        """
        try:
            refreshed_course = Course.objects.get(
                id=self.id
            )  # Retrieve the Course document from MongoDB
            self._data = (
                refreshed_course._data
            )  # Update the object's data with the refreshed data
            self._changed_fields = set()  # Clear any tracked changes
        except DoesNotExist:
            raise DoesNotExist("Course document with the object's ID does not exist.")

    def __str__(self):
        """
        Return a string representation of the Course document.

        Returns:
            str: A string representation of the Course document, including its ID.
        """
        return f"<Course(id={self.id}, markdown_content={self.markdown_content})>"
