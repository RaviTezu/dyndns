#!/usr/bin/python

import urllib2

#To update the DNS with the current public IP. To do this you'll be needing the freedns.afraid.org api key. To get the key:
# 1. You need a sign up for http://freedns.afraid.org/
# 2. Login to  http://freedns.afraid.org/
# 3. Go to the api page: http://freedns.afraid.org/api/ and Click on XML or ASCII for api key

#api key looks like this: RVF3dWNGRVNiQlFsxXVSMzJZQ5JhQ2dxOjEwOTA4Mjcc
#Warning: This api keys changes when you change your password 

api_key = "<Paste your api key>"

#To Get the current public facing IP.
#There are tons of websites which can find your current Public facing IP. Here I used the "ip.42.pl/raw" which provides you only the IP. 
#You can also use http://jsonip.com/ ,  http://checkip.dyndns.org/ , http://whatismyip.com/ etc.

try:
   public_ip  = urllib2.urlopen("http://ip.42.pl/raw").read()
except: 
   print "Unable to get your public facing IP!"

if public_ip:
   update_url = "https://freedns.afraid.org/dynamic/update.php?%s&address=%s"%(api_key, public_ip)
   try:
      update_dns = urllib2.urlopen(update_url)
      result = update_dns.read().strip()
      print result
   except: 
      print "Something is wrong, cannot update the dns!"
 
else: 
   print "Please check your Internet connection!"
