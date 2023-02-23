x=open("state.txt","r")
list1=[reversed(a.rstrip("\n").rsplit(",",1)) for a in x]
dict=dict(list1)
x.close()

    
while True:
    try:
        i = input("Enter a state capital to delete: ") 
        d=dict.pop(i)
        print("Capital deleted.")
        break
    except KeyError:
        print("Not a state capital.")
