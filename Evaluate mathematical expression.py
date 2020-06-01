#https://www.codewars.com/kata/52a78825cdfc2cfc87000005/train/python
import re
def wynik(ciag):
    znak,wyn,a,b,c=["*/","+-"],0,0,0,0

    while b<len(ciag): #Calculations
        if ciag[b] in znak[c]:
            if ciag[b]=="*": wyn=str(float(ciag[b-1])*float(ciag[b+1]))
            elif ciag[b]=="+": wyn=str(float(ciag[b-1])+float(ciag[b+1]))
            elif ciag[b]=="-": wyn=str(float(ciag[b-1])-float(ciag[b+1]))
            else: wyn=str(float(ciag[b-1])/float(ciag[b+1]))
            if len(ciag)>=3:
                ciag[b+1]=wyn
                del ciag[b-1:b+1]
            else:
                ciag[b-1]=wyn
                del ciag[b:b+2]
        else: b+=1
        if c==0 and b>=len(ciag)-1: c,b=1,0
    return(str(ciag[0]))

def pre_licz(strg): #Unnecessary characters / string to list
    licz,zmiana,a=[],[[" ",""],["--","+"],["-+","-"],["+-","-"],["++","+"]],0
    for x,y in zmiana: strg=strg.replace(x,y)
    while strg:
        ciag=re.match(r'[\d.]+|\+|\-|\*|\/',strg)
        licz.append(ciag.group(0))
        strg=re.sub(r'[\d.]+|\+|\-|\*|\/',"",strg,1)
    while a<len(licz)-1:
        if licz[a]=="-" and (a==0 or licz[a-1] in ("*/")):
            licz[a]=str(float(licz[a+1])*-1)
            del licz[a+1]
        elif licz[a]=="+" and (a==0 or licz[a-1] in ("*/")):
            del licz[a]
        else: a+=1
    return wynik(licz)

def calc(exp,a=0): #removing parentheses
    while "("  in exp:
        for x in range(len(exp)):
            if exp[x]=="(":a=x
            elif exp[x]==")":break
        exp=exp[:a]+pre_licz(exp[a+1:x])+exp[x+1:]
    return float(pre_licz(exp))
