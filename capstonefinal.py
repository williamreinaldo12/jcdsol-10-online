from datetime import datetime
import re
from tabulate import tabulate

dftrPasien = {
    '1A': {'Nama Depan': 'John', 'Nama Belakang': 'Doe', 'Tanggal Masuk': '2022-12-25',
        'Tanggal Keluar': '2022-12-29', 'Diagnosa': 'Lapar'},
    '2A': {'Nama Depan': 'Kevin', 'Nama Belakang': 'Anggora', 'Tanggal Masuk': '2022-6-11', 
        'Tanggal Keluar': '2022-6-21', 'Diagnosa': 'Haus'},
    '3A': {'Nama Depan': 'Gisel', 'Nama Belakang': 'Beaumont', 'Tanggal Masuk': '2019-7-22', 
        'Tanggal Keluar': '2019-7-23', 'Diagnosa': 'Kulit Kering'}
}

#Untuk memasukkan Key Baru Bernama 'Lama Rawat' kedalam dftrPasien
#Karena tidak bisa untuk menggunakan Variable yang belum diassign untuk mengassign Nilai dari Key yang kita mau

for i in dftrPasien:
    d1 = datetime.strptime(dftrPasien[i]['Tanggal Masuk'], "%Y-%m-%d")
    d2 = datetime.strptime(dftrPasien[i]['Tanggal Keluar'], "%Y-%m-%d")
    wakturawat = d2 - d1
    dftrPasien[i]['Lama Rawat']= str(wakturawat.days) + ' Hari'

def submenu1():
     
     
     while(True):
          print("-----Data Pasien Rumah Sakit-----")
          print("1. Print Seluruh Data Pasien")
          print("2. Print Data Pasien Tertentu")
          print("3. Balik ke Main Menu")
          submenu = int(input("Masukkan angka submenu yang ingin dijalankan [1-3]: "))
          print("\n")
          if submenu == 1:
               alldata()
          elif submenu ==2:
               subsubmenu()
          elif submenu ==3:
               break
          else:
               print("Masukkan Angka 1-3!")
def submenu2():
     
     while(True):
          print("-----Menambah Data Pasien-----")
          print("1. Tambah data Pasien")
          print("2. Balik ke Main Menu")
          submenu = int(input("Masukkan angka submenu yang ingin dijalnkan [1-2]: "))
          
          print("\n")
          if submenu == 1:
               adddata()
          elif submenu ==2:     
               break
          else:
               print("Masukkan Angka 1-2!")
def submenu3():
     
     while(True):
          print("-----Mengubah Data Pasien-----")
          print("1. Ubah seluruh data Pasien")
          print("2. Ubah sebagian data Pasien")
          print("3. Balik ke Main Menu")
          submenu = int(input("Masukkan angka submenu yang ingin dijalankan [1-3]: "))
          
          if submenu == 1:
               choice = input("Ketik Y jika ingin melanjutkan update Data, N Jika tidak: ")
               if choice.lower() != 'y' and choice.lower() != 'n':
                    print("Masukkan Y/N!")
               elif choice.lower() == 'y':
                    updatefulldata()
                    break
               else:
                    break
          elif submenu ==2:
               choice = input("Ketik Y jika ingin melanjutkan update Data, N Jika tidak: ")
               if choice.lower() != 'y' and choice.lower() != 'n':
                    print("Masukkan Y/N!")
               elif choice.lower() == 'y':
                    updatepartialdata()
                    break
               else:
                    break
          elif submenu == 3:
               break
          else:
               print("Masukkan Angka 1-3!")
def submenu4():
     
     while(True):
          print("-----Menghapus Data Pasien-----")
          print("1. Hapus Data Pasien menggunakan NIM")
          print("2. Hapus Data Pasien menggunakan Diagnosa")
          print("3. Balik ke Main Menu")
          submenu = int(input("Masukkan angka submenu yang ingin dijalankan [1-2]: "))
          print("\n")
          if submenu == 1:
               choice = input("Ketik Y jika ingin melanjutkan hapus Data, N Jika tidak: ")
               if choice.lower() != 'y' and choice.lower() != 'n':
                    print("Masukkan Y/N!")
               elif choice.lower() == 'y':
                    deletedata()
                    break
               else:
                    break
          elif submenu == 2:
               choice = input("Ketik Y jika ingin melanjutkan hapus Data, N Jika tidak: ")
               if choice.lower() != 'y' and choice.lower() != 'n':
                    print("Masukkan Y/N!")
               elif choice.lower() == 'y':
                    deletedatadiagnosa()
                    break
               else:
                    break
          elif submenu == 3:
               break
          else:
               print("Masukkan Angka 1-2!")
def subsubmenu():
     while(True):
          print("\n-----Print Data Pasien Tertentu-----")
          print("1. Print Data Pasien menggunakan NIM")
          print("2. Print Data Pasien lewat Diagnosa")
          print("3. Balik ke menu sebelumnya")
          submenu = int(input("Masukkan angka submenu yang ingin dijalankan[1-3]: "))
          print("\n")
          if submenu == 1:
               datatertentu()
          elif submenu == 2:
               datadiagnosa()
          elif submenu == 3:
               break
          else:
               print("Masukkan angka 1-3!")

def alldata():
     localdftrPasien = dftrPasien
     print("-----Daftar Pasien-----\n")
     headers = ["NIP", "Nama Depan", "Nama Belakang", "Tanggal Masuk", "Tanggal Keluar", "Diagnosa","Lama Rawat"]
     localdftrPasien = [[name, *inner.values()] for name, inner in localdftrPasien.items()]

     print(tabulate(localdftrPasien, headers=headers, tablefmt="fancy_outline"))
        
def datatertentu():
    
     print("-----Daftar Pasien-----\n")
     print("NIP\t|Nama Lengkap\t\t")
     # akan menginterate isi dari key dftrPasien (1A,2A,3A)
     for i in dftrPasien:
          print(f"{i}\t| {dftrPasien[i]['Nama Depan']} {dftrPasien[i]['Nama Belakang']}")
            
     print("\n")
    
     index = (input("Masukkan No Induk Pasien: "))
    
     if index not in dftrPasien:
          print("Data tidak ada!\n")
     else:
          print("\n")
          print("\nNIP\t|Nama Lengkap\t\t| Tgl Masuk\t| Tgl Keluar\t| Lama Rawat\t| Diagnosa")
          print(f"{index}\t| {dftrPasien[index]['Nama Depan']} {dftrPasien[index]['Nama Belakang']}\t\t| {dftrPasien[index]['Tanggal Masuk']}\t| { dftrPasien[index]['Tanggal Keluar']}\t| {dftrPasien[index]['Lama Rawat']}\t| {dftrPasien[index]['Diagnosa']} ")
          print("\n")

def datadiagnosa():
     
     print("-----Daftar Pasien-----\n")
     print("NIP\t| Nama Lengkap\t\t| Diagnosa")
    
     for i in dftrPasien:
          print(f"{i}\t| {dftrPasien[i]['Nama Depan']} {dftrPasien[i]['Nama Belakang']}\t\t| {dftrPasien[i]['Diagnosa']}")
            
     print("\n")
    
     index = (input("Masukkan Diagnosa Pasien: "))
     #mengecek apabila jumlah cek sama dengan size dftrPasien maka tidak ada data tersebut
     cek = 0
     for i in dftrPasien:
          if index.lower() != dftrPasien[i]['Diagnosa'].lower():
               cek += 1
     if cek == len(dftrPasien):
          print("Data tidak ada!")
          return
     else:
          print("NIP\t| Nama Lengkap\t\t| Tgl Masuk\t| Tgl Keluar\t| Lama Rawat\t| Diagnosa")
          for i in dftrPasien:
               if index.lower() == dftrPasien[i]['Diagnosa'].lower():
                    print(f"{i}\t| {dftrPasien[i]['Nama Depan']} {dftrPasien[i]['Nama Belakang']}\t\t| {dftrPasien[i]['Tanggal Masuk']}\t| { dftrPasien[i]['Tanggal Keluar']}\t| {dftrPasien[i]['Lama Rawat']}\t| {dftrPasien[i]['Diagnosa']} ")
        
def adddata():
    
     
  
     index = input("Masukkan No Induk Pasien yang ingin ditambahkan: ")
     #Jika NIM yang user input ada, maka akan direturn True lalu expression akan dijalankan
     if index in dftrPasien:
          print("Data sudah ada!")
     else:
          newNameFirst = input("Masukkan Nama Depan Pasien: ")
          newNameLast = input("Masukkan Nama Belakang Pasien: ")

          while(True):
               cekTglMsk = re.compile(r'\d\d\d\d-\d\d-\d\d')
               newTglMsk = cekTglMsk.search(input("Masukkan Tangal Masuk Pasien [yyyy-mm-dd]: "))
               if newTglMsk == None:
                    print("Format harus ada yyyy-mm-dd!")
               else:
                    break
          while(True):
               cekTglKlr = re.compile(r'\d\d\d\d-\d\d-\d\d')
               newTglKlr = cekTglKlr.search(input("Masukkan Tangal Keluar Pasien [yyyy-mm-dd]: "))
               if newTglKlr == None:
                    print("Format harus ada yyyy-mm-dd!")
               else:
                    break

          newDiagnosa = input("Masukkan Diagnosa Pasien: ")

          while(True):    
               save = input("Save data tersebut? [y/n]: ")
               if save.lower() != 'y' and save.lower() != 'n':
                    print("Masukkan y/n")
               elif save.lower() == 'y':
                    dftrPasien[index] = {'Nama Depan': newNameFirst, 'Nama Belakang': newNameLast, 'Tanggal Masuk': newTglMsk.group(),
                    'Tanggal Keluar': newTglKlr.group(), 'Diagnosa': newDiagnosa}
                    d1 = datetime.strptime(dftrPasien[index]['Tanggal Masuk'], "%Y-%m-%d")
                    d2 = datetime.strptime(dftrPasien[index]['Tanggal Keluar'], "%Y-%m-%d")
                    wakturawat = d2 - d1
                    dftrPasien[index]['Lama Rawat']= str(wakturawat.days) + ' Hari'
                    print("Data sudah tertambah!\n")
                    break
               elif save.lower() == 'n':
                    print("Data tidak tersimpan!\n")
                    break
                         
def updatefulldata():
     alldata()
     index = input("Masukkan No Induk Pasien yang ingin diubah: ")
     if index not in dftrPasien:
          print("Data tidak ada!")
     else:  
          newNameFirst = input("Masukkan Nama Depan Baru Pasien: ")
          newNameLast = input("Masukkan Nama Belakang Baru Pasien: ")
          while(True):
               cekTglMsk = re.compile(r'\d\d\d\d-\d\d-\d\d')
               newTglMsk = cekTglMsk.search(input("Masukkan Tangal Masuk Baru Pasien [yyyy-mm-dd]: "))
               if newTglMsk == None:
                    print("Format harus ada yyyy-mm-dd!")
               else:
                    break
          while(True):
               cekTglKlr = re.compile(r'\d\d\d\d-\d\d-\d\d')
               newTglKlr = cekTglKlr.search(input("Masukkan Tangal Keluar Baru Pasien [yyyy-mm-dd]: "))
               if newTglKlr == None:
                    print("Format harus ada yyyy-mm-dd!")
               else:
                    break

          newDiagnosa = input("Masukkan Diagnosa Baru Pasien: ")
          dftrPasien[index] = {'Nama Depan': newNameFirst, 'Nama Belakang': newNameLast, 'Tanggal Masuk': newTglMsk.group(),
          'Tanggal Keluar': newTglKlr.group(), 'Diagnosa': newDiagnosa}
          d1 = datetime.strptime(dftrPasien[index]['Tanggal Masuk'], "%Y-%m-%d")
          d2 = datetime.strptime(dftrPasien[index]['Tanggal Keluar'], "%Y-%m-%d")
          wakturawat = d2 - d1
          dftrPasien[index]['Lama Rawat']= str(wakturawat.days) + ' Hari'
          print("\nData sudah terupdate!\n")

def updatepartialdata():
     print("-----Daftar Pasien-----\n")
     alldata()
    
         
     index = input("Masukkan No Induk Pasien yang ingin diubah: ")
     if index not in dftrPasien:
          print("\nData tidak ada!\n")
     else:
          while(True):
               keterangan = input("Pilih keterangan mana yang ingin diubah [Nama Depan/Nama Belakang/Tanggal Masuk/Tanggal Keluar/Diagnosa]: ")
               if keterangan not in dftrPasien[index]:
                    print("Tidak ada keterangan tersebut")
               elif keterangan == 'Tanggal Masuk' or keterangan == 'Tanggal Keluar':
                    while(True):
                         cekTglKlr = re.compile(r'\d\d\d\d-\d\d-\d\d')
                         new = cekTglKlr.search(input(f"Masukkan {keterangan} baru [yyyy-mm-dd]: "))
                         
                         if new == None:
                              print("Format harus ada yyyy-mm-dd!")

                         else:
                              dftrPasien[index][keterangan] = new.group()
                              d1 = datetime.strptime(dftrPasien[index]['Tanggal Masuk'], "%Y-%m-%d")
                              d2 = datetime.strptime(dftrPasien[index]['Tanggal Keluar'], "%Y-%m-%d")
                              wakturawat = d2 - d1
                              dftrPasien[index]['Lama Rawat']= str(wakturawat.days) + ' Hari'
                              print("\nData sudah terupdate!\n")
                              break
                    break
               
               
               else:
                    new = input(f"Masukkan {keterangan} baru: ")
                    dftrPasien[index][keterangan] = new
                    print("\nData sudah terupdate!\n")
                    break


def deletedata():
     print("-----Daftar Pasien-----")
     alldata()

     index = input("Masukkan Nomor Induk Pasien yang ingin dihapus: ")
     if index not in dftrPasien:
          print("Data tidak ada!")
     else:
          while(True):    
               delete = input("Delete data tersebut? [y/n]: ")
               if delete.lower() != 'y' and delete.lower() != 'n':
                    print("Masukkan y/n")
               elif delete.lower() == 'y':
                    del dftrPasien[index]
                    print("\nData sudah terhapus!\n")
                    break
               elif delete.lower() == 'n':
                    print("\nData tidak terhapus!\n")
                    break

def deletedatadiagnosa():
     alldata()
     diagnosa = input("Masukkan diagnosa untuk menghapus pasien yang memiliki diagnosa tersebut: ")
     cek = 0
     for i in dftrPasien:
          if diagnosa.lower() != dftrPasien[i]['Diagnosa'].lower():
               cek += 1
     if cek == len(dftrPasien):
          print("Data tidak ada!")
          return
     else:
          while(True):    
               delete = input("Delete data tersebut? [y/n]: ")
               if delete.lower() != 'y' and delete.lower() != 'n':
                    print("Masukkan y/n")
               elif delete.lower() == 'y':
                    
                    for i in list(dftrPasien):
                         if diagnosa.lower() == dftrPasien[i]['Diagnosa'].lower():
                              del dftrPasien[i]
                    print("\nData sudah terhapus!\n")
                    break
               elif delete.lower() == 'n':
                    print("\nData tidak terhapus!\n")
                    break


def menu():
    
     while(True):
          print("-----Data Pasien Rumah Sakit-----")
          print("1. Data Pasien Rumah Sakit")
          print("2. Menambahkan Data Pasien")
          print("3. Mengubah Data Pasien")
          print("4. Menghapus Data Pasien")
          print("5. Exit")

          menu = int(input("Masukkan angka menu yang ingin dijalankan [1-5]: "))
          print("\n")
          if menu == 1:
               submenu1()  
          elif menu == 2:
               submenu2()
          elif menu == 3:
               submenu3()
          elif menu == 4:
               submenu4()
          elif menu == 5:
               break
          else:
               print("Masukkan angka 1-5!")

menu()

