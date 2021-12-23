import pyodbc
import config_file


async def update(value, serverid):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "update skipped set  skipped = ? where serverid = ?"
    values = (value, serverid)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def read(serverid):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "select skipped from skipped where serverid = ?"
    sql_cursor.execute(command, serverid)
    skipped = sql_cursor.fetchone()
    return skipped[0]