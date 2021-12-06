dataFile = open ("datamahasiswa.txt", "r")
datamhs = dataFile.readlines()
mhs = input("Masukkan NIM yang mau dicari: ")

for i in range(len(datamhs)):
    data = datamhs[i]. split("|")
    nim= datamhs[i]. split("|")[0]
    if nim == mhs:
        status = "ditemukan"
        print("Data Mahasiswa")
        print("NIM	: ",data[0])
        print("Nama	: ",data[1])
        print("Alamat	: ",data[2])
        break
    else:
        status = "tidak ditemukan"

if status == "tidak ditemukan":
        print("Data mahasiswa tidak ditemukan")
        

dataFile.close()
              
