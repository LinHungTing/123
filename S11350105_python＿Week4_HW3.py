a = input("Ente first name:")
b = input("Enter last name:")
c = int(input("Enter current salary:"))
if c<40000:
    c=c*1.05
else:
    c=(c+2000)+((c-40000)*0.02)

print("New salary for {0} {1}: ${2:,.2f}".format(a,b,c))
