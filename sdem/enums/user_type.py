from enum import Enum

import enum_tools.documentation

enum_tools.documentation.INTERACTIVE = True


@enum_tools.documentation.document_enum
class UserTypes(int, Enum):
    """
    Enumeration of User type of the user.
    This enumeration represents the different user types available for a user.
    Each user type is assigned a unique integer value.
    Attributes:
        FM (int): Family user type.
        SC (int): School user type.
        CL (int): Class user type.
        ST (int): Student user type.


    Methods:
        __int__: Returns the integer representation of the user type.
        __str__: Returns the string representation of the user type.
    """

    FM = 1  # doc:  Family
    SC = 2  # doc:  School
    CL = 3  # doc:  Class
    ST = 4  # doc:  Student

    def __int__(self):
        """
        Returns the integer  representation of the user type.
        Returns:
            str: The name of the user type.
        """
        return self.value

    def __str__(self):
        """
        Returns the string representation of the user type.
        Returns:
           str: The name of the user type.
        """
        return self.name
