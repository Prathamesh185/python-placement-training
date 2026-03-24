#wap to accept single digit and check the entered number is positive negative or 0

a = int(input('Enter a single digit'))
if(a > 0):
    print('Digit is positive')
if(a == 0):
    print('Digit is zero')
if(a < 0):
    print('Digit is negative')