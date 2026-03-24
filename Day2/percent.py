#calculate total, percent, and if percentage is greater than equal to 60 he or she is eligible for placement else not eligiblw

a = int(input('Enter first paper marks'))
b = int(input('Enter second paper marks'))
c = int(input('Enter third paper marks'))

total = a + b + c
percent = total/300 * 100

print('total =',total)
print('percent = ',percent)


if(percent >= 60):
    print('Eligible')
else:
    print('Not eligible')