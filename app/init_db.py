
from psycopg2 import cursor, connection,
import psycopg2
from config import Config 
from decouple import config

try:
    dev_postgres_db = psycopg2.connect( 
                                        host = config('AWS_db_HOST'),
                                        database="postgres",
                                        user=config('AWS_db_USER'),
                                  xw      password=config('AWS_db_PASSWORD')
                                        )
# Open a cursor to perform database operat\ions
cursor = connection.cursor()
# Print PostgreSQL details
print("PostgreSQL server information")
print(connection.get_dsn_parameters(), "\n")
# Executing a SQL query
cursor.execute("SELECT version();")
# Fetch result
record = cursor.fetchone()
print("You are connected to - ", record, "\n")
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
# Insert data into the table

cursor.execute('INSERT INTO "PlatformUsers"(user_id, username, user_first_name, user_last_name, password_hash, daycare_facility, created_at, last_modified_at, is_archived, role, last_login)'
    'VALUES(


cur.execute("INSERT INTO books (title, author, pages_num, review)"
            "VALUES (
                {},{},{},{},{},{},{},{},{},{},{}.format('(nextval(user_id)','bcasterton0@state.gov','Barth','Casterton','vIE1lb9v','37B4','','','false','user','2/16/2022')", 
                {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}.format('(nextval(user_id)', , 'srenault1@chronoengine.com', 'Sampson', 'Renault', 'vo67AE', '30S6', '', '2021-05-23 10:41:30', 'true', 'user', '9/14/2021'),


conn.commit()

cur.close()
conn.close()
