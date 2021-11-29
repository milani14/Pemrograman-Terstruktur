import random

def shuffleString(teks, n):
    listkata = []
    i = 0
    while i < n:
        kata = ''.join(random.sample(teks, len(teks)))
        if kata not in listkata:
            listkata.append(kata)
            i += i+1
        else:
            continue
    return listkata

print(shuffleString(input("Masukkan kata:"), int(input("Masukkan angka:"))))
