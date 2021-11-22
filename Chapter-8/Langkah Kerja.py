a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

#1-4
a.insert(3, 10), a.append(4), a.sort()
print(a)
b.insert(2,15), b.append(8), b.sort()
print(b)

#5
c = list(a[0:8])
print(c)
d = list(b[2:10])
print(d)

#6
e = []
dataE = []
if len(c) == len(d):
    for n in range(len(c)):
        dataE = c[n]+d[n]
        e.append(dataE)
    print('e=', e)

#7
myTuple = tuple(e)
print(myTuple)

#8
print("Maksimum:", max(myTuple))
print("Minimum:", min(myTuple))
print("Jumlah:", sum(myTuple))

#9-10
print('> python adalah bahasa pemrograman yang menyenangkan')
myString = 'python adalah bahasa pemrograman yang menyenangkan'
hurufPenyusun = set(myString)
print("> Huruf Penyusun:", hurufPenyusun)

#11
myList = ['r', 's', 'e', 'k', 'y', 'm', 'g', 'p', 'o', 'n', 'h', 'd', 't', 'b', 'a', ' ', 'l']
mySet = set(myList)
print(mySet)
