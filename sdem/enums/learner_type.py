from enum import Enum

import enum_tools.documentation

enum_tools.documentation.INTERACTIVE = True


@enum_tools.documentation.document_enum
class LearnerType(int, Enum):
    """
    Enumeration of Learner types.

    This enumeration represents the different types of Learners available.
    Each learner type is assigned a unique integer value.
    """

    M = 1  # doc: Male
    F = 2  # doc: Female
    C = 3  # doc: Class

    def __str__(self):
        """
        Returns the string representation of the learner type.
        Returns:
           str: The name of the learner type.
        """
        return self.name

    def __int__(self):
        """
        Returns the integer representation of the learner type.
        Returns:
           int: The value of the learner type.
        """
        return self.value
