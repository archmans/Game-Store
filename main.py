import code
import os
load = code.load() #load

if load[0] == True: #jika load[0] == True
    directory = load[1] #directory = load[1]
    parent_dir = os.path.dirname(__file__) 
    path = os.path.join(parent_dir, directory) #path untuk membuka folder

    user_arr = code.parser(path, "user.csv") #mengambil file user.csv yang berada di folder path
    game_arr = code.parser(path,"game.csv") #mengambil file game.csv yang berada di folder path
    riwayat_arr = code.parser(path,"riwayat.csv") #mengambil file riwayat.csv yang berada di folder path
    kepemilikan_arr = code.parser(path,"kepemilikan.csv") #mengambil file kepemilikan.csv yang berada di folder path

    username = code.login(user_arr) #login
    user_id = code.cek_id(username, user_arr) #cek id yang sedang login
    role = code.cek_role(username, user_arr) #cek role yang sedang login
    stat_game = True

    while stat_game: #perulangan untuk mengulang menu
        print("======================= B N M O =========================")
        print("apa yang ingin anda lakukan? \nketik 'help' jika anda bingung")
        command = input(">> ")
        if command == "help": 
            code.help(role) #help
        elif command == "register":#succes
            code.register(role, user_arr)
        elif command == "add game":#succes
            code.addgame(role, game_arr)
        elif command == "ubah game":#succes
            code.ubah_game(role, game_arr)
        elif command == "ubah stok":#succes
            code.ubahStok(role, game_arr)
        elif command == "list game store":#succes
            code.list_game_toko(game_arr)
        elif command == "search game store":#succes
            code.search_game_at_store(game_arr)
        elif command == "top up":#succes
            code.topup(role, user_arr)
        elif command == "buy game":#succes
            code.buy_game(user_id,role,user_arr,game_arr,riwayat_arr,kepemilikan_arr)
        elif command == "lihat game":#succes
            code.lihatgame(user_id, role, game_arr, kepemilikan_arr)
        elif command == "cari game":#succes
            code.cariGame(user_id, role, game_arr, kepemilikan_arr)
        elif command == "riwayat":#succes
            code.riwayatBeli(user_id, role, riwayat_arr)
        elif command == "exit":#SUCCES WItH SAVE
            code.exit(user_arr, game_arr, riwayat_arr, kepemilikan_arr)
            stat_game = False
        else:
            print("command tidak dikenali") #command tidak dikenali
else: #jika folder tidak ditemukan
    os.system('cls')
    print(load[1])


    
    
    





