#https://www.codewars.com/kata/5a5db0f580eba84589000979
import re

def tower(tow):
    if tow!=" ": return("".join("T"+tow))
    else: return(tow+tow)

def zombie_move(mapa,zombies,turn):
    z_out=0
    for x in range(len(mapa)):
        for y in range(len(mapa[x])):
            ciag=mapa[x][y][0]
            if ciag=="Z":
                ciag2=int(mapa[x][y][1:])
                z_out+=1
                if mapa[x][y-1]!=" ":mapa[x][y-1]=" "
                if y-1>=0: mapa[x][y],mapa[x][y-1]=mapa[x][y-1],mapa[x][y]
    for x in zombies:
        if x[0]>turn:z_out+=1
        if x[0]==turn:
            z_out+=1
            mapa[x[1]][len(mapa[0])-1]="Z"+str(x[2])
    if z_out==0:return None
    return(mapa)

def shoot_striaght(mapa):
    shoot=[0]*len(mapa)
    for x in range(len(mapa)):
        for y in mapa[x]:
            ciag=re.match(r'([T])(\d*)',y)
            if ciag:
                sh=int(ciag[2] or "0")
                shoot[x]+=sh
        for y in mapa[x]:
            ciag=re.match(r'([Z])(\d*)',y)
            if ciag:
                gdzie=mapa[x].index(y)
                if shoot[x]<int(ciag[2]):
                    mapa[x][gdzie]="Z"+str(int(ciag[2])-shoot[x])
                    shoot[x]=0
                else:
                    shoot[x]=shoot[x]-int(ciag[2])
                    if shoot[x]<0: shoot[x]=0
                    mapa[x][gdzie]=" "
    return(mapa)

def shoot_by_S(mapa):
    for y in range(len(mapa[0])-1,-1,-1):
        for x in range(len(mapa)):
            ciag=re.match(r'(TS)',mapa[x][y])
            if ciag:
                ile=len(mapa[x])-y
                #look up
                for z in range(1,min(x+1,ile)):
                    if mapa[x-z][y+z][0]=="Z" and (x-z)>=0:
                        ciag2=re.match(r'([Z])(\d*)',mapa[x-z][y+z])
                        if (int(ciag2[2])-1)==0: mapa[x-z][y+z]=" "
                        else: mapa[x-z][y+z]="Z"+str(int(ciag2[2])-1)
                        break
                #look straight
                for z in range(1,ile):
                    if mapa[x][y+z][0]=="Z":
                        ciag2=re.match(r'([Z])(\d*)',mapa[x][y+z])
                        if (int(ciag2[2])-1)==0: mapa[x][y+z]=" "
                        else: mapa[x][y+z]="Z"+str(int(ciag2[2])-1)
                        break
                #look down
                for z in range(1,min(len(mapa)-x,ile)):
                    if mapa[x+z][y+z][0]=="Z":
                        print("Cioch d",x,y)
                        ciag2=re.match(r'([Z])(\d*)',mapa[x+z][y+z])
                        if (int(ciag2[2])-1)==0: mapa[x+z][y+z]=" "
                        else: mapa[x+z][y+z]="Z"+str(int(ciag2[2])-1)
                        break
    return(mapa)


def plants_and_zombies(lawn,zombies):
    mapa=[list(map(tower,i)) for i in lawn]
    turn=0
    out=True
    while out:
        #move zombie
        mapa=zombie_move(mapa,zombies,turn)
        if mapa==None: return None
        #is zombie approach
        for x in mapa:
            if x[0][0]=="Z": return(turn+1)
        #shoot zombie straight
        mapa=shoot_striaght(mapa)
        #shoot zombie by S
        mapa=shoot_by_S(mapa)
        turn+=1
    return (None)
