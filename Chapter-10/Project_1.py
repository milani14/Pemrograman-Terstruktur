myfile = open('d:\project1.txt', 'r')
ganjil = 0
genap = 0

#bil 
for i in myfile:
    if (int(i) % 2==0):
        genap += 1
    else:
        ganjil += 1
print ("Banyaknya bilangan genap :", genap)
print ("Banyaknya bilangan ganjil :", ganjil)
