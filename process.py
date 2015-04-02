#!/usr/bin/env python

import csv, datetime

cleanarray = []

with open('tweets.csv') as csvfile:
	tweets = csv.DictReader(csvfile)
	for row in tweets:
		date = str(row['timestamp']).split(' ')[0]
		text = str(row['text'])
		cleanarray_item = date + "\t" + text
		cleanarray.append(cleanarray_item)

matched_dates = [str(datetime.date.today() + datetime.timedelta(-1)),str(datetime.date.today() + datetime.timedelta(-3)),str(datetime.date.today() + datetime.timedelta(-7)),str(datetime.date.today() + datetime.timedelta(-15)),str(datetime.date.today() + datetime.timedelta(-30)),str(datetime.date.today() + datetime.timedelta(-90))] 

chosencards = ['Date: '+str(datetime.date.today())+'\n']

for item in reversed(cleanarray):
	itemdate = str(item.split('\t')[0])
	itemtext = str(item.split('\t')[1])
	if itemdate in matched_dates :
		chosencards.append(itemdate+" | "+itemtext)

finaltext = '\n '.join(str(x) for x in chosencards) 
open('output','w').write(finaltext)
