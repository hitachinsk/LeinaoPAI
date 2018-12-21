#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import MySQLdb

imageName = sys.argv[1]
imageNameSplit = imageName.split('/')
provider = sys.argv[2]
description = sys.argv[3]
db = MySQLdb.connect("127.0.0.1", "root", "sangjing", "dataset", charset='utf8' )
cursor = db.cursor()
sql = """INSERT INTO images(name,place,description,provider,createtime) VALUES ("%s","%s/%s","%s","%s",NOW())"""%(imageNameSplit[2],imageNameSplit[0],imageNameSplit[1],description,provider)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()
db.close()