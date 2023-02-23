import random
x=["H","T"]
p=""
s=0
z=0

for i in range(32):
    n=random.choice(x)
    p=p+n
print(p)

for i in p:
    if i=="H":
        s+=1
        z=0
    elif i=="T":
        z+=1
        s=0
        
    if(s>=5) or (z>=5):
        break
if(s>=5) or (z>=5):   #如果不加那個判斷的話沒有連續五個也會print，迴圈跳出有兩種狀況，一個是每一個元素都讀完，這代表並沒有連續五個一樣的這樣不能print
                      #另一種狀況是當s或是p等於5跳出迴圈，這種情形才要print
     print("There was a run of five consecutive same outcomes")
        
    