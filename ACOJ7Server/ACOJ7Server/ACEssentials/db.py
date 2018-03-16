import pymysql
from ACOJ7Server.privacy import mysql

def sql(cmd, arg = ()) :
    conn =  pymysql.connect(
        host = 'localhost',
        user = mysql['username'],
        passwd = mysql['password'],
        db = 'ACOJ',
        port = 3306,
        charset = 'utf8'
    )
    cursor = conn.cursor()
    res = []
    try:
        cmd = cmd % arg
        cmdSet = cmd.split(';')
        for command in cmdSet :
            cursor.execute(command)
            res.append(cursor.fetchall())
        conn.commit()
    except:
        conn.rollback()
        res = None
    conn.close()
    return res

