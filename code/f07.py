from .function import *
from tabulate import tabulate 

def list_game_toko(game_arr): 
    os.system('cls')#clear screen
    skema =input("Masukkan skema sorting: ") #input skema sorting
    temp_game_arr = game_arr #copy game_arr ke temp_game_arr

    if skema == "tahun+": #sorting tahun+
        for i in range (length(game_arr)):
            for j in range(i+1,length(game_arr)):
                if int(temp_game_arr[i][3]) >= int(temp_game_arr[j][3]): #jika tahun rilis lebih besar
                    temp = temp_game_arr[i] 
                    temp_game_arr[i] = temp_game_arr[j]  
                    temp_game_arr[j] = temp 
        headers = ["ID Game", "Nama Game","Kategori Game","Tahun Rilis","Harga","Stok"] #header tabel
        print(tabulate(temp_game_arr, headers=headers, tablefmt='pipe')) #print tabel
    elif skema == "tahun-": #jika skema sorting = tahun-
        for i in range (length(game_arr)): #sorting tahun-
            for j in range(i+1,length(game_arr)): #
                if int(temp_game_arr[i][3]) <= int(temp_game_arr[j][3]):
                    temp = temp_game_arr[i]
                    temp_game_arr[i] = temp_game_arr[j]
                    temp_game_arr[j] = temp
        headers = ["ID Game", "Nama Game","Kategori Game","Tahun Rilis","Harga","Stok"]
        print(tabulate(temp_game_arr, headers=headers, tablefmt='pipe'))
    elif skema == "harga+": #jika skema sorting = harga+
        for i in range (length(game_arr)):
            for j in range(i+1,length(game_arr)): #looping untuk sorting
                if int(temp_game_arr[i][4]) >= int(temp_game_arr[j][4]):
                    temp = temp_game_arr[i]
                    temp_game_arr[i] = temp_game_arr[j]
                    temp_game_arr[j] = temp
        headers = ["ID Game", "Nama Game","Kategori Game","Tahun Rilis","Harga","Stok"]
        print(tabulate(temp_game_arr, headers=headers, tablefmt='pipe'))
    elif skema == "harga-": #jika skema sorting = harga-
        for i in range (length(game_arr)): #sorting harga-
            for j in range(i+1,length(game_arr)): 
                if int(temp_game_arr[i][4]) <= int(temp_game_arr[j][4]):
                    temp = temp_game_arr[i]
                    temp_game_arr[i] = temp_game_arr[j]
                    temp_game_arr[j] = temp
        headers = ["ID Game", "Nama Game","Kategori Game","Tahun Rilis","Harga","Stok"]
        print(tabulate(temp_game_arr, headers=headers, tablefmt='pipe'))
    elif skema == "": #jika skema sorting = ""
        headers = ["ID Game", "Nama Game","Kategori Game","Tahun Rilis","Harga","Stok"]
        print(tabulate(temp_game_arr, headers=headers, tablefmt='pipe'))
    else:
        print("Skema sorting tidak valid!")
