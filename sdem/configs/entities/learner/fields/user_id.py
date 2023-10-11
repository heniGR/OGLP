from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseConfig
from sqlalchemy import Integer

from sdem.configs.entities.user.user import User as UserConfig


class UserId(ABC):
    """
    Abstract base class representing the configuration for  User_id field.

    This class provides configuration options for  User_id field, including its database-specific attributes,
    and type information.

    Attributes:
        alias (str): The alias of the User_id field.
        name (str): The name of the User_id field.
        description (str): The description of the User_id field.
        required (bool): Indicates if the User_id field is required.
        nullable (bool): Indicates if the User_id field can be nullable in the database (SQL-specific).
        sql_type (Type): The SQL-specific type for the User_id field.
        ondelete (str) : indicates the config for the foreignkey.
        foreign_key (str): indicates the table_name for the foreignkey.
        lazy (str) : indicates the type of relationship object.
        type (Type): The type of the field.
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the User_id field.
        unique(bool): unique constraint for the foreignkey

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "user_id"
    name: str = "user_id"
    description: str = "Represents the user_id foreignkey for the Learner"
    required: bool = True

    # SQL-specific fields
    nullable: bool = False
    sql_type = Integer
    ondelete = "CASCADE"
    foreign_key = UserConfig.table_name + ".id"
    unique: bool = True
    lazy = "select"
    type: Type = int
    model_config: Type[BaseConfig] = BaseConfig
    class_validators = {}

    @abstractmethod
    def abstract_method(self):
        """
        An abstract method that should be implemented by subclasses.
        """
        pass
