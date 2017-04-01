import urllib2
import MySQLdb as sql
import csv

#the link to be downloaded from
link = "https://api.thingspeak.com/stream/channels/210904/feeds?api_key=BS3RRU9E3SUTTKYC&timezone=UTC"

#getting the response from server
response = urllib2.urlopen(link)

#saving to csvfile
csvfile = response.read()

#to check what you got in request, uncomment the next line
#print csvfile

#writing into csv file
target = open("target.csv", 'w')
target.write(csvfile)

#deleting the first line from file since it contains columns
with open('target.csv', 'r') as fin:
    data = fin.read().splitlines(True)
with open('target.csv', 'w') as fout:
    fout.writelines(data[1:])

#connection to database
db = sql.Connection (host = "localhost", user = "root", passwd = "root", db = "damn")

#cursor file
cur = db.cursor()

#creating database NOTE: RUN ONLY ONCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#cur.execute("CREATE DATABASE damn;")

#Necesarry shit NOTE: IF YOU WANT TO KEEP THE TABLE BEFORE NEXT EXECUTION, COMMENT THE NEXT LINE AND THE LINE AFTER THAT.
cur.execute("DROP TABLE IF EXISTS hell;")

#create the hell(after all i am the creator here.. xD)
cur.execute("CREATE TABLE hell(datentime VARCHAR, someshit INTEGER, someothershit FLOAT);")

#insert into the TABLE
#reading from file
csv_data = csv.reader(file('target.csv'))
for row in csv_data:

    cur.execute('INSERT INTO hell VALUES("%s", "%d", "%f")', row)

    #Commiting for further use
    cur.commit()
    
cur.execute("SELECT * FROM hell")
cur.close()
