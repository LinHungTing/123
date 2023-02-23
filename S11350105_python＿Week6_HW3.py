def ceil(x):
    if int(x)!=x:
        return int(x+1)
    else:
        return x
def main():
    midterm = float(input("Enter grade on midterm score:"))
    final = float(input("Enter grade on final score:"))
    average = (2*final+midterm)/3
    result = ceil(average)
    print("Semester Grade:",end="")
    
    if result>=90:
        print("A")
    elif result>=80:
        print("B")
    elif result>=70:
        print("C")
    elif result>=60:
        print("D")
    else:
        print("F")
main()
