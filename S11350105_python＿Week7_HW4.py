f = open('Cowboy.txt','w')
item = ["Item ","Colt Peacemaker ","Holster ","Levi Strauss jeans ","Saddle ","Stetson "]
price = ["Price\n","12.20\n","2.00\n","1.35\n","40.00\n","10.00\n"]
for i in range(6):
    f.write(item[i])
    f.write(price[i])
f.close()

f = open('Cowboy.txt','a')
f.write("Winchester Rifle,20.50\n")
f.close()
