buah = {'apel'     : 5000, 'jeruk'    : 8500, 'mangga'   : 7800, 'duku'     : 6500}
n=4

def ratarataHargaBuah(buah):
    harga = list(buah.values())
    rata = sum(harga)/n
    return rata

x = ratarataHargaBuah(buah)
print('Rata-rata harga buah adalah: ', x)

