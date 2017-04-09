import mysql.connector
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def showInfo():
        try:
                dbconfig = read_db_config()
                conn = MySQLConnection(**dbconfig)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM info")
                rows = cursor.fetchall()

                print('Total Entries:', cursor.rowcount)
                for row in rows:
                    print(row)

        except Error as e:
                print(e)
        finally:
                cursor.close()
                conn.close()

def showAdmin():
        try:
                dbconfig = read_db_config()
                conn = MySQLConnection(**dbconfig)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM admin")
                rows = cursor.fetchall()

                print('Total Entries:', cursor.rowcount)
                for row in rows:
                    print(row)

        except Error as e:
                print(e)
        finally:
                cursor.close()
                conn.close()

def showBoth():
        try:
                dbconfig = read_db_config()
                conn = MySQLConnection(**dbconfig)
                cursor = conn.cursor()
                cursor.execute("SELECT admin.GID, admin.StudentName, Device, Email, TheDate, TheTime FROM admin join info on admin.GID = info.GID")
                rows = cursor.fetchall()

                print('Total Entries:', cursor.rowcount)
                for row in rows:
                    print(row)

        except Error as e:
                print(e)
        finally:
                cursor.close()
                conn.close()

def showSpecificBoth(gid):
        try:

                dbconfig = read_db_config()
                conn = MySQLConnection(**dbconfig)
                cursor = conn.cursor()
                query = ("SELECT admin.GID, admin.StudentName, Device, Email, TheDate, TheTime FROM admin join info on admin.GID = info.GID where admin.GID = %s")
                cursor.execute(query % gid)
                rows = cursor.fetchall()

                for row in rows:
                   print(row)

        except Error as e:
                print(e)
        finally:
                cursor.close()
                conn.close()

def insert_info(gid, name, device, email):
        query = "insert into info values(%s, %s, %s, %s)"
        args = (gid, name, device, email)

        try:
                db_config = read_db_config()
                conn = MySQLConnection(**db_config)
 
                cursor = conn.cursor()
                cursor.execute(query, args)
                conn.commit()

        except Error as e:
                print(e)
 
        finally:
                cursor.close()
                conn.close()

def insert_admin(gid, name, date, time):
        query = "insert into admin values(%s, %s, %s, %s)"
        args = (gid, name, date, time)

        try:
                db_config = read_db_config()
                conn = MySQLConnection(**db_config)
 
                cursor = conn.cursor()
                cursor.execute(query, args)
                conn.commit()

        except Error as e:
                print(e)
 
        finally:
                cursor.close()
                conn.close()

def deleteAdminEntry(gid):
        query = "delete from admin where GID = %s"
        
        try:
                db_config = read_db_config()
                conn = MySQLConnection(**db_config)
 
                cursor = conn.cursor()
                cursor.execute(query, (gid,))
                conn.commit()

        except Error as e:
                print(e)
 
        finally:
                cursor.close()
                conn.close()

def deleteInfoEntry(gid):
        query = "delete from info where GID = %s"
        
        try:
                db_config = read_db_config()
                conn = MySQLConnection(**db_config)
 
                cursor = conn.cursor()
                cursor.execute(query, (gid,))
                conn.commit()

        except Error as e:
                print(e)
 
        finally:
                cursor.close()
                conn.close()
        
if __name__ == '__main__':
        #insert_admin('00216674', 'David Madurski', '2017-07-26', '12:30:00')
        #insert_info('00216674', 'David Madurski', 'Motorola X', 'djmadurs@oakland.edu')
        showSpecificBoth('00216674')
        
