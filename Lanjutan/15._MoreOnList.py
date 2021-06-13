# metode memanipulasi List
print('===============================================================================')
data = ['Pocophone','Oppo','Xiaomi','Iphone','Samsung']
print(data)

print('===============================================================================')
# menambah List
data.append('HP')           # guna menambah data list di ujung kanan
print(data)

data.extend('LG')           # guna menambah data list perhuruf di ujung kanan
print(data)

data.insert(3,'HP')         # guna menambah data list dengan menentukan lokasi index
print(data)

print('===============================================================================')
# menghitung anggota list
jumlah = data.count('HP')   # guna menghitung jumlah data list dan bukan huruf 
print('Jumlah Smartphone bermerek HP adalah =',jumlah)

print('===============================================================================')
# menghapus list
data.remove('Iphone')       # guna menghapus data list yang pertama ditemukan
print(data)
data.reverse()              # guna membalik data list dari kanan ke kiri
print(data)

print('===============================================================================')
# mengcopy list
datacopy = data.copy()      # mengcopy data list agar tidak memakai referensi atau sumber yg sama
datacopy.insert(0,'HP')
print(data)
print(datacopy)
print('===============================================================================')