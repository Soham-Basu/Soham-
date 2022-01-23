x=int(input("Enter the desired number:"))
for i in range(0,x+1):
    for j in range(0,i+1):
        print("*",end="")
        j+=1
    print(" ")
    i+=1
