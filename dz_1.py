n1 = int(input('Enter number a: '))
n2 = int(input('Enter number b: '))
n3 = int(input('Enter number c: '))
max_num = int

print('\t')

print('Choose the option:')
print ('1. Max. number.')
print ('2. Min. number.')
print ('3. AVG number.')
print('\t')

option = int(input('Enter your choice: '))

if option == 1:
    if n1 >= n2 and n1 >= n3:
        print('Max. number = ', n1)
    elif n2 >= n1 and n2 >= n3:
        print('Max. number = ', n2)
    else:
        print('Max. number = ', n3)
elif option == 2:
    if n1 <= n2 and n1 <= n3:
        print('Min. number = ', n1)
    elif n2 <= n1 and n2 <= n3:
        print('Min. number = ', n2)
    else:
        print('Min. number = ', n3)
elif option == 3:
        print(f' AVG. number = {(n1 + n2 + n3) / 3}')
