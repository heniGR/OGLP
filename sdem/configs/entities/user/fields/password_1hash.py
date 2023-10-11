from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseConfig
from sqlalchemy import String


class PasswordHash(ABC):
    """
    Abstract base class representing the configuration for a password_hash field.

    This class provides configuration options for a field representing the password_hash of a user,
    including its database-specific attributes, Pydantic model configuration, and type information.

    Attributes:
        alias (str): The alias of the password_hash field.
        name (str): The name of the password_hash field.
        description (str): The description of the password_hash field.
        required (bool): Indicates if the password_hash field is required.
        nullable (bool): Indicates if the password_hash field can be nullable in the database (SQL-specific).
        sql_type (Type): The SQL-specific type for the password_hash field.
        type (Type): The type of the field.
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the password_hash field.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "password_hash"
    name: str = "password_hash"
    description: str = "Represents the password of the user"
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
