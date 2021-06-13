def tambah (x,y):
    print(x,'+',y,'=',x+y)

def kurang (x,y):
    print(x,'-',y,'=',x-y)

def kali (x,y):
    print(x,'x',y,'=',x*y)

def bagi (x,y):
    print(x,'/',y,'=',x/y)

def main():
    print('Jika Teks Ini Muncul. Maka, Program Yang Dijalankan Adalah',__name__)

print(__name__)         # Untuk mencetak nama modul di program yg memanggil modul ini

if __name__ == '__main__':
    main()

