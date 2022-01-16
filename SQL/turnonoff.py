import pyodbc
import config_file


async def read(serverid, what):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    sql_cursor.execute("select value from turnonoff where idserver = ? and what = ?", serverid, what)
    value = sql_cursor.fetchone()
    return value[0]


async def update(value, serverid, what):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "update turnonoff set value = ? where idserver = ? and what = ?"
    values = (value, serverid, what)
    sql_cursor.execute(command, values)
    sql_connection.commit()