try:
    file = open("d:/anyfiles.txt","r")
    print('Isi file d:/anyfiles.txt adalah:')
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')

