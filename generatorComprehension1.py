#Generator Comprehension

prices = [200,400,500]
fee = 20
totals = (price - fee for price in prices)
print(totals)
print(totals.__next__())
print(totals.__next__())
print(totals.__next__())
print(totals.__next__())

#for total in totals:
#    print(total)
