from sdem.entities.api.course import Course as ApiCourse
from sdem.entities.mongo.course import Course as MongoCourse
from sdem.entities.sql.course import Course as SqlCourse


class Course:
    """
    Course class represents a course entity.

    Attributes:
        course_api (ApiCourse): An instance of ApiCourse representing the course in the API exchanges.
        course_sql (SqlCourse): An instance of SqlCourse representing the course in the SQL database exchanges.
        course_mongo (MongoCourse): An instance of MongoCourse representing the course in MongoDB exchanges.

    Methods:
        _init_: Initializes a new instance of the Course class.

    Raises:
        ValueError: If any of the parameters course_api, course_sql, or course_mongo is None.
        TypeError: If any of the parameters is not an instance of its respective class.
    """

    def __init__(
        self,
        course_api: ApiCourse = None,
        course_sql: SqlCourse = None,
        course_mongo: MongoCourse = None,
    ):
        """
        Initialize the Course class with instances of ApiCourse, SqlCourse, and MongoCourse.

        Args:
            course_api (ApiCourse, optional): An instance of the ApiCourse class.
            course_sql (SqlCourse, optional): An instance of the SqlCourse class.
            course_mongo (MongoCourse, optional): An instance of the MongoCourse class.

        Raises:
            ValueError: If any of the parameters course_api, course_sql, or course_mongo is None.
            TypeError: If any of the parameters is not an instance of its respective class.
        """
        if course_api is not None:
            if not isinstance(course_api, ApiCourse):
                raise TypeError("course_api must be an instance of ApiCourse.")
        else:
            raise ValueError("course_api must not be None.")

        if course_sql is not None:
            if not isinstance(course_sql, SqlCourse):
                raise TypeError("course_sql must be an instance of SqlCourse.")
        else:
            raise ValueError("course_sql must not be None.")

        if course_mongo is not None:
            if not isinstance(course_mongo, MongoCourse):
                raise TypeError("course_mongo must be an instance of MongoCourse.")
        else:
            raise ValueError("course_mongo must not be None.")

        self.course_api = course_api
        self.course_sql = course_sql
        self.course_mongo = course_mongo
