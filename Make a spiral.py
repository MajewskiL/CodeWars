#https://www.codewars.com/users/Spalding/completed_solutions
def spiralize(size):
    spiral=[[0 for x in range(size)] for x in range(size)]
    x,y,w,iter=0,-1,0,0
    wektor=[[0,1],[1,0],[0,-1],[-1,0]]
    while size>0:
        for i in range(size):
            x+=wektor[w][0]
            y+=wektor[w][1]
            spiral[x][y]=1
        iter+=1
        if iter%2==1:
            if iter<2: size-=1
            else: size-=2
        if size==1 and iter%2==0: return spiral
        w=(w+1)%4
    return spiral
