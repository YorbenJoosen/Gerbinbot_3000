import pyodbc
import config_file


async def update(value, serverid):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "update pause set pause = ? where serverid = ?"
    values = (value, serverid)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def read(serverid):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    sql_cursor.execute("select pause from pause where serverid = ?", serverid)
    pause = sql_cursor.fetchone()
    return pause[0]
