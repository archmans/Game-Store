from .function import *

def register(role, user_arr): # role = 'admin' or 'user'
    os.system('cls')
    if role == "Admin": #validasi role
        print("REGISTRASI")
        nama = input("Nama: ")
        username = input("Username: ")
        password = input("Password: ")
        

        new_user = ["BNMO"+str(length(user_arr)+1), username, nama, password, "User", "0"] #buat array baru
        
        for i in range (length(user_arr)): #cek username
                if username == user_arr[i][1]:
                    print("Username sudah ada")
                    break

        if validasi_char(username) == False: #validasi username
            os.system('cls')
            print("Username hanya dapat mengandung alfabet A-Za-z, underscore “_”, strip “-”, dan angka 0-9")
        else: #jika username valid
            os.system('cls')
            user_arr += [new_user] #tambahkan user baru ke array user
            print("Registrasi berhasil")
            return user_arr
    else:
        print("Register hanya bisa diakses oleh admin")
