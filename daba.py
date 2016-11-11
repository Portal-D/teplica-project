

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import time

def getkey():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT key2 FROM tkey where id=0")

        row = cursor.fetchone()

        return row
        print(row)
  

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
def sendup():
    stime=time.time()
    query = "INSERT INTO uptime(datetime, also) " \
    "VALUES(now(), 20)"
    args=(stime)
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query)

        row = cursor.fetchone()

        return(row)
        print(row)
  

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
def getid(idi):
    query="SELECT accecpt FROM users WHERE chatid ='"+str(idi)+"'"
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query)

        row = cursor.fetchone()
        #print (str(row))
        if str(row)=="None":
            return 0;
            print (0)
        else:
            return 20;

  

    except Error as e:
        print(e)

    #finally:
        #cursor.close()
        #conn.close()
def newuser(idi):
    query = ("INSERT INTO users SET `chatid`='12345'")
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query)

        row = cursor.fetchone()

        print(row)
  

    except Error as e:
        print(e)
        return(e)

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    query_with_fetchone()



