def add_1(name: str , holder: str, holders: list = []):
    holders.append(holder)
    return {'name':name,'holder':holder,'holders':holders}
a1=add_1('save','daksh')
a2=add_1('check','Divyansh')
print(a2)u