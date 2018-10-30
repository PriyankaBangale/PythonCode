#Dictionary Comprehensions

airports = {'LAX':'Los Angeles','HNL':'Honolulu','YYZ':'Toronto'}
hawaiidict = {code: city for code,city in airports.items()
              if code in ['HNL','ITO']}
print(hawaiidict)
