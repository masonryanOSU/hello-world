import math

iterations = int(input("Enter the number of iterations: "));

Pi_div_four = 0;

iterationCounter = 1;

for i in range(1, iterations + 1):
    if(i % 2 != 0):
        Pi_div_four = Pi_div_four + 1 / iterationCounter;

    else:
        Pi_div_four = Pi_div_four - 1 / iterationCounter;

    iterationCounter = iterationCounter + 2;

    piValue = Pi_div_four * 4;

    print("The approximation of pi is ", piValue)
