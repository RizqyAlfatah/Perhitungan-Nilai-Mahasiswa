def input_jurnal_umum():
    print("=== Program Input Jurnal Umum ===")
    nperus = input("Masukkan nama perusahaan: ")
    njur = input("Masukkan nama jurnal: ")
    nperiode = input("Masukkan periode: ")
    print("====================================")
    print(nperus)
    print(njur)
    print(nperiode)
   
    jurnal = []

    while True:
        print("\nMasukkan data transaksi:")
        tanggal = input("Tanggal (YYYY-MM-DD): ")
        keterangan = input("Keterangan: ")

        akun_debit_list = []
        while True:  # Input akun debit
            try:
                akun_debit = input("Nama akun (Debit): ")
                debit = float(input("Nominal Debit: "))
                akun_debit_list.append({"akun": akun_debit, "debit": debit})
                ulang_debit = input("Apakah ingin menambahkan akun debit lagi? (y/n): ").lower()
                if ulang_debit != 'y':
                    break
            except ValueError:
                print("Input tidak valid. Masukkan angka untuk nominal debit.")

        akun_kredit_list = []
        while True:  # Input akun kredit
            try:
                akun_kredit = input("Nama akun (Kredit): ")
                kredit = float(input("Nominal Kredit: "))
                akun_kredit_list.append({"akun": akun_kredit, "kredit": kredit})
                ulang_kredit = input("Apakah ingin menambahkan akun kredit lagi? (y/n): ").lower()
                if ulang_kredit != 'y':
                    break
            except ValueError:
                print("Input tidak valid. Masukkan angka untuk nominal kredit.")

        jurnal.append({
            "tanggal": tanggal,
            "keterangan": keterangan,
            "akun_debit_list": akun_debit_list,
            "akun_kredit_list": akun_kredit_list
        })

        lanjut = input("Apakah ingin menambahkan transaksi lagi? (y/n): ").lower()
        if lanjut != 'y':
            break

    print("\n=== Jurnal Umum ===")
    print("{:<15} {:<30} {:<20} {:<15} {:<20} {:<15}".format("Tanggal", "Keterangan", "Akun Debit", "Debit", "Akun Kredit", "Kredit"))
    print("-------------------------------------------------------------------------------------------------------------")
    for entry in jurnal:
        for akun_debit in entry["akun_debit_list"]:
            for akun_kredit in entry["akun_kredit_list"]:
                print("{:<15} {:<30} {:<20} {:<15} {:<20} {:<15}".format(
                    entry["tanggal"], entry["keterangan"], akun_debit["akun"], akun_debit["debit"], akun_kredit["akun"], akun_kredit["kredit"]
                ))

if __name__ == "__main__":
    input_jurnal_umum()
