friends={'name':"daksh",'age':17}
def fn(friend,name):#here friend=friends therefore for any mutable data the storage location is the same
    print(id(friend))
    friend[name]='Divyansh'
    friend['age']=24


print(id(friends))
print(id(friends['name']))#here the data in the dict is immutable and so it changes its memory location
fn(friends,'name')
print(id(friends))
print(id(friends['name']))
