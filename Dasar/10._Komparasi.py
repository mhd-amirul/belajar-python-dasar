# komparasi adlah > < => =< == != 
# is membandingkan 2 object (tidak menggunakan == dan tidak bisa menbandingkan literal)


a = 7
print('a = ',a)
b = 10
print('b = ',b)

print('=================')

c = a > 5
print('a > 5 :',c)
c = b < 5
print('b < 5 :',c)

print('=================')

c = a >= 7
print('a => 7 :',c)
c = b <= 5
print('b =< 5 :',c)

print('=================')

c = a == 7
print('a == 7 :',c)
c = b == 5
print('b == 5 :',c)

print('=================')

c = a != 7
print('a != 7 :',c)
c = b != 5
print('b != 5 :',c)

print('=================')

c = a is b
print('a is b :',c)
c = a is not b
print('a is not b :',c)