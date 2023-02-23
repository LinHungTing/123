def myFunc(date):
    fs=open("./Calendar2015.txt")
    mydict=dict([it.rstrip().split(",") for it in fs.readlines()] )
    fs.close()
    if date in mydict.keys():
        return mydict[date]
    else:
        return ""

c=input("Enter a date in 2015:")
print("{0} falls on a {1}".format(c,myFunc(c)))
