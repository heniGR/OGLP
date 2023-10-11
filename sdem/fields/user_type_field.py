from sdem.fields.base.pydantic_field import PydanticField
from sdem.fields.base.sql_field import SQLAlchemyColumn

UserTypeSQLField = SQLAlchemyColumn
"""
Alias for the `SQLAlchemyColumn` class representing an SQL field for the `user_type` attribute.
This alias can be used to specify an SQL field type in a field configuration for the `type` attribute.
"""

UserTypePydanticField = PydanticField
"""
Alias for the `PydanticField` class representing a Pydantic field for the `user_type` attribute.
This alias can be used to specify a Pydantic field type in a field configuration for the `user_type` attribute.
"""
