#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
from datetime import datetime, date

import flask , flask.views
from flask import request
import json

app = flask.Flask(__name__)



class View(flask.views.MethodView):
    def get(self):
        con = lite.connect('fluxCapacitor.db',detect_types=lite.PARSE_DECLTYPES) 
        with con:          
            cur = con.cursor()
            cur.execute("SELECT * FROM logs")
            rows = cur.fetchall()
        haxx = "all the stuff in the table" + "<br>\n"
        for row in rows:
            haxx = haxx + row[1] + ", " + row[2] + ", " + str(row[3]) + "<br>\n"
        return haxx  

    def put(self):
        parsed_json = json.loads(request.get_data(as_text=True))
        temp = datetime.now()
        con = lite.connect('fluxCapacitor.db',detect_types=lite.PARSE_DECLTYPES) 
        with con:           
            cur = con.cursor()           
            cur.execute("INSERT INTO logs(memberName,action,timestamp) VALUES (?,?,?);",(parsed_json['who'],parsed_json['what'],temp))
        print ("'Put " + parsed_json['who'] + "' in logs with action '" + parsed_json['what'] + "' at time " + str(temp))
        return "nothing"

app.add_url_rule('/',view_func=View.as_view('main'))


app.debug = True
app.run(host='0.0.0.0',port=5001)




      #  cur.execute("DROP TABLE IF EXISTS logs")
      #  cur.execute("CREATE TABLE logs (id integer primary key, memberName text, action text, [timestamp] timestamp)")







