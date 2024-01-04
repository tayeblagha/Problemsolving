store=[
    ("shirt",25),
    ("pant",25),
    ("shoes",27)
]

to_dinar= lambda data: (data[0],data[1]*3.2)
store_dinar=list(map(to_dinar,store))
print(store_dinar)


adding= lambda x,y: x+y
print(adding(5,2))

number=[1,2,3,4,5,6,7,8,9]
odd_numbers= list(filter(lambda x: (x%2==0),number))
print(odd_numbers)





