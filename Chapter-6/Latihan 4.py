def penjumlahan(*myData):
    #init values
    sum=0
   
    #input myData
    for data in myData:
        sum += data

    hasil=sum
    print('Jumlahnya adalah:', hasil)


def rerata(*myData):
    #init values
    sum=0
    i=0

    #input myData
    for data in myData:
        sum += data
        i += 1

    hasil=sum/i
    print('Rata-ratanya adalah: ',hasil)
    

def maksimum(*myData):
    #input myData
    for data in myData:
        hasil= max(data)
    print('Nilai Maksimumnya adalah: ',hasil)
    

def minimum(*myData):
    #input myData
    for data in myData:
        hasil= min(data)
    print('Nilai minimumnya adalah: ',hasil)
