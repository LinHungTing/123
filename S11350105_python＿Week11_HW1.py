x=input("Enter a sentence:")
#x="Always look on the bright side of life."
y=x.upper().replace(" ","")

dic={}
for i in y:
    keys=dic.keys()
    if i in keys:
        dic[i]+=1
    else:
        dic[i]=1
z=dict(sorted(dic.items(),key=lambda dic: dic[1],reverse=True))
c=list(z.keys())[:4]
for i in c[:4]:
    
    print(i,":",z.get(i))

