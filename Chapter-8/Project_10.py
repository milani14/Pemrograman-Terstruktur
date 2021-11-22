print('=======================================')
print('=====Program Menghitung Harga Buah=====')
print('=======================================')

buah = {'apel' : 5000 , 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}


harga =[]
while True :
    print('')
    jenisbuah = input('Nama buah yang dibeli: ')
    pembelian = int(input('Berapa Kg: '))
    data = buah.get(jenisbuah)
    hasil = pembelian * data
    harga += [hasil]
    print('')
    tambah = input('Beli buah yang lain (y/n) ? ')
    if (tambah == 'n') :
        break


sum = sum(harga)
print('-------------------------------------------')
print('Total harga		: Rp ', sum)
