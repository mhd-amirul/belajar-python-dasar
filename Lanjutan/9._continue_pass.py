# Break : Utk mengakhiri perulangan for
# continue : utk lngsng melanjutkan step berikutnya
# pass : utk perintah for kosong atau lewat aja

for i in range(1,10):

    if i == 5:
        print('==============>',i)
        break

    print('Nilai i adalah ',i)
else:
    ('END FOR')

print(50*'=')

for i in range(1,10):

    if i == 5:
        print('==============>',i)
        continue

    print('Nilai i adalah ',i)
else:
    ('END FOR')

print(50*'=')

for i in range(1,10):

    if i == 5:
        print('==============>',i)
        pass

    print('Nilai i adalah ',i)
else:
    ('END FOR')
    
print(50*'=')