myfile = open("bilangan2.txt", "r")
text = ''
for data in myfile:
    angka = data.split('|')
    angka = angka
    hasil = int(angka[0]) + int(angka[1].rstrip("\n"))
    text += str(output) + "\n"

filehasil = open("output.txt", "w")
filehasil.write(text)
filehasil.close()
