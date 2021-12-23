import pyodbc
import config_file


async def read():
    rpslist = []
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "select iduser, pointsuser, pointsbot from rps"
    sql_cursor.execute(command)
    results = sql_cursor.fetchall()
    for result in results:
        rpslist.append({"userid": result[0], "userpoints": result[1], "botpoints": result[2]})
    return rpslist


async def write(rpslist):
    last_value = len(rpslist) - 1
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "insert into rps (iduser, pointsuser, pointsbot) values (?, ?, ?)"
    values = (rpslist[last_value]["userid"], rpslist[last_value]["userpoints"], rpslist[last_value]["botpoints"])
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def update(userid, userpoints, botpoints):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "update rps set pointsuser = ?, pointsbot = ? where iduser = ?"
    values = (userpoints, botpoints, userid)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def delete(userid):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from rps where iduser = ?"
    value = userid
    sql_cursor.execute(command, value)
    sql_connection.commit()
