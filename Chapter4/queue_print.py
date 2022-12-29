from pythonds.basic.queue import Queue
import random

class Printer:
    def __init__(self, ppm):
        #初始化
        self.pagerate = ppm #打印速度
        self.currentTask = None #当前任务
        self.timRemaining = 0 #任务倒计时

    def tick(self):
        #打印1秒
        if self.currentTask != None:
            self.timRemaining = self.timRemaining - 1
            if self.timRemaining <= 0:
                self.currentTask = None
    
    def busy(self):
        #打印忙？
        if self.currentTask != None:
            return True
        else:
            return False
    
    def startNext(self, newtask):
        #打印新作业 
        self.currentTask = newtask
        self.timRemaining = newtask.getPages() \
                            * 60/self.pagerate

class Task:
    def __init__(self, time):
        #生成时间戳
        self.timestamp = time
        self.pages = random.randrange(1,21)  #打印任务有多少页

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages
    
    def waitTime(self, currenttime):
        #等待时间
        return currenttime - self.timestamp

def newPrintTask():
    #模拟180s 生成一个作业
    num = random.randrange(1,181)
    if num == 180:
        #生成打印作业
        return True
    else:
        return False

def simulation(numSeconds, pagePerMinute):
    """
    Paramaters:
        numSeconds: simulate whole running time 
        pagePerMinute: page printed per minute

    Return:
        summary of average waiting time and how many task remained
    """
    labprinter = Printer(pagePerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        #once generate printing task
        if newPrintTask():
            #generate print start time and No. of pages of one task
            task = Task(currentSecond)
            #enqueue print task into Printer Queue
            printQueue.enqueue(task) 
            
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()
    
    averageWait = sum(waitingtimes)/ len(waitingtimes)

    print("Average Wait %6.2f secs %3d task remaining." %(averageWait, printQueue.size()))

if __name__ == '__main__':
    for i in range(10):
        simulation(3600,5)
        