def kuadrat(bil):
    if(isinstance(bil, list)):
        for i in range(len(bil)):
            bil[i] **= 2
        return bil
    return False

n = int(input('Banyak bilangan bulat yang akan dimasukkan:'))
def inputbilangan():
    i = 1
    data = []
    while i <= n:
        bilangan = int(input("masukkan bilangan bulat:"))
        data.append(bilangan)
        i = i+1
    return data


datalist = inputbilangan()

if(datalist):
    print("bil :", datalist)
    result = kuadrat(datalist)
    print("hasil kuadratnya adalah :", result)
