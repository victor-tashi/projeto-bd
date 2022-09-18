n0 = int(input('digite um numero: '))
t0 = (n0 + n0 ** 2) / 2
n1 = n0
t1 = 0
while n1 >= 1:
    t1 = t1 + n1
    n1 -= 1
    print(t1)
    print('')
if t1 == t0:
    print('a formula funciona t0 = {} e t1 = {}'.format(t0, t1))
else:
    print('a formula não funciona t0 = {} e t1 = {}'.format(t0, t1))
