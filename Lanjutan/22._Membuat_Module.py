# == cara - cara penggunaan import / membuat module
# == cara 1
'''
from Module import Rumus_math as matic
print('===Cara 1===')
matic.tambah(7,3)
matic.kali(7,3)
'''
print('===================')

'''
# == cara 2
from Module import Rumus_math as matic
print('===Cara 2===')
matic.tambah(5,7)
matic.kali(5,7)
'''
print('===================')

'''
# == cara 3
# == error karna module di folder yg berbeda
from Multi_fungsi import tambah, kali
from Multi_fungsi import *
print('===Cara 3===')
tambah(4,3)
kali(4,3)
'''
print('===================')

'''
# == cara 4
# == error karna module di folder yg berbeda
from Multi_fungsi import tambah as t, kali as k
print('===Cara 4===')
t(6,6)
k(6,6)
print('===================')
'''
