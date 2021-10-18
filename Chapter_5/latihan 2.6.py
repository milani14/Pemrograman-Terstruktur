print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
from random import randint
angka = randint(0,100)
score = 100
while True:
  angkatebakan = int(input('Tebakan Anda: '))
  if (angkatebakan<angka):
    print('Hehehe... Bilangan tebakan anda terlalu kecil')
  elif(angkatebakan>angka):
    print('Hehehe... Bilangan tebakan anda terlalu besar')
  elif(angkatebakan==angka):
    print('Yeeee… Bilangan tebakan anda BENAR :-)')
    score -=3
    break
print ("Score Anda: ", score)
