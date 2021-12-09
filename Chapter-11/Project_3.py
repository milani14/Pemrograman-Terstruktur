file = open('datapinjam.txt', 'r')

kode  = []
nama  = []
judul = []
awalpinjam  = []
makspinjam  = []

for pin in file:
    spltpin = pin.split('|')
    kode.append(spltpin[0])
    nama.append(spltpin[1])
    judul.append(spltpin[2])
    awalpinjam.append(spltpin[3])
    makspinjam.append(spltpin[4].strip())
    
print ('')
print('Data Peminjaman Buku')
print('----------------------')
print('')

while True:
    cari = input('Masukkan Kode Member: ')
    print('')
    if cari in kode:
        data = True
        import datetime

        a = kode.index(cari)
        skrg = datetime.datetime.now()
        from datetime import datetime

        b = makspinjam[a]
        c = datetime.strptime(b, '%Y-%m-%d')
        hasil = c - skrg
        akhir = datetime.date(skrg)
        batas = datetime.date(c)

        if data:
            d = batas - akhir
            batas = d.days
            denda = 0
            if batas <= 0:
                bayar = 0
            elif batas >= 0:
                bayar = 2000 * int(batas)
                denda += bayar

            print('Data Peminjam Buku')
            print('Kode Member                  :', kode[a])
            print('Nama Member                  :', nama[a])
            print('Judul Buku                   :', judul[a])
            print('Tanggal Mulai Peminjaman     :', awalpinjam[a])
            print('Tanggal Maksimal Peminjaman  :', makspinjam[a])
            print('Tanggal Pengembalian         :', akhir)
            print('Terlambat                    :', batas, 'hari')
            print('Denda                        :', 'Rp.', denda)

    else:
        print('Data Tidak Ditemukan')

    print('')
    lagi = input('Ingin Mencari Lagi? (y/n): ')
    if lagi == 'y':
        print('')
        continue
    else:
        break
