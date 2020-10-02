#https://www.codewars.com/kata/5235c913397cbf2508000048
def ilo(string,x):
    if string[x]=="*":
        return(' '.join(string[0:x-1])+" "+str(float(string[x-1])*float(string[x+1]))+" "+' '.join(string[x+2:]))
    else:
        return(' '.join(string[0:x-1])+" "+str(float(string[x-1])/float(string[x+1]))+" "+' '.join(string[x+2:]))

def sru(string,x):
    if string[x]=="+":
        return(' '.join(string[0:x-1])+" "+str(float(string[x-1])+float(string[x+1]))+" "+' '.join(string[x+2:]))
    else:
        return(' '.join(string[0:x-1])+" "+str(float(string[x-1])-float(string[x+1]))+" "+' '.join(string[x+2:]))
           
 
class Calculator(object):
  def evaluate(self, string):
    string=string.split()
    hlp=""
    if len(string)==1:
        hlp=float(string[0])
    elif (string.count("*") or string.count("/"))!=0:
        z=len(string)
        s=len(string)
        if string.count("*")!=0: z=string.index("*")
        if string.count("/")!=0: z=string.index("/")
        hlp=Calculator().evaluate(ilo(string,min(z,s)))
    elif (string.count("+") or string.count("-"))!=0:
        z=len(string)
        s=len(string)
        if string.count("+")!=0: z=string.index("+")
        if string.count("-")!=0: z=string.index("-")
        hlp=Calculator().evaluate(sru(string,min(z,s)))
    return (hlp)
