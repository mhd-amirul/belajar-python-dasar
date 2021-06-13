# kuadrat , kali, tambah, kurang, bagi

def Kuadrat(nilai):
    total = nilai ** 2
    print('Nilai Kuadrat dari',nilai,'adalah',total)
    return total

def tambah(nilai,nilai2):
    total = nilai + nilai2
    print(nilai,'+',nilai2,'=',total)
    return total

def kali(nilai,nilai2):
    total = nilai * nilai2
    print(nilai,'*',nilai2,'=',total)
    return total

def bagi(nilai,nilai2):
    total = nilai / nilai2
    print(nilai,'/',nilai2,'=',total)
    return total

def kurang(nilai,nilai2):
    total = nilai - nilai2
    print(nilai,'-',nilai2,'=',total)
    return total


Kuadrat(5)
tambah(50,50)
kali(50,50)
bagi(50,50)
kurang(50,50)