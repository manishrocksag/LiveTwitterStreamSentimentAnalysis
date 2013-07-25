import sys
dic={}
def hw():
    print 'Hello, world!'

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
	while(line!=''and line!='\n'):
		scores=0
		tup=line.split(" ")
		if(len(tup)>=1):
			for x in (tup):
				if x in dic:
					scores=scores + dic[x]	
			print scores
		line=fp.readline()	
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    lines(sent_file)
    tweet(tweet_file)
if __name__ == '__main__':
    main()
