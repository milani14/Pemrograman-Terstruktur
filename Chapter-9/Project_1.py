ubahHuruf = ('MATEMATIKA', 'T', 'S')

#string ke list
string = ubahHuruf
mylist = list(ubahHuruf)
print(mylist)

#ubah huruf
def ubahHuruf(string):
    ubah = string.replace('T', 'S')
    print(ubah)
    return ubah

string = "MATEMATIKA"
ubahHuruf(string)
