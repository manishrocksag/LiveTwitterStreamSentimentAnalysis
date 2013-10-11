'''
This script assigns sentiment scores to those tweets whose term is not contained in the sentiment scores file.
'''


import sys
import json
import re
def main():
    dic={} 
    lis=[] 
    rec={} 
    res={} 
    lop=[]	
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    line=sent_file.readline()
#Takes the raw sentiment data file and builds a dictiomary from it containg sentiment term as key and its score as value
    while(line!=''):
		lis=line.split('\t')
		dic[lis[0]]=lis[1]
		line=sent_file.readline()
    i=0
#Takes the raw tweet data file and parse it for english tweets only
    for line in tweet_file:
		try:
			tex=json.loads(line)
			if tex.has_key("text"):
        			z=tex["text"]
				text=re.split("[^A-Za-z@]",z)
				score=0.0
				for keys in text:
					if keys in dic:
						keys=keys.encode("utf-8")
						score=score+int(dic[keys])
				rec[i]=score
				i=i+1
		except ValueError:
			pass
    q=0
#prints the calculated sentiment score for tweets which are not there in the sentiment file
    for key,value in res.items():
		if q==0:
			lop.append(1)
			q=1
		else:
			print "{0}\t{1}".format(key,value)
if __name__ == '__main__':
    main()
