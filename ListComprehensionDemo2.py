#Nested List Comprehension

prices = [200,400,500]
fees = [20,50]
#totals = []
#for price in prices:
#    for fee in fees:
#        totals.append(price-fee)

totals = [price - fee for fee in fees for price in prices]
print(totals)

for total in totals:
    print(total)
