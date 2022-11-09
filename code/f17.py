from .function import *
from .f16 import *
def exit(user_arr, game_arr , riwayat_arr, kepemilikan_arr): #fungsi untuk keluar
    os.system('cls') #clear screen
    isSave = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (Y / N): ") #input apakah anda mau melakukan penyimpanan file yang sudah diubah

    while not (isSave == "y" or isSave == "Y" or isSave == "n" or isSave == "N"): #cek apakah input yang dimasukkan benar
      print("Input tidak valid. Input Y atau N dalam huruf kecil atau besar")
      isSave = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (Y / N):  ")

    if (isSave == "y" or isSave == "Y"): #jika input y
      save(user_arr, game_arr , riwayat_arr, kepemilikan_arr) #panggil fungsi save
      print("Data berhasil disimpan")
      print("Anda berhasil keluar dari BNMO")
    elif (isSave == "n" or isSave == "N"): #jika input n
      print("Anda berhasil keluar dari BNMO") #print anda berhasil keluar dari BNMO tanpa save

