"""
benefits of xargs is if we give input in a function its parameters no need to change
here number of inputs are no matter
"""


def studentInfo(*details):
    print(details)


studentInfo("mohammad", 19, 3.89, "CSE", "UAP")


def summation(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)


summation(1, 23)
summation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

"""
xxargs are same as xargs but difference here is we can use key value method here as well
as we give two ** astrics here
"""


def student(**details):
    print(details)


student(id="19101019", name="mohammad",cgpa=3.89 )


def student(**details):
    print(details["id"])


student(id="19101019", name="mohammad",cgpa=3.89 )


