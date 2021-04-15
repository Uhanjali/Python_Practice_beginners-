name = input("Please enter your name:")
age = int(input("Hi, {} please enter your age:".format(name)))
n = int(input("Please enter how many times you want to repeate the message:"))
now_year = int(input("Please enter current year:"))
year = (now_year + 100) - age
# for i in range(0,101):
#     sum=age+i
#     if(sum==100):
#         year=2021+i
#         break

print("This is the year {} you will turn to 100 years"'\n'.format(year) * n)
