print("Program Perhitungan IP Mahasiswa Prodi Komputerisasi Akuntansi Politeknik Negeri Semarang")
print("===================================================================================================")
NIM = input("Masukkan NIM: ")
Nama = input("Masukkan Nama: ")

JSKS = 0
JKREDIT = 0
i = 0

while True:  # Simulating repeat-until
    i += 1
    MATKUL = input(f"Masukkan nama mata kuliah ke {i} : ")
    SKS = float(input("Masukkan SKS: "))
    NHAR = float(input("Masukkan nilai harian: "))
    NTUG = float(input("Masukkan nilai tugas: "))
    NUTS = float(input("Masukkan nilai UTS: "))
    NUAS = float(input("Masukkan nilai UAS: "))
        
    NA = (0.2 * NHAR) + (0.2 * NTUG) + (0.3 * NUTS) + (0.3 * NUAS)

    if NA >= 80:
        NHRF = "A"
        NBBT = 4.00
    elif NA >= 75:
        NHRF = "B"
        NBBT = 3.00 
    elif NA >= 60:
        NHRF = "C"
        NBBT = 2.00
    elif NA >= 40:
        NHRF = "D"
        NBBT = 1.00
    else:
        NHRF = "E"
        NBBT = 0.00

    KREDIT = (NBBT * SKS)

    print("MATA KULIAH: ", MATKUL)
    print("SKS: ", SKS) 
    print("NILAI AKHIR: ", NA)
    print("NILAI HURUF: ", NHRF)
    print("NILAI BOBOT: ", NBBT)
    print("NILAI KREDIT: ", KREDIT)
    print("===================================================================================================")

    JSKS += SKS
    JKREDIT += KREDIT

    if i == 3:  # Ex7it condition for repeat-until
        break

# Menampilkan output
IP = JKREDIT / JSKS
print("Nama Mahasiswa: ", Nama)
print("NIM Mahasiswa: ", NIM)
print("Jumlah Mata Kuliah: ", i)
print("Jumlah SKS: ", JSKS)
print("Jumlah Kredit: ", JKREDIT)       
print("IP: ", IP)
