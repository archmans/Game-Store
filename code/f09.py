from .function import *
from tabulate import tabulate

def lihatgame(user_id, role, game_arr, kepemilikan_arr): #fungsi untuk menampilkan game
    os.system('cls')
    if role == "User": 
        temp_game_arr1 = [] #array untuk menampung game yang dimiliki user
        temp_game_arr2 = [[]] #array untuk menampung game yang dimili user untuk output ke tabulate      
        cek = False
        for i in range (length(kepemilikan_arr)): #cek apakah user memiliki game
            if kepemilikan_arr[i][1] == user_id: 
                for j in range (length(game_arr)): #cek apakah game yang dimiliki user ada di game_arr
                    if kepemilikan_arr[i][0] == game_arr[j][0]:
                        
                        temp_game_arr1 = [game_arr[j][0], game_arr[j][1], game_arr[j][2], game_arr[j][3], game_arr[j][4]] #buat array baru untuk game yang dimiliki user
                        temp_game_arr2 += [temp_game_arr1] #tambahkan game yang dimiliki user ke array temp_game_arr2
                        cek = True
        if cek:
            headers = ["ID Game", "Nama Game","Kategori Game","Tahun Rilis","Harga"] #buat header tabel
            print(tabulate(temp_game_arr2, headers=headers, tablefmt='pipe')) #print tabel
        else:
            print("Anda tidak memiliki game apapun!")                                   
    else:
        print("Akses hanya dapat diakses oleh User")