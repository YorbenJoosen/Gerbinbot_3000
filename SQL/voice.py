import pyodbc
import config_file


async def read():
    voicelist = []
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "select iduser, timejoined, timeleft, points, idserver from leaderboardvoice"
    sql_cursor.execute(command)
    results = sql_cursor.fetchall()
    for result in results:
        voicelist.append({"userid": result[0], "begintime": result[1], "endtime": result[2], "score": result[3], "serverid": result[4]})
    return voicelist


async def write(iduser, timejoined, timeleft, points, server):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "insert into leaderboardvoice (iduser, timejoined, timeleft, points, idserver) values(?, ?, ?, ?, ?)"
    values = (iduser, timejoined, timeleft, points, server)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def update(iduser, timejoined, timeleft, points, server):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "update leaderboardvoice set timejoined = ?, timeleft = ?, points = ? where iduser = ? and idserver = ?"
    values = (timejoined, timeleft, points, iduser, server)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def delete(iduser, server):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from leaderboardvoice where iduser = ? and idserver = ?"
    values = (iduser, server)
    sql_cursor.execute(command, values)
    sql_connection.commit()
