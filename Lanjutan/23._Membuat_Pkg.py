# memanggil module dalam folder yg berbeda
# cth :
'''
from Module import Rumus_math as math # as berguna membuat singkatan nama module
math.tambah(5,5)
math.kali(5,5)
math.kurang(5,5)
math.bagi(5,5)
print('===================')
'''
# bisa juga lngsng memanggil fungsi nya
'''
from Module import tambah
tambah(5,5)
print('===================')
'''
# atau menggunakan init
# pemanggilan module di lakukan dalam init 
# karna mengimport folder yg berisi file init yg akan di proses terlebih dahulu
'''
import Module
Module.tambah(5,5)
Module.kali(5,5)
Module.kurang(5,5)
Module.bagi(5,5)
print('===================')
'''

# mengimport pkg yg sudah tersedia di python
'''
import math
print(math.cos(22/7))
print(math.cos(3.14))
print('===================')
'''