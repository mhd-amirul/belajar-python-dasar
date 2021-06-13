## For Loop
print(80*'=')

#  List Sebagai Iterable
Laptop =['Asus','Lenovo','HP','Dell','Acer']

for x in Laptop:
    print(x)
    print(len(x))   # Metode menghitung panjang str

print(80*'=')

#  String Sebagai Iterable
a = 'Dubai'

for y in a:
    print(y)

print(80*'=')

#  for in for
Smartphone =['Pocophone','Oppo','Xiaomi','Iphone','Samsung']
Aplikasi = ['Whatsapp','Facebook','Instagram','Telegram','Line']

all_item = [Laptop,Smartphone,Aplikasi]

for i in all_item:
    print(i)
    for j in i:
        print(j)
print(80*'=')