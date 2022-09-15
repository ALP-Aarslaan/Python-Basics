studentFile = open("student.txt", "r")
# print(studentFile.readable())
# text = studentFile.read()
# print(text)
# print(studentFile.read())
# size = len(text)
# print(size)
# text = studentFile.readlines()[0]  # it takes only one line and print this
# print(text)
for line in studentFile:
    print(line)
studentFile.close()
# print(studentFile) we can't print file info
