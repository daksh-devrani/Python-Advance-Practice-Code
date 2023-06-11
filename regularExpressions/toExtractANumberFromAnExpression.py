import re

price='Price:$1,250.74'
expression='Price:\$([0-9,]*\.[0-9]*)'
result=re.search(expression,price)
print(result.group(0)) #gets the entire match
print(result.group(1)) #gets the first bracket
pwc=result.group(1).replace(',','')
price_number=float(pwc)
print(price_number)
