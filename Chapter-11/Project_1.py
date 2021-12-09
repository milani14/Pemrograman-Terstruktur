from datetime import *
def diffDate(x):
    skrg = datetime.now()
    tglskrg = str(skrg.year) + '-' + str(skrg.month) + '-' + str(skrg.day)
    today = datetime.strptime(str(tglskrg), '%Y-%m-%d')
    later = datetime.strptime(str(x), '%Y-%m-%d')
    selisih = later - today
    print (selisih.days)
print("Maka selisih harinya yaitu:")
diffDate('2021-12-30')

    
