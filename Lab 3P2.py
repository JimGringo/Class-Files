elNum = int(input("Enter a Number 20-49 "))

if int(elNum) >= 20 and int(elNum) <= 49:
   elNum = list(str(elNum))
   if elNum[0] == '2':
      num1 = "twenty"
   elif elNum[0] == '3':
      num1 = "thirty"
   elif elNum[0] == '4':
      num1 = "forty"
   
   if elNum[1] == '0':
      num2 = ""
   elif elNum[1] == '1':
      num2 = "one"
   elif elNum[1] == '2':
      num2 = "two"
   elif elNum[1] == '3':
      num2 = "three"
   elif elNum[1] == '4':
      num2 = "four"
   elif elNum[1] == '5':
      num2 = "five"
   elif elNum[1] == '6':
      num2 = "six"
   elif elNum[1] == '7':
      num2 = "seven"
   elif elNum[1] == '8':
      num2 = "eight"
   elif elNum[1] == '9':
      num2 = "nine"   
   print(num1, num2)
else:
   print("Number Not Within Specified Range")
   
    