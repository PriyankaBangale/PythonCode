#List Comprehension

prices = [200,400,500]
fee = 20
#totals = []
#for price in prices:
#    totals.append(price-fee)

#print(totals)

totals = [price - fee for price in prices]
print(totals)

for total in totals:
    print(total)
