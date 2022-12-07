NENRI = 1.05
money = 10000
year = 0

while money <= 15000:
    money = money * NENRI
    year = year + 1

print(year,'年後に超える')