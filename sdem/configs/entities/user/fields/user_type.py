from abc import ABC, abstractmethod
from enum import Enum
from typing import Type

from pydantic import BaseConfig
from sqlalchemy import Integer

from sdem.enums.user_type import UserTypes


class UserType(ABC):
    """
    Abstract base class representing the configuration for a user_type field.

    This class provides configuration options for a user_type field, including its SQL-specific attributes,
    Pydantic model configuration, and user_type information.

    Attributes:
        alias (str): The alias of the user_type field.
        name (str): The name of the user_type field.
        description (str): The description of the user_type field.
        required (bool): Indicates if the user_type field is required.
        nullable (bool): Indicates if the user_type field can be nullable in the database (SQL-specific).
        sql_type (Type[Enum]): The SQL-specific type for the user_type field.
        type (Type[Enum]): The type of the field, represented as an enum.
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the type field.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "user_type"
    name: str = "user_type"
    description: str = "Represents the type of the user"
    required: bool = True
    nullable: bool = False
    sql_type = Integer  # Use EnumField to represent enum type in SQLAlchemy
    type: Type[Enum] = UserTypes  # Set the type as the ContentType enum
    model_config: Type[BaseConfig] = BaseConfig
    class_validators = {}

    @abstractmethod
    def abstract_method(self):
        """
        An abstract method that should be implemented by subclasses.
        """
        pass
