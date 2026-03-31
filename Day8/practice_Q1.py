mylist = [3, 3, 4, 2, 4, 4, 2, 4, 4]

n = len(mylist)

for i in mylist:
    if mylist.count(i) > n/2:
        print("Majority element=",i)
        break