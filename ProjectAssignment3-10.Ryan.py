hourWages = float(input("Enter the hourly wage: "))
regularHours = float(input("Enter the number of regular hours: "))
overtimeHours = float(input("Enter the overtime hours worked: "))
weeklyPay = (hourWages * regularHours) + (1.5 * hourWages * overtimeHours)
print("The weekly pay is", weeklyPay)
