from sdem.entities.api.user import User as ApiUser
from sdem.entities.sql.user import User as SqlUser


class User:
    """
    User class represents a user entity.

    Attributes:
        user_api (ApiUser): An instance of ApiUser representing the user in the API exchanges.
        user_sql (SqlUser): An instance of SqlUser representing the user in the SQL database exchanges.

    Methods:
        _init_: Initializes a new instance of the User class.

    Raises:
        ValueError: If any of the parameters user_api or user_sql is None.
        TypeError: If any of the parameters is not an instance of its respective class.
    """

    def __init__(
        self,
        user_api: ApiUser = None,
        user_sql: SqlUser = None,
    ):
        """
        Initialize the User class with instances of ApiUser and SqlUser

        Args:
            user_api (ApiUser, optional): An instance of the ApiUser class.
            user_sql (SqlUser, optional): An instance of the SqlUser class.


        Raises:
            ValueError: If any of the parameters user_api or user_sql is None.
            TypeError: If any of the parameters is not an instance of its respective class.
        """
        if user_api is not None:
            if not isinstance(user_api, ApiUser):
                raise TypeError("user_api must be an instance of ApiUser.")
        else:
            raise ValueError("user_api must not be None.")

        if user_sql is not None:
            if not isinstance(user_sql, SqlUser):
                raise TypeError("user_sql must be an instance of SqlUser.")
        else:
            raise ValueError("user_sql must not be None.")

        self.user_api = user_api
        self.user_sql = user_sql
