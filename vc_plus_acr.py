
l1size=10
l2size=100
vcsize=5

lrusize=100
fifosize=100



l2misses=0
l1misses=0
vcmisses=0

l1hits=0
l2hits=0
vchits=0

lrumisses=0
fifomisses=0

lruevicted=0
fifoevicted=0

#currentl1=0;
#currentl2=0;
#currentvc=0;  
#
#currentfifo=0
#currentlru=0
      

l1=[None]*l1size
l2=[]
vc=[] 

lru=[]
fifo=[]
policy=0

        
def insertCache(addr):
    global l1misses,l2misses,vcmisses,vc,l1,l2,l2hits,l1hits
    n=addr%l1size

    
    if l1[n]!=addr:
        l1misses+=1
    else: 
        l1hits+=1
        return
    
    if not vcsearch(addr):    
        vcmisses+=1
    else:
        addtol1(addr)
        return
        #vc.remove(addr)
    
    if not l2search(addr):
        l2misses+=1
    else:
        l2hits+=1
        addtol1(addr)
        update(addr)
        return
    
    
    addtol1(addr)
    addtol2(addr)
        


def update(addr):
    global lru,lrusize,lrumisses,fifo,fifomisses,fifosize
    if addr in lru:
        lru.remove(addr)
        lru.append(addr)
    else:
        lrumisses+=1
        if len(lru)<lrusize:
            lru.append(addr)
        else :
            lruevicted=lru[0]
            lru=lru[1:]
            lru.append(addr)
            
    if addr not in fifo:
        fifomisses+=1
        if len(fifo)<fifosize:
            fifo.append(addr)
        else:
            fifoevicted=fifo[0]
            fifo=fifo[1:]
            fifo.append(addr)
    



        
def addtol1(addr):
    global l1,l1size
    n=addr%l1size
    if l1[n] is not None  and l1[n]!=addr:
        vcinsert(l1[n])
    l1[n]=addr
    


def evict(addr):
    global policy,lru,fifo,l2
    
    if policy==0:
        if addr in lru:
            for i in l2:                    #all wouldnt be same element
                if i not in lru:           
                    l2.remove(i)             #remove from l2 not in lru
                    l2.append(addr)
                    
        else:                                    
            l2.remove(lruevicted)               #remove from l2 same as lru
            l2.append(addr)
    else:
        if addr in fifo:
            for i in l2:
                if i not in fifo:
                    l2.remove(i)            #remove from l2 not in fifo
                    l2.append(addr)
        else:
            l2.remove(fifoevicted)              #remove same as fifo
            l2.append(addr)
    
    
                    
                                        
                    
#    #policy decide,
#    call evict
#    common update
    
def addtol2(addr):
    global lru,fifo,l2,lrumisses,fifomisses,policy,lrusize
    
    update(addr)
    
    if lrumisses>fifomisses:
        policy=1
    else:
        policy=0
        
    if len(l2)<l2size:
        l2.append(addr)
    else:
        evict(addr)
    
    
#    global l2,currentl2
#    updatelru(addr)
#    
#    if addr in l2:
#        l2.remove(addr)
#        l2.append(addr)
#        return
#    if currentl2<l2size:
#        l2.append(addr)
#        currentl2+=1
#    else:
#        l2=l2[1:]
#        l2.append(addr)
    
    
        


def vcinsert(addr):
    global vc
    
    if len(vc)<vcsize:
        vc.append(addr)
    else:
        vc=vc[1:]
        vc.append(addr)
    
        
        


def vcsearch(addr):
    global vchits,vc
    if addr in vc:
        vchits+=1
        vc.remove(addr)
        return True
    return False



      
def l2search(addr):
    if addr in l2:
        return True
    return False


def main():
    afile = open("Randommix.txt", "r" )
    r=[]
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
#    
#r=[1,2,3,4,1,5,2,3,4]
#
#for i in r:
#    insertCache(i)     
    
        
        
