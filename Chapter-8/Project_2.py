n = int(input('Banyak bilangan bulat yang akan dimasukkan:'))
def datastat(x):
    if(isinstance(x, list)):
        tupleX = tuple(x)
        a = sum(tupleX) / len(tupleX)
        b = max(tupleX)
        c = min(tupleX)
    return[a, b, c]


def inputdata():
    i = 1
    data = []
    while i<= n:
        bilangan = int(input("masukkan bilangan bulat:"))
        data.append(bilangan)
        i = i + 1
    return data


datalist = inputdata()
if(datalist):
    hasil = datastat(datalist)
    print("Rata-Ratanya adalah {0} : {1}" .format(datalist, hasil[0]))
    print("Nilai tertingginya adalah{0} : {1}" .format(datalist, hasil[1]))
    print("Nilai terendahnya adalah {0} : {1}" .format(datalist, hasil[2]))
