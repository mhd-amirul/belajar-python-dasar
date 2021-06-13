# == inheritance atau turunan
'''artinya semua atribut yg dimiliki suatu object atau class 
    bisa di berikan kepada object atau class lainnya tanpa 
    DRY (Dont Repeat Yourself) mengulangnya '''

class ojek():
    id = 0
    def __init__(self, nama, jns_kendaraan, daerah):
        self.nama = nama
        self.jns_kendaraan = jns_kendaraan
        self.daerah = daerah
        ojek.id += 1


    def CekIdDriver(self):
        print('ID              :',self.id)
        print('Nama            :',self.nama)
        print('Jenis kendaraan :',self.jns_kendaraan)
        print('Daerah          :',self.daerah)
        print('\n=================================\n')

class grab(ojek):       # ini adalah inheritance atau turunan class ojek oleh class grab
    pass

class gojek(ojek):
    def CekIdDriver(self):
        print('Informassi lebih lanjut di www.gojek.com')           # ini menimpa atribut dari fungsi CekIdDriver dengan yg baru di class ini
        print('\n=================================\n')


# == Main

print('\n=============DRIVER==============\n')

Ojk1 = ojek('Ismail','Mobil','Aceh')
Ojk1.CekIdDriver()

Ojk2 = grab('Andi','Motor','Medan')
Ojk2.CekIdDriver()

Ojk3 = gojek('Tono','Mobil','Padang')
Ojk3.CekIdDriver()