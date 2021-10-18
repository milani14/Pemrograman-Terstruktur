#input nilai
nilaiBahasaIndonesia = int(input("Nilai Bahasa Indonesia: "))
nilaiIPA             = int(input("Nilai IPA: "))
nilaiMatematika      = int(input("Nilai Matematika: "))



if (nilaiBahasaIndonesia>=0)and(nilaiBahasaIndonesia<=0) and (nilaiIPA>=0) and (nilaiIPA<=100)and(nilaiMatematika>=0)and(nilaiMatematika<=100):
    if (nilaiBahasaIndonesia>=60) and (nilaiIPA>=60) and (nilaiMatematika>=70):
         print ("Status Kelulusan  = Lulus")
    else:
         print ("Status Kelulusan  = Tidak Lulus")
else:
    print ("Maaf input ada yang tidak valid")

