from abc import ABC, abstractmethod


class User(ABC):
    """
    Abstract base class representing the configuration for a User Entity.

    This class provides configuration options for a User Entity, its database-specific attributes.

    Attributes:
        table_name (str): The table name of the User Entity.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    table_name: str = "users"

    @abstractmethod
    def abstract_method(self):
        """
        An abstract method that should be implemented by subclasses.
        """
        pass
