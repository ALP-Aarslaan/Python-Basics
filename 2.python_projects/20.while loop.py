i= int(input("starting point : "))
n=int(input("ending point : "))
# while i <= n:
#     print(i)
#     i = i + 1
# print("program end")

while i <= n:
    if i%2 == 0:
        print(i," is even")
    else:
        print(i,"is odd")
    i = i + 1