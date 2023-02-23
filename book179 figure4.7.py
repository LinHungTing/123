def input1():
    firstname = input("Enter first name:")
    lastname = input("Enter last name:")
    salary = eval(input("Enter current salary:"))
    Newsalsary(salary)
    output(firstname , lastname , Newsalsary(salary)) 
    
def Newsalsary(salary):
    if salary < 40000:
        Newsalsary = salary * 1.05
    else:
        Newsalsary = 40000 + (salary - 40000) * 1.02 + 2000 
    return Newsalsary

def output(firstname , lastname , Newsalsary):
    print("New salary for" , firstname , lastname , ":" , Newsalsary)
    
input1()