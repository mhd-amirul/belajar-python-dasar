## Looping For, Else, Range, Break
#  Contoh
#  membuat virtual list dengan range

no = 30

for i in range(0,31,2):     # angka 5 adalah increment atau loncatan dari angka 0 sd 30 (0 5 10 dsb)
    print(i)
    if i is no:
        print('Angka Ditemukan => ',i)
        break   # break berguna untuk keluar dari looping for
else:   # else untuk kondisi false dari for
    print('Angka Tidak Ditemukan')
