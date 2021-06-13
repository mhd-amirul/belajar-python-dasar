### Operator dalam bentuk method
##  merubah case dari string
#   merubah data string ke upper atau lower case
data = "Aku aNaK InDoNeSiA"
print('Isi data : ' + data)
print(35*"=")

data_1 = data.upper()
print('Isi data upper : ' + data_1)
print(35*"=")

data_2 = data.lower()
print('Isi data lower : ' + data_2)
print(35*"=")

##  pengecekan menggunakan isx method
#   contoh lower case
data_3 = "aku anak indonesia"
cek = data_3.islower()
print(data_3)
print('apakah str di atas huruf kecil? : ' + str(cek))

#   contoh upper case
cek = data_3.isupper()
print('apakah str di atas huruf besar? : ' + str(cek))
print(35*"=")

'''
metode - metode pengecekan isx
isupper         ---> pengecekan huruf besar
islower         ---> pengecekan huruf keci
isalnum         ---> pengecekan huruf dan angka
isalpha         ---> pengecekan semua nya huruf
isascii         ---> pengecekan 
isdecimal       ---> pengecekan semua nya angka
isdigit         ---> pengecekan 
isidentifier    ---> pengecekan 
isnumeric       ---> pengecekan 
isprintable     ---> pengecekan 
isspace         ---> pengecekan Space, tab, newline \n
istitle         ---> pengecekan semua kata dimulai dengan huruf besar
'''

#   contoh title case
judul = "Sun Shine Becomes You"
print(judul)
cek = judul.istitle()
print('apakah str di atas judul? : ' + str(cek))
print(35*"=")

#   pengecekan komponen startswith(), endswith()
data_4 = "Kementrian Sosial"
cek = data_4.startswith("Kementrian")
print(data_4)
print('apakah str diatas diawali dengan Kementrian? :' + str(cek))

cek = data_4.endswith("Sosial")
print('apakah str diatas diakhiri dengan Sosial? :' + str(cek))
print(35*"=")

#   Penggabungan str --> split(), join()
data_5 = ['automatic','teller','machine']
smbg = ' '.join(data_5)
print(data_5)
print('After Join :' + str(smbg),'\n')

data_6 = 'kekkekkukakikakakukokkakukakukek'
print(data_6)
print('After Split : ',data_6.split('ku'))
print(35*"=")

#   alokasi karakter rjust(), ljust(), center()
print(10*"-" + 'Contoh' + '-'*10)

center = 'tengah'.center(30,'-') # tambah argumen untuk menukar space
print('\'',center,'\'')

right = 'Kanan'.rjust(30)
print('\'',right,'\'')

left = 'kiri'.ljust(30)
print('\'',left,'\'')
print(35*"=")

#   menghilangkan space ---> strip()
cth = left.strip(' ')
print('\'',cth,'\'')