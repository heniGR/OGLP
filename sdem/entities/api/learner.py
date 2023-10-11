from pydantic import BaseModel
from pydantic.fields import FieldInfo

from sdem.configs.entities.learner.fields.first_name import (
    FirstName as LearnerFirstNameConfig,
)
from sdem.configs.entities.learner.fields.id import Id as LearnerIdConfig
from sdem.configs.entities.learner.fields.last_name import (
    LastName as LearnerLastNameConfig,
)
from sdem.configs.entities.learner.fields.type import Type as LearnerTypeConfig
from sdem.enums.learner_type import LearnerType
from sdem.fields.first_name_field import FirstNamePydanticField
from sdem.fields.id_field import IdPydanticField
from sdem.fields.last_name_field import LastNamePydanticField
from sdem.fields.type_field import TypePydanticField


class Learner(BaseModel):
    """
    Learner model represents a learner entity.

    Attributes:
        id (int): The ID of the learner.
        first_name (str, optional): The first name of the learner.
        last_name (str, optional): The last name of the learner.
        type (int, optional): The type of the learner.

    """

    id: int = (
        IdPydanticField(
            alias=LearnerIdConfig.alias,
            name=LearnerIdConfig.name,
            required=LearnerIdConfig.required,
            type_=LearnerIdConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=LearnerIdConfig.alias,
                name=LearnerIdConfig.name,
                required=LearnerIdConfig.required,
                type=LearnerIdConfig.type,
            ),
        ),
    )
    first_name: str = (
        FirstNamePydanticField(
            alias=LearnerFirstNameConfig.alias,
            name=LearnerFirstNameConfig.name,
            required=LearnerFirstNameConfig.required,
            type_=LearnerFirstNameConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=LearnerFirstNameConfig.alias,
                name=LearnerFirstNameConfig.name,
                required=LearnerFirstNameConfig.required,
                type=LearnerFirstNameConfig.type,
            ),
        ),
    )
    last_name: str = (
        LastNamePydanticField(
            alias=LearnerLastNameConfig.alias,
            name=LearnerLastNameConfig.name,
            required=LearnerLastNameConfig.required,
            type_=LearnerLastNameConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=LearnerLastNameConfig.alias,
                name=LearnerLastNameConfig.name,
                required=LearnerLastNameConfig.required,
                type=LearnerLastNameConfig.type,
            ),
        ),
    )
    type: LearnerType = (
        TypePydanticField(
            alias=LearnerTypeConfig.alias,
            name=LearnerTypeConfig.name,
            required=LearnerTypeConfig.required,
            type_=LearnerTypeConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=LearnerTypeConfig.alias,
                name=LearnerTypeConfig.name,
                required=LearnerTypeConfig.required,
                type=LearnerTypeConfig.type,
            ),
        ),
    )

    def __init__(
        self,
        first_name: str,
        last_name: str,
        type: LearnerType,
        id: int = None,
    ):
        """
        Constructs a Learner instance.

        Args:
            id (int, optional): The ID of the learner.
            first_name (str): The first name of the learner.
            last_name (str): The last name of the learner.
            type (int): The type of the learner.
        """
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.type = type

    def __str__(self):
        """
        Return a string representation of the Learner model.

        """
        return f"<Learner(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, type={self.type})>"

    class Config:
        """
        Configuration class for the Learner model.

        Attributes:
            from_attributes (bool): Flag to enable ORM mode for the model.
            arbitrary_types_allowed (bool): Flag to allow arbitrary types in the model.
        """

        from_attributes = True
        arbitrary_types_allowed = True
