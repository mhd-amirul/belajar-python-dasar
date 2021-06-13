## operasi bitwise 

'''
Note = true = 1, false = 0

and = &
1. true and true   = True
2. true and false  = False
3. false and true  = False
4. false and false = False

or = |
1. true and true   = True
2. true and false  = True
3. false and true  = True
4. false and false = False

xor = ^
1. true and true   = False
2. true and false  = True
3. false and true  = True
4. false and false = False
'''


x = 5
y = 7

print('=============OR===============')
z = x | y
print('Nilai x :',x, 'binary :',format(x,'08b'))
print('Nilai y :',y, 'binary :',format(y,'08b'))
print('=============================(|)')
print('Nilai z :',z, 'binary :',format(z,'08b'))

print('\n=============AND==============')
z = x & y
print('Nilai x :',x, 'binary :',format(x,'08b'))
print('Nilai y :',y, 'binary :',format(y,'08b'))
print('=============================(&)')
print('Nilai z :',z, 'binary :',format(z,'08b'))

print('\n=============XOR==============')
z = x ^ y
print('Nilai x :',x, 'binary :',format(x,'08b'))
print('Nilai y :',y, 'binary :',format(y,'08b'))
print('=============================(^)')
print('Nilai z :',z, 'binary :',format(z,'08b'))

print('\n=============NOT==============')
z = ~x
print('Nilai x :',x, 'binary :',format(x,'08b'))
print('=============================(~)')
print('Nilai z :',z, 'binary :',format(z,'08b'))

## Shifting (Menggeser)

#  Shifting right
print('\n=============>>==============')
z = x >> 1
print('Nilai x :',x, 'binary :',format(x,'08b'))
print('=============================(>>)')
print('Nilai z :',z, 'binary :',format(z,'08b'))

#  Shifting Left
print('\n=============<<==============')
z = x << 1
print('Nilai x :',x, 'binary :',format(x,'08b'))
print('=============================(<<)')
print('Nilai z :',z, 'binary :',format(z,'08b'))