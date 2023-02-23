x=input("input a sentence:")   #讓使用者輸入一串句子
y="".join([i for i in x if not i.isdigit()])  #用for 迴圈把句子中非數字的部分加入到新的字串
if x.isalpha():  #假如輸入的都是英文直接print出來
    print(x)
elif x.isdigit():  #假如輸入都是數字直接print出來
    print(x)
else:           #假如輸入是英文和數字利用新字串y,print出來
    print(y)
    