# -*- coding: utf-8 -*-
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener

ckey = 'G7VgdxmMgAAVEP2ozjvpNTjpN'
csecret = 'ZglQSSeT7PCrXrMNQ7cUnVM8F0e7J6w9vZGC0c8bnoFFZkMzBN'
atoken = '1853542332-IrMAqhDYo5v5MMjZiu5bnOb5EOnDde3a0SpfueZ'
asecret = 'MHJF6Hg7wtcYkerIn45h6RfaNyNNRqNc5LSW5tzjCRO4m'

class Listener(StreamListener):
    def on_status(self,status):
        f=open("stark.txt","a")
        f.write("%s\n" %status.text.encode("utf-8"))
        f.close()
        print(status.text)
        print(status.text)
    def on_error(self,status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
l=Listener()

twitterStream = Stream(auth, l)

t=u"targaryen"

twitterStream.filter(track=[t])
