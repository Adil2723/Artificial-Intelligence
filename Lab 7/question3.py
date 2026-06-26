grid=[
[0,6,0,2,0,5],
[0,0,4,6,0,0],
[0,1,2,0,0,0],
[0,5,6,0,4,0],
[0,4,3,0,2,0],
[3,0,5,0,0,6]]
n=6
rb=2
cb=3
def valid(r,c,v):
    for i in range(n):
        if grid[r][i]==v or grid[i][c]==v:
            return False
    br=(r//rb)*rb
    bc=(c//cb)*cb
    for i in range(br,br+rb):
        for j in range(bc,bc+cb):
            if grid[i][j]==v:
                return False
    return True
def solve():
    for i in range(n):
        for j in range(n):
            if grid[i][j]==0:
                for v in range(1,n+1):
                    if valid(i,j,v):
                        grid[i][j]=v
                        if solve():
                            return True
                        grid[i][j]=0
                return False
    return True
if solve():
    for r in grid:
        print(' '.join(str(x) for x in r))
else:
    print('No solution')
