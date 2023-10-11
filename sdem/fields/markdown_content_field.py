from sdem.fields.base.mongo_field import MongoStringField
from sdem.fields.base.pydantic_field import PydanticField

MarkdownContentMongoField = MongoStringField
"""
Alias for the `MongoStringField` class representing a MongoDB string field.
This alias can be used to specify a MongoDB string field type in a field configuration.
"""

MarkdownContentPydanticField = PydanticField
"""
Alias for the `PydanticField` class representing a Pydantic field.
This alias can be used to specify a Pydantic field type in a field configuration.
"""
