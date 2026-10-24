s1=set([2,4,6,8,10,15])
s2=set([1,3,5,7,9,11,15])
s3=set([1,2,3,4,5,6,15])
s11=s1&s2
print(s11&s3)
print("--------------------------------")
s12=s1-(s2|s3)
s13=s2-(s3|s1)
s14=s3-(s1|s2)
print(s12|s13|s14)
print("--------------------------------")
s4=set([1,2,3,4])
s5=set([6,9,1,2,3,87,4,8])
print(s4<s5)
print("--------------------------------")
s7=set([56,98,25])
print(s1)
print(s7)
s99=s7&s1
if len(s99)==0:
    print("This is a disjoint set")
else:
    print("Not disjoint")
print("--------------------------------------------")
print(s1)
print(s3)
s34=s1|s3
s24=s1&s3
print("Symmetric difference ",s34-s24)
print("---------------------------------------------")
"""n=input("Enter the sentence: ")
l2=n.split()
print(set(l2))"""
print("-----------------------------------------------------------")
n=input("Enter the sentence: ")
count=0
v=set(('a','e','i','o','u','A','E','I','O','U'))
for i in n:
    if i in v:
        count+=1
print("There are ",count," vovels")
print("----------------------------------------------------------------------")
l4=list(())
n4=int(input("Enter the number of elements: "))
for i4 in range(n4):
    l4.append(input("Enter the name: "))
l4.sort()
s88=set(l4)
print(s88)
print("------------------------------------------------------------------------")
d1=set(())
for p in range(1,101):
    d1.add(p)
print(d1)
d2=set(())
p2=int(input("Enter the number of elements: "))
for q in range(p2):
    l7=int(input("Enter the number to be aaded to set: "))
    d2.add(l7)
p8=d1-d2
print(p8)