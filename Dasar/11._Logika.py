## Logika adlah OR, AND, XOR, NOT

a = False
b = not a

print('========================NOT')
print('Nilai a :',a)
print('Nilai a di not kan :',b)


print('\n=========================OR')
# jika terdapat nilai true atau 1 maka hasil nya true, jika tidak maka false atau 0
a1 = True
a2 = True
b1 = False
b2 = False

c = a1 or a2
print('True OR True   :',c)
c = a1 or b1
print('True OR False  :',c)
c = b1 or a2
print('False OR True  :',c)
c = b1 or b2
print('False OR False :',c)


print('\n========================AND')
# jika terdapat nilai false atau 0 maka hasil nya false, jika tidak maka true atau 1
c = a1 and a2
print('True and True   :',c)
c = a1 and b1
print('True and False  :',c)
c = b1 and a2
print('False and True  :',c)
c = b1 and b2
print('False and False :',c)


print('\n========================XOR')
# jika terdapat nilai yang sama maka hasil nya false, jika tidak maka true 
c = a1 ^ a2
print('True XOR True   :',c)
c = a1 ^ b1
print('True XOR False  :',c)
c = b1 ^ a2
print('False XOR True  :',c)
c = b1 ^ b2
print('False XOR False :',c)