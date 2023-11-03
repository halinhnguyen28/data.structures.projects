
class BinaryHeap:
    
    def __init__(self):
        self.heapList = [None]
        self.currentSize = 0
        
    def insert(self,k):
       work = 0
       self.heapList.append(k)
       work += 1
       self.currentSize += 1
       work += self.perc_up(self.currentSize)
       return work

    def perc_up(self,i):
        work = 0
        while i//2>0: 
            work += 1
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
                work += 3
            i = i//2
            work += 1
        return(work)

    def get_root(self):
        work = 0
        check, w = self.is_empty()
        work += w
        if check == True:
            return None, work #I added this; it wasn't in the book
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        work += 4
        work += self.percDown(1)
        return (retval), work
    
    def percDown(self,i):
        work = 0
        while(i*2) <= self.currentSize:
            work += 1
            mc, w = self.minChild(i)
            work += w
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp 
                work += 3
            i = mc
            work += 1
        return work
        
    def minChild(self,i):
        work = 0
        if i*2 +1 > self.currentSize:
            work += 1
            return i*2, work
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                work += 1
                return i*2, work
            else:
                work += 1
                return i*2+1, work

    def size(self):
        work = 1
        return (self.currentSize), work
    
    def is_empty(self):
        work =1
        return (self.currentSize == 0), work   
            
    def __str__(self):
        work = len(self.heapList)
        return (str(self.heapList)), work

