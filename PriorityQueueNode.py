import Node

class PriorityQueueNode:

    def __init__(self): # attributes and variables in the Priority Queue Node
        self._front = None
        self._rear  = None 
        self._length = 0 
    
    def enqueue(self, item):  # adds a node to the end of the Priority Queue Node
        node = Node.Node(item)
        if self.is_empty():
            self._front = node
            self._rear = node
        else:
            low = self._front
            high = None
            while low is not None and item > low.get_data():
                high = low
                low = low.get_next()

            if high is None:
                node.set_next(self._front)
                self._front = node

            elif low is None:
                high.set_next(node)
                self._rear = node

            else:
                high.set_next(node)
                node.set_next(low)

        self._length += 1
            
    def dequeue(self): # removes and returns the data of the node at the top of the Priority Queue Node
        if self.is_empty():
            return None 
        else:
            f = self._front.get_data()
            self._front = self._front.get_next()
            self._length -= 1
            return f
            
    def __str__(self): # returns a string of the Priority Queue Node
        s = ""
        next = self._front
        while next != None:
            s += str(next.get_data()) + " "
            next = next.get_next()
        return s

    def is_empty(self): # returns True if empty, False if not
        if self._front == None:
            return True 
        return False

    def size(self): #returns the length of the Priority Queue Node
        return (self._length)
