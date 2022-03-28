print("Input the lengths of the triangle sides: ")

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y and y == z:
    print("Equilateral triangle")
else:
    print("Not Equilateral triangle")
