def add_balance(name, amount):
    amounts[name] +=amount

amounts={'savings':2200, 'current':1100}
a1=[('savings',-200),('savings',220), ('current',100),('current',-110)]
for i in a1:
    add_balance(*i)

print(amounts)

a2=[{'name':'savings','amount':-200},{'name':'savings','amount':220}, {'name':'current','amount':100},{'name':'current','amount':-110}]
for t in a2:
    add_balance(**t)
print(amounts)
