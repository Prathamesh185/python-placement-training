#wap to accept days and check the working day or weekend

day = input('Enter a day: ')
if(day.lower() == 'saturday' or day.lower() == 'sunday'):
    print('Holiday')
else:
    print('Working day')