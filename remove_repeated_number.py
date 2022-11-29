list1 = []

number = int(input("how many number do you want to enter: "))

for i in range(number):
    list1.append(int(input("enter a number: ")))

print("first list is:  ", list1)
print("list whitout repeat is: ", set(list1))