revenue=float(550000)
expenses=float(410000)
netincome=revenue-expenses
print(format(netincome,'.2f'))    #我覺得怪怪的

#正解
revenue=float(550000)
expenses=float(410000)
netincome=revenue-expenses
print("{0:.2f}".format(netincome))