from sdem.entities.api.learner import Learner as ApiLearner
from sdem.entities.sql.learner import Learner as SqlLearner


class Learner:
    """
    Learner class represents a learner entity.

    Attributes:
        learner_api (ApiLearner): An instance of ApiLearner representing the learner in the API exchanges.
        learner_sql (SqlLearner): An instance of SqlLearner representing the learner in the SQL database exchanges.

    Methods:
        _init_: Initializes a new instance of the Learner class.

    Raises:
        ValueError: If any of the parameters learner_api or learner_sql is None.
        TypeError: If any of the parameters is not an instance of its respective class.
    """

    def __init__(
        self,
        learner_api: ApiLearner = None,
        learner_sql: SqlLearner = None,
    ):
        """
        Initialize the Learner class with instances of ApiLearner and SqlLearner.

        Args:
            learner_api (ApiLearner, optional): An instance of the ApiLearner class.
            learner_sql (SqlLearner, optional): An instance of the SqlLearner class.

        Raises:
            ValueError: If any of the parameters learner_api or learner_sql is None.
            TypeError: If any of the parameters is not an instance of its respective class.
        """
        if learner_api is not None:
            if not isinstance(learner_api, ApiLearner):
                raise TypeError("learner_api must be an instance of ApiLearner.")
        else:
            raise ValueError("learner_api must not be None.")

        if learner_sql is not None:
            if not isinstance(learner_sql, SqlLearner):
                raise TypeError("learner_sql must be an instance of SqlLearner.")
        else:
            raise ValueError("learner_sql must not be None.")

        self.learner_api = learner_api
        self.learner_sql = learner_sql
