# manipulasi String 

# menyambung string (Concatenate)

Nama_awal = 'Uzumaki '
Nama_tengah = 'Reza '
Nama_akhir = 'Syeh'

Sambung = Nama_awal + Nama_tengah + Nama_akhir
print(Sambung)

print('======================================')

# Menghitung panjang string

hitung = len(Sambung)
print(hitung)

print('======================================')
# operator untuk string
# mengecek keberadaan char dlam string
# tanda + hanya digunakan utk menyambung string bukan boolean
d = 'R'
status = d in Sambung
print('Adakah huruf R : ' + str(status))

d = 'r'
status = d not in Sambung
print('Tidak ada huruf r : ',status)
print('======================================')

# mengulang string
print(5 * 'Python ')
print('Python ' * 5)
print('======================================')

# Indexing
# index minus diambil dari belakang 
# cara ambil index minus = [-4 -3 -2 -1 0 1 2 3 4] = positif dari [0:5] [5:10] | negatif dari [0:-5] [-5:-10]
# pengambilan index dengan loncatan/increment 2 angka cth [0:10:2] ujung nya atau 2 adlh banyaknya loncatan
print('dari index [10] :' + Sambung[10])
print('dari index [-9] :' + Sambung[-9])
print('dari index [8:12] :' + Sambung[8:12])
print('dari index [-4:-1] :' + Sambung[-4:-1])
print('dari index [2,4,,6,8,10,12] :' + Sambung[0:17:2])
print('======================================')

# item paling kecil 
print('Item terkecil dalam ASCII code adlh :' + '\'' + min(Sambung) + '\'')
print('Item terbesar dalam ASCII code adlh :' + '\'' + max(Sambung) + '\'')
print('======================================')

# mengecek nilai char ke ASCII code
ascii_code = ord("G")
print('ASCII code dari G : ',ascii_code)
print('======================================')

# Mengecek isi ASCII code 
data = 200
print('isi :',chr(data))
print('======================================')

# metode dalam string
# menhitung jmlah suatu char dlm string menggunakan metode (count)
x = Sambung.count('e')
print('Jumlah e pada '+  Sambung + ' = ' +str(x))
