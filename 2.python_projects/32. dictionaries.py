"""
dictionaries works like for a given key we can store any value under it
example : suppose if we think a key as a string or a number where we will store my name under it
or my name under my roll number
"""
studentInfo = {
    19: "mohammad",
    20: "Jonayed",
    21: "sarkar",
    18: "arif",
}

print(studentInfo[19])
print(studentInfo.get(22))
print(studentInfo.get(34, "no such key available"))
print(studentInfo.get(20))
print(studentInfo)
# studentInfo[18] = "arif"
studentInfo[19] = "quraeshi"
print(studentInfo)
