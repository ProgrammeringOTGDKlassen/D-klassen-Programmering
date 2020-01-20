from stack import Stack

s = Stack()

s.push(1)
s.push(5)

for i in range(10):
    s.push(i)

print(s.pop())
print(s.pop())
print(s.pop())
