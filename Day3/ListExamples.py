#hetrogenous data = store different types of values are possible in the list

# mylist = ["prashant", "Ashish", "komal", "ankush", "Ashish", 77, "sandip",60.52, "prashant"]

# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

#list is mutable
# mylist[2] = "Akshay"
# print(mylist)

#membership operator (in)
# if "ankush" in mylist:
#     print("yes ankush is available")
# else:
#     print("not avialable")


#we represnt stack, queue, linkedlist in list datatype in python

# append method
# mylist.append('harsh')
# mylist.append('laxman')
# print(mylist)


#insert method
#if we have to add the value at specified index
# mylist.insert(1,"sanket")
# print(mylist)

#remove method
# mylist.remove("sandip")
# print(mylist)

#copy method
# newlist = mylist.copy()
# print(newlist)

# #multi-dimentional list
# mylist = [['prashant', 'jha'], ['85.56'],[440022,"yyy"]]
# print(mylist)
# print(mylist[0][0]) 
# print(mylist[0][1]) 
# print(mylist[1][0]) 
# print(mylist[2][0]) 
# print(mylist[2][1]) 

# list1 = ["prashant", "jha"]
# print(list1 * 2)
# list2 = [50, 25.50]
# print(list1 + list2)

# #del function
# list2 = [50, 25.50, 'prashant']
# del list2[2]
# print(list2)

# del list2
# print(list2)


# #clear function
# list2 = [50, 25.50, 'prashant']
# list2.clear()
# print(list2)


# #list typecast
# name = "prashant"
# print(name)
# myname = list(name)
# print(myname)

# #reverse example
# mylist = [40, 30, 20, 10]
# mylist.reverse()
# print(mylist)


# #sorting example
# mylist = [44, 22, 77, 0, 9, 88]
# mylist.sort()
# print(mylist)
# mylist.sort(reverse=True)
# print(mylist)

# #list aliasing
# mylist = [4, 22, 77, 0, 9, 88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

#for loop examples
# for i in range(5):
#     print(i)

# for i in range(1,11):
#     print(i)

for i in range(1,11):
    print(i*2,"\t", i*3, "\t",i*4,"\t", i*5,"\t", i*6,"\t", i*7, "\t",i*8, "\t",i*9, "\t", i* 10)

print("\n")
for i in range(1,11):
    print(i*11, "\t", i*12,"\t", i*13, "\t",i*14,"\t", i*15,"\t", i*16,"\t", i*17, "\t",i*18, "\t",i*19, "\t", i* 20)
