print('=======================================')
print('=====Program Menghitung Harga Buah=====')
print('=======================================')

# list
buah = {'apel' : 5000 ,'jeruk' : 8500,'mangga' : 7800,'duku' : 6500}

# tampilan awal
print('Menu :')
print('A. Tambah data buah')
print('B. Beli buah')

print('')
answer = input('Masukkan pilihan : ')

if (answer == 'A'):
    # input data
    while True :
        namaBuah = input('Masukkan nama buah 		: ')
        hargaBuah = int(input('Masukkan harga satuan		: '))
        if namaBuah in buah.keys() :
            print ('Nama buah sudah ada di dalam dictionary.')
        else :
            buah[namaBuah] = hargaBuah
        print('')
        tambah = input('Tambah data yang lain (y/n) ? ')
        if (tambah == 'n'):
            break

    # tampilan
    print('')
    print('Data buah : ')
    print('')
    for x, y in buah.items() :
        print('- ', x, ' ( Harga Rp ', y, ')' )

        
elif (answer == 'B'):
    # inputdata
    harga =[]
    while True :
        namaBuah = input('Nama buah yang dibeli 	: ')
        banyakKg = int(input('Berapa Kg		: '))
        data = buah.get(namaBuah, 0)
        hasil = banyakKg * data
        harga += [hasil]
        print('')
        tambah = input('Beli buah yang lain (y/n) ? ')
        if (tambah == 'n'):
            break
        
    # hitung
    sum = sum(harga)
    print('-------------------------------------------')
    print('Total harga		: Rp ', sum)


