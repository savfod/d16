def parse_ints(l):
	n=list(map(int, l.split()))
	return n

def convert(s):
    for i in s:
        i[2]=i[2]*2.7
        i[4]=i[4]*2.7
        return s
  
queries=[]
f_read = open('Newfile.py', 'r')
for line in f_read:
    line = line.strip()
    queries.append(line)
print(queries)
hum=0
for i in range(len(queries)):
    queries[i]=parse_ints(queries[i])
    queries[i].insert(0, "pb")
    queries[i].insert(3, 0)
    queries[i].insert(5, hum)
    hum+=1
print (queries)
queries=convert(queries)
print (queries)
class event:
    type_e=1
    where=1
    when=1
    lift=1
    destination=1
    human=1
class lift:
    k=0
for i in queries:
    for k in range(len(i)):
        i[k]=0
print(queries)    
