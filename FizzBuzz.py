#Sum of numbers which are divide 3 and 5
x=0
for i in range(1000,20001):
    if i % 3 == 0 and i % 5 == 0:
        x+=i
print(x)  

#FizzBuzz
number = input("Введите число:")
# check numeric
if number.isnumeric():
    # check FizzBuzz
    if int(number) % 3 == 0 and int(number) % 5 == 0:
        print('FizzBuzz')
    elif int(number) % 3 == 0:
        print('Fizz')
    elif int(number) % 5 == 0:
        print('Buzz')
    else: print('Opps')
else:  print('Вы ввели неверное число.')
