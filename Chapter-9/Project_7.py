mhs = ['K001:ROSIHAN ARI:1979/09/01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979/09/17:KUDUS',
       'K003:FAZA FAUZAN:2005/01/28:KARANGANYAR']

print("======================================================================")
print("NIM		NAMA MAHASISWA		 TGL LAHIR	TEMPAT LAHIR")
print("----------------------------------------------------------------------")
for i in mhs:
    split = i.split(':')
    #nim,nama,tgllahir, tmptlahir
    nim = split[0]
    nama = split[1]
    tgllahir = split[2]
    tempatlahir = split[3]
    #tgllahir
    splittgl = tgllahir.split('/')
    tgl = splittgl[2]
    bln = splittgl[1]
    thn = splittgl[0]
    print(nim.ljust(15), nama.ljust(24), tgllahir.ljust(14), tempatlahir)

print("======================================================================")

