n = int(input('Banyak buah yang akan dimasukkan:'))
def sortStringByChar(myData):
    myData.sort(reverse = True, key = len)
    return(myData)

def inputbuah():
    i = 1
    data = []
    while i <= n:
        namaBuah = (input('Masukkan Nama Buah: '))
        data.append(namaBuah)
        i = i+1
    return data

dataList = inputbuah()

if(dataList):
    result = sortStringByChar(dataList)
    print(result)
