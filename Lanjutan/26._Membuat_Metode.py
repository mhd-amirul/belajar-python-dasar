# ==== Class 2


# == Class
# class wajib di atas karena bhs python interpreted atau baris perbaris
class mahasiswa():
    nama = 'nama'

    # metode (self berguna utk mengindentifikasi pemilik nya dan nama_hmj adalah tambahan atribut)
    def hmj(self, nama_hmj):
        print(self.nama,'bergabung di Himpunan Jurusan',nama_hmj)

    def ukm(self, nama_ukm):
        print(self.nama,'bergabung di Organisasi',nama_ukm)


# == Main
print('====================================================')

mhs1 = mahasiswa()
mhs1.nama = 'Diluc'
print('Nama :',mhs1.nama)
mhs1.hmj('TIK')
mhs1.ukm('DPM')

print('====================================================')

mhs2 = mahasiswa()
mhs2.nama = 'Jean'
print('Nama :',mhs2.nama)
mhs2.hmj('Kimia')
mhs2.ukm('BEM')

print('====================================================')

mhs3 = mahasiswa()
mhs3.nama = 'Ganyu'
print('Nama :',mhs3.nama)
mhs3.hmj('Tata Niaga')
mhs3.ukm('ICLOP')

print('====================================================')
