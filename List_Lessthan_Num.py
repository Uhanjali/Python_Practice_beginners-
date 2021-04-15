a = [1, 1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89]
empty = []
for number in a:
    if number < 5:
        empty.append(number)
print(empty)
print("-"*40)
user_num = int(input("Please enter a number:"))
for number in a:
    if number < user_num:
        empty.append(number)
print(empty)
