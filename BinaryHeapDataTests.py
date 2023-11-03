import BinaryHeap
import time
import random

random.seed(2007)

#test insert
insert_file_bh = open("BinaryHeapData_insert.csv","w")
insert_file_bh.write("operation, n, work\n")
insert_file_bh.close()

insert_file_bh = open("BinaryHeapData_insert.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    bh = BinaryHeap.BinaryHeap()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        bh.insert(random.randint(11,1000))
    
    #now that the heap is big, set up the tests and check how long it takes to insert a new item of high priority
    size, w = bh.size()
    work = bh.insert(8)
    
    insert_file_bh.write("insert, "+str(size)+", "+str(work)+"\n")
    print("inserted 8 into a heap with size "+str(size))
print("End binary heap insert\n")

insert_file_bh.close()

#test perc_up
perc_up_file_bh = open("BinaryHeapData_perc_up.csv","w")
perc_up_file_bh.write("operation, n, work\n")
perc_up_file_bh.close()

perc_up_file_bh = open("BinaryHeapData_perc_up.csv","a")
for i in range(0,20):

    #create a random list of a random size
    bh = BinaryHeap.BinaryHeap()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        bh.insert(random.randint(11,1000))

    #now that the heap is big, set up the tests and check how long it takes to perc up 
    size, w = bh.size()
    work = bh.perc_up(size)
    
    perc_up_file_bh.write("perc_up, "+str(size)+", "+str(work)+"\n")
    print("Performed perc_up on a heap with size "+str(size))
print("End perc_up\n")

perc_up_file_bh.close()

#test get_root()
get_root_file_bh = open("BinaryHeapData_get_root.csv","w")
get_root_file_bh.write("operation, n, work\n")
get_root_file_bh.close()

get_root_file_bh = open("BinaryHeapData_get_root.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    bh = BinaryHeap.BinaryHeap()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        bh.insert(random.randint(11,1000))
    
    #now that the heap is big, set up the tests and check how long it takes to get the root of the heap
    size, w = bh.size()
    retval, work = bh.get_root()
    
    get_root_file_bh.write("get_root, "+str(size)+", "+str(work)+"\n")
    print("got root and balanced a heap with size "+str(size))
print("End binary heap get root\n")

get_root_file_bh.close()

#test perc_down
perc_down_file_bh = open("BinaryHeapData_perc_down.csv","w")
perc_down_file_bh.write("operation, n, work\n")
perc_down_file_bh.close()

perc_down_file_bh = open("BinaryHeapData_perc_down.csv","a")
for i in range(0,20):

    #create a random list of a random size
    bh = BinaryHeap.BinaryHeap()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        bh.insert(random.randint(11,1000))

    #now that the heap is big, set up the tests and check how long it takes to balance the heap using percDown
    size, w = bh.size()
    work = bh.percDown(8)

    perc_down_file_bh.write("percDown, "+str(size)+", "+str(work)+"\n")
    print("Performed percDown on a heap with size "+str(size))
print("End percDown\n")

perc_down_file_bh.close()

#test minChild
minChild_file_bh = open("BinaryHeapData_minChild.csv","w")
minChild_file_bh.write("operation, n, work\n")
minChild_file_bh.close()

minChild_file_bh = open("BinaryHeapData_minChild.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    bh = BinaryHeap.BinaryHeap()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        bh.insert(random.randint(11,1000))
    
    #now that the heap is big, set up the tests and check how long it takes to get the min child
    size, w = bh.size()
    i = random.randint(1, size)
    min_child, work = bh.minChild(i)
    
    minChild_file_bh.write("minChild, "+str(size)+", "+str(work)+"\n")
    print("got min child of node "+str(i)+" in a heap with size "+str(size))
print("End binary heap minChild\n")

minChild_file_bh.close()

#test __str__
str_file_bh = open("BinaryHeapData_str.csv","w")
str_file_bh.write("operation, n, work\n")
str_file_bh.close()

str_file_bh = open("BinaryHeapData_str.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    bh = BinaryHeap.BinaryHeap()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        bh.insert(random.randint(11,1000))
    
    #now that the heap is big, set up the tests and check how long it takes to return the string of the heap
    size, w = bh.size()
    heap, work = bh.__str__()
    
    str_file_bh.write("__str__, "+str(size)+", "+str(work)+"\n")
    print("get the string from a heap with size "+str(size))
print("End binary heap str\n")

str_file_bh.close()


#test size
size_file_bh = open("BinaryHeapData_size.csv","w")
size_file_bh.write("operation, n, work\n")
size_file_bh.close()

size_file_bh = open("BinaryHeapData_size.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    bh = BinaryHeap.BinaryHeap()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        bh.insert(random.randint(11,1000))
    
    #now that the heap is big, set up the tests and check how long it takes to get the size of the heap
    size, work = bh.size()
    
    size_file_bh.write("size, "+str(size)+", "+str(work)+"\n")
    print("get the size from a heap with size "+str(size))
print("End binary heap size\n")

size_file_bh.close()

#test is_empty
is_empty_file_bh = open("BinaryHeapData_is_empty.csv","w")
is_empty_file_bh.write("operation, n, work\n")
is_empty_file_bh.close()

is_empty_file_bh = open("BinaryHeapData_is_empty.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    bh = BinaryHeap.BinaryHeap()
    for i in range(random.randint(100,10000)):
        #fill the list with random integers
        bh.insert(random.randint(11,1000))
    
    #now that the heap is big, set up the tests and check how long it takes to check if the heap is empty or not
    size, w = bh.size()
    check, work = bh.is_empty()
    
    is_empty_file_bh.write("size, "+str(size)+", "+str(work)+"\n")
    print("check if the heap is empty from a heap with size "+str(size))
print("End binary heap is_empty\n")

is_empty_file_bh.close()

print("Done. check the file for your test results")

