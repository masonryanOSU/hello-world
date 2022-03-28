#prompt for file dataname
filename = input("Enter the file name: ")

#opening file
file = open(filename)

#printing header of the output
print("{0:18s}".format("\nName"), "{0:11s}".format("Hours"), "{0:s}".format("Total Pay"))

#for each line in file
for line in file:
   #splits line into list
   line = line.split()
  
   #sets name as first value in list
   name = line[0]
  
   #sets hours as second value in list
   Hours = int(line[1])
  
   #sets wage as last value in the list
   wage = float(line[2])
  
   #calculating total pay
   totalPay = hours * wage
  
   #printing output
   print("{0:11s}".format(name), "{0:11d}".format(hours), "{0:15.2f}".format(totalPay))
