import pandas as pd

# 1. Baca file CSV
try:
    df = pd.read_csv('DatMat.csv', encoding='latin1')

    # 2. Cari kolom secara otomatis menggunakan keyword
    # Kita cari kolom yang namanya mengandung 'Time' dan 'Tctl'
    kolom_waktu = [c for c in df.columns if 'Time' in c]
    kolom_suhu = [c for c in df.columns if 'Tctl' in c]

    if kolom_waktu and kolom_suhu:
        # Mengambil kolom pertama yang ditemukan untuk masing-masing keyword
        nama_kolom_waktu = kolom_waktu[0]
        nama_kolom_suhu = kolom_suhu[0]
        
        # 3. Filter data
        df_hasil = df[[nama_kolom_waktu, nama_kolom_suhu]]
        
        # 4. Simpan ke file baru
        df_hasil.to_csv('Data_Suhu_Ringkas.csv', index=False)
        df_hasil.to_excel('Data_Suhu_Ringkas.xlsx', index=False)
        
        print("Berhasil!")
        print(f"Kolom yang diambil: {nama_kolom_waktu} dan {nama_kolom_suhu}")
        print(df_hasil.head())
    else:
        print("Kolom tidak ditemukan. Coba jalankan 'print(df.columns)' untuk melihat daftar nama kolom.")

except Exception as e:
    print(f"Terjadi error: {e}")