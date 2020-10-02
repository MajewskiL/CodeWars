#https://www.codewars.com/kata/594b898169c1d644f900002e
import re

def defrag(txt,funkcja={}):
    wynik=""
    while txt:
        ciag=re.match(r'([FLRPp()])(\d*)',txt)
        txt=re.sub(r'^([FLRPp()])(\d*)','',txt)
        if ciag[1]=="p":
            ciag2=re.match(r'(.*?)(q)',txt)
            txt=re.sub(r'^(.*?(q))','',txt)
            keyw={str(ciag[1].upper()+ciag[2]):ciag2[1]}
            if str(ciag[1].upper()+ciag[2]) in funkcja: raise NameError("Error")
            if str(ciag[1].upper()+ciag[2]) in ciag2[1]: raise NameError("Error")
            funkcja.update(keyw)
        else:
            wynik=wynik+ciag[1]+ciag[2]
    for x,y in funkcja.items():
        for z,s in funkcja.items():
            if x in s and z in y: raise NameError("Error")
            
    glab=0
    pod,txt="",""
    while wynik:
            ciag=re.match(r'([FLRP()])(\d*)',wynik)
            wynik=re.sub(r'^([FLRP()])(\d*)','',wynik)
            pow=int(ciag[2] or "1")
            if ciag[1] in ("FLR"):
                if glab==0:txt=txt+ciag[1]*pow
                else: pod=pod+ciag[1]*pow
            elif ciag[1] in ("P"):
                if glab==0:
                    wynik=funkcja[ciag[1]+ciag[2]]+wynik
                else: 
                    pod=pod+funkcja[ciag[1]+ciag[2]]
            elif ciag[1]=="(":
                if glab!=0: pod=pod+ciag[1]+ciag[2]
                glab+=1
            elif ciag[1]==")":
                glab-=1
                if glab==0:
                    txt+=defrag(pod,funkcja)*pow
                    pod=""
                else: pod=pod+ciag[1]+ciag[2]
    
    return(txt)

def execute(txt):
    print(txt)
    txt=defrag(txt,{})
    x,y,b,k=0,0,0,0
    kier=[[0,1],[1,0],[0,-1],[-1,0]]
    mapa=["*"]
    hlp=""
    while txt:
            ciag=re.match(r'([FLRP()])(\d*)',txt)
            txt=re.sub(r'^([FLRP()])(\d*)','',txt)
            pow=int(ciag[2] or "1")
            for i in range(pow):
                if ciag[1]=="R":
                    k+=1
                    if k>3:k=0
                elif ciag[1]=="L":
                    k-=1
                    if k<0:k=3
                elif ciag[1]=="F":
                    lm,hm=len(mapa[x]),len(mapa)
                    x,y=x+kier[k][0],y+kier[k][1]
                    if y==lm:
                        for z in range(hm): mapa[z]="".join(mapa[z]+" ")
                    elif x==hm: mapa.append(" "*lm)
                    elif y<0:
                        for z in range(hm): mapa[z]="".join(" "+mapa[z])
                        y=0
                    elif x<0:
                        mapa=[" "*lm]+mapa
                        x=0
                    mapa[x]="".join(mapa[x][:y]+"*"+mapa[x][y+1:])
    return("\r\n".join(mapa))
