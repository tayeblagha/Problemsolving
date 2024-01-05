from functools import reduce
##
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __repr__(self):
#         return f"Person('{self.name}', {self.age})"

# people = [Person("Alice", 26), Person("Bob", 25), Person("Charlie", 35)]
# youngest_person = min(people, key=lambda p: p.age)

# print(youngest_person)

def mymap(my_func,my_iter):
    result= []
    for item in my_iter:
        result.append(my_func(item))
    return result

nums= [3,4,6,1,2,7]
newarr= mymap(lambda x: x*5,nums)
newss = list(map(lambda x:x*2,nums))
newz = list(filter(lambda x : x>5,nums))
MultiplyAll = reduce(lambda x, y: x * y, nums, 1)
print(MultiplyAll)




