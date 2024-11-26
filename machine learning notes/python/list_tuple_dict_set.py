# types of objects in python
# 1.immutable objects - whose value can not be changed once its created - int float string bool tuple
# 2.mutable objects - whose value can be changed once created - list set dictionary

# list

# list should be included in the square brackets
# list can have multiple data type value whereas set does not allow this
# allows duplicate values whereas set does not allow
my_list  = [1,2,3.0,"tarun",5]
print(type(my_list))
print(my_list[1])
my_list.append(True)
my_list.remove(1) 
del my_list[2]
print(my_list)                                                                          
my_list = []  #empty list 


# tuple
# enclosed with parenthesis
# allow multiple data type in a single tuple
# indexing same as list
tup1 = (1,2,3,4)
# convert list into tuple
list4 = [1,2,3]
print(tuple(list4))



# set 
# indexing is not support
#does not allows duplicate values if present automatically deleted repeated values
my_set = {1,2,3,4}                


# dictionary
#does not allow duplicate values
my_dict  = {'name':'Devid','age':19,'country':'india'}
print(my_dict.keys())
print(my_dict.values())
print(my_dict['age'])
print(my_dict)

