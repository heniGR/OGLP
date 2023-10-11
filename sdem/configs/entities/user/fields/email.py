from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseConfig
from sqlalchemy import String


class Email(ABC):
    """
    Abstract base class representing the configuration for the email field.

    This class provides configuration options for a field representing the email of the user,
    including its database-specific attributes, Pydantic model configuration, and type information.

    Attributes:
        alias (str): The alias of the email field.
        name (str): The name of the email field.
        description (str): The description of the email field.
        required (bool): Indicates if the email field is required.
        nullable (bool): Indicates if the email field can be nullable in the database (SQL-specific).
        sql_type (Type): The SQL-specific type for the email field.
        type (Type): The type of the field.
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the email field.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "email"
    name: str = "email"
    description: str = "Represents the email of the user"
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
