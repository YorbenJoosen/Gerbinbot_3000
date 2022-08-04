import pyodbc
import config_file


async def write(serverid, voicechannelid, textchannelid):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "insert into voicerecord (serverid, voicechannelid, textchannelid) values(?, ?, ?)"
    values = (serverid, voicechannelid, textchannelid)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def read(serverid):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    sql_cursor.execute("select voicechannelid from voicerecord where serverid = ?", serverid)
    voicechannelid = sql_cursor.fetchone()
    return voicechannelid


async def delete(textchannelid):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from voicerecord where textchannelid = ?"
    values = textchannelid
    sql_cursor.execute(command, values)
    sql_connection.commit()