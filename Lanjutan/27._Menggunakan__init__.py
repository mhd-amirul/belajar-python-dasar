# ==== Class 3


# == Class
# class wajib di atas karena bhs python interpreted atau baris perbaris
class mahasiswa():

    # menggunakan __init__ untuk lebih menyederhanakan program 
    # __init__ metode yg akan di gunakan ketika suatu variabel di inisialisasikan ke dalam class
    def __init__(self, inp_nama, inp_nim, inp_status):
        self.nama = inp_nama
        self.nim = inp_nim
        self.status = inp_status

    # metode (self berguna utk mengindentifikasi pemilik nya dan nama_hmj adalah tambahan atribut)
    def hmj(self, nama_hmj):
        print(self.nama,'bergabung di Himpunan Jurusan',nama_hmj)

    def ukm(self, nama_ukm):
        print(self.nama,'bergabung di Organisasi',nama_ukm)


# == Main
# perbedaan bisa di lihat pada program class 2 sebelumnya
print('====================================================')

# perbedaan pertama
mhs1 = mahasiswa('Diluc','2057301001','Belum Kawin')

print('Nama   :',mhs1.nama)
print('NIM    :',mhs1.nim)
print('Status :',mhs1.status)
mhs1.hmj('TIK')
mhs1.ukm('DPM')

print('====================================================')

# perbedaan kedua
mhs2 = mahasiswa('Jean','2057301002','Kawin')
print('Nama   :',mhs2.nama)
print('NIM    :',mhs2.nim)
print('Status :',mhs2.status)
mhs2.hmj('Kimia')
mhs2.ukm('BEM')

print('====================================================')

# perbedaan ketiga
mhs3 = mahasiswa('Ganyu','2057301001','Belum Kawin')
print('Nama   :',mhs3.nama)
print('NIM    :',mhs3.nim)
print('Status :',mhs3.status)
mhs3.hmj('Tata Niaga')
mhs3.ukm('ICLOP')

print('====================================================')