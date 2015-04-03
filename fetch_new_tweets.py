#!/usr/bin/env python

import twitter, datetime

fetched_tweets = [line.strip() for line in open('fetched_tweets_db.csv')]
new_fetched_tweets = []

api = twitter.Api(consumer_key='KEY',consumer_secret='SECRET',access_token_key='KEY',access_token_secret='SECRET')

statuses = api.GetUserTimeline('USERNAME', count=1000, max_id=None)

for status in statuses:
	tweetdate = datetime.datetime.fromtimestamp(int(status.created_at_in_seconds)).strftime('%Y-%m-%d')
	tweetid = status.id
	tweettext = status.text
	dataline = str(tweetid) + "\t" + str(tweetdate) + "\t" + str(tweettext)
	if dataline not in fetched_tweets:
		new_fetched_tweets.append(dataline)

new_tweets_to_append = "\n"+'\n'.join(new_fetched_tweets)
open('fetched_tweets_db.csv','a').write(new_tweets_to_append)
