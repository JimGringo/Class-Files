totalMoney = largeMoney = smallDay = bigDay = goalMet = 0
smallMoney = 10001
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for x in range(7):
    money = 0
    while money < 1 or money > 10000:
        money = int(input("Enter daily sales for " + days[x] + " "))
        if money >= 1 and money <=10000:
            totalMoney += money
            if largeMoney < money:
                bigDay = days[x]
                largeMoney = money
            if smallMoney > money:
                smallDay = days[x]
                smallMoney = money
            if money >= 5000:
                goalMet += 1
        
print("Total sales:                  ",format(totalMoney,">9"))
print("Highest sale day:             ",format(bigDay,">9"))
print("Highest sale day amount:      ",format(largeMoney,">9"))
print("Smallest sale day:            ",format(smallDay,">9"))
print("Smallest sale day amount:     ",format(smallMoney,">9"))
print("Average Weekly sales:         ",format(format(totalMoney/7,".2f"),">9"))
print("Number of days sales were met:",format(goalMet,">9"))