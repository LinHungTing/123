n=int(input("請輸入十進制的數:"))
s=str()

if n>0:                    #如果要4bit 那迴圈就不能n=0就結束
    for i in range(0,4):   #會跑四次
        s=str(n%2)+str(s)  #n除以2的餘數接在s前面
        n=int((n-n%2)/2)   #就是n/2
    print("二進制為:"+s)
else:                      #負數
    n=n+16
    for i in range (0,4):   #會跑四次
        s=str(n%2)+str(s)   #n除以2的餘數接在s前面
        n=int((n-n%2)/2)    #就是n/2
    print("二進制為:"+s)
  
    
