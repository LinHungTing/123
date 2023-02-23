a=str(input("Enter a sentence: ").upper())
n={"O":a.count("O"),"L":a.count("L"),"E":a.count("E"),"I":a.count("I")}
i=0
while i<4:
    s=sorted(n.items(), key=lambda item:item[1],reverse=True)
    e=str(s[i]).replace("(","").replace(")","").replace("'","").split(",")
    print(e[0],":",e[1])
    i+=1 