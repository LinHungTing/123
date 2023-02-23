
f = open('Cowboy.txt','w')
item = ["Item ","Colt Peacemaker ","Holster ","Levi Strauss jeans ","Saddle ","Stetson "]
price = ["Price\n","12.20\n","2.00\n","1.35\n","40.00\n","10.00\n"]
for i in range(6):
    f.write(item[i])
    f.write(price[i])
f.close()

f = open('Order.txt','w')
ordernumber = ["3\n","2\n","10\n","1\n","4\n",""]
for i in range(5):
    f.write(ordernumber[i])
    
f = open('Cowboy.txt','r')
line1 = f.readlines()
f.close()

f = open('Order.txt','r')
line2 = f.readlines()
f.close()

total = 0.00
for i in range(5):
    print(line2[i].strip(),end =' ')
    line = line1[i+1].split(" ")
    for j in range(len(line)-1):
        if j == (len(line)-2):
            print(line[j],end ='')
        else:
            print(line[j],end =' ')
    print(":",sep='',end =' ')
    num = float(line[-1].strip())*int(line2[i].strip())
    print("$",'%.2f' % num,sep='')
    total += num
print("Total: $",'%.2f' % total, sep='')
