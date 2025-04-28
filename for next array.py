print("Program Perhitungan Indeks Prestasi")
print("Prgram Studi Komputer Akuntansi")
print("Jurusan Akuntansi")
print("Politeknik Negeri Semarang 2025")
print("=====================================")

nmr = 1
jsks = 0
jkredit = 0

nim = input("No. Induk Mahasiswa : ")
nm = input("Nama Mahasiswa      : ")
ulang = int(input("Berapa Data yang akan diinput ? : "))

# Array untuk menyimpan data
mata_kuliah = []
sks_list = []
nilai_harian = []
nilai_tugas = []
nilai_mid = []
nilai_uas = []
nilai_akhir = []
nilai_huruf = []
bobot_list = []
kredit_list = []

for i in range(1, ulang + 1):
    nmk = input(f"Nama Mata Kuliah {i} : ")
    sks = int(input("SKS : "))
    nharian = float(input("Nilai Harian : "))
    ntugas = float(input("Nilai Tugas : "))
    nmid = float(input("Nilai Tengah Semester : "))
    nuas = float(input("Nilai Akhir Semester : "))

    nakhir = ((0.2 * nharian) + (0.2 * ntugas) + (0.3 * nmid) + (0.3 * nuas))
    print(nakhir)

    if nakhir >= 85:
        nh = "A"
        bbt = 4
    elif nakhir >= 75:
        nh = "B"
        bbt = 3
    elif nakhir >= 65:
        nh = "C"
        bbt = 2
    elif nakhir >= 55:
        nh = "D"
        bbt = 1
    else:
        nh = "E"
        bbt = 0
    print("Nilai Huruf Anda Adalah :", nh)
    print("Bobot Nilai :", bbt)

    kredit = bbt * sks
    jsks += sks
    jkredit += kredit
    print("Kredit : ", kredit)

    # Simpan data ke dalam array
    mata_kuliah.append(nmk)
    sks_list.append(sks)
    nilai_harian.append(nharian)
    nilai_tugas.append(ntugas)
    nilai_mid.append(nmid)
    nilai_uas.append(nuas)
    nilai_akhir.append(nakhir)
    nilai_huruf.append(nh)
    bobot_list.append(bbt)
    kredit_list.append(kredit)

nmr += 1
ips = jkredit / jsks
print("=======================================================================================================")
print(f"Indeks Prestasi: {ips:.2f}")
print("=======================================================================================================")

# Menampilkan data yang telah disimpan
print("\nData Mata Kuliah:")
print("=======================================================================================================")
print("No. Nama M.Kuliah       SKS  N. Harian  N. Tugas  N. Tengah Smt   N. Akhir Smt  N. Huruf Bobot Kredit")
print("=======================================================================================================")
for i in range(ulang):
    print(f"{i+1:2}  {mata_kuliah[i]:<20} {sks_list[i]:<4} {nilai_harian[i]:<10} {nilai_tugas[i]:<8} {nilai_mid[i]:<15} {nilai_akhir[i]:<13.2f} {nilai_huruf[i]:<8} {bobot_list[i]:<5} {kredit_list[i]:<6}")
print("=======================================================================================================")