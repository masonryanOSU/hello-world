import math
def prediction():
    initial_organisms = int(input("Enter the initial number of organisms: "))

    growth = float(input("Enter the rate of growth(a real number greater than 1): "))

    while(growth<1):
        print("invalid growth rate.")

        growth = float(input("Enter the rate of growth(a real number greater than 1): "))

    growthRateHours = int(input("Enter the number of hours to reach the rate of growth: "))

    totalHours = int(input("Enter the total hours of growth: "))

    totalPop = initial_organisms
    hours = 1

    while (hours < totalHours):

        totalPop *= growth

        hours += growthRateHours

    print("The total population is " + str(int(totalPop)))

prediction()
