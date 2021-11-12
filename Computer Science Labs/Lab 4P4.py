num1 = int(input("Enter a number 1-10 "))
if num1 >= 1 and num1 <= 10:
    print('Multiplication table for', num1)
    for x in range(1, 11):
        print(format(x, '>2'), '*', num1, '=', format(x*num1, '>3'))
else:
    print("Invalid Input")