import tweepy
#import pandas as pd

from datetime import timedelta,datetime
day=datetime.now().day
month=datetime.now().strftime("%B")
keywords=[ month+' security patch','android 10 update','android 11']
print(keywords)




ACCESS_TOKEN = "584597840-Mijzn2fu7Po2BTDSuQZAGifhSMIMr7riiuDtSTcc"
ACCESS_TOKEN_SECRET = "6v2oU9jeS0lmqJ0QC2k9KCD8OsQhE77cu02YjTxNcBAvK"
CONSUMER_KEY = "nTerNLKtbTPTzPZOLYvOQHjJk"
CONSUMER_SECRET = "ItwbiyRXXRTWaOVoHGudqt7aaGAx9Sp4Fkbpfpw1dPNvMe7mn7"
 
auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#f=open('zenfone.txt','w')
twees=[]
twee=dict()
for key in keywords:
	i=1
	for tweet in tweepy.Cursor(api.search,q=key+' -filter:retweets',count=100,lang='en',tweet_mode='extended',result_type='recent').items():
		print(i)
		
		s=tweet.created_at+timedelta(hours=5,minutes=30)
		
		twee['Time']= s
		
		data=tweet.full_text
		d=data.find('https://',-25,-1)
		

		twee['Tweet']=data[:d]
		link=f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
	
		twee['Link']=link
		
		if 'media' in tweet.entities:
			for image in  tweet.entities['media']:
	
				twee['img_url']=image["media_url"]
		else:
		
					twee['img_url']='Nil'
		
		twees.append(twee.copy())
		i+=1
		if s.day!=day:
			#print(tweet)
			break
		

twees=sorted(twees,key=lambda x: datetime.strftime(x['Time'], '%Y-%m-%d %H:%M:%S'),reverse=True)


i=1
with open('tweets.html','w',encoding='utf-8')as file:
		file.write('<!DOCTYPE html>')
		file.write('<html>')
		file.write('''<head>
	
		<title>HTML Image as link</title></head>''')
		file.write('<body>')

		for twee in twees:
			file.write('<p style="font-size:10px">')
			if twee['img_url']!='Nil':
				file.write('''<a href=" '''+twee['img_url']+''' ">'''+
         '''<img alt="image" src=" '''+twee['img_url']+
        ''' " width="200" " height="160" align="right"></a>''')
			file.write(str(i)+'] ')
			file.write(twee['Time'].strftime('%Y-%m-%d %I:%M %p')+' <br> '+'''<a href=" '''+twee['Link']+''' ">'''+'#Tweet '+'</a><br>')
			file.write('<b> '+twee['Tweet']+'</b><br>')
			
			file.write('</p><br><br>')
	
			i+=1
		file.write('</body>')
		file.write('</html>')
	