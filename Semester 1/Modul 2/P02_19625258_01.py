"""
NIM/Nama : Bryan Pamungkas Prahara
Tanggal : 17 Oktober 2025
Deskripsi :
"""

TotalStrawberry = int(input("Masukkan banyak strawberry yang dibeli (buah): "))
JumlahTamu = int(input("Masukkan  jumlah tamu yang datang: "))
JumlahJus = int(TotalStrawberry//7)

if TotalStrawberry >= 7 :
    if TotalStrawberry%7 == 0 : 
        print("Nona Sal dapat membuat" , JumlahJus , "gelas jus strawberry dan membutuhkan" , JumlahJus*3 ,  "gram gula." )
    else :
        print("Nona Sal dapat membuat" , JumlahJus , "gelas jus strawberry dengan sisa" , TotalStrawberry%7 , "buah strawberry, dan membutuhkan" , JumlahJus*3 ,  "gram gula." )
else :
    print("Bahan yang dibeli Nona Sal tidak cukup untuk membuat jus untuk para tamu.")
