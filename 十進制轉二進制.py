n=int(input("請輸入十進制的數:"))
str_=""
if n == 0:
    str_= str(n)+str_
    print("二進制為:"+ str_) 
else:
    if n > 0:
        while n != 0:
            str_ = str(n % 2)+str_
            n = n//2
        print("二進制為:"+ str_)
    else:
        n = (n+1)*(-1)
        while n != 0:
            if (n % 2) == 0:
                str_ = "1"+str_
            else:
                str_ = "0"+str_
            n = n//2
        str_ = "1" +str_
        print("二進制為:"+str_)

        
