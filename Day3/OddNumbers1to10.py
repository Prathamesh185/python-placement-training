# for i in range(1,11):
#     if i%2 == 0:
#         print("even:",i)
#     else:
#         print("odd:",i)

even = 0
odd = 0
for i in range(1,11):
    if i%2 == 0:
        even += 1
    else:
        odd += 1

print("even:",even)
print("odd",odd)