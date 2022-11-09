from .function import *

def search_game_at_store(game_arr): #fungsi untuk mencari game di toko
    os.system('cls')
    idG = input("Masukkan ID Game: ")
    namaG = input("Masukkan Nama Game: ")
    hargaG =input("Masukkan Harga Game: ")
    kategoriG = input("Masukkan Kategori Game: ")
    tahunG = input("Masukkan Tahun Rilis Game: ")
    cek = False #untuk mengecek apakah ada game yang cocok
    temp_game_arr2 = [[]] #array kosong untuk menampung hasil pencarian
    for i in range (length(game_arr)):
        if game_arr[i][0] == idG or game_arr[i][1] == namaG or game_arr[i][2] == kategoriG or game_arr[i][3] == tahunG or game_arr[i][4] == hargaG :
            temp_game_arr1 = [[game_arr[i][0], game_arr[i][1], game_arr[i][2], game_arr[i][3], game_arr[i][4]]] #buat array baru untuk game yang cocok
            temp_game_arr2 += temp_game_arr1 #tambahkan game yang cocok ke array temp_game_arr2
            cek = True
    
    if cek == False:#jika tidak ada game yang cocok
        print("Daftar game pada toko yang memenuhi kriteria:")
        print("Tidak ada game pada toko yang memenuhi kriteria")
    
    elif cek == True: #jika ada game yang cocok
        print("Daftar game pada toko yang memenuhi kriteria:")
        headers = ["ID Game", "Nama Game","Kategori Game","Tahun Rilis","Harga"] #buat header tabel
        print(tabulate(temp_game_arr2, headers=headers, tablefmt='pipe')) #print tabel