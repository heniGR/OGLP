# Import the necessary module or class
from sdem.configs.no_sql.no_sql_db_config import MongoDbConfig
from sdem.configs.sql.sql_db_config import SQLDbConfig
from sdem.entities.mongo.course import Course as MongoCourse
from sdem.entities.sql.course import Course as SQLCourse

# Init NoSQL Config & Connect to MongoDB
MongoDbConfig.connect()

# Init SQL Config & Create Tables in Postgres
SQLDbConfig.create_tables()

# Create a new SQLCourse object with the desired attributes
course_sql = SQLCourse(name="test", type=2, order=1, is_hidden=True)

print("\nSQL Insert")
# Save the SQLCourse object to the database
course_sql.save()

# Print the retrieved SQLCourse object
print(course_sql)

# Updating some values
course_sql.name = "updated_test_name"
course_sql.order = 3

print("\nSQL Update")
# Save the SQLCourse object to the database
course_sql.save()

# Print the retrieved SQLCourse object
print(course_sql)

# Create a new MongoCourse object with the desired attributes
course_mongo = MongoCourse(id=course_sql.id, markdown_content="#Dummy")

print("\nNoSQL Insert")
# Save the MongoCourse object to MongoDB
course_mongo.save()
# Print the retrieved MongoCourse object
print(course_mongo)
# Updating some values
course_mongo.markdown_content = "#NewDummy"

print("\nNoSQL Update")
# Save the MongoCourse object to MongoDB
course_mongo.save()

# Print the retrieved MongoCourse object
print(course_mongo)


print("\nSQL Retrieve")
existing_course_sql = SQLCourse(id=10)
existing_course_sql.refresh()
print(existing_course_sql)

print("\nNoSQL Retrieve")
existing_course_mongo = MongoCourse(id=11)
existing_course_mongo.refresh()
print(existing_course_mongo)
