import pyodbc
import config_file


async def update(value, serverid):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "update disconnected set  disconnected = ? where serverid = ?"
    values = (value, serverid)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def read(serverid):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "select disconnected from disconnected where serverid = ?"
    sql_cursor.execute(command, serverid)
    disconnected = sql_cursor.fetchone()
    return disconnected[0]