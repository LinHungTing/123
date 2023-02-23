s=1000
list_1 = list()
list_2 = list()
for i in range(1,5):
    a = s * (1+0.05) ** i
    list_1.append(a)
    b = s+(s*0.05)*i
    list_2.append(b)
print("Simple Interest","Compound Interest")
for i in range(4):
    print(i+1,end="")
    print(" ${:,.2f}\t\t  ${:,.2f}".format(list_2[i],list_1[i]))


