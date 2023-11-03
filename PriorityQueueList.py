
class PriorityQueueList:
    def __init__(self): #initializes the attributes of the object
        self.queue = []

    def is_empty(self): #returns True if the queue is empty, False otherwise
        return (len(self.queue) == 0)

    def size(self): #returns the number of items in the queue
        return (len(self.queue))

    def enqueue(self,i): #insert the item into the last position in the queue
        if self.is_empty():
            self.queue.append(i)
        else: # find item's correct location and insert to that location
            self._enqueue(i)

    def _enqueue(self, i): #helper function of enqueue(): using binary search to find the corect location and insert i at that place 
        # Use binary search to find the correct position to insert i
        first = 0
        last = len(self.queue) - 1

        while first <= last:
            midpoint = (first + last) // 2
            if i < self.queue[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
        
        # Insert i at the correct position
        self.queue.insert(first, i)

    def dequeue(self): #removes the first item in the queue
        if self.is_empty():
            return None 
        return self.queue.pop(0)

    def __str__(self): #returns a string version of the queue
        return (str(self.queue))
