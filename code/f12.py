from .function import *

def topup(role, user_arr):
    os.system('cls')
    if role == "Admin":
        username = input("Masukkan username yang ingin topup: ")
        saldo = int(input("Masukkan saldo yang ingin ditambahkan: "))

        for i in range (length(user_arr)): #looping untuk mencari username
            if username == user_arr[i][1]:
                if user_arr[i][4] == "User": #jika username yang dicari adalah user
                    if saldo >= 0: #jika saldo yang ditambahkan lebih besar dari 0
                        user_arr[i][5] = int(user_arr[i][5]) + saldo #mengupdate saldo
                        print("Saldo user " + user_arr[i][0] + " sekarang adalah " + str(user_arr[i][5]))
                        break
                    elif saldo < 0 and saldo + int(user_arr[i][5]) >= 0: #jika saldo yang ditambahkan kurang dari 0
                        user_arr[i][5] = int(user_arr[i][5]) + saldo #mengupdate saldo
                        print("Saldo user " + user_arr[i][0] + " sekarang adalah " + str(user_arr[i][5]))
                        break
                    else: #jika saldo yang ditambahkan kurang dari 0 dan saldo user + saldo yang ditambahkan kurang dari 0
                        print("Masukkan anda tidak valid!")
                        break
                else:
                    print("Username " + user_arr[i][1] + " bukan user!") #jika username yang dicari bukan user
                    break
        else:
            print("Username " + username + " tidak ditemukan.") #jika username yang dicari tidak ditemukan
            
    else:
        print("Command hanya untuk admin") #jika role bukan admin