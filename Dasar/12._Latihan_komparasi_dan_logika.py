'''
soal :
1. +++++++++10---------20++++++++++
2. ---------10++++++++++20---------
3. +++++0-----5+++++8-----11+++++
4. -----0+++++5-----8+++++11-----
'''

inp = int(input('Masukkan Nilai : '))

print('\n============================================')
print('+++++++++10---------20++++++++++')
print('============================================\n')
kuranglebih = inp < 10 or inp > 20
print('inputan < 10 OR > 20 :',kuranglebih)

print('\n============================================')
print('---------10++++++++++20---------')
print('============================================\n')
kuranglebih = inp > 10 and inp < 20
print('inputan > 10 AND < 20 :',kuranglebih)

print('\n============================================')
print('+++++0-----5+++++8-----11+++++')
print('============================================\n')
kuranglebih = inp < 0 or inp > 5 and inp < 8 or inp > 11
print('inputan < 0 OR > 5 AND < 8 OR > 11 :',kuranglebih)

print('\n============================================')
print('-----0+++++5-----8+++++11-----')
print('============================================\n')
kuranglebih = inp > 0 and inp < 5 or inp > 8 and inp < 11
print('inputan > 0 AND < 5 OR > 8 AND < 11 :',kuranglebih)
