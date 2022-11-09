from .function import *

def cariGame(user_id, role, game_arr, kepemilikan_arr):  #fungsi untuk mencari game
    os.system('cls')
    if role == "User":
      id_game = input("Masukkan ID Game: ")
      tahun_rilis = input("Masukkan Tahun Rilis Game: ")
      print("Daftar game pada inventory yang memenuhi kriteria:")
    
      num = 0 #untuk menghitung jumlah game yang ditemukan
      check = False #untuk mengecek apakah ada game yang ditemukan
    
      for i in range (length(kepemilikan_arr)): #cek apakah user memiliki game
          if (kepemilikan_arr[i][1] == user_id): 
              for j in range (length(game_arr)): #cek apakah game yang dimiliki user ada di game_arr
                  if (kepemilikan_arr[i][0] == game_arr[j][0]): #jika game yang dimiliki user ada di game_arr
                      if (id_game == "" and tahun_rilis == ""): 
                        num += 1
                        print(str(num) + ". " + game_arr[j][0] + " \t | " + game_arr[j][1] + " \t | " + game_arr[j][2] + " \t | " + game_arr[j][3] + " \t | " + game_arr[j][4] + " \t | " + game_arr[j][5])
                        check = True
                        break

                      elif (id_game == game_arr[j][0] and tahun_rilis == game_arr[j][3]): #jika id game dan tahun rilis diisi
                          num += 1
                          print(str(num) + ". " + game_arr[j][0] + " \t | " + game_arr[j][1] + " \t | " + game_arr[j][2] + " \t | " + game_arr[j][3] + " \t | " + game_arr[j][4] + " \t | " + game_arr[j][5])
                          check = True
                          break
            
                      elif (id_game == game_arr[j][0] and tahun_rilis == ""): #jika id game diisi
                          num += 1
                          print(str(num) + ". " + game_arr[j][0] + " \t | " + game_arr[j][1] + " \t | " + game_arr[j][2] + " \t | " + game_arr[j][3] + " \t | " + game_arr[j][4] + " \t | " + game_arr[j][5])
                          check = True

                      elif (id_game == "" and tahun_rilis == game_arr[j][3]): #untuk mencari game berdasarkan tahun rilis
                          num += 1
                          print(str(num) + ". " + game_arr[j][0] + " \t | " + game_arr[j][1] + " \t | " + game_arr[j][2] + " \t | " + game_arr[j][3] + " \t | " + game_arr[j][4] + " \t | " + game_arr[j][5]) 
                          check = True
    
                      elif ((id_game != game_arr[j][0] or tahun_rilis != game_arr[j][3]) and check == False): #jika tidak ada game yang ditemukan
                          print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
                          check = True
                          break

      if (check == False):
          print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else:
        print("Hanya bisa diakses user")

