import sys
import json
import re
def main():
    dic={} lis=[] rec={} res={} lop=[]	
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    line=sent_file.readline()
    while(line!=''):
	lis=line.split('\t')
	dic[lis[0]]=lis[1]
	line=sent_file.readline()
    i=0
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
    tw_file = open(sys.argv[2])
    j=0
    for line in tw_file:
	try:
		tex=json.loads(line)
		if tex.has_key("text"):
        		z=tex["text"]
			text=re.split("[^A-Za-z@]",z)
			score=0.0
			for keys in text:
				if keys not in dic:
					keys=keys.encode("utf-8")
					if keys in res:
						res[keys]=res[keys] + rec[j]
					else:
						res[keys]=rec[j]
			j=j+1
	except ValueError:
		pass
    q=0
    for key,value in res.items():
	if q==0:
		lop.append(1)
		q=1
	else:
		print "{0}\t{1}".format(key,value)
def lines(fp):
        print_files(fp)	  
def print_files(files):
    x=0
    lines="oops"
    while(lines!=''):
	lines=files.readline()
	line=lines.split('\t')
	if(len(line) >= 2):
		scores=line[1]
		dic[line[0]]=int(scores)
def tweet(fp):
	line=fp.readline()
	scores=0
	while(line!=''):
		tup=line.split(" ")
		z=len(tup)
		tup[z-1]='elite'
		for x in (tup):
			if x in dic:
				scores=scores + dic[x]
			else:
				if x not in diction:
					diction[x]=scores
					print x,scores	
		line=fp.readline()
if __name__ == '__main__':
    main()
