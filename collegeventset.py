#Q) A college organizes a technical fest with 3 events coding,debugging and quiz.
# Each event has a set of registered students.Find the students who registered for all 3 events ?

coding=set()
n=int(input("ENTER THE NO OF STUDENT REGISTERED CODING :"))
for i in range(n):
    coding.add(input("ENTER THE NAMES :"))
print("SET OF NAMES :",coding)

debugging=set()
m=int(input("ENTER THE NO OF STUDENT REGISTERED DEBUGGING :"))
for i in range(m):
    debugging.add(input("ENTER THE NAMES :"))
print("SET OF NAMES :",debugging)

quiz=set()
k=int(input("ENTER THE NO OF STUDENT REGISTERED QUIZ :"))
for i in range(k):
    quiz.add(input("ENTER THE NAMES :"))
print("SET OF NAMES :",quiz)

allthree=coding&debugging&quiz
print("STUDENT WHO REGISTERED FOR THREE EVENTS :",allthree)