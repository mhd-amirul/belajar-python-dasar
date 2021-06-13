### Format Str
#  cth generic

## f/format --> berguna untuk format str tanpa harus casting
# huruf
Nama = "amirul"
format_str = f"Halo {Nama}"
print(format_str)
print(35*"=")

# boolean
boolean = True
boolean2 = False
format_bool = f"isi data boolean = {boolean} {boolean2}"
print(format_bool)
print(35*"=")

# angka
angka = 2020.5
format_angka = f"Isi data angka = {angka}"
print(format_angka)
print(35*"=")

# bilangan bulat (d --> agar hanya akan menampilkan bilangan bulat saja)
# dengan format {variabel:d} 
bulat = 20
format_bulat = f"Isi data bulat = {bulat:d}"
print(format_bulat)
print(35*"=")

# otomatis koma di bilangan ribuan / jutaan atau lebih
# dengan format {variabel:,} 
jutaan = 2000000000
format_jutaan = f"Isi data jutaan = {jutaan:,}"
print(format_jutaan)
print(35*"=")

# bil desimal
# dengan format {variabel:.2f} f ---> tipe data float dan titik untuk menandakan angka setelah tanda titik
desimal = 2000.0528
format_desimal = f"Isi data desimal = {desimal:.2f}"
print(format_desimal)
print(35*"=")

# Leading zero
# dengan format {variabel:08.2f} 
# 0 pertama berguna untuk mengisi nilai kosong ke nol 
# 8 kedua  berguna untuk menggeser isi data dan memasukkan nilai kosong di depan nya
lzero = 2000.0528
format_lzero = f"Isi data lzero = {lzero:08.2f}"
print(format_lzero)
print(35*"=")

# menampilkan tanda minus atau plus
# dengan format {variabel:+d} 
minus = -5
plus = 10
format_minus = f"angka minus = {minus:+d}"
format_plus = f"angka plus = {plus:+d}"
print(format_minus)
print(format_plus)
print(35*"=")

# persentase %
# dengan format {variabel:.2%}
# .2 untuk mengambil 2 data setelah tanda titik
# % untuk mengubah data ke dalam bentuk persen 
persen = 0.050
format_persen = f"Isi data persen = {persen:.2%}"
print(format_persen)
print(35*"=")

# operasi aritmatika di dlam kurawal atau placeholder
harga = 100000
jumlah = 10
format_oper = f"Jumlah harga 10 ayam = {harga*jumlah:,}"
print(format_oper)
print(35*"=")

# format angka biner, octal, hexadcml
data = 15
format_biner = f"convert to biner = {bin(data)}"
format_octal = f"convert to octal = {oct(data)}"
format_hex = f"convert to hex = {hex(data)}"

print(format_biner)
print(format_octal)
print(format_hex)
print(35*"=")