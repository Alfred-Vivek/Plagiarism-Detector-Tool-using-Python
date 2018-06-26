import sys
import math
import glob
import string
import datetime
today=datetime.datetime.now()
class plag_check:
	'''This Class contains all the functions to be computed on two files 
	to check the plagiarism between the two, and display the matrix representation.'''
	def __init__(self):
		self.max_count=0
	def bagofwords(self,l1,l2):
		'''This function computes the approximate plagiarism between two files using 
		the Bag of Words Technique.
		Input  : Two lists containing all the words of the current files respectively
		Output : Percentage of Plagiarism Found between both the Lists'''
		count_dict1={}
		sum1,sum2=0,0
		for e in (l1):   
			if e.lower() not in count_dict1.keys():
				count_dict1[e.lower()] = 1
			else:
				count_dict1[e.lower()] += 1
		count_dict2={}
		for e in (l2):   
			count = l2.count(e)
			if e.lower() not in count_dict2.keys():
				count_dict2[e.lower()] = 1
			else:
				count_dict2[e.lower()] += 1
		common=[]
		for key in count_dict1.keys():
			if key in count_dict2:
				common.append(key)
		for v in count_dict1.values():
			sum1=sum1+(v**2)
		sum1=sum1**0.5
		for v in count_dict2.values():
			sum2=sum2+(v**2)
		sum2=sum2**0.5
		sum1=sum1*sum2
		sum2=0
		for i in common:
			sum2=sum2+(count_dict1[i]*count_dict2[i])
		sum2=sum2
		distance=(sum2/sum1)*100
		return int(distance)
	def lc_substring(self,s1,s2):
		'''This function computes the approximate plagiarism between two files using 
		the Longest Common Substring Technique.
		Input  : Two strings containing the content of two current files respectively
		Output : Percentage of Plagiarism Found between both the Lists'''
		matrix=[[0]*(len(s2)+1) for i in range(len(s1)+1)]
		self.max_count=0
		for i in range(1,len(s1)+1):
			for j in range(1,len(s2)+1):
				if s1[i-1]==s2[j-1]:
					matrix[i][j]=matrix[i-1][j-1]+1
					if matrix[i][j]>self.max_count:
						self.max_count=matrix[i][j]
				else:
					matrix[i][j]=0
		return self.max_count
	def fingerprinting(self,s):
		'''This function computes the approximate plagiarism between two files using 
		the Fingerprinting Technique.
		Input  : A String containing the content of the current file
		Output : List of all Unique Hash values of the given string '''
		stopwords=["a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below",
		"between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from",
		"further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how",
		"i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of",
		"off","on","once","only","or","other","ought","our","ours"]
		k_grms=6
		s=s.split(' ')
		s=[word.strip(string.punctuation)for word in s]
		fullstr=''
		for i in s:
			if i not in stopwords:
				fullstr=fullstr+i
		fullstr=fullstr.lower()
		kgrams_list=[]
		for i in range (0,len(fullstr)-k_grms,1):
			kgrams_list.append(fullstr[i:i+k_grms])	
		self.hash_list=[]
		for i in kgrams_list:
			hash=0
			exp=5
			for j in i:
				exp-=1
				hash+=ord(j)*(k_grms**exp)
			if hash not in self.hash_list:
				self.hash_list.append(hash)
		return self.hash_list
	def display_matrix(self,final1,final2,final3):
		'''This function displays all the resultant lists in a Matrix format.
		Input  : Three lists containing all the final values after computation
		Output : Displays all the three lists in a matrix format '''
		print("----------------------------------------%s----------------------------------------"%(today))
		print("Text Files present in the directory :",files[1:])
		print("Plagiarism detected using Bag Of Words Technique!!\n")
		for i in range(len(final1)):
			for j in range(len(final1)):
				print(final1[i][j].ljust(4),end="\t")
			print("\n")
		print("\n\nPlagiarism detected using Longest Common Substring Technique!!\n")	
		for i in range(len(final2)):
			for j in range(len(final2)):
				print(final2[i][j].ljust(4),end="\t")
			print("\n")
		print("\n\nPlagiarism detected using Fingerprinting Technique!!\n")	
		for i in range(len(final3)):
			for j in range(len(final3)):
				print(final3[i][j].ljust(4),end="\t")
			print("\n")
string_B=[]
string_L=[]
files=["FN"]
for filename in glob.glob('*.txt'):
	if filename=="logfile.txt":
		continue
	files.append(filename.strip(".txt"))
	f = open(filename,'r')
	while 1:		
		line=f.readline()
		if not line:break
		string_L.append(line)
		string_B.append(line.split())
	f.close()
P=plag_check()
#The following code computes the plagiarism using the Bag of Words Technique.
final1=[]
final1.append(files)
for i in range (len(string_B)):
	temp=[final1[0][i+1]]
	for j in range(len(string_B)):
		if i==j:
			temp.append("SF")
		else:
			temp.append(str(P.bagofwords(string_B[i],string_B[j]))+"%")
	final1.append(temp)
#The following code computes the plagiarism using the Longest Common Substring Technique.
final2=[]
final2.append(files)
for i in range (len(string_L)):
	temp=[final2[0][i+1]]
	for j in range(len(string_L)):
		if i==j:
			temp.append("SF")
		else:
			sum_str=len(string_L[i])+len(string_L[j])
			lcs=P.lc_substring(str(string_L[i]),str(string_L[j]))
			match=((lcs*2)/sum_str)*100
			temp.append(str(int(match))+"%")
	final2.append(temp)
#The following code computes the plagiarism using the Fingerprinting Technique.
final3=[]
final3.append(files)
for i in range(len(string_L)):
	temp=[final2[0][i+1]]
	for j in range(len(string_L)):
		if i==j:
			temp.append("SF")
		else:
			hlist1=P.fingerprinting(str(string_L[i]))
			hlist2=P.fingerprinting(str(string_L[j]))
			common=[]
			for k in hlist1:
				if k in hlist2:
					common.append(k)
			hsum1=sum(hlist1)
			hsum2=sum(hlist2)
			csum=sum(common)
			per=(2*csum)*100/(hsum1+hsum2)
			temp.append(str(math.ceil(per))+"%")
	final3.append(temp)
#The following code displays the output and stores the same in a logfile.
P.display_matrix(final1,final2,final3)
f=open("logfile.txt", "a+")
sys.stdout=f
P.display_matrix(final1,final2,final3)
f.close()