#tarif sewa rental mobil

#untuk12jampertama
tarifawal = 200000 #12jampertama
#tarifper-jam
tarifselanjutnya = 10000 

waktuawalsewa = 6.00
waktuakhirsewa = 23.50

#menghitung lama waktu sewa
lamasewa = int (waktuakhirsewa-waktuawalsewa)
#menghitung lama waktu sewa selanjutnya
lamasewaselanjutnya = lamasewa - 12
#menghitung tarif sewa selanjutnya
tarifsewaselanjutnya = lamasewaselanjutnya * tarifselanjutnya
totaltarif = tarifawal + tarifsewaselanjutnya
print('jadi, total tarif yang harus  dibayar kepada rental mobil adalah sebesar', totaltarif)
