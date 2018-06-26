import math
import glob
def fingerprinting(s):
	stopwords=["a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below",
	"between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from",
	"further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how",
	"i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of",
	"off","on","once","only","or","other","ought","our","ours"]
	k_grms=6
	s=s.split(' ')
	fullstr=''
	for i in s:
		if i not in stopwords:
			fullstr=fullstr+i
	kgrams_list=[]
	for i in range (0,len(fullstr)-k_grms,1):
		kgrams_list.append(fullstr[i:i+k_grms])	
	hash_list=[]
	for i in kgrams_list:
		hash=0
		exp=5
		for j in i:
			exp-=1
			hash+=ord(j)*(k_grms**exp)
		hash_list.append(hash)
	return hash_list
string=[]
for filename in glob.glob('*.txt'):
	f = open(filename,'r')
	while 1:		
		line=f.readline()
		if not line:break
		string.append(line)
	f.close()
final=[]
for i in range(len(string)):
	temp=[]
	for j in range(len(string)):
		if i==j:
			temp.append(-1)
		else:
			hlist1=fingerprinting(str(string[i]))
			hlist2=fingerprinting(str(string[j]))
			common=[]
			for k in hlist1:
				if k in hlist2:
					common.append(k)
			common=list(set(common))
			hsum1=sum(hlist1)
			hsum2=sum(hlist2)
			csum=sum(common)
			per=(2*csum)*100/(hsum1+hsum2)
			temp.append(math.ceil(per))
	final.append(temp)
for i in final:
	print(i,"\n")		