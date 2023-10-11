from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseConfig
from sqlalchemy import String


class PhoneNumber(ABC):
    """
    Abstract base class representing the configuration for a phone_number field.

    This class provides configuration options for a field representing the phone_number of a user,
    including its database-specific attributes, Pydantic model configuration, and type information.

    Attributes:
        alias (str): The alias of the phone_number field.
        name (str): The name of the phone_number field.
        description (str): The description of the phone_number field.
        required (bool): Indicates if the phone_number field is required.
        nullable (bool): Indicates if the phone_number field can be nullable in the database (SQL-specific).
        sql_type (Type): The SQL-specific type for the phone_number field.
        type (Type): The type of the field.
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the phone_number field.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "phone_number"
    name: str = "phone_number"
    description: str = "Represents the phone number of the user"
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
