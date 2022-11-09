from .function import *
import os

def save(user_arr, game_arr , riwayat_arr, kepemilikan_arr): #fungsi untuk menyimpan data ke file
    os.system('cls')
    file_exist = False 
    nama_folder = input("Masukkan nama folder penyimpanan: ") #input nama folder penyimpanan
    list_folder = os.listdir("./") #inisialisasi list_folder
    for files in list_folder: #cek apakah folder ada
        if files == nama_folder:
            file_exist = True
            print("Saving....")
            break

    if file_exist: #jika ada
        directory = nama_folder #inisialisasi directory
        usercsv = directory + "/user.csv" #inisialisasi usercsv
        f = open(usercsv,'w',encoding='utf-8') #buka file user.csv
        f.write(rewind_parser(user_arr,"user")) #write user.csv
        f.close() #tutup file user.csv

        gamecsv = directory + "/game.csv" #inisialisasi gamecsv
        f = open(gamecsv,'w',encoding='utf-8') #buka file game.csv
        f.write(rewind_parser(game_arr ,"game")) #write game.csv
        f.close() #tutup file game.csv

        riwayatcsv = directory + "/riwayat.csv" #inisialisasi riwayatcsv
        f = open(riwayatcsv,'w',encoding='utf-8') #buka file riwayat.csv
        f.write(rewind_parser(riwayat_arr,"riwayat")) #write riwayat.csv
        f.close() #tutup file riwayat.csv

        kepemilikancsv = directory + "/kepemilikan.csv" #inisialisasi kepemilikancsv
        f = open(kepemilikancsv,'w',encoding='utf-8') #buka file kepemilikan.csv
        f.write(rewind_parser(kepemilikan_arr,"kepemilikan")) #write kepemilikan.csv
        f.close() #tutup file kepemilikan.csv
        print("Save telah berhasil") #print save berhasil
    else: #jika tidak ada
        directory = nama_folder #inisialisasi directory
        parent_dir = os.path.dirname(__file__) #inisialisasi parent_dir
        path = os.path.join(parent_dir, "..",directory) #inisialisasi path
        os.mkdir(path) #buat folder
        usercsv = directory + "/user.csv" #inisialisasi usercsv
        f = open(usercsv,'w',encoding='utf-8') #buka file user.csv
        f.write(rewind_parser(user_arr,"user")) #write user.csv
        f.close() #tutup file user.csv

        gamecsv = directory + "/game.csv"   #inisialisasi gamecsv
        f = open(gamecsv,'w',encoding='utf-8') #buka file game.csv
        f.write(rewind_parser(game_arr ,"game")) #write game.csv
        f.close() #tutup file game.csv

        riwayatcsv = directory + "/riwayat.csv" #inisialisasi riwayatcsv
        f = open(riwayatcsv,'w',encoding='utf-8') #buka file riwayat.csv
        f.write(rewind_parser(riwayat_arr,"riwayat")) #write riwayat.csv
        f.close() #tutup file riwayat.csv

        kepemilikancsv = directory + "/kepemilikan.csv" #inisialisasi kepemilikancsv
        f = open(kepemilikancsv,'w',encoding='utf-8') #buka file kepemilikan.csv    
        f.write(rewind_parser(kepemilikan_arr,"kepemilikan")) #write kepemilikan.csv
        f.close() #tutup file kepemilikan.csv
        print("Save telah berhasil") #print save berhasil


    