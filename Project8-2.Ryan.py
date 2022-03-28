import math
tolerance=0.00001
estimate=1.0
def newton(num,estimate):

   estimate=(estimate+num/estimate)/2
   difference = abs(num-estimate ** 2)
   if difference <= tolerance:
       return estimate
   else:
       return newton(num,estimate)

def main():

    while True:

        x = input("Enter a positive number or enter to quit: ")
        if x == "":
            break
        x = float(x)
        estimate = 1.0
        print("The program's estimate: ", newton(x,estimate))
        print("Python's estimate: ", math.sqrt(x))

if __name__ == "__main__":
    main()
