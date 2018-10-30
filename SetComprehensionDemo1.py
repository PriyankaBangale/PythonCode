#Set Comprehension

airports = {'LAX','HNL','YYZ'}
hawaiiairports = {airport for airport in airports
                  if airport in ['HNL','ITO']}
print(hawaiiairports)
