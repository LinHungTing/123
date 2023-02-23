f = open('Cowboy.txt','r')
line2 = f.readlines()
f.close()

f = open('Cowboy2.txt','w')
for i in range(6):
    line = line2[i].split(" ")
    if line[0] == "Saddle":
        str1 = line[0] + " "
        f.write(str1)
        str2 = str('%.2f' % (float(line[-1].strip()) * 0.8))+"\n"
        f.write(str2)
    else:
        f.write(line2[i])
f.close()
