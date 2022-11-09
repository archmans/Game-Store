import datetime
import os
from tabulate import tabulate

def length(x): #len primitif
    index = 0
    for i in x:
        index += 1
    return index

def parser(parent_dir, a): #csv to array
    b = 0
    
    if a == "user.csv":
      b = 6 
      path = parent_dir + "/user.csv" 
    elif a == "game.csv":
      b = 6
      path = parent_dir + "/game.csv"
    elif a == "riwayat.csv":
      b = 5
      path = parent_dir + "/riwayat.csv"
    elif a == "kepemilikan.csv":
      b = 2
      path = parent_dir + "/kepemilikan.csv"
    
    
    
  
    
    f = open(path,'r') #buka file
    data = f.read() #baca file
    f.close() #tutup file
    f = open(path,'r') #buka file
    baris = f.readlines() #baca file
    jmlhBaris = length(baris) #hitung jumlah baris
    f.close #tutup file
    data_arr = [x for x in data] #buat array dari data per huruf
    i = 0  #untuk indeks array huruf
    j = 0 #untuk indeks baris csv
    k = 0 #untuk indeks kolom csv
  
    arr = [["" for i in range(b)] for j in range(jmlhBaris)] #buat array kosong
    


    while j != jmlhBaris: #perulangan untuk mengisi array
        while data_arr[i] != "\n" : #perulangan untuk mengisi array
            if data_arr[i] != ";" : #jika data bukan ";"
                arr[j][k] += str(data_arr[i]) #tambahkan ke array
                i += 1 #tambahkan i
               
            else: #jika data = ";"
                k += 1 #tambahkan k
                i += 1 #tambahkan i
            if i == length(data_arr): #jika i sudah sama dengan panjang data
                break #keluar perulangan
        j += 1 #tambahkan j
        k = 0 #reset k
        i += 1 #tambahkan i
    return arr #kembalikan array

def rewind_parser(a,b): #array to csv
    c = 0 #untuk batas kolom array
  
    if b == "user":
      c = 6 
    elif b == "game":
      c = 6
    elif b == "riwayat":
      c = 5
    elif b == "kepemilikan":
      c = 2
    baris = 0
    for row in a: #perulangan untuk mengecek jumlah baris
          baris = baris + 1
    new_string = ""
    for i in range (baris): #perulangan untuk mengecek jumlah kolom
        for j in range (c): #perulangan untuk mengecek jumlah kolom
              if j != c-1:  #jika bukan kolom terakhir
                new_string += str(a[i][j]) #tambahkan ke string
                new_string += ";" #tambahkan ; sebagai pemisah
              elif j == c-1: #jika kolom terakhir
                new_string += str(a[i][j]) #tambahkan ke string           
        new_string += "\n" #tambahkan \n sebagai pemisah baris
    return new_string #kembalikan string

def cek_id(username, user_arr): #cek id user yang sedang login

    baris = 0 #jumlah baris
    for row in user_arr: #perulangan untuk mengecek jumlah baris
            baris = baris + 1
    user_id = "" #id user
    for i in range(baris): #perulangan untuk mengecek jumlah kolom
        if username == (str(user_arr[i][1])) : #jika username sama dengan username di user
            user_id = user_arr[i][0] #id user
            break
    return user_id #kembalikan id user

def cek_role(username, user_arr): #cek role user yang sedang login

    baris = 0 
    for row in user_arr: #perulangan untuk mengecek jumlah baris
            baris = baris + 1 
    role_id = "" # role
    for i in range(baris): #perulangan untuk mengecek jumlah kolom
        if username == (str(user_arr[i][1])) : #jika username sama dengan username di user
            role_id = user_arr[i][4] #role
            break
    return role_id #kembalikan role
    
def dimiliki(kepemilikan_arr,idGame,idUser): #cek apakah game milik user
    for i in range (length(kepemilikan_arr)): #perulangan untuk mengecek jumlah baris
        if kepemilikan_arr[i][0] == idGame and kepemilikan_arr[i][1] == idUser: #jika id game dan id user sama dengan milik_arr
            return True #kembalikan True
    return False #kembalikan False

def validasi_char(x): #validasi inputan char
  baris = 0 #jumlah baris
  x = [x for x in x] #buat array perhuruf dari x
  for row in x: #perulangan untuk mengecek jumlah baris
        baris = baris + 1 
  
  a = 0 #untuk indeks array
  
  for i in range (65, 91): #A-Z
    for j in range (baris): #perulangan berdasarkan jumlah 
      if chr(i) == x[j]: #jika huruf sama dengan x
        a += 1 #tambahkan a
  
  for i in range (97, 123): #a-z
    for j in range (baris): #perulangan berdasarkan jumlah
      if chr(i) == x[j]: #jika huruf sama dengan x
        a += 1 #tambahkan a

  for i in range (48, 58): #0-9 
    for j in range (baris): #perulangan berdasarkan jumlah
      if chr(i) == x[j]: #jika huruf sama dengan x
        a += 1  #tambahkan a

  for i in range (baris): #underscore dan strip
    if x[i] == "_": #jika x = "_"
      a += 1
    elif x[i] == "-": #jika x = "-"
      a += 1

  if a == baris: #jika semua huruf valid jumlah a akan sama jumlah array baris dan inputan berarti valid
    return True
  else: #jika tidak valid
    return False
