from class1 import student
x=str(input("Enter name:"))
y=int(input("Enter grade:"))
student1=student(x,y)
print(student1.name)
if y>8:
    print("You have passed!!!")
else:
    print("Sorry!You failed to clear!!!")
