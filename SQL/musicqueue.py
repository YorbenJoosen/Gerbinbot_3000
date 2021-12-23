import pyodbc
import config_file


async def write(url, title, duration, serverid):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "insert into musictable (url, title, duration, serverid) values (?, ?, ?, ?)"
    values = (url, title, duration, serverid)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def read(serverid):
    urllist = []
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "select url, title, duration, timestamp from musictable where serverid = ?"
    sql_cursor.execute(command, serverid)
    results = sql_cursor.fetchall()
    for result in results:
        urllist.append({"url": result[0], "title": result[1], "duration": result[2], "time": result[3]})
        urllist = sorted(urllist, key=lambda i: i["time"])
    return urllist


async def delete(serverid):
    musiclist = await read(serverid)
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from musictable where timestamp = ? and serverid = ?"
    value = musiclist[0]["time"]
    values = (value, serverid)
    sql_cursor.execute(command, values)
    sql_connection.commit()


async def empty(serverid):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from musictable where serverid like ?"
    sql_cursor.execute(command, serverid)
    sql_connection.commit()


async def sqlsort(musiclist, serverid):
    await empty(serverid)
    for i in range(len(musiclist)):
        await write(musiclist[i]["url"], musiclist[i]["title"], musiclist[i]["duration"], serverid)
