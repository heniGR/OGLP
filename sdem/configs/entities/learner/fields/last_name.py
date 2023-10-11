from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseConfig
from sqlalchemy import String


class LastName(ABC):
    """
    Abstract base class representing the configuration for a last name field.

    This class provides configuration options for a field representing the last name of a learner,
    including its database-specific attributes, Pydantic model configuration, and type information.

    Attributes:
        alias (str): The alias of the last name field.
        name (str): The name of the last name field.
        description (str): The description of the last name field.
        required (bool): Indicates if the last name field is required.
        nullable (bool): Indicates if the last name field can be nullable in the database (SQL-specific).
        sql_type (Type): The SQL-specific type for the last name field.
        type (Type): The type of the field.
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the last name field.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "last_name"
    name: str = "last_name"
    description: str = "Represents the last name of the learner"
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
