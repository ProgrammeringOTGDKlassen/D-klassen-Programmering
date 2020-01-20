from que import Queue

q = Queue()

q.enqueue(1)
print(q.l)
print(q.h)
q.enqueue(5)
print(q.l)
print(q.h)
q.dequeue()
print(q.l)
print(q.h)
q.enqueue(52)
print(q.l)
print(q.h)