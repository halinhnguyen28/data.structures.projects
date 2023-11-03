import PQNode
import time
import random

random.seed(2007)

#testing enqueue
enqueue_file_pqn = open("PQNodeData_enqueue.csv","w")
enqueue_file_pqn.write("operation, n, work\n")
enqueue_file_pqn.close()

enqueue_file_pqn = open("PQNodeData_enqueue.csv","a") #open in append mode so the data isn't overwritten
for i in range(20): #we're going to run 20 experiments
    
    #create a random list of a random size
    pqn = PQNode.PriorityQueueNode()
    for j in range(random.randint(100,10000)):
        #fill the list with random integers
        pqn.enqueue(random.randint(11,1000))
    
    size, w = pqn.size()
    work = pqn.enqueue(7)
    
    enqueue_file_pqn.write("enqueue, "+str(size)+", "+str(work)+"\n")
    print("enqueued 7 into a priority queue node with size "+str(size))
print("End priority queue node enqueue\n")
enqueue_file_pqn.close()

#testing dequeue
dequeue_file_pqn = open("PQNodeData_dequeue.csv","w")
dequeue_file_pqn.write("operation, n, work\n")
dequeue_file_pqn.close()

dequeue_file_pqn = open("PQNodeData_dequeue.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    pqn = PQNode.PriorityQueueNode()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        pqn.enqueue(random.randint(11,1000))

    size, w = pqn.size()
    temp, work = pqn.dequeue()
    dequeue_file_pqn.write("dequeue, "+str(size)+", "+str(work)+"\n")
    print("dequeued the highest priority item from a priority queue node with size "+str(size))
print("End priority queue node dequeue\n")

dequeue_file_pqn.close()

#testing str function
str_file_pqn = open("PQNodeData_str.csv","w")
str_file_pqn.write("operation, n, work\n")
str_file_pqn.close()

str_file_pqn = open("PQNodeData_str.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    pqn = PQNode.PriorityQueueNode()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        pqn.enqueue(random.randint(11,1000))

    size, w = pqn.size()
    queue, work = pqn.__str__()
    str_file_pqn.write("__str__, "+str(size)+", "+str(work)+"\n")
    print("return the string version of a priority queue node with size "+str(size))
print("End priority queue node __str__\n")

str_file_pqn.close()

#testing is_empty function
is_empty_file_pqn = open("PQNodeData_is_empty.csv","w")
is_empty_file_pqn.write("operation, n, work\n")
is_empty_file_pqn.close()

is_empty_file_pqn = open("PQNodeData_is_empty.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    pqn = PQNode.PriorityQueueNode()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        pqn.enqueue(random.randint(11,1000))

    size, w = pqn.size()
    check, work = pqn.is_empty()
    is_empty_file_pqn.write("is_empty, "+str(size)+", "+str(work)+"\n")
    print("check if the queue is empty of a priority queue list with size "+str(size))
print("End priority queue list check is_empty\n")

is_empty_file_pqn.close()

#testing size function
size_file_pqn = open("PQNodeData_size.csv","w")
size_file_pqn.write("operation, n, work\n")
size_file_pqn.close()

size_file_pqn = open("PQNodeData_size.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    pqn = PQNode.PriorityQueueNode()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        pqn.enqueue(random.randint(11,1000))

    size, work = pqn.size()

    size_file_pqn.write("size, "+str(size)+", "+str(work)+"\n")
    print("return size of a priority queue list with size "+str(size))
print("End priority queue list check size\n")

size_file_pqn.close()

print("Done. check the files for your test results")