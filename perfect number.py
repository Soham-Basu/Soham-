x=int(input("Enter the number:"))
s=0
for i in range(1,x):
    if(x%i ==0):
        s+=i
    i+=1
print(s)
if(x==s):
 print("It is a perfect number:")
else:
 print("It is not a perfect number:")
