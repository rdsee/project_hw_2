n1 = int(input('Enter meters: '))
print('\t')

print('Choose the option:')
print ('1. Meters to miles.')
print ('2. Meters to inches.')
print ('3. Meters to yards.')
print('\t')

option = int(input('Enter your choice: '))

if option == 1:
    miles = n1 * 0.0006213
    print(miles, 'miles')

elif option == 2:
    inches = n1 * 39.3701
    print(inches, 'inches')

elif option == 3:
    yards = n1 * 1.09361
    print(yards, 'yards')

else:
    print('Wrong option')


