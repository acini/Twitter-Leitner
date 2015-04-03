#!/usr/bin/env python

import datetime

cleanarray = []

tweets_in_db = [line.strip() for line in open('fetched_tweets_db.csv')]

for tweet in tweets_in_db:
	print tweet
	date = tweet.split('\t')[1]
	text = tweet.split('\t')[2]
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
open('print','w').write(finaltext)
