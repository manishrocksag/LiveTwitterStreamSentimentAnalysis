'''
This script prints the top ten hash tags from the tweet file.
We parse the Entities field in the tweet file to get hashtags.
Entities which have been parsed out of the text of the Tweet. 
Example:
"entities":
{
    "hashtags":[],
    "urls":[],
    "user_mentions":[]
}
'''

import sys
import json
import difflib	
import re
from collections import OrderedDict

def main():
    dic={}
    tweets_text=[]
    tweets_location=[]
    lis=[]
    sent_file = open(sys.argv[1])
    for line in sent_file:
	try:
	#parse the tweet file and get hash tags from it
		tweet=json.loads(line)
		if tweet.has_key("entities"):
			text=tweet["entities"]
			for keys in text:
				tex=text["hashtags"]				
				for keys in tex:
					word=keys["text"]
					word=re.split("[^A-Za-z]",word)
					x=word[0]
	#put the hashtags in dict and count their frequency. 
					if x in dic:
						dic[x]=dic[x] + 0.25
					else:
						dic[x]=0.25
	except ValueError:
		pass
    i=0
#sort the dic from increasing order using python lambda function
    d_sort=OrderedDict(sorted(dic.items(),key=lambda x:(-x[1],x[0])))
#print the top ten keys
    for keys in d_sort:
	foo=keys.encode('utf-8')
		foo=keys.encode('utf-8')
		i=i+1
		z=d_sort[foo]
		print foo,int(z+1)
if __name__ == '__main__':
    main()
