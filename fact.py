import math
list1=[]

for i in range(1000):
    list2 = math.factorial(i)
    list1.append(list2)

number = int(input("enter a number? "))

if number in list1:
    print("the input number is factorial")
else:
    print("input number is not factorial")
