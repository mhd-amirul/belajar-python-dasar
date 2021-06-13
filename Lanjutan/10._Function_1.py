# Function

# mendefinisikan fungsi
def hewan(nama):
    print('Nama Hewan :',nama)

def harga():
    #global satuan
    satuan = 75000
    print('Harga Satuan : 75.000')

def hargatotal(Ekor):
    harga()
    satuan = 75000
    total = Ekor * satuan
    print('Harga',Ekor,'Ekor nya Adalah :',total)


# memanggil fungsi
print(70*'=')
hewan('Ayam')
hargatotal(4)

print(70*'=')
hewan('Bebek')
hargatotal(5)

print(70*'=')
hewan('Kelinci')
hargatotal(2)

print(70*'=')
hewan('Puyuh')
hargatotal(10)
print(70*'=')