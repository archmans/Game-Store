from .function import *

def login(user_arr): 
    os.system('cls')
    valid = False
    while not valid: #validasi username dan password
        username= str(input("Masukkan username: "))
        password= str(input("Masukkan password: "))
        for i in range (length(user_arr)): #cek username
            if username == (str(user_arr[i][1])) and password == (str(user_arr[i][3])): #cek password
                os.system('cls')
                print("Halo", (user_arr[i][2]) ,"! Selamat datang di BNMO.")
                x = i
                valid = True
                break
        else:
            os.system('cls')
            print("Password atau username salah atau tidak ditemukan.")

    Username = user_arr[x][1] 
    
    return Username      

