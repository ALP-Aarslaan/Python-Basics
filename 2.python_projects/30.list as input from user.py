number = input("enter numbers :")
list = number.split()
sum = 0
for num in list:
    sum = sum + int(num)
print(sum)

numOfDigits = 0
numOfLetters = 0
numOfWords = 0
string = input("enter strings : ")
for x in string:
    x = x.lower()
    if "a" <= x <= 'z':
        numOfLetters = numOfLetters + 1
    # elif "A" <= x <= "Z":
    #     numOfLetters = numOfLetters + 1
    elif x == " ":
        numOfWords = numOfWords + 1
    elif '0' <= x <= '9':
        numOfDigits = numOfDigits + 1
print("number of letters in this string is : ", numOfLetters)
print("number of words in this string is : ", numOfWords + 1)
print("number of digits in this string is : ", numOfDigits)
