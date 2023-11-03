class Node:    
    def __init__(self,d):
        self._data = d
        self._next = None

    def get_data(self):
        return(self._data)

    def get_next(self):
        return(self._next)

    def set_data(self,newData):
        self._data = newData

    def set_next(self,newNext):
        self._next = newNext

    def __str__(self):
        return str(self._data) 

class PriorityQueueNode:

    def __init__(self): # attributes and variables in the Priority Queue Node
        self._front = None
        self._rear  = None 
        self._length = 0 

    def enqueue(self, item):  # adds a node to the end of the Priority Queue Node
        work = 0
        node = Node(item)
        check, w = self.is_empty()
        work += w+1

        if check == True:
            self._front = node
            self._rear = node
            work += 2
        else:
            low = self._front
            high = None
            work += 2
            while low != None and item > low.get_data():
                high = low
                low = low.get_next()
                work += 2

            if high == None:
                node.set_next(self._front)
                self._front = node
                work += 2

            elif low == None:
                high.set_next(node)
                self._rear = node
                work += 2

            else:
                high.set_next(node)
                node.set_next(low)
                work += 2

        self._length += 1
        work += 1

        return work
    
    def dequeue(self): # removes and returns the data of the node at the top of the Priority Queue Node
        work = 0
        check, w = self.is_empty()
        work += w
        if check == True:
            return None, work
        else:
            f = self._front.get_data()
            self._front = self._front.get_next()
            self._length -= 1
            work += 3
            return f, work
            
    def __str__(self): # returns a string of the Priority Queue Node
        work = 0
        s = ""
        next = self._front
        work += 2
        while next != None:
            s += str(next.get_data()) + " "
            next = next.get_next()
            work += 2
        return s, work

    def is_empty(self): # returns True if empty, False if not
        work = 1
        return (self._front == None), work

    def size(self): #returns the length of the Priority Queue Node
        work = 1
        return (self._length), work

