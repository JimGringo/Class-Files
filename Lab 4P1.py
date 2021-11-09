print("Part 1")
x = 10
while x <= 25:
    print(x)
    x += 1
x = 20
print('Part 2')
while x >= 0:
    print(x, end= ' ')
    x -= 1
print('Part 3')
x = 0
while x <= 10:
    print(format(x, ">4"))
    x += .5
print('Part 4')
x = 1792
while x <= 2020:
    print(x)
    x += 4
x = int(input("Any Number "))
y = int(input('The exponent '))
n = 1
z = x
while n < y:
    z = x * z
    n += 1
print(z)