# myset = {1, 2, "sanjay", 5.66, "rahul", "ayush", "ramesh", "ankit", "rishikesh"}
# print(myset)
# print(type(myset))

# myset.add(60)
# print(myset)

# #discard function
# myset.discard(3)
# print(myset)

# #remove
# myset.remove(3)
# print(myset)

'''
    if value not present in the set and
        if we use discard --> no error
        if we use remvoe --> error
'''

# myset = {10, 20, 30, 40}
# yorset = {"prashant", "jha"}
# newset = myset.union(yorset)
# print(newset)
# # union() 

# #intersection - returns common elements in both the sets
# myset = {10, 20, 30, 40}
# yorset = {10, 20, 60, 30}

# print(myset.intersection(yorset))


# #difference() returns in first set but not in second
# myset = {10, 20, 30, 40}
# yorset = {10, 50, 60, 30}
# print(myset.difference(yorset))

#clear() - used to clear the data of set
#pop() - used to remove object
myset = {10, 20, 30, 40}
print(myset.pop())
print(myset.clear())