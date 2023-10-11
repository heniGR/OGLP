from abc import ABC, abstractmethod


class UserSession(ABC):
    """
    Abstract base class representing the configuration for a UserSession Entity.

    This class provides configuration options for a UserSession Entity, its database-specific attributes.

    Attributes:
        table_name (str): The table name of the UserSession Entity.
        model_name (str): The model name of the UserSession Entity.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    table_name: str = "user_sessions"
    model_name: str = "UserSession"

    @abstractmethod
    def abstract_method(self):
        """
        An abstract method that should be implemented by subclasses.
        """
        pass
