from abc import ABC, abstractmethod

from mongoengine import connect, disconnect


class MongoDbConfig(ABC):
    """
    Abstract base class representing the configuration for MongoDB connection.

    This class provides methods for establishing and closing a connection to the MongoDB server.

    Attributes:
        host (str): The hostname of the MongoDB server.
        port (int): The port number of the MongoDB server.
        db_name (str): The name of the MongoDB database.
        username (str): The username for authenticating with the MongoDB server.
        password (str): The password for authenticating with the MongoDB server.
    """

    host = "localhost"
    port = 27017
    db_name = "mongo_test_db"
    username = "lab2301"
    password = "xftekko"

    @classmethod
    def connect(cls):
        """
        Establish a connection to the MongoDB server.
        """
        connect(
            db=cls.db_name,
            alias=cls.db_name,
            host=cls.host,
            port=cls.port,
            username=cls.username,
            password=cls.password,
        )

    @classmethod
    def disconnect(cls):
        """
        Close the connection to the MongoDB server.
        """
        disconnect()

    @abstractmethod
    def abstract_method(self):
        """
        An abstract method that should be implemented by subclasses.
        """
        pass
