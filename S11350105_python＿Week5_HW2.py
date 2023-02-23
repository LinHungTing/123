test1=int(input("Enter one of five grades:"))
test2=int(input("Enter one of five grades:"))
test3=int(input("Enter one of five grades:"))  
test4=int(input("Enter one of five grades:"))
test5=int(input("Enter one of five grades:"))

x=min(test1,test2,test3,test4,test5)

y=10000;
if test1 < y and test1 != x:
    y = test1
if test2 < y and test2 != x:
    y = test2
if test3 < y and test3 != x:
    y = test3
if test4 < y and test4 != x:
    y = test4
if test5 < y and test5 != x:
    y = test5

total = float(test1+test2+test3+test4+test5-x-y)

avg=total/3

print("Average grade:",str(avg))
    
   




