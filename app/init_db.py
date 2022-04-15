
from psycopg2 import cursor, connection, comm
from config import Config 
from os import environ

host = environ.get('AWS_db_HOST')
database="postgres",
user=environ.get('AWS_db_USER')
password=environ.get('AWS_db_PASSWORD')

# Open a cursor to perform database operations
cur = connection.cursor()


# Insert data into the table

cur.execute('INSERT INTO "PlatformUsers"(user_id, username, user_first_name, user_last_name, password_hash, daycare_facility, created_at, last_modified_at, is_archived, role, last_login)'
    'VALUES(


cur.execute("INSERT INTO books (title, author, pages_num, review)"
            "VALUES (
                {},{},{},{},{},{},{},{},{},{},{}.format('(nextval(user_id)','bcasterton0@state.gov','Barth','Casterton','vIE1lb9v','37B4','','','false','user','2/16/2022')", 
                {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}.format('(nextval(user_id)', , 'srenault1@chronoengine.com', 'Sampson', 'Renault', 'vo67AE', '30S6', '', '2021-05-23 10:41:30', 'true', 'user', '9/14/2021'),


conn.commit()

cur.close()
conn.close()
