subject = ["math", "physics", "english", "chemistry", "Bengali", "islam"]
print(len(subject))
subject.append("history")  # it adds value after the last index
print(subject)

subject.insert(0, "CSE")  # it adds value at given index
print(subject)

subject.remove("history")
print(subject)

numbers = [9, 3, 10, 3, 5, 4, 2, 6, 7]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.pop()  # it pops the last value of the list
print(numbers)
numbers.clear()
print(numbers)

subject2 = subject.copy()
print(subject2)

odd = [2, 6, 8, 10, 4, 4, 4, ]
position = odd.index(4)
print(position)

count = odd.count(4)
print(count)
