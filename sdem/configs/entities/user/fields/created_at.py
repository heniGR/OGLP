from abc import ABC, abstractmethod
from datetime import date
from enum import Enum
from typing import Type

from pydantic import BaseConfig
from sqlalchemy import DateTime, func


class CreatedAt(ABC):
    """
    Abstract base class representing the configuration for an created_at field.

    This class provides configuration options for an created_at field, including its SQL-specific attributes,
    Pydantic model configuration, and created_at information.

    Attributes:
        alias (str): The alias of the created_at field.
        name (str): The name of the created_at field.
        description (str): The description of the created_at field.
        required (bool): Indicates if the created_at field is required.
        nullable (bool): Indicates if the created_at field can be nullable in the database (SQL-specific).
        default  (int):  Indicates the default value for the  created_at field.
        sql_type (int): The SQL-specific created_at for the created_at field.
        type (Type[Enum]): The created_at of the field, represented as an enum.
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the created_at field.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "created_at"
    name: str = "created_at"
    description: str = "Represents the date of the created user "
    required: bool = True
    nullable: bool = False
    default: date = func.now()
    sql_type = DateTime(timezone=True)
    type: Type[Enum] = date
    model_config: Type[BaseConfig] = BaseConfig
    class_validators = {}

    @abstractmethod
    def abstract_method(self):
        """
        An abstract method that should be implemented by subclasses.
        """
        pass
