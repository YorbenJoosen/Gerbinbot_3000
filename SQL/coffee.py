import pyodbc
import config_file


async def read():
    coffeelist = []
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "select iduser, points, idserver from leaderboardcoffee"
    sql_cursor.execute(command)
    results = sql_cursor.fetchall()
    for result in results:
        coffeelist.append({"userid": result[0], "score": result[1], "serverid": result[2]})
    return coffeelist


async def write(iduser, points, idserver):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "insert into leaderboardcoffee (iduser, points, idserver) values(?, ?, ?)"
    values = (iduser, points, idserver)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def update(iduser, points, idserver):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "update leaderboardcoffee set points = ? where iduser = ? and idserver = ?"
    values = (points, iduser, idserver)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def delete(iduser, idserver):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from leaderboardcoffee where iduser = ? and idserver = ?"
    values = (iduser, idserver)
    sql_cursor.execute(command, values)
    sql_connection.commit()
