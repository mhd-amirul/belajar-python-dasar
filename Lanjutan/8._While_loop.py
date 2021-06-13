start = True
i = 0

while start:
    # print('Reply from 192.168.56.1: bytes=32 time<1ms TTL=128')
    print('Nilai :',i)
    
    if i == 10:
        start = False
    
    i += 1       
else:
    print('End Loop')
    # print('Request time out')

print(50*'=')

# while menggunakan break, continue, dan pass
mulai = True

while mulai:
    print('Nilai :',i)
    
    if i == 0:
        mulai = False
        # continue
        # break
        # pass

    i -= 1
else:
    print('End Loop')

print(50*'=')

print(i)