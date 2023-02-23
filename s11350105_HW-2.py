x=float(input('請輸入十進位數：'))#輸入十進位的實數

#將整數與小數分開
u=x-int(x)#小數部分
x=int(x)#整數部分
#先處理整數部分
t=0 #設定一個變數計算x能被2除幾次
y=[]#設定一個串列能存放於數
z=[]#設定一個串列放二進位小數值
y.append(x%2)#將x值除以2的餘數從串列y加入
if x != 0:  #如果這個數字根本只有小數，整數部分是0，要想辦法不要讓它進入迴圈無限打轉
    while (x != 1): 
        x=x//2
        t+=1
        y.append (x%2)
y.reverse()
#處理小數的部分
e=0 #計算有幾位小數
while(u!=0.00):
    e+=1
    u = u*2     
    if(u>=1):
        z.append (1)
        u-=1
    else:
        z.append(0)
#輸出結果
print( "二進位：",end="")
for i in range(t+1): #輸出串列y(從頭依序輸出到原本放入口的前一個位置）
     print(y[i],end="")
if e!= 0:           #有要輸出小數才輸出.
    print('.',end="")
for j in range(e):#輸出串列z（跳過原本放入的0，依序輸出）→你本來就沒有放0，不用跳過
    print(z[j],end="")  #輸出之間不需要空格