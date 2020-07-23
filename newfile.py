#import tweepy4
import os
from flask import Flask


app=Flask(__name__)

@app.route('/')
def home():
	os.system('python tweepy4.py')
	return open('tweets.html').read()

if __name__=='__main__':
	app.run()
	