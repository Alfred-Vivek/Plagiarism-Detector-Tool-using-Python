import glob
def plag_check(s1,s2):
   matrix=[[0]*(len(s2)+1) for i in range(len(s1)+1)]
   max_count=0
   for i in range(1,len(s1)+1):
       for j in range(1,len(s2)+1):
           if s1[i-1]==s2[j-1]:
               matrix[i][j]=matrix[i-1][j-1]+1
               if matrix[i][j]>max_count:
                   max_count=matrix[i][j]
           else:
               matrix[i][j]=0
   return max_count
string=[]
for filename in glob.glob('*.txt'):
	f = open(filename,'r')
	while 1:		
		line=f.readline()
		if not line:break
		string.append(line)
	f.close()
final=[]
for i in range (len(string)):
	temp=[]
	for j in range(len(string)):
		if i==j:
			temp.append(-1)
		else:
			sum_str=len(string[i])+len(string[j])
			lcs=plag_check(str(string[i]),str(string[j]))
			match=((lcs*2)/sum_str)*100
			temp.append(int(match))
	final.append(temp)
for i in final:
	print(i,"\n")