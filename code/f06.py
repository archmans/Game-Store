from .function import *

def ubahStok(role, game_arr):
    os.system('cls')
    if role == "Admin": #validasi role
        id_game = input("Masukkan ID game: ")

        for i in range (length(game_arr)): #cek ID game
            if (id_game == game_arr[i][0]):
                jumlah = int(input("Masukkan jumlah: "))
            
                if (jumlah > 0): #jika jumlah stok lebih dari 0
                    game_arr[i][5] = int(game_arr[i][5]) + jumlah #tambah stok
                    stok = "Stok game " + str(game_arr[i][1]) + " berhasil ditambahkan. Stok sekarang: " + str(int(game_arr[i][5]))
                    print(stok)
                elif (jumlah + int(game_arr[i][5]) < 0): #jika jumlah stok < stok yang ingin dikurangi
                    game_arr[i][5] = int(game_arr[i][5]) #stok tetap sama
                    stok = "Stok game " + str(game_arr[i][1]) + " gagal dikurangi karena stok kurang. Stok sekarang: " + str(int(game_arr[i][5]))
                    print(stok)
                elif(jumlah + int(game_arr[i][5]) >= 0): #jika jumlah stok >= stok yang ingin dikurangi
                    game_arr[i][5] = int(game_arr[i][5]) + jumlah #tambah stok
                    stok = "Stok game " + str(game_arr[i][1]) + " berhasil dikurangi. Stok sekarang: " + str(int(game_arr[i][5]))
                    print(stok)

                break

        else : #jika tidak ada game dengan ID tersebut
            print("Tidak ada game dengan ID tersebut!")
            
    else: #jika role bukan admin
        print("Akses hanya dapat diakses oleh Admin")
