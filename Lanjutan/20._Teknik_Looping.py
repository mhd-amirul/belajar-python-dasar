#  Teknik Looping

# == List data
Judul = ['Sword Art Online',
        'Haikyuu',
        'Masamune-kun Revenge',
        'Kekkaishi',
        'Barakamon']

Genre = ['RPG',
        'Sport',
        'Romance',
        'Fantasy',
        'Slice of Life']

# == Enumerate => berguna membuat penomoran berdasarkan index
for i,jdl in enumerate(Judul):
    print(i,':',jdl)
print('\n')
for i,Gen in enumerate(Genre):
    print(i,':',Gen)
print('==============================================================================================')

# == Zip => berguna untuk menggabung 2 list
for jdl,gen in zip(Judul,Genre):
    print('Film berjudul :',jdl,'bergenre',gen) 
print('==============================================================================================')

# == Set
Sport = {'Basket','Volyball','Football','Baseball','Football'}

for sp in sorted(Sport):            # sorted berguna utk mengurutkan
    print('Nama Olahraga :',sp)
print('==============================================================================================')

# == Dictionary
Judul2 = {'Sword Art Online' : 'RPG',
        'Haikyuu' : 'Sport',
        'Masamune-kun Revenge' : 'Romance',
        'Kekkaishi' : 'Fantasy',
        'Barakamon' : 'Slice of Life'}
n = 1
print('Keys :')
for i in Judul2.keys():
    print(n,':',i)
    n += 1
print('==============================================================================================')
n = 1
print('Values :')
for i in Judul2.values():
    print(n,':',i)
    n += 1
print('==============================================================================================')
n = 1
print('Items :')
for i in Judul2.items():
    print(n,':',i)
    n += 1
print('==============================================================================================')

for i in reversed(range(1,6,1)):        # reverse utk membalik
    print(i)