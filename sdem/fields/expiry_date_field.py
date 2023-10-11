from sdem.fields.base.pydantic_field import PydanticField
from sdem.fields.base.sql_field import SQLAlchemyColumn

ExpiryDateSQLField = SQLAlchemyColumn
"""
Alias for the `SQLAlchemyColumn` class representing an SQL field for the `expiry_date` attribute.
This alias can be used to specify an SQL field type in a field configuration for the `expiry_date` attribute.
"""

ExpiryDatePydanticField = PydanticField
"""
Alias for the `PydanticField` class representing a Pydantic field for the `expiry_date` attribute.
This alias can be used to specify a Pydantic field type in a field configuration for the `expiry_date` attribute.
"""
