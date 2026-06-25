shirts=[f'S{i}' for i in range(1,6)]
pants=[f'P{i}' for i in range(1,4)]
sq=[f'SQ{i}' for i in range(1,3)]
sp=[s+'-'+p for s in shirts for p in pants]
items=sp+sq
days=['Mon','Tue','Wed','Thu','Fri']
assignment={}
used=set()
count=0
samples=[]
def backtrack(i=0):
    global count
    if i==5:
        count+=1
        if len(samples)<20:
            samples.append(assignment.copy())
        return
    d=days[i]
    for it in items:
        if it in used:
            continue
        if d in ('Mon','Thu') and '-' not in it:
            continue
        if d=='Fri' and it not in sq:
            continue
        used.add(it)
        assignment[d]=it
        backtrack(i+1)
        used.remove(it)
        del assignment[d]
backtrack()
print(count)
for s in samples:
    print(' '.join(d+':'+s[d] for d in days))
