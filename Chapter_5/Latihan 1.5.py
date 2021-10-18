kodekaryawan = input("Masukkan kode karyawan :")
namakaryawan = input("Masukkan Nama Karyawan :")
golongan = input("Masukkan golongan : ")


# golongan
if golongan == "A":
    gajipokok = 10000000
    potongan = 2.5
elif golongan == "B":
    gajipokok = 8500000
    potongan = 2.0
elif golongan == "C":
    gajipokok = 7000000
    potongan = 1.5
elif golongan == "D":
    gajipokok = 5500000
    potongan = 1.0
else:
    golongan = False
    print("tidak masuk golongan")
if(golongan != False):
    status = int(input("Masukan Status (1:menikah, 2:blm) : "))
    if(status == 1):
        tunjangansuamiistri = gajipokok * 10/100
        jumlahanak = int(input("Masukkan Jumlah Anak : "))
        tunjangananak = gajipokok * 5/100 * jumlahanak
    elif(status == 2):
        tunjangansuamiistri = 0
        tunjangananak = 0
    else:
        print("Input ada yang tidak valid")
        status = False

if(status != False):
    print("==============================")
    print("STRUK RINCIAN GAJI KARYAWAN")
    print("------------------------------")
    print("Nama Karyawan :", namakaryawan)
    print("Golongan :", golongan)
    print("Status Menikah :", status)
    print("Jumlah anak :", jumlahanak)
    print("-----------------------------")
    print("Gaji Pokok :",  gajipokok)
    print("Tunjangan istri/suami :", tunjangansuamiistri)
    print("Tunjangan Anak :", tunjangananak)
    print("----------------------------- +")
    gajiKotor = gajipokok + tunjangansuamiistri + tunjangananak
    print("Gaji Kotor : ", gajiKotor)
    potonganGaji = int(gajiKotor*potongan/100)
    print("Potongan (",potongan,"% ) : ",potonganGaji)
    print("--------------------------------------- -")
    gajiBersih = gajiKotor - potonganGaji
    print("Gaji Bersih : ", gajiBersih)

