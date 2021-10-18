#input nilai
nilaiBahasaIndonesia = int(input("Nilai Bahasa Indonesia: "))
nilaiIPA             = int(input("Nilai IPA: "))
nilaiMatematika      = int(input("Nilai Matematika: "))
rangenilaiawal       = 0
rangenilaiakhir      = 100



if (nilaiBahasaIndonesia>=60) and (nilaiIPA>=60) and (nilaiMatematika>=70):
    print ("Status Kelulusan  = Lulus")
else:
    print ("Status Kelulusan  = Tidak Lulus")

