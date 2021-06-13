# == Input Output File
'''
    Cara membuat file :
    vairabel = open('nama_file','mode')

    mode ada 4 :
    1. w = write mode / menulis mode dan menghapus isi yg lama
    2. r = read only / hanya bisa membaca
    3. a = appending mode / menambah isi file di akhir
    4. r+ = read dan write mode
'''
# == membuat file
WriteData = open('file.txt','w')

WriteData.write('File yang di buat dengan menggunakan write')
WriteData.write('\nIni baris ke dua')
WriteData.write('\nIni baris ke tiga')
WriteData.write('\nIni baris ke empat')
WriteData.write('\nIni baris ke lima')

WriteData.close()


# == membaca file

ReadData = open('file.txt','r')

print('=================================================')
# print(ReadData.read())      # membaca semua
# print(ReadData.read(10))    # membaca dengan parameter jumlah karakter
print(ReadData.readline())    # membaca per line
print(ReadData.readline())    # akan melanjutkan line sebelumnya
print('=================================================')

ReadData.close()

# == menammbah isi file

TambahData = open('file.txt','a')

# berguna untuk menambah isi file di akhir 
TambahData.write('\nIni baris ke enam dibuat dengan mode append (a)')

TambahData.close()