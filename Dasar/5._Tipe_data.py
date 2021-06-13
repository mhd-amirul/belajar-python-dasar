# Tipe data di python
# int, str, boolean, dan Float

#int
a = 5
print("Nilai :",a,"\n- Tipe data :",type(a))

print("============================")

#float
b = 10.5
print("Nilai :",b,"\n- Tipe data :",type(b))

print("============================")

#str
c = "amirul"
print("Nilai :",c,"\n- Tipe data :",type(c))

print("============================")

#boolean
#nilai bolean hanya 2 yaitu : true dan false
#jika bernilai 0 maka hasilnya akan false
#dan jika bernilai 1 atau lebih maka nilainya akan true

d = True
print("Nilai :",d,"\n- Tipe data :",type(d))

print("============================")

#data complex

Data_complex = complex(5,5)
print("Nilai :",Data_complex,"\n- Tipe data :",type(Data_complex))

print("============================")

#import data C

from ctypes import c_double

dari_c_double = c_double(5.5)
print("Nilai :",dari_c_double,"\n- Tipe data :",type(dari_c_double))
