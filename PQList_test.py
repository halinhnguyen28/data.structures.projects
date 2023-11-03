import time
import random
import PQList
random.seed(2007)

#testing enqueue
enqueue_file = open("PQListData_enqueue.csv","w")
enqueue_file.write("operation, n, work\n")
enqueue_file.close()

enqueue_file = open("PQListData_enqueue.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    pql = PQList.PriorityQueueList()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        pql.enqueue(random.randint(11,1000))
    
    #now that the heap is big, set up the tests and check how long it takes to insert a new item of high priority
    size, w = pql.size()
    work = pql.enqueue(7)
    
    enqueue_file.write("enqueue, "+str(size)+", "+str(work)+"\n")
    print("enqueued 7 into a priority queue list with size "+str(size))
print("End priority queue list enqueue\n")
enqueue_file.close()

#testing dequeue
dequeue_file = open("PQListData_dequeue.csv","w")
dequeue_file.write("operation, n, work\n")
dequeue_file.close()

dequeue_file = open("PQListData_dequeue.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    pql = PQList.PriorityQueueList()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        pql.enqueue(random.randint(11,1000))
    
    #now that the heap is big, set up the tests and check how long it takes to insert a new item of high priority
    size, w = pql.size()
    temp, work = pql.dequeue()
    dequeue_file.write("dequeue, "+str(size)+", "+str(work)+"\n")
    print("dequeued the highest priority item from a priority queue list with size "+str(size))
print("End priority queue list dequeue\n")

dequeue_file.close()

#testing str function
str_file = open("PQListData_str.csv","w")
str_file.write("operation, n, work\n")
str_file.close()

str_file = open("PQListData_str.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    pql = PQList.PriorityQueueList()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        pql.enqueue(random.randint(11,1000))
    
    #now that the heap is big, set up the tests and check how long it takes to insert a new item of high priority
    size, w = pql.size()
    queue, work = pql.__str__()
    str_file.write("__str__, "+str(size)+", "+str(work)+"\n")
    print("return the string version of a priority queue list with size "+str(size))
print("End priority queue list str\n")

str_file.close()

#testing is_empty function
is_empty_file = open("PQListData_is_empty.csv","w")
is_empty_file.write("operation, n, work\n")
is_empty_file.close()

is_empty_file = open("PQListData_is_empty.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    pql = PQList.PriorityQueueList()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        pql.enqueue(random.randint(11,1000))
    
    #now that the heap is big, set up the tests and check how long it takes to insert a new item of high priority
    size, w = pql.size()
    check, work = pql.is_empty()
    is_empty_file.write("is_empty, "+str(size)+", "+str(work)+"\n")
    print("check if the queue is empty of a priority queue list with size "+str(size))
print("End priority queue list check is_empty\n")

is_empty_file.close()

#testing size function
size_file = open("PQListData_size.csv","w")
size_file.write("operation, n, work\n")
size_file.close()

size_file = open("PQListData_size.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    pql = PQList.PriorityQueueList()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        pql.enqueue(random.randint(11,1000))
    
    #now that the heap is big, set up the tests and check how long it takes to insert a new item of high priority
    size, work = pql.size()

    size_file.write("size, "+str(size)+", "+str(work)+"\n")
    print("return size of a priority queue list with size "+str(size))
print("End priority queue list check size\n")

size_file.close()

print("Done. check the files for your test results")