import glob
def plag_check(l1,l2):
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
string = []
for filename in glob.glob('*.txt'):
	f = open(filename,'r')
	while 1:		
		line = f.readline()
		if not line:break
		string.append(line.split())
	f.close()
final=[]
for i in range (len(string)):
	temp=[]
	for j in range(len(string)):
		if i==j:
			temp.append(-1)
		else:
			temp.append(plag_check(string[i],string[j]))
	final.append(temp)
for i in final:
	print(i,"\n")