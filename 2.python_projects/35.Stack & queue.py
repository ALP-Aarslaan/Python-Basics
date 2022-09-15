"""
stack is one kind of data structures, it has many operations such as push,pop.
push means storing data into stack and pop means deleting data from stack. stack is like storing
books in real life. it follows first in last out "FILO" formula.
if we use pop operation it will delete the 1st above element from stack
"""
books = []
books.append("learn c")
books.append("learn c++")
books.append("learn java")
books.append("learn Python")

print(books[1])
print(books)

books.pop()
print("now the top item is : ", books[-1])
print(books)

books.pop()
print("now the top item is : ", books[-1])
print(books)

books.pop(0)
print(books)
books.pop()

if not books:
    print("NO books left")

# queue :
"""
queue is like serial row of people waiting for movie ticket.
it's working procedure is like first in first out "FIFO" 
"""
from collections import deque

bank = deque(["mohammad", "jonayed", "sarkar"])
print(bank)
bank.popleft()
print(bank)
bank.pop()
print(bank)

