colors=['R','G','B']
nodes=['A','B','C','D','E']
edges={('A','B'),('A','E'),('B','C'),('B','D'),('C','D'),('D','E')}
assignment={}
solutions=[]
def valid(n,c):
    for a,b in edges:
        if n==a and b in assignment and assignment[b]==c:
            return False
        if n==b and a in assignment and assignment[a]==c:
            return False
    return True
def backtrack(i=0):
    if i==len(nodes):
        solutions.append(assignment.copy())
        return
    n=nodes[i]
    for c in colors:
        if valid(n,c):
            assignment[n]=c
            backtrack(i+1)
            del assignment[n]
backtrack()
print(len(solutions))
for s in solutions:
    print(' '.join(k+':'+v for k,v in sorted(s.items())))
