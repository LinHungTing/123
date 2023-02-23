n=int(input("請輸入十進制的數:"))   #給使用者看
str_=""                            #設str_ 為一個空字串
if n == 0:                         #如果n等於0
    str_= str(n)+str_              #把n除以2的餘數接在既有str_字串的裡面
    print("二進制為:"+ str_)       #給使用者看二進制為最後輸出的字串
else:
    if n > 0:                        #如果n大於0
        while n != 0:                #當n不等於0
            str_ = str(n % 2)+str_   #把n除以2的餘數接在既有str_字串的裡面
            n = n//2                 #原始的n被除以2,商再賦予給新的n
        print("二進制為:"+ str_)     #給使用者看二進制為最後輸出的字串

        
#法2
integer = int(input())
remainder_list=list()
while integer!=0:
    remainder=integer%2
    remainder_list.append(remainder)
    integer//2
remainder_list.reverse()
for i in remainder_list:
    print(i,end="")