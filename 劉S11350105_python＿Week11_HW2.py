infile=open("StatesANC(2).txt","r")
a=str(infile.readlines()).strip()
while True:
    n=str(input("Enter a satste capital to delete: "))
    if n in a:
        print("Capital deleted.")
        a.replace(n,"")
        break
    elif n not in a:
        print("Not a state capital.")

