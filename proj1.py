sun = mon = tues = wed = thurs = fri = sat = 0
dayMoney = [sun,mon,tues,wed,thurs,fri,sat]
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for x in range(7):
    while dayMoney[x] < 1 or dayMoney[x] > 10000:
        dayMoney[x] = int(input("Enter daily sales for " + days[x] + " "))
        
print(sum(dayMoney))
print(max(dayMoney))
    