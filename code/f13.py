from .function import *

def riwayatBeli(user_id, role, riwayat_arr): #user = user id
    os.system('cls')
    if role == "User":
        cek = False #cek apakah user memiliki riwayat beli
        temp_riwayat_arr2 = [[]] #array untuk menampung riwayat beli yang dimiliki user
        for i in range (length(riwayat_arr)): #cek apakah user memiliki riwayat beli
            if (riwayat_arr[i][3] == user_id): #cek apakah user_id sama dengan user_id pada riwayat_arr
                temp_riwayat_arr1 = [[riwayat_arr[i][0], riwayat_arr[i][1], riwayat_arr[i][2], riwayat_arr[i][4]]] #buat array baru untuk riwayat beli yang dimiliki user
                temp_riwayat_arr2 += temp_riwayat_arr1 #tambahkan riwayat beli yang dimiliki user ke array temp_riwayat_arr2
                cek = True
              
        if cek: #jika user memiliki riwayat beli
            headers = ["ID Game", "Nama Game","Harga","Tahun Rilis"] #buat header tabel
            print(tabulate(temp_riwayat_arr2, headers=headers, tablefmt='pipe')) #print tabel

        else:#jika user tidak memiliki riwayat beli
            print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah \033[1mbuy_game untuk membeli")
    else:
        print("Hanya user yang dapat melihat riwayat pembelian")
