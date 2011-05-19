#!/usr/bin/env python
import os
import os.path
import sqlite3

db_filename = "/tmp/sqlitedb"
if os.path.exists(db_filename):
    os.remove(db_filename)

print "Creating DB {}".format(db_filename)
db_conn = sqlite3.connect(db_filename)
db = db_conn.cursor()

db.execute("create table entries ( key text, value text, attribute text, time int )")

tables = db.execute("SELECT name FROM sqlite_master WHERE type='table';")
print "Tables: " + ",".join([row[0] for row in tables.fetchall()])

values = [
    ( "AA", "value", "attribute", 99 ),
    ( "BB", "test", "hello", 4 ),
    ( "AA", "value", "duplicate", 45),
    ( "CC", "hello world", "goodbye", 9),
    ]
for v in values:
    db.execute("insert into entries values (?,?,?,?)", v)

db_conn.commit()  # Sync to DB

print "Dumping the DB..."
db.execute("select * from entries")

for row in db:
    print row

print "Listing all the keys..."
db.execute("select key from entries")
keys = set([ row[0] for row in db.fetchall() ])

print keys

print "Listing all duplicate keys..."
db.execute("select key, count(key) as NumOccurrences from entries group by key having (count(key) > 1)")

for row in db:
    print row

db.close()
db_conn.close()
