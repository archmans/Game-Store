from .function import *

def help (role): #fungsi help
  os.system('cls') #clear screen
  if role=="Admin" or role=="admin": #jika role admin
    print('============ HELP ============')
    print('1. register - Untuk melakukan registrasi user baru')    
    print('2. add game - Untuk menambah game yang dijual pada toko')    
    print('3. ubah game - Untuk mengubah game pada toko game  ')
    print('4. ubah stok -  Untuk mengubah stok sebuah game pada toko')     
    print('5. list game store - Untuk memberikan daftar game yang dimiliki')
    print('6. search game store - Untuk mencari game di toko')
    print('7. top up - Untuk menambahkan saldo kepada user')
    
  elif role=="User" or role=="user": #jika role user
    print('============ HELP ============')
    print('1. list game store - Untuk melihat list game yang dijual pada toko')
    print('2. buy game - Untuk membeli game')   
    print('3. lihat game - Untuk menampilkan daftar game yang dimiliki pengguna')
    print('4. cari game - Untuk mendapatkan informasi game')
    print('5. search game store - Untuk mencari game di toko')
    print('6. riwayat - Untuk melihat riwayat pembelian')