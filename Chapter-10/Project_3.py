dataFile = open ("datamahasiswa.txt", "r")
dataList = []
data = dataFile.readlines()
for i in range(len(data)):
    delete = data[i].replace("\n", "")
    pecahData = delete.split("|")
    dataDict = {"nim": pecahData[0], "nama": pecahData[1], "Asal": pecahData[2]}
    dataList.append(dataDict)
print(dataList)
dataFile.close()
