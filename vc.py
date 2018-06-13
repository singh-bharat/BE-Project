
import random

l1size=10
l2size=100
vcsize=5

vchits=0
l2misses=0
l1misses=0
vcmisses=0
zero=0

l1hits=0
l2hits=0

class block(object):
    def __init__(self):
        self.valid=False 
        self.add=0
        


class cache(object):
    def __init__(self,noOfBlocks):
        self.size=0
        self.blocks=[None]*noOfBlocks
        #self.blocks=[]



l1=cache(l1size)
l2=cache(l2size)
vc=cache(zero) 



def createCache():                 
    for i in range(l1size):             #direct mapped for l1
        l1.blocks[i]=block() 

    for i in range(l2size):          #2 way set associative
        l2.blocks[i]=[block(),block()]
        
        
#    for i in range(vcsize):
#        vc.blocks[i]=block()
        
def insertCache(addr):
    global l1misses,l2misses,vcmisses,l1hits,l2hits,l1,l2,vc
    n=addr%l1size
    
    if l1.blocks[n].add!=addr:
        l1misses+=1
    else: 
        l1hits+=1
        return
        
    if not vcsearch(addr):    
        vcmisses+=1
    else:
        addtol1(addr)
        return
        
    
    if not l2search(addr):
        l2misses+=1
    else:
        l2hits+=1
        addtol1(addr)
        return
        
    addtol2(addr)
    addtol1(addr)
        
        
        
        
        
        
        
def addtol1(addr):
    n=addr%l1size
    if l1.blocks[n].valid and l1.blocks[n].add!=addr:
        vcinsert(l1.blocks[n].add)
    l1.blocks[n].add=addr
    l1.blocks[n].valid=True
    
def addtol2(addr):
    n=addr%l2size
    b=block()
    b.add=addr
    b.valid=True
    l2.blocks[n][1]=l2.blocks[n][0]
    l2.blocks[n][0]=b
    
        


def vcinsert(addr):
    b=block()
    b.add=addr
    b.valid=True
    
    if vc.size<vcsize:
        vc.blocks.append(b)
        vc.size+=1
    else:
        vc.blocks=vc.blocks[1:]
        vc.blocks.append(b)
        
        


def vcsearch(addr):
    global vchits
    if vc.size==0:
        return False
    for i in range(vc.size):
        if vc.blocks[i].add==addr:
            vchits+=1
            return True
    return False



      
def l2search(addr):
    for i in range(l2size):
        for j in 0,1:
            if l2.blocks[i][j].add==addr:
                return True
    return False


def main():
    afile = open("Random.txt", "r" )
    r=[]
    createCache()
    for l in afile:
        for w in l.split():
            r.append(int(w))
        
    for i in r:
        insertCache(i)
    
    print("Misses in L1 :",l1misses)
    print("Hits in L1 :",l1hits)
    print("Misses in L2 :",l2misses)
    print("Hits in L2 :",l2hits)
    print("Misses in Victim Cache :",vcmisses)
    print("Hits in Victim Cache :",vchits)
    
    "calculate time with variables l1hits,l1misses,l2hits,l2misses,vcmisses,vchits"
        
main()
     
    
        
        
        
