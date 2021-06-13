# Bentuk tipe data dictionary ==> data = {key:value, key:value}  
# == menggunakan kurawal 
# == key sebagai kata kunci, dan value sebagai isi dari key 
# == EX :

data1 = {"ID":101,
        'Nama':'Ichika',
        'Pekerjaan':'Pelajar',
        'Status':'Jomblo'}

data2 = {"ID":102,
        'Nama':'Nino',
        'Pekerjaan':'Pelajar',
        'Status':'Jomblo'}

data3 = {"ID":103,
        'Nama':'Itsuki',
        'Pekerjaan':'Pelajar',
        'Status':'Jomblo'}

data4 = {"ID":104,
        'Nama':'Yotsuba',
        'Pekerjaan':'Pelajar',
        'Status':'Jomblo'}

data5 = {"ID":105,
        'Nama':'Miku',
        'Pekerjaan':'Pelajar',
        'Status':'Jomblo'}

# == Contoh pemanggilan tipe data dictionary
print('===============================================================================================')
print(data1)
print(data1['ID'])
print(data1['Nama'])
print(data1.keys())
print(data1.values())
print('===============================================================================================')
print(data1.items())
print('===============================================================================================')
print(data2.items())
print('===============================================================================================')
print(data3.items())
print('===============================================================================================')
print(data4.items())
print('===============================================================================================')
print(data5.items())
print('===============================================================================================')