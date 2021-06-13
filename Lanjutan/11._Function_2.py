# function 2

# fungsi dengan menggunakan argumen sederhana

def nama_siswa(nama):
    print('Nama Siswa :',nama)

print('=====Daftar Murid======')
nama_siswa('Budi')
print(70*'=')
# fungsi dengan menggunakan keyword argumen

def nama_guru(nama,mapel):
    print('Nama Guru :',nama)
    print('Mata Pelajaran :',mapel)
    print(23*'=')

print('======Daftar Guru======')
print(23*'=')
nama_guru('Senku','Kimia')
nama_guru(nama='Chrome',mapel='Fisika')     # tidak masalah terbalik
nama_guru('Olahraga','Kinru')       # fatal takut terbalik
print(70*'=')

# fungsi dengan menggunakan default Argumen

def pegawai_perpus(nama,jkel='Pria',shift='07.00 - 10.30'):
    print('Nama Pegawai :',nama)
    print('Jenis Kelamin :',jkel)
    print('Jam Kerja :',shift)
    print(38*'=')


print('=====Daftar Pegawai Perpustakaan======')
print(38*'=')
pegawai_perpus('Hyoga')
pegawai_perpus(nama='Kohaku',jkel='Wanita')
pegawai_perpus(nama='Tsukasa',shift='11.00 - 14.30')

# inputan User
inp = input('Masukkan Nama Pegawai :')
inp2 = input('Jenis Kelamin :')

print(38*'=')
pegawai_perpus(nama=inp,jkel=inp2)
print(70*'=')