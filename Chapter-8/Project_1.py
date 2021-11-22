n = int(input('Banyak bilangan bulat yang akan dimasukkan:'))

#input bilangan
i=1
data = []
while (i <= n):
    bilangan = int(input('masukkan bilangan bulat:'))
    data.append(bilangan)
    i = i+1

#Descending
data.sort(reverse=True)
print("Berikut bilangan bulat dari yang terbesar ke terkecil:", data)














