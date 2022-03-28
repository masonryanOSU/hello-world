print("Input the lengths of the triangle sides: ")

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if ((x + y == z) or (y + z == x) or (x + z == y)):
    print("Right triangle")
else:
    print("Not right triangle")
