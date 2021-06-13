
def tambah (x,y):
    z = x+y
    print(x,'+',y,'=',z)
    return z

def Kurang (z,y):
    z = x-y
    print(x,'-',y,'=',z)
    return z

def Kali (z,y):
    z = x*y
    print(x,'*',y,'=',z)
    return z

def bagi (z,y):
    z = x/y
    print(x,'/',y,'=',z)
    return z

def kuadrat(x):
    z = x ** 2
    print('Nilai Kuadrat dari',x,'adalah',z)
    return z

print('=======================================')
print('|        Kalkulator Sederhana         |')
print('=======================================\n\n')
print('=======================================')
print('|=============Input Nilai=============|')
print('=======================================')
x = int(input("Masukkan Nilai Pertama = "))
y = int(input("Masukkan Nilai Kedua = "))

print('=======================================\n\n')
print('=======================================')
print ("|====Pilih menu Operasi Aritmatika===|")
print('=======================================')
print ("1 - Tambah ")
print ("2 - Kurang")
print ("3 - Kali")
print ("4 - Bagi")
print ("5 - Kuadrat")

choose = int(input("Pilihan = "))
print('=======================================\n\n')
print('=======================================')
print('|============== Hasil ================|')
print('=======================================')
if choose == 1 :
    tambah(x,y)
elif choose == 2 :
    Kurang(x,y)
elif choose == 3 :
    Kali(x,y)
elif choose == 4 :
    bagi(x,y)
elif choose == 5 :
    kuadrat(x)
else :
    print("0")

print('=======================================')