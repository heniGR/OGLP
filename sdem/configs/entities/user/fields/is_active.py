from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseConfig
from sqlalchemy import Boolean


class IsActive(ABC):
    """
    Abstract base class representing the configuration for an is_active status field.

    This class provides configuration options for a field representing the activity status of a user,
    including its database-specific attributes, Pydantic model configuration, and type information.

    Attributes:
        alias (str): The alias of the is_active status field.
        name (str): The name of the is_active status field.
        description (str): The description of the is_active status field.
        required (bool): Indicates if the is_active status field is required.
        nullable (bool): Indicates if the is_active status field can be nullable in the database (SQL-specific).
        sql_type (Type): The SQL-specific type for the is_active status field.
        type (Type): The type of the field.
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the is_active status field.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "is_active"
    name: str = "is_active"
    description: str = "Represents the user activity status"
    required: bool = True

    # SQL-specific fields
    nullable: bool = False
    sql_type = Boolean
    type: Type = bool
    model_config: Type[BaseConfig] = BaseConfig
    class_validators = {}

    @abstractmethod
    def abstract_method(self):
        """
        An abstract method that should be implemented by subclasses.
        """
        pass
