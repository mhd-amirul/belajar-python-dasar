Nama = 'alex'
pekerjaan = 'Pns'

def ubahnama(namabaru):
    global Nama
    Nama = namabaru
    print('Nama yg di ubah menjadi',Nama)

def ubahpekerjaan(kerjabaru):
    global pekerjaan
    pekerjaan = kerjabaru
    print('Pekerjaan yg di ubah menjadi',pekerjaan)

print('=======================================')
ubahnama('Rangga')
ubahpekerjaan('Polisi')
print('=======================================')
print('Nama      =',Nama,'\nPekerjaan =',pekerjaan)
print('=======================================')
