import sqlite3
import os
from shutil import copyfile
count = 0
for filename in os.listdir("D:/OffloadedData/"):
    count = count +1
    if filename.endswith(".sqlite3") and filename != "db1.sqlite3":
        oscwd = os.getcwd()
        #Create new database
        db = sqlite3.connect('D:/OffloadedData/db1.sqlite3')
        cursor = db.cursor()
        cursor.execute('UPDATE main.matchscout_matchscout SET "id" = main.matchscout_matchscout.id +' + str(200*count))
        filenamelong = f'ATTACH "D:\\OffloadedData\\{filename}" AS db2'
        cursor.execute(filenamelong)
        cursor.execute('INSERT INTO main.matchscout_matchscout SELECT * FROM db2.matchscout_matchscout')
        db.commit()
        cursor.close()
        print(filename)

print ('Data Combinaton Complete')

        
