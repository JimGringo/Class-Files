grade = input("Enter Letter Grade ")
a = 0
b = 0
c = 0
d = 0
f = 0
unknown = 0
while True:
    if grade == 'Q' or grade == 'q':
        break
    elif grade == 'A' or grade == 'a':
        a += 1
    elif grade == 'B' or grade == 'b':
        b += 1
    elif grade == 'C' or grade == 'c':
        c += 1
    elif grade == 'D' or grade == 'd':
        d += 1
    elif grade == 'F' or grade == 'f':
        f += 1    
    else:
        unknown += 1
    grade = input("Enter Letter Grade ")
print("There are", a, "A(s)\nThere are", b, "B(s)\nThere are", c, "C(s)\nThere are", d, "D(s)\nThere are", f, "F(s)\nThere are", unknown, "unknown grades")