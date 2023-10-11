from abc import ABC, abstractmethod
from enum import Enum
from typing import Type

from pydantic import BaseConfig
from sqlalchemy import Integer

from sdem.enums.learner_type import LearnerType


class Type(ABC):
    """
    Abstract base class representing the configuration for a type field.

    This class provides configuration options for a type field, including its SQL-specific attributes,
    Pydantic model configuration, and type information.

    Attributes:
        alias (str): The alias of the type field.
        name (str): The name of the type field.
        description (str): The description of the type field.
        required (bool): Indicates if the type field is required.
        nullable (bool): Indicates if the type field can be nullable in the database (SQL-specific).
        sql_type (Type[Enum]): The SQL-specific type for the type field.
        type (Type[Enum]): The type of the field, represented as an enum.
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the type field.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "learner_type"
    name: str = "learner_type"
    description: str = "Represents the type of the learner"
    required: bool = True
    nullable: bool = False
    sql_type = Integer  # Use EnumField to represent enum type in SQLAlchemy
    type: Type[Enum] = LearnerType  # Set the type as the LearnerType enum
    model_config: Type[BaseConfig] = BaseConfig
    class_validators = {}

    @abstractmethod
    def abstract_method(self):
        """
        An abstract method that should be implemented by subclasses.
        """
        pass
