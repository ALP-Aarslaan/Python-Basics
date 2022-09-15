limit = int(input("enter last number : "))

sum = 0

for x in range(1, limit + 1, 1):
    print(x)
    sum = sum + x
print(sum)

sum = 0
print("\n\n")
for y in range(2,limit + 1, 2):
    print(y)
    sum = sum + y
print(sum)

print("\n\n")
sum = 0
for z in range(1, limit + 1, 2):
    print(z)
    sum = sum + z
print(sum)

print("\n\n")
sum=0
for p in range(1, limit + 1, 1):
    p = p * p
    print(p)
    sum = sum + p

print(sum)
