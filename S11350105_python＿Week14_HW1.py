import random
def main():
    name=input("Enter name of human:")
    name_1=input("Enter name of computer:")
    score_me=0
    score_he=0
    for i in range(0,3):
        x=Human(name)
        me=x.choice()
        y=Computer(name_1)
        he=y.choice()
        if (me=='rock'
            and he=='scissors')or(me=='paper'
                                  and he=='rock')or(me=='scissors'
                                                    and he=='paper'):
            score_me+=1
            print(name,":",score_me," ",name_1,":",score_he)
        elif(me=='rock'
             and he=='paper')or(me=='paper'
                                and he=='scissors')or(me=='scissors'
                                                      and he=='rock'):
            score_he+=1
            print(name,":",score_me," ",name_1,":",score_he)
        elif(me=='rock'
             and he=='rock')or(me=='paper'
                               and he=='paper')or(me=='scissors'
                                                  and he=='scissors'):

            print(name,":",score_me," ",name_1,":",score_he)
    print()
    if score_me>score_he:
        print(name,"Wins")
    elif score_me<score_he:
        print(name_1,"Wins")
    else:
        print("tie")


class Contestant:
    def __init__(self,n=""):
        self.name=n

class Human(Contestant):
    def choice(self):
        print(self.name,end="")
        choose=input(", enter your choice:")
        return choose
class Computer(Contestant):
        
    def choice(self):
        three=["paper","scissors","rock"]
        a=random.choice(three)
        print(self.name,"chooses",a)
        return a

main()