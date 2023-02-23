num=int(input("Enter a number:"))
list1=[]

for i in range(num):
    a=1+i*2
    list1.append(str(a))
    print(",".join(list1))