height = float(input("Enter the initial height of the ball: "))
bounciness = float(input("Enter the bounciness index of the ball: "))
bounces = int(input("Enter the amount of times the ball bounces: "))

distance = height

for i in range(bounces - 1):
    height *= bounciness
    distance += 2 * height

distance += height * bounciness

print("The total distance traveled is: " + str(distance) + " units.")
