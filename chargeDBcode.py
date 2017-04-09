import mysql.connector
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

#DATABASE SETUP/CREATION
#If you would like to use this database backend AS IS, you need to run the following
#MySQL commands (in order) to create/setup the tables and database

#create database charge;
#use charge;
#create table info(CID int, GID int(8), StudentName varchar(25), Device varchar(25), Email varchar(25), primary key(CID));
#create table admin(CID int, GID int(8), StudentName varchar(25), TheDate date, TheTime time, primary key(CID));
#alter table admin modify cid int auto_increment;
#alter table info modify cid int auto_increment;
#alter table info add constraint fk_info foreign key(CID) references admin(CID) on delete cascade on update cascade;

def showInfo():
        try:
                dbconfig = read_db_config()
                conn = MySQLConnection(**dbconfig)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM info")
                rows = cursor.fetchall()

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
                cursor.execute("SELECT admin.CID, admin.GID, admin.StudentName, Device, Email, TheDate, TheTime FROM admin join info on admin.GID = info.GID")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

        except Error as e:
                print(e)
        finally:
                cursor.close()
                conn.close()

def showSpecificGIDBoth(gid):
        try:

                dbconfig = read_db_config()
                conn = MySQLConnection(**dbconfig)
                cursor = conn.cursor()
                query = ("SELECT admin.CID, admin.GID, admin.StudentName, Device, Email, TheDate, TheTime FROM admin join info on admin.GID = info.GID where admin.GID = %s")
                cursor.execute(query % gid)
                rows = cursor.fetchall()

                for row in rows:
                   print(row)

        except Error as e:
                print(e)
        finally:
                cursor.close()
                conn.close()

def showSpecificCIDBoth(cid):
        try:

                dbconfig = read_db_config()
                conn = MySQLConnection(**dbconfig)
                cursor = conn.cursor()
                query = ("SELECT admin.CID, admin.GID, admin.StudentName, Device, Email, TheDate, TheTime FROM admin join info on admin.GID = info.GID where admin.CID = %s")
                cursor.execute(query % cid)
                rows = cursor.fetchall()

                for row in rows:
                   print(row)

        except Error as e:
                print(e)
        finally:
                cursor.close()
                conn.close()

def insert_info(gid, name, device, email):
        query = "insert into info(GID, StudentName, Device, Email) values(%s, %s, %s, %s)"
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
        query = "insert into admin(GID, StudentName, TheDate, TheTime) values(%s, %s, %s, %s)"
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

def deleteAdminEntryCID(cid):
        query = "delete from admin where CID = %s"
        
        try:
                db_config = read_db_config()
                conn = MySQLConnection(**db_config)
 
                cursor = conn.cursor()
                cursor.execute(query, (cid,))
                conn.commit()

        except Error as e:
                print(e)
 
        finally:
                cursor.close()
                conn.close()

def deleteInfoEntryCID(cid):
        query = "delete from info where CID = %s"
        
        try:
                db_config = read_db_config()
                conn = MySQLConnection(**db_config)
 
                cursor = conn.cursor()
                cursor.execute(query, (cid,))
                conn.commit()

        except Error as e:
                print(e)
 
        finally:
                cursor.close()
                conn.close()

def populate():
        query1A = "insert into admin(GID, StudentName, TheDate, TheTime) values('00245839', 'John Doe', '2017-04-07', '12:30')"
        query1I = "insert into info(GID, StudentName, Device, Email) values('00245839', 'John Doe', 'Droid Turbo', 'JDoe@oakland.edu')"
        query2A = "insert into admin(GID, StudentName, TheDate, TheTime) values('00123456', 'Amanda Salar', '2017-04-03', '9:25')"
        query2I = "insert into info(GID, StudentName, Device, Email) values('00123456', 'Amanda Salar', 'IPhone 7', 'ASalar@oakland.edu')"
        query3A = "insert into admin(GID, StudentName, TheDate, TheTime) values('00647332', 'Brad Karmon', '2017-03-24', '1:00')"
        query3I = "insert into info(GID, StudentName, Device, Email) values('00647332', 'Brad Karmon', 'Samsumg Galaxy S7', 'BKarmon@oakland.edu')"
        query4A = "insert into admin(GID, StudentName, TheDate, TheTime) values('00123456', 'Amanda Salar', '2017-04-03', '10:47')"
        query4I = "insert into info(GID, StudentName, Device, Email) values('00123456', 'Amanda Salar', 'IPad 2', 'ASalar@oakland.edu')"
        query5A = "insert into admin(GID, StudentName, TheDate, TheTime) values('00473555', 'Lisa Bunroe', '2017-03-14', '3:10')"
        query5I = "insert into info(GID, StudentName, Device, Email) values('00473555', 'Lisa Bunroe', 'Motorola Z', 'LBunroe@oakland.edu')"

        try:
                db_config = read_db_config()
                conn = MySQLConnection(**db_config)
                cursor = conn.cursor()
                cursor.execute(query1A)
                cursor.execute(query1I)
                cursor.execute(query2A)
                cursor.execute(query2I)
                cursor.execute(query3A)
                cursor.execute(query3I)
                cursor.execute(query4A)
                cursor.execute(query4I)
                cursor.execute(query5A)
                cursor.execute(query5I)
                conn.commit()

        except Error as e:
                print(e)
 
        finally:
                cursor.close()
                conn.close()
        
        
if __name__ == '__main__':
        #insert_admin('00216674', 'David Madurski', '2017-07-26', '12:30:00')
        #insert_info('00216674', 'David Madurski', 'Motorola X', 'djmadurs@oakland.edu')
        #showSpecificGIDBoth('00216674')
        #showSpecificCIDBoth('1')
        #populate()
        showBoth()
        #deleteInfoEntryCID('1')
        #deleteAdminEntryCID('1')
        #showInfo()
        #showAdmin()
        
