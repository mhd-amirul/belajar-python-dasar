# membuat anonymous function dengan lambda
# kalkulator sederhana dengan lambda

# lambda pengganti function def
tambah = lambda a,b: print(a,'+',b,'=',a+b)
kali = lambda a,b: print(a,'*',b,'=',a*b)
bagi = lambda a,b: print(a,'/',b,'=',a/b)
kurang = lambda a,b: print(a,'-',b,'=',a-b)
kuadrat = lambda a: print('Nilai Kuadrat dari',a,'adalah',a**2)

print('=======================================')
print('|        Kalkulator Sederhana         |')
print('=======================================\n\n')
print('=======================================')
print('|=============Input Nilai=============|')
print('=======================================')
a = int(input('Masukkan Nilai Pertama = '))
b = int(input('Masukkan Nilai Kedua = '))

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
    tambah(a,b)
elif choose == 2 :
    kurang(a,b)
elif choose == 3 :
    kali(a,b)
elif choose == 4 :
    bagi(a,b)
elif choose == 5 :
    kuadrat(a)
else :
    print("0")
print('=======================================')
