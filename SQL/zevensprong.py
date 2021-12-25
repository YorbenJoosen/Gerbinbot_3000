import pyodbc
import config_file


async def read():
    zevenspronglist = []
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "select iduser, points from leaderboardzevensprong"
    sql_cursor.execute(command)
    results = sql_cursor.fetchall()
    for result in results:
        zevenspronglist.append({"userid": result[0], "score": result[1]})
    return zevenspronglist


async def write(iduser, points):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "insert into leaderboardzevensprong (iduser, points) values(?, ?)"
    values = (iduser, points)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def update(iduser, points):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "update leaderboardzevensprong set points = ? where iduser = ?"
    values = (points, iduser)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def delete(iduser):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from leaderboardzevensprong where iduser = ?"
    values = (iduser)
    sql_cursor.execute(command, values)
    sql_connection.commit()
