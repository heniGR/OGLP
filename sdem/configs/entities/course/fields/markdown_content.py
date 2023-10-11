from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseConfig


class MarkdownContent(ABC):
    """
    Abstract base class representing the configuration for a markdown content field.

    This class provides configuration options for a field representing the markdown content of a course,
    including its database-specific attributes, Pydantic model configuration, and type information.

    Attributes:
        alias (str): The alias of the markdown content field.
        name (str): The name of the markdown content field.
        description (str): The description of the markdown content field.
        required (bool): Indicates if the markdown content field is required.
        db_field (str): The name of the field in the database (MongoDB-specific).
        unique (bool): Indicates if the markdown content field should be unique (MongoDB-specific).
        nullable (bool): Indicates if the markdown content field can be nullable in the database (SQL-specific).
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the markdown content field.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "markdown_content"
    name: str = "markdown_content"
    description: str = "Represents the markdown_content of the course"
    required: bool = True

    # MongoDB-specific fields
    db_field: str = "markdown_content"
    unique: bool = False

    # SQL-specific fields
    nullable: bool = True
    model_config: Type[BaseConfig] = BaseConfig
    class_validators = {}

    @abstractmethod
    def abstract_method(self):
        """
        An abstract method that should be implemented by subclasses.
        """
        pass
