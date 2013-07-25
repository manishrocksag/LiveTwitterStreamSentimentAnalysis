import sys
import json
import difflib	
import re
def main():
    dic={} tweets_text=[] tweets_location=[] lis=[]
    sent_file = open(sys.argv[1])
    for line in sent_file:
	try:
		tweet=json.loads(line)
		if tweet.has_key("text"):
			text=tweet["text"]
			tex=re.split("[^A-Za-z,.]",text)
			tex=re.split("[^A-Za-z]",text)
			for word in tex:
				if word in dic:
					dic[word]=dic[word] + 1.0
				else:
					dic[word]=1.0
	except ValueError:
		pass
    x=len(dic)
    i=0
    for keys in dic:
	foo=keys.encode('utf-8')
	if i==0:
		lis.append(1)
		i=1
	else:
		foo=keys.encode('utf-8')
		print foo,dic[foo]/x	
     	     for keys in dic:
	sys.stdout.write('{0}\t{1}\n'.format(keys.encode('utf-8'),dic[keys]/x))	
if __name__ == '__main__':
    main()
