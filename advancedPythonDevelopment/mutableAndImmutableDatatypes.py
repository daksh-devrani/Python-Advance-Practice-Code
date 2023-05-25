'''every datatype that has the same id after a function is called on them is mutable datatype while
the others are immutable datatype'''
dict1={'name':'Daksh','age':17}
print(id(dict1))
dict1['age']=18
print(id(dict1))
list1=[1,2,3,4,5]
print(id(list1))
list1.append(6)
print(id(list1))
int1=5
print(id(int1))
int1=int1 + 5
print(id(int1))
str1='hi'
print(id(str1))
str1=str1 + 'hello'
print(id(str1))
tup1=(1,2,3,4)
print(id(tup1))
tup1= tup1+(5,)
print(id(tup1))
flo1=1.11
print(id(flo1))
flo1=flo1+ 0.1
print(id(flo1))
