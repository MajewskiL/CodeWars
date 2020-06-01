#https://www.codewars.com/kata/58c5577d61aefcf3ff000081
def rozkmin (string,n):
    l=[[] for i in range(n)]
    x=0
    s=1
    for a in range(len(string)):
        l[x].append(string[a])
        if s==1:x=x+1
        else: x=x-1
        if x==n:
            x=n-2
            s=0
        if x<0:
            x=1
            s=1
    return(l)

def encode_rail_fence_cipher(string, n):
    #print(string,n)
    wynik=""
    l=rozkmin(string,n)
    for a in l:
        wynik=wynik+"".join(a)
    return(wynik)

def decode_rail_fence_cipher(string, n):
    wynik=""
    k=[[] for i in range(n)]
    z=len(string)
    l=rozkmin(string,n)
    for a in range(len(l)):
        k[a].append(string[:len(l[a])])
        string=string[len(l[a]):]
    x=0
    s=1
    for a in range(z):
        wynik=wynik+k[x][0][0]
        k[x][0]=k[x][0][1:]
        if s==1:x=x+1
        else: x=x-1
        if x==n:
            x=n-2
            s=0
        if x<0:
            x=1
            s=1
    return(wynik)

    def encode_rail_fence_cipher(string, n):
        wynik=""
        l=rozkmin(string,n)
        for a in l:
            wynik=wynik+"".join(a)
        return(wynik)
