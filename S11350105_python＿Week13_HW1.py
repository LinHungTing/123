class Wages:
    def __init__(self,name,worked,wage ):
        self.name=name
        self.worked=worked
        self.wage=wage
    def Pay_For_Week(self):
        w=self.worked
        s=self.wage
        if w<40:
            wages=w*s
            print("Pay for {0}: ${1:.2f} ".format(self.name,wages))
        elif w>=40:
            wages = (w * s)+(w-40) *( s/2)
            print("Pay for {0}: ${1:.2f} ".format(self.name,wages))

n=input("Enter person's name:")
hours=eval(input("Enter number of hours worked:"))
salary=eval(input("Enter hourly wage:"))
a=Wages(n,hours,salary)
a.Pay_For_Week()
