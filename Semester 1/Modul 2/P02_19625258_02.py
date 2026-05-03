"""
NIM/Nama : Bryan Pamungkas Prahara
Tanggal : 17 Oktober 2025
Deskripsi :
"""
mawar = int(input("Masukkan jumlah stock bunga mawar:  ")) 
carnation = int(input("Masukkan jumlah stock bunga carnation : "))  
lily = int(input("Masukkan jumlah stock bunga lily:  ")) 
aster = int(input("Masukkan jumlah stock bunga aster: "))
tulip = int(input("Masukkan jumlah stock bunga tulip: ")) 
daisy = int(input("Masukkan jumlah stock bunga daisy: ")) 

KM = int(mawar//5)
KC = int(carnation//2)
KL = int(lily//3)
KA = int(aster//4)
KT = int(tulip//6)
KD = int(daisy//1)


if KM > 0 :
    if KC > 0:
        if KL > 0:
            if KA > 0:
                if KT > 0:
                    if KD > 0:
                        if KL*4*3 <= aster and 2*KM*5 <= carnation and KT*6 <= daisy :
                            print("Nona Sal dapat menyusun karangan bunga dengan" , KM*5, "mawar , " , 2*KM*5 , 
                              "carnation ," , KL*3 , "lily ," , KL*4*3 , "aster ," , KT*6 ,  "tulip ," , KT*6 , "daisy.")

elif KM >= 0 :
     if KC >= 0:
        if KL > 0:
            if KA > 0:
                if KT > 0:
                    if KD > 0:
                        if KL*4*3 <= aster and KT*6 <= daisy :
                            print("Nona Sal dapat menyusun karangan bunga dengan" , KL*3 , "lily ," , KL*4*3 , "aster ," , KT*6 ,
                                    "tulip ," , KT*6 , "daisy.")

elif KC > 0:
        if KL > 0:
            if KA > 0:
                if KT > 0:
                    if KD > 0: 
                        if  2*KM*5 <= carnation and KT*6 <= daisy :
                            print("Nona Sal dapat menyusun karangan bunga dengan" , KM*5, "mawar , " , 2*KM*5 , 
                                "carnation ," , KT*6 ,  "tulip ," , KT*6 , "daisy.")
    
elif KC > 0:
        if KL > 0:
            if KA > 0:
                if KT > 0:
                    if KD > 0:
                        if KL*4*3 <= aster and 2*KM*5 <= carnation :
                         print("Nona Sal dapat menyusun karangan bunga dengan" , KM*5, "mawar , " , 2*KM*5 , 
                            "carnation ," , KL*3 , "lily ," , KL*4*3 , "aster ,")
    
else : 
    print("Nona Sal gagal menyusun karangan bunga pelanggan .")

