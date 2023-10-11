from abc import ABC, abstractmethod
from datetime import datetime, timedelta  # Import datetime and timedelta
from enum import Enum
from typing import Type

from pydantic import BaseConfig
from sqlalchemy import DateTime


class ExpiryDate(ABC):
    """
    Abstract base class representing the configuration for an expiry_date field.

    This class provides configuration options for an expiry_date field, including its SQL-specific attributes,
    Pydantic model configuration, and expiry_date information.

    Attributes:
        alias (str): The alias of the expiry_date field.
        name (str): The name of the expiry_date field.
        description (str): The description of the expiry_date field.
        required (bool): Indicates if the expiry_date field is required.
        nullable (bool): Indicates if the expiry_date field can be nullable in the database (SQL-specific).
        default  (datetime): Indicates the default value for the expiry_date field.
        sql_type (DateTime): The SQL-specific expiry_date for the expiry_date field.
        type (Type[Enum]): The expiry_date of the field, represented as an enum.
        model_config (Type[BaseConfig]): The Pydantic model configuration class.
        class_validators: A dictionary of class validators for the expiry_date field.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    alias: str = "expiry_date"
    name: str = "expiry_date"
    description: str = "Represents the expiry date of the user_session "
    required: bool = True
    nullable: bool = False

    # Use datetime for calculations
    default: datetime = datetime.now() + timedelta(hours=72)

    sql_type = DateTime(timezone=True)  # Use SQLAlchemy's DateTime type
    type: Type[Enum] = datetime  # Use datetime type
    model_config: Type[BaseConfig] = BaseConfig
    class_validators = {}

    @abstractmethod
    def abstract_method(self):
        """
        An abstract method that should be implemented by subclasses.
        """
        pass
