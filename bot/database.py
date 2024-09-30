from pyexpat.errors import messages

from config import *
import pymysql
from mysql.connector import Error


from main import bot

CREATE_DB_SEEKSHELP = f"CREATE DATABASE IF NOT EXISTS {NAME_DB_SEEKSHELP}"

create_offershelp_table = f"""
CREATE TABLE IF NOT EXISTS {NAME_TB_OFFERSHELP} (
    username VARCHAR(100) UNIQUE,
    id VARCHAR(10) UNIQUE,
    spheres TINYTEXT DEFAULT NULL,
    short_description TINYTEXT DEFAULT NULL,
    rating INT(5) DEFAULT 100,
    points INT(5) DEFAULT 0,
    status BOOL DEFAULT 1
) ENGINE = InnoDB
"""
create_seekshelp_table = f"""
CREATE TABLE IF NOT EXISTS {NAME_TB_SEEKSHELP} (
    username VARCHAR(50) UNIQUE,
    id VARCHAR(10) UNIQUE,
    spheres TINYTEXT DEFAULT NULL,
    short_description TINYTEXT,
    deadline VARCHAR(10) DEFAULT 'd',
    status BOOL DEFAULT 1
) ENGINE = InnoDB
"""
create_site_table = f"""
CREATE TABLE IF NOT EXISTS {NAME_TB_SITE} (
    username VARCHAR(50),
    id VARCHAR(50) UNIQUE,
    points INT(5) DEFAULT 0
) ENGINE = InnoDB
"""
create_admins_table = f"""
CREATE TABLE IF NOT EXISTS {NAME_TB_ADMINS} (
    username VARCHAR(50) UNIQUE
) ENGINE = InnoDB
"""



"""
def create_connection(host_name, user_name, user_password, db_name):
    connections = None
    try:
        connections = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connections
connection = create_connection(f"{NAME_HOST}", f"{NAME_ADMIN}", f"{PASSWORD_ADMIN}", f"{NAME_DB_SEEKSHELP}")
"""

connection = pymysql.connect(host=f'{NAME_HOST}',
                             user=f'{NAME_ADMIN}',
                             password=f'{PASSWORD_ADMIN}',
                             database=f"{NAME_DB_SEEKSHELP}",
                             charset=f'{CHARSET}',
                             cursorclass=pymysql.cursors.DictCursor)

def create_database(connections, query):
    cursor = connections.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
create_database(connection, f"{CREATE_DB_SEEKSHELP}")


def execute_query(connections, query):
    cursor = connections.cursor()
    try:
        cursor.execute(query)
        connections.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connections, query):
    cursor = connections.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def add_users_seeks(connection, username, id):
    sql = f"INSERT INTO {NAME_TB_SEEKSHELP} (username, id) VALUE (%s, %s)" # QUERY содержится в файле config.py
    value = [(username, id)]
    cursor = connection.cursor()
    cursor.executemany(sql, value)
    connection.commit()

def exists_user(connections, username, db):
    sql = f"SELECT username FROM {db} WHERE username = '{username}'"
    exists = execute_read_query(connections, sql)
    return not len(exists)

def add_get_describe_offers(connections, username, id, spheres, short_description, db):
    sql = f"INSERT INTO {NAME_TB_OFFERSHELP} (username, id, spheres, short_description) VALUES (%s, %s, %s, %s)"
    value = [(username, id, spheres, short_description)]
    cursor = connections.cursor()
    cursor.executemany(sql, value)
    connections.comit()

def add_admins(connections, user_name):
    sql = f"INSERT INTO `{NAME_TB_ADMINS}` (`username`) VALUES ('{user_name}');"
    execute_query(connections, sql)

# Добавление данных uid и сферы помощи для обоих БД
def add_spheres_in_bd(connections, username, userid, spheres, db):
    sql_site = f"INSERT INTO `{NAME_TB_SITE}` (`username`, `id`) VALUES ('{username}', '{userid}');"
    sql = f"INSERT INTO `{db}`  (`username`, `id`, `spheres`) VALUES ('{username}', '{userid}', '{spheres}');"
    execute_query(connections, sql)
    execute_query(connections, sql_site)

def update_spheres_in_bd(connections, username, spheres, tb):
    cursor = connections.cursor()
    print(f"spheres = {spheres}")
    sql = f"UPDATE `{tb}` SET `spheres`= %s WHERE `username` = %s"
    value = [(spheres, username)]
    cursor.executemany(sql, value)
    connections.commit()

# первоначальное добавление данных о пользователе после НАЧАЛО -> Хочу помочь (Нужна помощь)

def add_description_in_bd(connections, username, short_description, tb):
    cursor = connections.cursor()
    sql = f"UPDATE `{tb}` SET `short_description` = %s WHERE `username` = %s"
    value = [(short_description, username)]
    cursor.executemany(sql, value)
    connections.commit()

def add_deadline_in_bd(connections, username, deadline):
    cursor = connections.cursor()
    sql = f"UPDATE `{NAME_TB_SEEKSHELP}` SET `deadline` = %s WHERE `username` = %s"
    value = [(deadline, username)]
    cursor.executemany(sql, value)
    connections.commit()


execute_query(connection, create_seekshelp_table)
execute_query(connection, create_offershelp_table)
execute_query(connection, create_site_table)
execute_query(connection, create_admins_table)

users_offers = f"SELECT * from {NAME_TB_OFFERSHELP}"
select_users = f"SELECT * from {NAME_TB_SEEKSHELP}"
users = execute_read_query(connection, select_users)
offers = execute_read_query(connection, users_offers)

for user in users:
    print(user)
for user in offers:
    print(user)