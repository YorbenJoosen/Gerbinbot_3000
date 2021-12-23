import pyodbc
import config_file


async def read():
    textlist = []
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "select iduser, points, idserver from leaderboardtext"
    sql_cursor.execute(command)
    results = sql_cursor.fetchall()
    for result in results:
        textlist.append({"userid": result[0], "score": result[1], "serverid": result[2]})
    return textlist


async def write(iduser, points, server):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "insert into leaderboardtext (iduser, points, idserver) values(?, ?, ?)"
    values = (iduser, points, server)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def update(iduser, points, server):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "update leaderboardtext set  points = ? where iduser = ? and idserver = ?"
    values = (points, iduser, server)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def delete(iduser, server):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from leaderboardtext where iduser = ? and idserver = ?"
    values = (iduser, server)
    sql_cursor.execute(command, values)
    sql_connection.commit()