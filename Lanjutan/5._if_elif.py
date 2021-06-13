# if elif dan else

Nilai = 70#int(input("Masukkan Nilai anda = "))

if Nilai > 89 and Nilai <= 100 :
    print("Nilai anda A")
if Nilai > 69 and Nilai <= 89 :
    print("Nilai anda B")
if Nilai > 49 and Nilai <= 69 :
    print("Nilai anda C")
if Nilai <= 49 :
    print("Nilai anda D")

print(50 * '=')

a = 50
b = 80

if a == 50:                                 #Equal Explisit
    print("nilai anda C")
    if b == 80:
        print("nilai anda B")

print(50 * '=')

if a is b:                                 #Equal
    print("nilai anda C")

if b is not a:                             #Not Equal 
    print("nilai anda bukan C")

print(50 * '=')


if 89 <= Nilai <= 100 :
    print("Nilai anda A")
elif 69 < Nilai <= 89 :
    print("Nilai anda B")
elif 49 < Nilai <= 69 :
    print("Nilai anda C")
elif Nilai <= 49 :
    print("Nilai anda D")
else:
    print("Error")

print(50 * '=')

value = ['Asus','HP','LG','Lenovo','Acer','Dell','Apple']
Belian1 = 'Lenovo'
Belian2 = 'Oppo'
if Belian1 in value:
    print('Harga Laptop',Belian1,': 10.000.000.00')

if not Belian2 in value:
    print('Maap bg salah server')

print(50 * '=')

char = 'A'
if char in Belian1:
    print('Ada Huruf',char,'di Lenovo')
else:
    print('Tidak Ada Huruf',char,'di Lenovo')

print(50 * '=')
