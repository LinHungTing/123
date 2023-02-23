def selection_sort(number):  #定義函數名字
    a=0 #給個初始直0
    while a<=len(number)-1:   #len(number)-1 這樣轉成index才會正確 不然會有list index out of range的問題發生
        k=a                   #a賦予給k
        for i in range(a+1,len(number)):   #目地就是跟第一個數比較(範圍從第二個數開始跑 跑到最後一個數)
            if int(number[k])>int(number[i]): #如果比較後大於原本的那個數就把i 賦予給k
                k=i                              #把i 賦予給k
                
        number[a],number[k]=number[k],number[a]     #最後比較出來最小的值跟unsorted第一個交換
        a+=1  #a加一再繼續跑回圈
    print(number) #輸出答案
number=input("Enter number:").split(" ")   #把使用者輸入的字串分割 ,字符串以列表形式呈現
selection_sort(number)   #呼叫函式
