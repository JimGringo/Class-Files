palindrome = input("Enter a palindrome")
x = 0
while palindrome != "":
    for s in palindrome:
        x += 1
        length = len(palindrome)
        if s != palindrome[-x]:
            isPalindrome = False
            break
        elif (x == (length // 2)) and (s == palindrome[-x]):
            isPalindrome = True
    print("String: ", palindrome)  
    print("Reverse String: ", palindrome[::-1]) 
    if isPalindrome == True:
        if len(palindrome) % 2 == 0:
            print("This is an even palindrome")
        else:
            print("This is an odd palindrome")
    else:
        print("This is not a palindrome")
    palindrome = input("Enter a palindrome")
    x = 0

    


