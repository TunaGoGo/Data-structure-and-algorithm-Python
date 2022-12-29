from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name) #将名字按照顺序先后放入queue中

    while simqueue.size() > 1:
        for i in range(num-1):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    
    return simqueue.dequeue()

print(hotPotato([1,2,3,4,5,6],7))    