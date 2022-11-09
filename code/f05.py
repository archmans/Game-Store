from .function import *

def ubah_game(role, game_arr): 
    if role == "Admin": #validasi role
        os.system('cls')
        id_game = input("Masukkan ID game: ")
        nama = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        Tahun_rilis = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")


        for i in range (length(game_arr)): #cek ID game
            if (id_game == game_arr[i][0]):
            
                if (nama != ""): #jika nama game diisi
                    game_arr[i][1] = nama
                if (kategori != ""):#jika kategori diisi
                    game_arr[i][2] = kategori
                if(Tahun_rilis != ""): #jika tahun rilis diisi
                    game_arr[i][3] = Tahun_rilis
                if(harga != ""): #jika harga diisi
                    game_arr[i][4] = harga
                print(game_arr[i])
                break
        else:
            print("Tidak ada game dengan ID tersebut!")
                
    else: #jika role bukan admin
        print("Command hanya untuk admin!")

