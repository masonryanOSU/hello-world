filename = input("Enter the file name: ")

file = open(filename)

print("{0:18s}".format("\nName"), "{0:11s}".format("Hours"), "{0:s}".format("Total Pay"))

for line in file:
   line = line.split()
   name = line[0]
   hours = int(line[1])
   wage = float(line[2])
   totalPay = hours * wage

print("{0:11s}".format(name), "{0:11d}".format(hours), "{0:15.2f}".format(totalPay))
