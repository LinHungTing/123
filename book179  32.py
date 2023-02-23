def main():
    alpha = list()
    delete(alpha)
    output(alpha)

def list():
    infile = open("Months.txt" , "r")
    alpha = [line.rstrip() for line in infile]
    infile.close()
    return alpha

def delete(alpha):
    for i in alpha:
        if "r" not in i: #march
            del i
    return alpha

def output(alpha):
    alpha = ",".join(alpha)
    print(alpha)

main()