from abc import ABC, abstractmethod


class Learner(ABC):
    """
    Abstract base class representing the configuration for a learner Entity.

    This class provides configuration options for a learner Entity, its database-specific attributes.

    Attributes:
        table_name (str): The table name of the learner Entity.
        model_name (str): The model name of the Learner Entity.

    Methods:
        abstract_method: An abstract method that should be implemented by subclasses.
    """

    table_name: str = "learners"
    model_name: str = "Learner"

    @abstractmethod
    def abstract_method(self):
        """
        An abstract method that should be implemented by subclasses.
        """
        pass
