class PriorityQueueList:
    def __init__(self): #initializes the attributes of the object
        self.queue = []

    def is_empty(self): #returns True if the queue is empty, False otherwise
        work = 1
        return (len(self.queue) == 0), work

    def size(self): #returns the number of items in the queue
        work = 1
        return (len(self.queue)), work

    def enqueue(self,i): #insert the item into the last position in the queue
        work = 0
        check, w = self.is_empty()
        work += w
        if check == True:
            self.queue.append(i)
            work += 1
        else: # find item's correct location and insert to that location
            work += self._enqueue(i)

        return (work)

    def _enqueue(self, i): #helper function of enqueue(): using binary search to find the corect location and insert i at that place 
        # Use binary search to find the correct position to insert i
        work = 0
        first = 0
        last = len(self.queue) - 1
        work += 2

        while first <= last:
            work += 1
            midpoint = (first + last) // 2
            work += 1
            if i < self.queue[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
            work += 1
        
        # Insert i at the correct position
        self.queue.insert(first, i)
        work += 1
        return (work)

    def dequeue(self): #removes the first item in the queue
        work = 0
        check, w = self.is_empty()
        work += w
        if check == True:
            return None, work 
        else:
            work += 1
            return self.queue.pop(0), work

    def __str__(self): #retrun the string version of the queue
        work = len(self.queue)
        return str(self.queue), work
