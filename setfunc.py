"""
#fruits={"apple","orange","mango","grapes","watermelon"}
#fruits=set(["apple","orange","mango","grapes","watermelon"])
fruits=set()
n=int(input("ENTER THE RANGE :"))
for i in range(n):
    fruits.add(input("ENTER THE VALUES :"))
print(fruits)

"""
print("Create a set of five numbers and print all the elements.")
numbers=set()
n=int(input("ENTER THE RANGE :"))
for i in range(n):
    numbers.add(int(input("ENTER THE VALUES :")))
print("SET OF NUMBERS :",numbers)
m=int(input("ENTER THE LIMIT TO ADD :"))
for i in range(m):
    numbers.add(int(input("ENTER THE VALUES :")))
print("NEW NUMBERS :",numbers)
k=int(input("ENTER THE LIMIT TO REMOVE :"))
for i in range(k):
    numbers.remove(int(input("ENTER THE VALUES TO REMOVE :")))
print("NEW NUMBERS :",numbers)

print("Check whether a particular element exists in a set")
value=int(input("ENTER THE VALUE TO SEARCH :"))
if value in numbers:
    print("Element exists")
else:
    print("Element does not exist")

print("TOTAL NUMBER OF ELEMENTS IS :",len(numbers))

print("Print maximum and minimum values")
list1=list(numbers)
list1.sort()
print(list1)
print("MAXIMUM VALUE IS :", list1[len(list1) - 1])
print("MINIMUM VALUE IS :", list1[0])

print("Find the sum of all elements")
sum=0
for i in range(len(list1)):
    sum=sum+list1[i]
print("SUM OF ALL ELEMENTS :",sum)




