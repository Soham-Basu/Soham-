x=int(input("Enter the year :"))
if(((x%4==0 ) and (x%100!=0)) or (x%400==0)):
    print("Entered year is a leap year")
else:
    print("Entered year is not a leap year")
