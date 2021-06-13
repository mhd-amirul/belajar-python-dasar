#Celcius ke ---------------
def cel_to_fah (C) :
    cel = ((9/5) * C) + 32
    return cel

def cel_to_re (C) :
    cel = (4/5) * C
    return cel

def cel_to_kel (C) :
    cel = C + 273
    return cel

#Fahrenheit ke ---------------
def fah_to_cel (F) :
    fah = (5/9) * (F-32)
    return fah

def fah_to_re (F) :
    fah = (4/9) * (F-32)
    return fah

def fah_to_kel (F) :
    fah = ((5/9) * (F-32)) + 273
    return fah

#Reamur ke ---------------
def re_to_cel (F) :
    re = (5/4) * R
    return re

def re_to_fah (F) :
    re = ((9/4) * R) + 32
    return re

def re_to_kel (F) :
    re = (5/4) * R + 273
    return re

#Kelvin ke ---------------
def kel_to_cel (F) :
    kel = K - 273
    return kel

def kel_to_fah (F) :
    kel = (9/5) * (K-273) + 32
    return kel

def kel_to_re (F) :
    kel = (4/5) * (K-273)
    return kel

print("===========================")
print("Pilih Konversi Suhu")
print("===========================")


print("1  - Celcius ke Fahrenheit \n2  - Celcius ke Reamur \n3  - Celcius ke Kelvin ")
print("===========================")
print("4  - Fahrenheit ke Celcius \n5  - Fahrenheit ke Reamur \n6  - Fahrenheit ke Kelvin ")
print("===========================")
print("7  - Reamur ke Celcius \n8  - Reamur ke Fahrenheit \n9  - Reamur ke Kelvin ")
print("===========================")
print("10 - Kelvin ke Celcius \n11 - Kelvin ke Fahrenheit \n12 - Kelvin ke Reamur ")
print("===========================")

User = float(input("Masukkan Nilai Suhu : "))

choose = input("Masukkan Pilihan Konversi : ")

C = User
F = User
K = User
R = User

if choose == '1' :
    print("Hasilnya : ",cel_to_fah(C))
elif choose == '2' :
    print("Hasilnya : ",cel_to_re(C))
elif choose == '3' :
    print("Hasilnya : ",cel_to_kel(C))
elif choose == '4' :
    print("Hasilnya : ",fah_to_cel(F))
elif choose == '5' :
    print("Hasilnya : ",fah_to_re(F))
elif choose == '6' :
    print("Hasilnya : ",fah_to_kel(F))
elif choose == '7' :
    print("Hasilnya : ",re_to_cel(R))
elif choose == '8' :
    print("Hasilnya : ",re_to_fah(R))
elif choose == '9' :
    print("Hasilnya : ",re_to_kel(R))
elif choose == '10' :
    print("Hasilnya : ",kel_to_cel(K))
elif choose == '11' :
    print("Hasilnya : ",kel_to_fah(K))
elif choose == '12' :
    print("Hasilnya : ",kel_to_re(K))
else :
    print("0")

