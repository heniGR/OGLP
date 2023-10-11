from sdem.entities.api.user_session import UserSession as ApiUserSession
from sdem.entities.sql.user_session import UserSession as SqlUserSession


class UserSession:
    """
    User_session class represents a user_session entity.

    Attributes:
    user_session_api (ApiUserSession): An instance of ApiUserSession representing the user_session in the API exchanges.
    user_session_sql (SqlUserSession): An instance of SqlUserSession representing the user_session in the SQL database
    exchanges.

    Methods:
        _init_: Initializes a new instance of the User_session class.

    Raises:
        ValueError: If any of the parameters user_session_api or user_session_sql is None.
        TypeError: If any of the parameters is not an instance of its respective class.
    """

    def __init__(
        self,
        user_session_api: ApiUserSession = None,
        user_session_sql: SqlUserSession = None,
    ):
        """
        Initialize the User_session class with instances of ApiUserSession and SqlUserSession(just testing)

        Args:
            user_session_api (ApiUser, optional): An instance of the ApiUserSession class.
            user_session_sql (SqlUser, optional): An instance of the SqlUserSession class.


        Raises:
            ValueError: If any of the parameters user_session_api or user_session_sql is None.
            TypeError: If any of the parameters is not an instance of its respective class.
        """
        if user_session_api is not None:
            if not isinstance(user_session_api, ApiUserSession):
                raise TypeError(
                    "user_session_api must be an instance of ApiUserSession."
                )
        else:
            raise ValueError("user_session_api must not be None.")

        if user_session_sql is not None:
            if not isinstance(user_session_sql, SqlUserSession):
                raise TypeError(
                    "user_session_sql must be an instance of SqlUserSession."
                )
        else:
            raise ValueError("user_session_sql must not be None.")

        self.user_api = user_session_api
        self.user_sql = user_session_sql
