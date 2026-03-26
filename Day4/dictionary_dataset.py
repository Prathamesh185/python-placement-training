mydict = {
    101 : "prashant",
    "professional" : "developer", 
    "empid" : 1001
}

# print(mydict)
# print(type(mydict))

# mydict = {
#     101 : "prashant",
#     102 : "ashish",
#     "103" : "mohini",
#     "104" : "triveni", 
#     101 : "ashish", 
#     104 : "ashish"
# }
# print(mydict)
# prashant has been updated by ashish 

# a = mydict[102]
# print(a)

# #updating values of dict - old value update by new value
# mydict[102] = "peter"
# print(mydict)

# #only print key x=0,1
# for x in mydict:
#     print(x,mydict[x])

# # only print values x=0
#values()
# for x in mydict.values():
#     print(x)

# #Printing both keys and values using item()
# #items()
# for x,y in mydict.items():
#     print(x,y)

# #adding new key and value
# mydict["mobile_no"] = 8867664083
# print(mydict)


# #pop() method remove pair by specific key value
# mydict.pop(101)
# print(mydict)

newdict = mydict
print(newdict)