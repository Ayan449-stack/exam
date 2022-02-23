import sqlite3
con=sqlite3.connect('Dataformovie.db')    #created database
print('created database')
con.execute('create table if not exists movies(id int,moviesname text,actorname text,actressname text,directorsname text,realeasedate int)')
print('table is created')    #created is created
con.execute('insert into movies(id,moviesname,actorname,actressname,directorsname,realeasedate) values(101,"pushpa-the rise","Allu arjun","Rashmika mandhana","xyz","jan 2, 2021")')
con.execute('insert into movies(id,moviesname,actorname,actressname,directorsname,realeasedate) values(102,"Race","salman khan","Jeqlin","Remo", "Apr 2, 2021")')
print('data is inserted')   #data will be inserted
con.commit()

data=con.execute("select * from movies")   #fetch the data from table
for row in data:    #All data fetch from table
     print("id is:{},Moviesname:{},Actorname:{},Actressname:{},Directorname:{},Releasedate:{}".format(row[0],row[1],row[2],row[3],row[4],row[5]))
     #print the all the data
