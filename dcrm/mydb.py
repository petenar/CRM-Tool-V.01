# -*- coding: utf-8 -*-

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    port = 3308,
    user = 'root',
    passwd = 'Z@fighterdbz999'
    
    )

#preapare a curser object
cursorObject = dataBase.cursor()

#create Database
cursorObject.execute("CREATE DATABASE petrco")
print("You Did It!")
