import pyodbc
import config_file


async def read(song_or_queue, serverid):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    if song_or_queue == "song":
        sql_cursor.execute("select song from loops where serverid = ?", serverid)
        song = sql_cursor.fetchone()
        return song[0]
    elif song_or_queue == "queue":
        sql_cursor.execute("select queue from loops where serverid = ?", serverid)
        queue = sql_cursor.fetchone()
        return queue[0]


async def update(song_or_queue, value, serverid):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    if song_or_queue == "song":
        command = "update loops set song = ? where serverid = ?"
        values = (value, serverid)
        sql_cursor.execute(command, values)
        sql_connection.commit()
    elif song_or_queue == "queue":
        command = "update loops set queue = ? where serverid = ?"
        values = (value, serverid)
        sql_cursor.execute(command, values)
        sql_connection.commit()
