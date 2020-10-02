#https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
def is_ship(ship,x,y):
    a,b,dl=x,y,1
    while ship[a][b+1]==1: b,dl=b+1,dl+1
    while ship[a+1][b]==1: a,dl=a+1,dl+1
    return([[x,y],[a,b],dl])

def mark(ship,axs):
    for a in range(axs[0][0],axs[1][0]+1):
        for b in range (axs[0][1],axs[1][1]+1): ship[a][b]=2
    return(ship)

def ext_ships(ships):
    temp=[[0 for x in range(len(ships[0])+2)] for y in range(len(ships)+2)]
    for x in range(0,len(ships)):
        for y in range(0,len(ships[0])):
             temp[x+1][y+1]=ships[x][y]
    return(temp)

def alone(ships,axs):
    for a in range(axs[0][0]-1,axs[1][0]+2):
        for b in range (axs[0][1]-1,axs[1][1]+2):
            if (a<axs[0][0] or a>axs[1][0]) and (b<axs[0][1] or b>axs[1][1]):
                if ships[a][b]==1:
                    return True
    return False   

def validate_battlefield(ships):
    wynik=[0]*4
    ships=ext_ships(ships)
    for x in range(1,len(ships)-1):
        for y in range(1,len(ships)-1):
            if ships[x][y]==1:
                #find ship
                axs=is_ship(ships,x,y)
                if axs[2]>4: return False
                #is ship alone
                if alone(ships,axs): return False
                wynik[axs[2]-1]+=1
                #mark ship
                ships=mark(ships,axs)

    return(wynik[0]==4 and wynik[1]==3 and wynik[2]==2 and wynik[3]==1)
