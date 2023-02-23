with open('Cowboy.txt','w') as a:
    a.write("{0:25} {1}\n".format("Item","price($)") )
    list1=["Colt Peacemaker","Holster","Levi Strauss jeans","Saddle","Stetson"]
    list2=[12.20,2.00,1.35,40.00,10.00]
    for i in range(len(list1)):
        a.write("{0:25s}{1}\n".format(list1[i],list2[i]))
