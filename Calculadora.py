op= input('Digite a função desejada ( soma, mult, div, sub): ')
n1= int(input('Digite um número: '))
n2= int(input('Digite outro número: '))

if op == 'soma':
    r = n1+n2
if op == 'mult':
    r = n1*n2
if op == 'div':
    r = n1/n2
if op == 'sub':
   r = n1-n2

print(r)


