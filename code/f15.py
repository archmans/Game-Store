import argparse 
import os

def load(): #fungsi load
  parser = argparse.ArgumentParser(description="Running file tubes daspro") #parser
  parser.add_argument("Namafolder", type=str, help="Nama folder csv") #argument
  args = parser.parse_args() #parse argument
  file_exist = False #inisialisasi file_exist
  list_files = os.listdir('./') #inisialisasi list_files
  for files in list_files: #cek apakah folder ada
    if files == args.Namafolder:
      file_exist = True
  if file_exist == False: #jika tidak ada
      a = f"Folder {args.Namafolder} tidak ditemukan."
      return False, a #return False, a
  elif file_exist == True: #jika ada
      return True, args.Namafolder #return True, nama folder