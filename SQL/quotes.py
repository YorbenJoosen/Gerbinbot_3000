import pyodbc


async def read():
    quotelist = []
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "select quote, userid, serverid from quotes"
    sql_cursor.execute(command)
    results = sql_cursor.fetchall()
    for result in results:
        quotelist.append({"quote": result[0], "userid": result[1], "serverid": result[2]})
    return quotelist


async def write(quote, userid, serverid):
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "insert into quotes(quote, userid, serverid) values(?, ?, ?)"
    values = (quote, userid, serverid)
    sql_cursor.execute(command, values)
    sql_connection.commit()