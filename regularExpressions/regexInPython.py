import re

email='dakshdev@gmail.com'
expression='[a-z\.]+'
result=re.findall(expression,email)
name=result[0]
domain=result[1]
print(name)
print(domain)


