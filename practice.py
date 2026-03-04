n1 = int(input('Enter a number 1: '))
n2 = int(input('Enter a number 2: '))
n3 = int(input('Enter a number 3: '))

print(n1 > n2)
print(n1 < n2)
print(n1 >= n2)
print(n1 <= n2)
print('\t')

print(n1 == n2) #если н1 не равно н2 тогда выводит false
print(n1 != n2) #если н1 не равно н2 тогда выводи true
print('\t')

print (n1 == n2 or n2 == n3) #будет вывод true, если н1 равно одному из двуз условий
print(n1 == n3 and n1 != n2) #выводит true, если н1 равно одному и неравно другому одновременно
print('\t')

is_valid = True
print(is_valid)
print(not is_valid) #Это инверсия, когда получается изменить одно значение на другое, работает с true / false.

print('a' in 'hello wold') #так как буквы а - нет, вывод будет False.
print('\t')

if n1 <= n3 or n2 == n1:
    print('OK')
else:
    print ('Not ok!')

print('\t')

if n1 > n2:
    print('a')
elif n2 < n3:
    print('b')
else:
    print('error')

