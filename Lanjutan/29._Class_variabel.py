class mahasiswa():

    elemen = 'Cryo'
    jumlah = 0       
    # menggunakan __init__ untuk lebih menyederhanakan program 
    # __init__ metode yg akan di gunakan ketika suatu variabel di inisialisasikan ke dalam class
    def __init__(self, inp_nama, inp_nim):
        self.nama = inp_nama            # Public Atribut
        self.nim = inp_nim              # Public Atribut
        mahasiswa.jumlah += 1
    

print('====================================================')

mhs1 = mahasiswa('Jean','2057301001')
mhs2 = mahasiswa('Ganyu','2057301002')

mhs1.elemen = 'Anemo'

# elemen adlh variable mahasiswa
print(mahasiswa.elemen)
# elemen adlh variable mahasiswa dan tertimpa ke instance atau object mhs1 karena baris 16
print(mhs1.elemen)
# elemen adlh variable mahasiswa
print(mhs2.elemen)

print('====================================================')

print(mahasiswa.__dict__)
print(mhs1.__dict__)
print(mhs2.__dict__)

print('====================================================')

# Cth menggunakan variable class
print('jumlah Mahasiswa :',mahasiswa.jumlah)

print('====================================================')