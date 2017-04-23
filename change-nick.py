#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Dev script to change user rfid. """

import sqlite3 as lite

dbName = input("Enter db to operate on:")

con = lite.connect(dbName)

with con:
    cur = con.cursor()
    
    oldnick = input("Enter user old nick:")
    newnick = input("Enter user new nick:")
    
    cur.execute("UPDATE logs SET memberName = ? WHERE memberName = ?", (newnick, oldnick))

