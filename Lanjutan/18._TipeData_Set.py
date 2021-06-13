# Set atau Himpunan = 
# 1. Tidak memiliki urutan 
# 2. jika memiliki 2 data yang sama akan di anggap satu


# Cara Ke - 1 membuat tipe data set =

Pkg_Makanan = {'Nasi goreng',
                'Ayam goreng',
                'Tempe goreng',
                'Tahu goreng',
                'Sambal goreng'}        # aturan 1

Pkg_Makanan.add('Kacang goreng')
Pkg_Makanan.add('Nasi goreng')          # aturan 2
# Untuk menyortir atau menyusun bisa menggunakan sorted
# sorted mengikuti huruf abjad tidak bisa utk angka
print(Pkg_Makanan)
print(sorted(Pkg_Makanan))
print('================================================================================================')
# Cara Ke - 2 membuat tipe data set =

Pkg_Minuman = set()

Pkg_Minuman.add('Jus')
Pkg_Minuman.add('Cola')
Pkg_Minuman.add('Teh')
Pkg_Minuman.add('Kopi')

print(Pkg_Makanan)

Ganjil = {1,3,5,7,9}
Genap  = {2,4,6,10}
Prima  = {1,2,3,4}

print(Ganjil.union(Genap))              # gabungan
print('================================================================================================')
print(Ganjil.intersection(Prima))       # Irisan
print(Genap.intersection(Prima))