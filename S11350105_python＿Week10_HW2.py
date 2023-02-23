def func(year):
    dict={1:"Freshman",2:"Sophmore",3:"Junior"}
    return dict.get(year,"Senior")
x=int(input("請輸入數字:"))
print(func(x))
