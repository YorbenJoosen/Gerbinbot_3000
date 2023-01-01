import pyodbc
import config_file


async def disconnected(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from disconnected where serverid = ?"
    sql_cursor.execute(command, serverid)
    sql_connection.commit()


async def loops(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from loops where serverid = ?"
    sql_cursor.execute(command, serverid)
    sql_connection.commit()


async def pause(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from pause where serverid = ?"
    sql_cursor.execute(command, serverid)
    sql_connection.commit()


async def skip(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from skipped where serverid = ?"
    sql_cursor.execute(command, serverid)
    sql_connection.commit()


async def turnonoff(guild):
    for i in range(len(config_file.functions)-1):
        serverid = guild.id
        sql_connection = pyodbc.connect(config_file.sql_connection_string)
        sql_cursor = sql_connection.cursor()
        command = "delete from turnonoff where idserver = ? and what = ?"
        sql_cursor.execute(command, serverid, config_file.functions[i+1])
        sql_connection.commit()


async def leaderboardvoice(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from leaderboardvoice where idserver = ?"
    sql_cursor.execute(command, serverid)
    sql_connection.commit()


async def leaderboarstream(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from leaderboardstream where idserver = ?"
    sql_cursor.execute(command, serverid)
    sql_connection.commit()


async def leaderboardcamera(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from leaderboardcamera where idserver = ?"
    sql_cursor.execute(command, serverid)
    sql_connection.commit()


async def leaderboardtext(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from leaderboardtext where idserver = ?"
    sql_cursor.execute(command, serverid)
    sql_connection.commit()


async def quotes(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from quotes where serverid = ?"
    sql_cursor.execute(command, serverid)
    sql_connection.commit()


async def leaderboardcoffee(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from leaderboardcoffee where serverid = ?"
    sql_cursor.execute(command, serverid)
    sql_connection.commit()