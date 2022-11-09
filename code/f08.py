from .function import *

def buy_game(user_id, role,user_arr, game_arr, riwayat_arr, kepemilikan_arr): #fungsi untuk membeli game
    os.system('cls')
    if role == "User":
        x = 0
        cek = False

        idGame = input("Masukkan id game yang akan dibeli: ")
        for i in range (length(game_arr)): #cek ID game
            if idGame == game_arr[i][0]:
                x = i
                cek = True
                break
        
        for i in range (length(user_arr)): #cek ID user
            if user_id == user_arr[i][0]:
                saldo_user = int(user_arr[i][5]) #ambil saldo user
                break
        
        nama_game = game_arr[x][1] #ambil nama game
        harga_game = int(game_arr[x][4]) #ambil harga game
        stok_game = int(game_arr[x][5]) #ambil stok game
        harga_game_str = str(harga_game) #ubah harga game ke string

        if dimiliki(kepemilikan_arr,idGame,user_id): #cek apakah user sudah memiliki game tersebut
            print("Anda sudah memiliki game tersebut!")
        
        elif saldo_user >= harga_game and stok_game > 0 and cek: #jika saldo user lebih dari harga game dan stok game lebih dari 0
            saldo_user -= harga_game
            game_arr[x][5] = str(int(game_arr[x][5])-1)

            for j in range (length(user_arr)): #cek ID user
                if user_arr[j][0] == user_id :
                    user_arr[j][5] = str(saldo_user)
                    break
            
            temp_milik = [idGame, user_id] #buat array baru untuk kepemilikan
            kepemilikan_arr += [temp_milik] #tambahkan kepemilikan baru ke array kepemilikan

            tahun_beli = str(datetime.date.today().year) #ambil tahun sekarang
            temp_riwayat =[idGame,nama_game,harga_game_str,user_id,tahun_beli] #buat array baru untuk riwayat
            riwayat_arr += [temp_riwayat] #tambahkan riwayat baru ke array riwayat

            print("Game "+ str(game_arr[x][1])+" berhasil dibeli!") 

        elif cek == False: #jika ID game tidak ditemukan
            print("id game tidak ditemukan")
        
        elif stok_game == 0 and cek: #jika stok game habis
            print("Stok Game tersebut sedang habis!")
            
        elif saldo_user <= harga_game and stok_game > 0 and cek: #jika saldo user kurang dari harga game
            print("Saldo anda tidak cukup untuk membeli Game tersebut!")
    else: #jika role bukan user
        print("Akses hanya dapat diakses oleh User")



