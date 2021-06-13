# beberapa struktur Data yg ada di python : List, Tuple, Set, Dictionary 
# Tipe data Tuple sama seperti list tapi tidak bisa di manipulasi di ubah, hapus, maupun tambah
import sys          # disini digunakan untuk mengecek size data
import timeit       # disini digunakan untuk mengecek waktu data

data_list = [1,2,3,4,5,6,7,8,9,10]
data_tuple = (1,2,3,4,5,6,7,8,9,10)

# mengecek type dan apa saja yg bisa di lakukan list dan tuple
print(5*'==================')
print('Data :',data_list)
print(type(data_list))
print(5*'==================')
print(dir(data_list))
print(5*'==================')
# Menghitung ukuran atau size data list dan menghitung waktu data
time_list = timeit.timeit(stmt='[1,2,3,4,5,]',number=100)       # timeit.timeit untuk menghitung lama waktu data
size_list = sys.getsizeof(data_list)                            # getsizeof untuk menghitung ukuran data
print('Data :',data_list)
print('Ukuran data list :',size_list)
print(5*'==================')
print('Waktu data list :',time_list)

print(5*'==================','\n')
print(5*'==================')

print('Data :',data_tuple)
print(type(data_tuple))
print(5*'==================')
print(dir(data_tuple))
print(5*'==================')
# Menghitung ukuran atau size data dan tuple menghitung waktu data
time_tuple = timeit.timeit(stmt='(1,2,3,4,5,)',number=100)
size_tuple = sys.getsizeof(data_tuple)
print('Data :',data_tuple)
print('Ukuran data tuple :',size_tuple)
print(5*'==================')
print('Waktu data tuple :',time_tuple)
print(5*'==================')