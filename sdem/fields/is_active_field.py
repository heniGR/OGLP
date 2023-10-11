from sdem.fields.base.pydantic_field import PydanticField
from sdem.fields.base.sql_field import SQLAlchemyColumn

IsActiveSQLField = SQLAlchemyColumn
"""
Alias for the `SQLAlchemyColumn` class representing an SQL field for `is_active` attribute.
This alias can be used to specify an SQL field type in a field configuration for `is_active` attribute.
"""

IsActivePydanticField = PydanticField
"""
Alias for the `PydanticField` class representing a Pydantic field for `is_active` attribute.
This alias can be used to specify a Pydantic field type in a field configuration for `is_active` attribute.
"""
