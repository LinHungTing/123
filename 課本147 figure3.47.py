x=input("Enter a telephone number:")
list1=list(x)
for i in list1:
    if i == "-":
        list1.remove("-")
print("".join(list1))
#list1.remove("-")
#list1.remove("-")
#print("".join(list1))


#法2
x=input("Enter a telephone number:")
list1=list(x)
for i in list1:
    if "-" in i:
        list1.remove("-")
print("".join(list1))
#you can look book 139 ex7