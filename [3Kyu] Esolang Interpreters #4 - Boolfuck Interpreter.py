#https://www.codewars.com/kata/5861487fdb20cff3ab000030
import textwrap
def boolfuck(code, temp=""):
  c, t, i, table, inp, output,p,k =0,0,0,["0"],[],"",0,0
  for item in temp: #change chr to bin
      c=list(bin(ord(item)))
      c.pop(1)
      c=c[::-1]
      if len(c)<8:c+=["0"]*(8-len(c))
      inp+=c
  c=0
  while len(code)>c:
    if code[c]==",":
      if i<len(inp): table[t]=inp[i]
      else: table[t]="0"
      i+=1
    elif code[c] in "+":
      if table[t]=="0": table[t]="1"
      else: table[t]="0"
    elif code[c]==">":
      t+=1
      if t==len(table): table.insert(t,"0")
    elif code[c]=="<":
      if t-1<0: table.insert(0,"0")
      else:  t-=1
    elif code[c]==";": output+=table[t]
    elif code[c]=="[" and table[t]=="0":
      for x in range(c+1,len(code)):
        if code[x]=="]" and p==0:
          c,p=x,0
          break;
        elif code[x]=="[": p+=1
        elif code[x]=="]" and p!=0: p-=1
    elif code[c]=="]" and table[t]!="0":
      for x in range(c-1,-1,-1):
        if code[x]=="[" and p==0:
          c,p=x,0
          break;
        elif code[x]=="]": p+=1
        elif code[x]=="[" and p!=0: p-=1
    c+=1
  if len(output)!=0 and len(output)%8!=0: output+="0"*(8-len(output)%8)
  output=textwrap.wrap(output,8)
  for x in range(len(output)):
      output[x]=chr(int(output[x][::-1],2))
  return ("".join(output))
