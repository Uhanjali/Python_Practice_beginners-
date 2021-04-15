user_num = int(input("Please enter the number:"))
divisors = []
x = list(range(1, user_num + 1))
for num in x:
    if user_num % num == 0:
        divisors.append(num)
print(divisors)
