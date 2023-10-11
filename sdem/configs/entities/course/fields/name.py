from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseConfig
from sqlalchemy import String


class Name(ABC):
    """
    Abstract base class representing the configuration for a name field.

    This class provides configuration options for a field representing the name of a course,
    including its database-specific attributes, Pydantic model configuration, and type information.

    Attributes:
        alias (str): The alias of the name field.
        name (str): The name of the name field.
        description (str): The description of the name field.
        required (bool): Indicates if the name field is required.
        nullable (bool): Indicates if the name field can be nullable in the database (SQL-specific).
        sql_type (Type): The SQL-specific type for the name field.
        type (Type): The type of the field.
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the name field.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "name"
    name: str = "name"
    description: str = "Represents the name of the course"
    required: bool = True
    nullable: bool = False
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
