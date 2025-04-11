# -*- coding: utf-8 -*-

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = '[youruser]',
    passwd = '[yourpassword]'
    
    )

#preapare a curser object
cursorObject = dataBase.cursor()

#create Database
cursorObject.execute("CREATE DATABASE petrco")
print("You Did It!")
