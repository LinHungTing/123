"""with open("Calendar2015.txt","r") as f:
    d={}
    dictword=f.read().split("\n")
    for i in range(len(dictword)-1):
        #print(dictword[i])
        a=(dictword[i].split(","))
        d[a[0]]=a[1]"""

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
