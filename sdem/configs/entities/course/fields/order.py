from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseConfig
from sqlalchemy import Integer


class Order(ABC):
    """
    Abstract base class representing the configuration for an order field.

    This class provides configuration options for a field representing the order of a course,
    including its database-specific attributes, Pydantic model configuration, and type information.

    Attributes:
        alias (str): The alias of the order field.
        name (str): The name of the order field.
        description (str): The description of the order field.
        required (bool): Indicates if the order field is required.
        nullable (bool): Indicates if the order field can be nullable in the database (SQL-specific).
        sql_type (Type): The SQL-specific type for the order field.
        type (Type): The type of the field.
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the order field.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "order"
    name: str = "order"
    description: str = "Represents the order of the course"
    required: bool = True
    nullable: bool = False
    sql_type = Integer
    type: Type = int
    model_config: Type[BaseConfig] = BaseConfig
    class_validators = {}

    @abstractmethod
    def abstract_method(self):
        """
        An abstract method that should be implemented by subclasses.
        """
        pass
