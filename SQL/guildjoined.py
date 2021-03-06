import pyodbc
import config_file


async def disconnected(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "insert into disconnected (disconnected, serverid) values (?, ?)"
    values = (0, serverid)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def loops(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "insert into loops (song, queue, serverid) values (?, ?, ?)"
    values = (0, 0, serverid)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def pause(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "insert into pause (pause, serverid) values (?, ?)"
    values = (0, serverid)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def skip(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "insert into skipped (skipped, serverid) values (?, ?)"
    values = (0, serverid)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def turnonoff(guild):
    for i in range(len(config_file.functions)-1):
        serverid = guild.id
        sql_connection = pyodbc.connect(config_file.sql_connection_string)
        sql_cursor = sql_connection.cursor()
        command = "insert into turnonoff (idserver, what, value) values (?, ?, ?)"
        values = (serverid, config_file.functions[i+1], 1)
        sql_cursor.execute(command, values)
        sql_connection.commit()