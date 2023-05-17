low = input("Please enter the lower bound: ")
high = input("Please enter the upper bound: ")

print()
print("Celsius ", "Fahrenheit")
for i in range(int(low), int(high) + 1):
     print(i, " "*(7 - len(str(i))), i*9.0/5.0 + 32)
