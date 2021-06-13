# ==== Class 4
# == Private atribut
# == cth :
# ini adlah private atribute akan error jika di jalankan
# Private Atribut menggunakan double underscore (__)


# == Class
# class wajib di atas karena bhs python interpreted atau baris perbaris
class mahasiswa():

    __ipk = 0        
    # menggunakan __init__ untuk lebih menyederhanakan program 
    # __init__ metode yg akan di gunakan ketika suatu variabel di inisialisasikan ke dalam class
    def __init__(self, inp_nama, inp_nim, inp_status):
        self.nama = inp_nama            # Public Atribut
        self.nim = inp_nim              # Public Atribut
        self.status = inp_status        # Public Atribut
    
    # cara mengakses private atribut =
    def ipk(self, inp_ipk):
        self.__ipk += inp_ipk
    
    def check(self):
        if self.__ipk > 1.5:
            print('Uas    : Lulus')
        else:
            print('Uas    : Tidak Lulus')
            


# == Main
# perbedaan bisa di lihat pada program class 2 sebelumnya
print('====================================================')

# perbedaan pertama
mhs1 = mahasiswa('Diluc','2057301001','Belum Kawin')

print('Nama   :',mhs1.nama)
print('NIM    :',mhs1.nim)
print('Status :',mhs1.status)
mhs1.ipk(1)
mhs1.check()

print('====================================================')

# perbedaan kedua
mhs2 = mahasiswa('Jean','2057301002','Kawin')
print('Nama   :',mhs2.nama)
print('NIM    :',mhs2.nim)
print('Status :',mhs2.status)
mhs2.ipk(2)
mhs2.check()

print('====================================================')

# perbedaan ketiga
mhs3 = mahasiswa('Ganyu','2057301001','Belum Kawin')
print('Nama   :',mhs3.nama)
print('NIM    :',mhs3.nim)
print('Status :',mhs3.status)
mhs3.ipk(4)
mhs3.check()

print('====================================================')