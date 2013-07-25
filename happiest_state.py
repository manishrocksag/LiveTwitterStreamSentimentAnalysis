import sys
import json
import difflib	
import re
def main():
    dic={} sco={} res={} tweets_text=[] tweets_location=[]
    lis=[]
    sent_file = open(sys.argv[2])
    read_file= open(sys.argv[1])
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
    line=read_file.readline()
    while(line!=''):
	foo=line.split('\t')
	if(len(foo) >= 2):
		scores=foo[1]
		sco[foo[0]]=int(scores)
		line=read_file.readline()
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
     for keys in res:
	if res[keys] > max:
		max=res[keys]
		key=keys
     print key
if __name__ == '__main__':
    main()
