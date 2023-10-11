from datetime import date, timedelta

from pydantic import BaseModel
from pydantic.fields import FieldInfo

from sdem.configs.entities.user_session.fields.created_at import (
    CreatedAt as UserSessionCreatedAtConfig,
)
from sdem.configs.entities.user_session.fields.id import Id as UserSessionIdConfig
from sdem.configs.entities.user_session.fields.secret_key import (
    SecretKey as UserSessionSecretKeyConfig,
)
from sdem.fields.created_at_field import CreatedAtPydanticField
from sdem.fields.id_field import IdPydanticField
from sdem.fields.secret_key_field import SecretKeyPydanticField


class UserSession(BaseModel):
    """
    UserSession model represents a user_session entity.

    Attributes:
        id (int): The ID of the user_session.
        secret_key (str): secret key of the user_session.
        expiry_date (date): date of expiration of the user_session.
        created_at (date): date of creation of the user_session.


    """

    id: int = (
        IdPydanticField(
            alias=UserSessionIdConfig.alias,
            name=UserSessionIdConfig.name,
            required=UserSessionIdConfig.required,
            type_=UserSessionIdConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=UserSessionIdConfig.alias,
                name=UserSessionIdConfig.name,
                required=UserSessionIdConfig.required,
                type=UserSessionIdConfig.type,
            ),
        ),
    )

    secret_key: str = (
        SecretKeyPydanticField(
            alias=UserSessionSecretKeyConfig.alias,
            name=UserSessionSecretKeyConfig.name,
            required=UserSessionSecretKeyConfig.required,
            type_=UserSessionSecretKeyConfig.type,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=UserSessionSecretKeyConfig.alias,
                name=UserSessionSecretKeyConfig.name,
                required=UserSessionSecretKeyConfig.required,
                type=UserSessionSecretKeyConfig.type,
            ),
        ),
    )

    expiry_date: date  # Declare expiry_date without initializing it

    created_at: date = (
        CreatedAtPydanticField(
            alias=UserSessionCreatedAtConfig.alias,
            name=UserSessionCreatedAtConfig.name,
            required=UserSessionCreatedAtConfig.required,
            model_config=BaseModel,
            field_info=FieldInfo(
                alias=UserSessionCreatedAtConfig.alias,
                name=UserSessionCreatedAtConfig.name,
                required=UserSessionCreatedAtConfig.required,
            ),
        ),
    )

    def __init__(
        self,
        id: int,
        secret_key: str,
        created_at: date,
    ):
        """
        Constructs a UserSession instance.

        Args:
            id (int): The ID of the user_session.
            secret_key (str): secret key of the user_session.
             expiry_date (date): date of expiration of the user_session.
            created_at (date): date of creation of the user_session.
        """
        self.id = id
        self.secret_key = secret_key
        self.expiry_date = created_at + timedelta(hours=72)  # Calculate expiry_date
        self.created_at = created_at

    def __str__(self):
        """
        Return a string representation of the user_session model.

        Returns:
            str: A string representation of the user_session model.
        """
        return (
            f"<User(id={self.id},"
            f" secret_key={self.secret_key}, created_at={self.created_at},"
            f" expiry_date={self.expiry_date},"
        )

    class Config:
        """
        Configuration class for the user_session model.

        Attributes:
            from_attributes (bool): Flag to enable ORM mode for the model.
            arbitrary_types_allowed (bool): Flag to allow arbitrary types in the model.
        """

        from_attributes = True
        arbitrary_types_allowed = True
