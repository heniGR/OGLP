from sdem.fields.base.mongo_field import MongoIntField
from sdem.fields.base.pydantic_field import PydanticField
from sdem.fields.base.sql_field import SQLAlchemyColumn

IdSQLField = SQLAlchemyColumn
"""
Alias for the `SQLAlchemyColumn` class representing an SQL field.
This alias can be used to specify an SQL field type in a field configuration.
"""

IdMongoField = MongoIntField
"""
Alias for the `MongoField` class representing a MongoDB field.
This alias can be used to specify a MongoDB field type in a field configuration.
"""

IdPydanticField = PydanticField
"""
Alias for the `PydanticField` class representing a Pydantic field.
This alias can be used to specify a Pydantic field type in a field configuration.
"""
