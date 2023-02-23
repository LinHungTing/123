test1=int(input("Enter one of five grades:"))
test2=int(input("Enter one of five grades:"))
test3=int(input("Enter one of five grades:"))  
test4=int(input("Enter one of five grades:"))
test5=int(input("Enter one of five grades:"))

x=min(test1,test2,test3,test4,test5)

total = float(test1+test2+test3+test4+test5-x)

avg=total/3

print("Average grade:",str(avg))
