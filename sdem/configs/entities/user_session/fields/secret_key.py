from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseConfig
from sqlalchemy import String


class SecretKey(ABC):
    """
    Abstract base class representing the configuration for a secret_key field.

    This class provides configuration options for a field representing the secret_key of a user,
    including its database-specific attributes, Pydantic model configuration, and type information.

    Attributes:
        alias (str): The alias of the secret_key field.
        name (str): The name of the secret_key field.
        description (str): The description of the secret_key field.
        required (bool): Indicates if the secret_key field is required.
        nullable (bool): Indicates if the secret_key field can be nullable in the database (SQL-specific).
        sql_type (Type): The SQL-specific type for the secret_key field.
        type (Type): The type of the field.
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the secret_key field.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "secret_key"
    name: str = "secret_key"
    description: str = "Represents the secret key of the user_session"
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
