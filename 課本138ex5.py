x=int(input("Enter a number from 1 through 20:"))
for i in range(x):
    for j in range(i+1):
        print("*",end="")
    print()

