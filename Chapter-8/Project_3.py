n = int(input('Jumlah mahasiswa yang akan dimasukkan:'))


i = 1
data = []
while i <= n:
    namamahasiswa = input("Nama mahasiswa :")
    data.append(namamahasiswa)
    i = i+1

#ascending
data.sort()
for namamahasiswa in data:
    print("{0} ({1} karakter)".format(namamahasiswa, len(tuple(namamahasiswa))))
