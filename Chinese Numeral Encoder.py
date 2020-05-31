#https://www.codewars.com/kata/52608f5345d4a19bed000b31
def to_chinese_numeral(n):
    print(n)
    numerals = {
        "-":"负",
        ".":"点",
        0:"零",
        1:"一",
        2:"二",
        3:"三",
        4:"四",
        5:"五",
        6:"六",
        7:"七",
        8:"八",
        9:"九",
        10:"十",
        100:"百",
        1000:"千",
        10000:"万"
    }
    long={5:10000,4:1000,3:100,2:10,1:1}
    n=str(n)
    end,przed,pre,middle="",n,"",""
    if "." in n:
        tu=n.index(".")
        przed,po,end=n[:tu],n[tu+1:],"点"
        for z in po: end+=numerals[int(z)]
    if przed[0]=="-": pre,przed=numerals["-"],przed[1:]
    if len(przed)==2 and int(przed)<20:
        return pre+numerals[10]+end if int(przed)==10 else pre+numerals[10]+numerals[int(przed[1])]+end
    for z in range(len(przed),0,-1):
            middle+=numerals[int(przed[0])]
            if przed[0]!="0" and z!=1: middle+=numerals[long[z]]
            przed=przed[1:]
    if len(middle)!=1: middle=middle.rstrip(numerals[0])
    for x in range(len(middle)-1,0,-1):
        if middle[x]==numerals[0] and middle[x-1]==numerals[0]:
            middle=middle[:x]+middle[x+1:]
    return pre+middle+end
