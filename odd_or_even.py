num = int(input("Please enter the number:"))
check = int(input("Please enter the number to divide with num:"))
if num % 2 == 0:
    print("{} is even number :)".format(num))
else:
    print("{} is odd number :)".format(num))
print("-" * 40)
if num % 4 == 0:
    print("{} is a multiple of 4 :)".format(num))
else:
    print("{} is not a multiple of 4 :)".format(num))
print("-" * 40)
if num % check == 0:
    print("{} divides {} evenly :)".format(check, num))
else:
    print("{} will not divide {} evenly :)".format(check, num))
