import mysql.connector as sql 
conn = sql.connect(   
    host='localhost', 
    user='root', 
    password='root', 
    database='Aster_Database' ) 
c1 = conn.cursor() 
 
c1.execute('''CREATE TABLE Patient_Details( 
    Patient_Name varchar(20) Primary Key,  
    Patient_Age int(10),  
    Patient_Problems varchar(100),  
    Phone_no int(10)) 
    ''') 
c1.execute('''CREATE TABLE Doctor_Details( 
    Doctor_Name varchar(20) Primary Key, 
    Doctor_Age int, 
    Doctor_Department varchar(100), 
    Phone_no int(10)) 
    ''') 
c1.execute('''CREATE TABLE Staff_Details(
    Staff_Name varchar(20) Primary Key, 
    Staff_Age int, 
    Staff_Workname varchar(100), 
    Phone_no int(10)) 
    ''') 
