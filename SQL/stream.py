import pyodbc
import config_file


async def read():
    streamlist = []
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "select iduser, timejoined, timeleft, points, idserver from leaderboardstream"
    sql_cursor.execute(command)
    results = sql_cursor.fetchall()
    for result in results:
        streamlist.append({"userid": result[0], "begintime": result[1], "endtime": result[2], "score": result[3], "serverid": result[4]})
    return streamlist


async def write(iduser, timejoined, timeleft, points, server):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "insert into leaderboardstream (iduser, timejoined, timeleft, points, idserver) values(?, ?, ?, ?, ?)"
    values = (iduser, timejoined, timeleft, points, server)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def update(iduser, timejoined, timeleft, points, server):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "update leaderboardstream set timejoined = ?, timeleft = ?, points = ? where iduser = ? and idserver = ?"
    values = (timejoined, timeleft, points, iduser, server)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def delete(iduser, server):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from leaderboardstream where iduser = ? and idserver = ?"
    values = (iduser, server)
    sql_cursor.execute(command, values)
    sql_connection.commit()
