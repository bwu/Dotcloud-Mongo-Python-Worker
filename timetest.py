#!/usr/local/env python

from datetime import datetime
import pymongo
from pymongo import Connection
import json
import time


# Open the environment file and get the name of the host and port
with open('/home/dotcloud/environment.json') as f:
  env = json.load(f)

# Assign the host and port
host = env['DOTCLOUD_DATA_MONGODB_URL']

# Connect to the database and assign the correct name for the database and collection
connection = Connection(host=host)
db = connection.tests
collection = db.times

# Open the file and make a row Writer
FILE_NAME = 'test.csv'
rowWriter = csv.writer(open(FILE_NAME, 'w'), delimiter = ",")

while True:
	# Give todays date as an item in a dictionary.
	today = { 'date and time' : datetime.today() }
	collection.insert(today)

	row = []
	row.append('date and time')
	row.append(item['date and time'])
	rowWriter.writerow(row)

	time.sleep(60)