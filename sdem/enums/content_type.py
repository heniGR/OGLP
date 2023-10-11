from enum import Enum

import enum_tools.documentation

enum_tools.documentation.INTERACTIVE = True


@enum_tools.documentation.document_enum
class ContentType(int, Enum):
    """
    Enumeration of content type of the course.
    This enumeration represents the different content types available for a course.
    Each content type is assigned a unique integer value.
    Attributes:
        EM (int): Empty content type.
        MD (int): Markdown content type.
    Methods:
        __int__: Returns the integer representation of the content type.
    """

    EM = 1  # doc:  Empty
    MD = 2  # doc:  Markdown

    def __int__(self):
        """
        Returns the integer representation of the content type.
        Returns:
            int: The value of the content type.
        """
        return self.value

    def __str__(self):
        """
        Returns the string representation of the content type.
        Returns:
            str: The name of the content type.
        """
        return self.name
