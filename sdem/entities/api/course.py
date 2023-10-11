from pydantic import BaseModel
from pydantic.fields import FieldInfo

from sdem.configs.entities.course.fields.id import Id as CourseIdConfig
from sdem.configs.entities.course.fields.is_hidden import (
    IsHidden as CourseIsHiddenConfig,
)
from sdem.configs.entities.course.fields.markdown_content import (
    MarkdownContent as CourseMarkdownContentConfig,
)
from sdem.configs.entities.course.fields.name import Name as CourseNameConfig
from sdem.configs.entities.course.fields.order import Order as CourseOrderConfig
from sdem.configs.entities.course.fields.type import Type as CourseTypeConfig
from sdem.enums.content_type import ContentType
from sdem.fields.id_field import IdPydanticField
from sdem.fields.is_hidden_field import IsHiddenPydanticField
from sdem.fields.markdown_content_field import MarkdownContentPydanticField
from sdem.fields.name_field import NamePydanticField
from sdem.fields.order_field import OrderPydanticField
from sdem.fields.type_field import TypePydanticField


class Course(BaseModel):
    """
    Course model represents a course entity.

    Attributes:
        id (int): The ID of the course.
        name (str): The name of the course.
        type (int): The type of the course.
        order (int): The order of the course.
        is_hidden (bool): Indicates if the course is hidden.
        markdown_content (str): The markdown content of the course.
    """

    id: int = (
        IdPydanticField(
            alias=CourseIdConfig.alias,
            name=CourseIdConfig.name,
            required=CourseIdConfig.required,
            type_=CourseIdConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=CourseIdConfig.alias,
                name=CourseIdConfig.name,
                required=CourseIdConfig.required,
                type=CourseIdConfig.type,
            ),
        ),
    )
    name: str = (
        NamePydanticField(
            alias=CourseNameConfig.alias,
            name=CourseNameConfig.name,
            required=CourseNameConfig.required,
            type_=CourseNameConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=CourseNameConfig.alias,
                name=CourseNameConfig.name,
                required=CourseNameConfig.required,
                type=CourseNameConfig.type,
            ),
        ),
    )
    type: ContentType = (
        TypePydanticField(
            alias=CourseTypeConfig.alias,
            name=CourseTypeConfig.name,
            required=CourseTypeConfig.required,
            type_=CourseTypeConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=CourseTypeConfig.alias,
                name=CourseTypeConfig.name,
                required=CourseTypeConfig.required,
                type=CourseTypeConfig.type,
            ),
        ),
    )
    order: int = (
        OrderPydanticField(
            alias=CourseOrderConfig.alias,
            name=CourseOrderConfig.name,
            required=CourseOrderConfig.required,
            type_=CourseOrderConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=CourseOrderConfig.alias,
                name=CourseOrderConfig.name,
                required=CourseOrderConfig.required,
                type=CourseOrderConfig.type,
            ),
        ),
    )
    is_hidden: bool = (
        IsHiddenPydanticField(
            alias=CourseIsHiddenConfig.alias,
            name=CourseIsHiddenConfig.name,
            required=CourseIsHiddenConfig.required,
            type_=CourseIsHiddenConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=CourseIsHiddenConfig.alias,
                name=CourseIsHiddenConfig.name,
                required=CourseIsHiddenConfig.required,
                type=CourseIsHiddenConfig.type,
            ),
        ),
    )
    markdown_content: str = (
        MarkdownContentPydanticField(
            alias=CourseMarkdownContentConfig.alias,
            name=CourseMarkdownContentConfig.name,
            required=CourseMarkdownContentConfig.required,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=CourseMarkdownContentConfig.alias,
                name=CourseMarkdownContentConfig.name,
                required=CourseMarkdownContentConfig.required,
            ),
        ),
    )

    def __init__(
        self,
        name: str,
        type: ContentType,
        order: int,
        is_hidden: bool,
        markdown_content: str,
        id: int = None,
    ):
        """
        Constructs a Course instance.

        Args:
            id (int, optional): The ID of the course.
            name (str): The name of the course.
            type (int): The type of the course.
            order (int): The order of the course.
            is_hidden (bool): Indicates if the course is hidden.
            markdown_content (str): The markdown content of the course.
        """
        self.id = id
        self.name = name
        self.type = type
        self.order = order
        self.is_hidden = is_hidden
        self.markdown_content = markdown_content

    def __str__(self):
        """
        Return a string representation of the Course model.

        Returns:
            str: A string representation of the Course model, including its ID, name, type, order, is_hidden,
            and markdown_content.
        """
        return (
            f"<Course(id={self.id}, name={self.name}, type={self.type}, order={self.order},"
            f" is_hidden={self.is_hidden},markdown_content={self.markdown_content})>"
        )

    class Config:
        """
        Configuration class for the Course model.

        Attributes:
            from_attributes (bool): Flag to enable ORM mode for the model.
            arbitrary_types_allowed (bool): Flag to allow arbitrary types in the model.
        """

        from_attributes = True
        arbitrary_types_allowed = True
