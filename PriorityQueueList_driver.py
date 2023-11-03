import PriorityQueueList

pql = PriorityQueueList.PriorityQueueList()

#inserts items into the queue
pql.enqueue(3)
pql.enqueue(0)
pql.enqueue(10)
pql.enqueue(7)
pql.enqueue(15)
pql.enqueue(12)
pql.enqueue(9)
print(pql)

#deletes first items from the queue
pql.dequeue()
pql.dequeue()
print(pql)

#check other functions
pql.is_empty()
pql.size()
print(pql)