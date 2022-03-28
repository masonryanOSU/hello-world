import math
tolerance=0.00001
estimate=1.0

def newton(num,estimate=1):

    difference = abs(num-estimate**2)
    if difference <= tolerance:
        return estimate
    else:
        return newton(num,(estimate+num/estimate)/2)

def main():

    while True:
        x=input("Enter a positive number or enter to quit: ")
        if x=="":
            break
        x = float(x)
        print("The program's estimate: ", newton(x))
        print("Python's estimate: ", math.sqrt(x))

if __name__=="__main__":
    main()
