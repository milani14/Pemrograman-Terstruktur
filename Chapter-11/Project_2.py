from datetime import*
dataFile = open("datapinjam.txt", "a")


while True :
    print('')
    kode = input("Masukkan Kode Member: ")
    nama = input("Masukkan Nama Member: ")
    judul = input("Masukkan Judul :")
    
    x = datetime.date(datetime.now())
    awal = str(str(x.year) + "-" + str(x.month) + "-" + str(x.day))
    y = str(x + timedelta(days=+7))
    
    myString = kode+"|"+nama+"|"+judul+"|"+ awal + "|" + y + "\n"
    
    dataFile.write(myString)
    
    tambah = input("Ulangi lagi (y/n) ? ")
    if tambah in("n","N"):
        break

dataFile.close()
