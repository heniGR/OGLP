from datetime import date

from pydantic import BaseModel
from pydantic.fields import FieldInfo

from sdem.configs.entities.user.fields.created_at import (
    CreatedAt as UserCreatedAtConfig,
)
from sdem.configs.entities.user.fields.email import Email as UserEmailConfig
from sdem.configs.entities.user.fields.id import Id as UserIdConfig
from sdem.configs.entities.user.fields.is_active import IsActive as USerIsActiveConfig
from sdem.configs.entities.user.fields.password_1hash import (
    PasswordHash as UserPasswordHashConfig,
)
from sdem.configs.entities.user.fields.phone_number import (
    PhoneNumber as UserPhoneNumberConfig,
)
from sdem.configs.entities.user.fields.user_type import UserType as UserTypeConfig
from sdem.configs.entities.user.fields.username import UserName as UserUsernameConfig
from sdem.enums.user_type import UserTypes
from sdem.fields.created_at_field import CreatedAtPydanticField
from sdem.fields.email_field import EmailPydanticField
from sdem.fields.id_field import IdPydanticField
from sdem.fields.is_active_field import IsActivePydanticField
from sdem.fields.password_1hash_field import PasswordHashPydanticField
from sdem.fields.phone_number_field import PhoneNumberPydanticField
from sdem.fields.user_type_field import UserTypePydanticField
from sdem.fields.username_field import UsernamePydanticField


class User(BaseModel):
    """
    User model represents a user entity.

    Attributes:
        id (int): The ID of the user.
        email (str, optional): The email of the user.
        created_at (date): date of creation of the user.
        is_active (bool): Indicates whether the user is active or no.
        phone_number (str, optional): The phone number of the user.
        password_hash (str): The password of the user.
        username (str): The username of the user.
        user_type (UserTypes): The type of the user.


    """

    id: int = (
        IdPydanticField(
            alias=UserIdConfig.alias,
            name=UserIdConfig.name,
            required=UserIdConfig.required,
            type_=UserIdConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=UserIdConfig.alias,
                name=UserIdConfig.name,
                required=UserIdConfig.required,
                type=UserIdConfig.type,
            ),
        ),
    )

    email: str = (
        EmailPydanticField(
            alias=UserEmailConfig.alias,
            name=UserEmailConfig.name,
            required=UserEmailConfig.required,
            type_=UserEmailConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=UserEmailConfig.alias,
                name=UserEmailConfig.name,
                required=UserEmailConfig.required,
                type=UserEmailConfig.type,
            ),
        ),
    )
    username: str = (
        UsernamePydanticField(
            alias=UserUsernameConfig.alias,
            name=UserUsernameConfig.name,
            required=UserUsernameConfig.required,
            type_=UserUsernameConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=UserUsernameConfig.alias,
                name=UserUsernameConfig.name,
                required=UserUsernameConfig.required,
                type=UserUsernameConfig.type,
            ),
        ),
    )
    created_at: date = (
        CreatedAtPydanticField(
            alias=UserCreatedAtConfig.alias,
            name=UserCreatedAtConfig.name,
            required=UserCreatedAtConfig.required,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=UserCreatedAtConfig.alias,
                name=UserCreatedAtConfig.name,
                required=UserCreatedAtConfig.required,
            ),
        ),
    )
    is_active: bool = (
        IsActivePydanticField(
            alias=USerIsActiveConfig.alias,
            name=USerIsActiveConfig.name,
            required=USerIsActiveConfig.required,
            type_=USerIsActiveConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=USerIsActiveConfig.alias,
                name=USerIsActiveConfig.name,
                required=USerIsActiveConfig.required,
                type=USerIsActiveConfig.type,
            ),
        ),
    )
    phone_number: str = (
        PhoneNumberPydanticField(
            alias=UserPhoneNumberConfig.alias,
            name=UserPhoneNumberConfig.name,
            required=UserPhoneNumberConfig.required,
            type_=UserPhoneNumberConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=UserPhoneNumberConfig.alias,
                name=UserPhoneNumberConfig.name,
                required=UserPhoneNumberConfig.required,
                type=UserPhoneNumberConfig.type,
            ),
        ),
    )
    password_hash: str = (
        PasswordHashPydanticField(
            alias=UserPasswordHashConfig.alias,
            name=UserPasswordHashConfig.name,
            required=UserPasswordHashConfig.required,
            type_=UserPasswordHashConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=UserPasswordHashConfig.alias,
                name=UserPasswordHashConfig.name,
                required=UserPasswordHashConfig.required,
                type=UserPasswordHashConfig.type,
            ),
        ),
    )
    user_type: UserTypes = (
        UserTypePydanticField(
            alias=UserTypeConfig.alias,
            name=UserTypeConfig.name,
            required=UserTypeConfig.required,
            type_=UserTypeConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=UserTypeConfig.alias,
                name=UserTypeConfig.name,
                required=UserTypeConfig.required,
                type=UserTypeConfig.type,
            ),
        ),
    )

    def __init__(
        self,
        id: int,
        created_at: date,
        email: str,
        username: str,
        is_active: bool,
        phone_number: str,
        password_hash: str,
        user_type: UserTypes,
    ):
        """
        Constructs a User instance.

        Args:
            id (int): The ID of the user.
            email (str, optional): The email of the user.
            created_at (date): date of creation of the user.
            is_active (bool): Indicates whether the user is active or no.
            phone_number (str, optional): The phone number of the user.
            password_hash (str): The password of the user.
            username (str): The username of the user.
            user_type (UserTypes): The type of the user.

        """
        self.id = id
        self.created_at = created_at
        self.email = email
        self.username = username
        self.is_active = is_active
        self.phone_number = phone_number
        self.password_hash = password_hash
        self.user_type = user_type

    def __str__(self):
        """
        Return a string representation of the user model.

        Returns:
            str: A string representation of the user model.
        """
        return (
            f"<User(id={self.id}, email={self.email}, username={self.username},"
            f" is_active={self.is_active}, phone_number={self.phone_number},user_type={self.user_type},"
            f" created_at={self.created_at}, password_hash={self.password_hash})>"
        )

    class Config:
        """
        Configuration class for the user model.

        Attributes:
            from_attributes (bool): Flag to enable ORM mode for the model.
            arbitrary_types_allowed (bool): Flag to allow arbitrary types in the model.
        """

        from_attributes = True
        arbitrary_types_allowed = True
