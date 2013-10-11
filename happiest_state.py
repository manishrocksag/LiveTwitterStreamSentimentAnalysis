'''
This script takes the tweet file and parses it to get location of tweets.It then prints the state with the highest positive sentiment score.
For example:
"place":
{
    "attributes":{},
     "bounding_box":
    {
        "coordinates":
        [[
                [-77.119759,38.791645],
                [-76.909393,38.791645],
                [-76.909393,38.995548],
                [-77.119759,38.995548]
        ]],
        "type":"Polygon"
    },
     "country":"United States",
     "country_code":"US",
     "full_name":"Washington, DC",
     "id":"01fbe706f872cb32",
     "name":"Washington",
     "place_type":"city",
     "url": "http://api.twitter.com/1/geo/id/01fbe706f872cb32.json"
}

'''


import sys
import json
import difflib	
import re

def main():
    dic={} sco={} res={} tweets_text=[] tweets_location=[]
    lis=[]
    sent_file = open(sys.argv[2])
    read_file= open(sys.argv[1])
#Take the tweet file as input and parse it for location based tweets.
    for line in sent_file:
	try:
		tweet=json.loads(line)
		if tweet.has_key("place"):
			loc=tweet["place"]
			if str(loc)=="None":
				lis.append(1)		
		else:
			code=loc["country_code"]
			text=tweet["text"]
			tex=re.split("[^A-Za-z]",text)
			if dic.has_key(code):
				dic[code].append(tex)
			else:
				dic[code]=tex 
	except ValueError:
		pass
#take the sentiment file and put all the sentiment word and value in key value pairs in dict.

    line=read_file.readline()
    while(line!=''):
	foo=line.split('\t')
	if(len(foo) >= 2):
		scores=foo[1]
		sco[foo[0]]=int(scores)
		line=read_file.readline()
#read the sentiment dict and assign sentiment scores to location based tweets

    for keys in dic:
    	score=0
	for values in dic[keys]:
		if len(values) >1 and type(values) is not list: 
			if values in sco:
				values=values.encode('utf-8')
				score=score+sco[values]
		else:
			for item in values:
				if item in sco:
					item=item.encode('utf-8')
					score=score+sco[item]			
     res[keys]=score
     max=-32767
     key=''
#print the loc with highest sentiment score
     for keys in res:
	if res[keys] > max:
		max=res[keys]
		key=keys
     print key
if __name__ == '__main__':
    main()
