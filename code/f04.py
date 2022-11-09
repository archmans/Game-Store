from .function import *

def addgame(role, game_arr):
    os.system('cls')
    if role == "Admin":
        x = True
        while x:  #validasi input
          print("TAMBAH GAME")
          nama = input("Masukkan nama game: ")
          kategori = input("Masukkan kategori: ")
          tahun_rilis = input("Masukkan tahun rilis: ")
          harga = input("Masukkan harga: ")
          stok = input("Masukkan stok awal: ")
          

          new_game = ["Game"+str(int(length(game_arr))+1), nama, kategori, tahun_rilis, harga, stok] #buat array baru

    
          
          for i in range (6): #cek inputan
                  if new_game[i] == "":
                      print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
                      x = True
                      break
                  else:
                      x = False
                  
                    
      
                      
          if x == False: #jika input valid maka tambahkan game baru ke array game
            game_arr += [new_game]
            print("Game berhasil ditambahkan!")
          return game_arr
    else:
        print("Addgame hanya bisa diakses oleh admin")