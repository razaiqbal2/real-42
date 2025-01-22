def number___in___list(num):
    return num

n=int(input('Please enter a number : '))

num=[12,13,98,76,45,30,84]

if n==num:
    print('\n your guess is  correct ')
else:
    print(f'\nYour guess is not  correct')
    if n%2==0:
        print(f'\n Number is a even')
    else:
         print(f'\n Number is odd')


