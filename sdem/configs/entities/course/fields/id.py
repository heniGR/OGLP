from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseConfig
from sqlalchemy import Integer


class Id(ABC):
    """
    Abstract base class representing the configuration for an ID field.

    This class provides configuration options for an ID field, including its database-specific attributes,
    Pydantic model configuration, and type information.

    Attributes:
        alias (str): The alias of the ID field.
        name (str): The name of the ID field.
        description (str): The description of the ID field.
        required (bool): Indicates if the ID field is required.
        db_field (str): The name of the field in the database (MongoDB-specific).
        unique (bool): Indicates if the ID field should be unique (MongoDB-specific).
        nullable (bool): Indicates if the ID field can be nullable in the database (SQL-specific).
        autoincrement (bool): Indicates if the ID field should auto-increment in the database (SQL-specific).
        primary_key (bool): Indicates if the ID field is a primary key in the database (SQL-specific).
        sql_type (Type): The SQL-specific type for the ID field.
        type (Type): The type of the field.
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the ID field.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "id"
    name: str = "id"
    description: str = "Represents the unique identifier for the course"
    required: bool = True

    # MongoDB-specific fields
    db_field: str = "_id"
    unique: bool = True

    # SQL-specific fields
    nullable: bool = False
    autoincrement: bool = True
    primary_key: bool = True
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
