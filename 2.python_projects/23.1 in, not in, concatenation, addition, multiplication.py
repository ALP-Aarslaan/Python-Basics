language = ["c", "c++", "java", "android", "python"]
print(language)
print("Python" in language)  # it will check whether certain string is in that list
# here python is in the list but still it will give false because python is case sensitive
# so we need to provide small 'p'

print("python" in language)
print("swift" not in language)

print(language * 3)  # it will print the given list values 3 times

print(language + ["swift", "javascript", 19])  # concatenation

