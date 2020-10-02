#https://www.codewars.com/kata/58905bfa1decb981da00009e
class Dinglemouse(object):

    def __init__(self, queues, capacity):

        self.wys=len(queues)
        self.ile=capacity
        self.kolej=[list(x) for x in queues]
        self.winda=[]
        pass

    def theLift(self):
        ptr,kier,stop,output,osob=0,1,1,[0],0
        for x in self.kolej: osob+=len(x)
        while osob!=0 or len(self.winda):
            if len(self.winda)!=0:
                temp=self.winda.copy()
                for x in temp:
                    if x==ptr:
                        self.winda.remove(x)
                        osob-=1
                        stop=1
            temp=self.kolej[ptr].copy()
            for x in temp:
                if ((x>ptr and kier==1) or (x<ptr and kier==-1)):
                    if len(self.winda)<self.ile:
                        self.winda.append(x)
                        self.kolej[ptr].remove(x)
                    stop=1
            if stop==1 and output[len(output)-1]!=ptr:
                output.append(ptr)
            stop=0
            ptr+=kier
            if ptr==self.wys: ptr,kier=ptr-1,-1
            elif ptr==-1: ptr,kier=0,1
        if output[len(output)-1]!=0: output.append(0)
        return (output)
