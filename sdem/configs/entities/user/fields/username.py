from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseConfig
from sqlalchemy import String


class UserName(ABC):
    """
    Abstract base class representing the configuration for a user_name field.

    This class provides configuration options for a field representing the user_name of a user,
    including its database-specific attributes, Pydantic model configuration, and type information.

    Attributes:
        alias (str): The alias of the user_name field.
        name (str): The name of the user_name field.
        description (str): The description of the user_name field.
        required (bool): Indicates if the user_name field is required.
        nullable (bool): Indicates if the user_name field can be nullable in the database (SQL-specific).
         unique (bool): Indicates if the user_name field should be unique.
        sql_type (Type): The SQL-specific type for the user_name field.
        type (Type): The type of the field.
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the user_name field.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "user_name"
    name: str = "user_name"
    description: str = "Represents the username of the user"
    required: bool = True
    nullable: bool = False
    unique: bool = True
    sql_type = String
    type: Type = str
    model_config: Type[BaseConfig] = BaseConfig
    class_validators = {}

    @abstractmethod
    def abstract_method(self):
        """
        An abstract method that should be implemented by subclasses.
        """
        pass
