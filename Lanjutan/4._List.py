## list

data = [1, 2, 4, 8, 16, 32, 64, 128]
data2 = [1000, 2000, 5000, 10000]

print('mengakses list')
Indata1 = data[5]       # Index dari 0
Indata2 = data[-4]

print(Indata1)
print(Indata2)
print('======================================================================')

print('memotong atau mengambil sebagian data list')
Indata3 = data[0:5]     # pengambilan kurang 1 dari angka yg ditentukan jika 0:5 maka 0:4
Indata4 = data[-5:]

print(Indata3)
print(Indata4)
print('======================================================================')

print('menambah list')
data3 = data + data2

print(data3)
print('======================================================================')

print('merubah isi list')
data3[7] = 1000
data3[-4] = 128

print(data3)
print('======================================================================')

print("mengcopy isi list dgn benar")
a = data 
#--->ini hanya mengakses isi list si data jika a di ubah data juga ikut berubah
#--->akan berakibat fatal jika tidak diperhatikan

b = data[:] # ini cara yg benar utk mengcopy isi list si data
b[5] = 9999

print(data)
print(b)
print('======================================================================')

print('merubah isi list dengan metode slicing')
data3[7:9] = [128, 1000]

print(data3)
print('======================================================================')

print('multidimensional list (list dlm list)')
data4 = [data,data2]

print(data4)
print('======================================================================')

print('mengakses multidimensional list') 
data5 = data4[1] [3]    # ingat index dari 0

print(data4)
print(data5)
print('======================================================================')

print('method unruk list')
data2.append(20000)     # menambah isi list

print(data2)
print('======================================================================')

print('fungsi pd list')
jmlh = len(data)

print(data)
print('Jumlah data dlm variabel data = ',jmlh)
print('======================================================================')