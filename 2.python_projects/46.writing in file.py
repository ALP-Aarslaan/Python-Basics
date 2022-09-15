file = open("student.txt", "a")
"""
here "a" means append. this append mode doesn't delete previously stored
information in that file . if we open file in write mode "w" then 
previously stored data will be deleted and new information will take its place    
"""

text = file.write("\n i am mohammad , iD: 19")
file.close()

file1 = open("student1.txt","w")

text1 = file1.write(" this is a file")

file1.close()

# creating html file

file2 = open("document.html","a")

text2 = file2.write("<h1>this is heading 1</h1>")

file2.close()

