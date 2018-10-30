#List Comprehension with Conditional

prices = [200,400,500]
fee = 30
min = 200

totals = [price - fee for price in prices if price > min]
print(totals)

for total in totals:
    print(total)
