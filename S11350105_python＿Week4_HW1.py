coffee=212
room=70
k=0.079
m=0
while coffee>150:
    x=k*(coffee-70)
    m+=1
    coffee-=x
print("The coffee will cool to below  150 degree in {} minutes.".format(m))
