from kasir import KasirClass

obj = KasirClass()


class main:

    pilihan = "x"

    while pilihan == "x":
        print("=========================================================")
        print("|\t\t\t SEBLAK SEHATI \t\t\t|")
        print("|\t\t\t DAFTAR MENU \t\t\t|")
        print("| \t1. Seblak Ceker \t\t10000 \t\t|")
        print("| \t2. Seblak Sosis \t\t10000 \t\t|")
        print("| \t3. Seblak Bakso \t\t10000 \t\t|")
        print("| \t4. Seblak Seafood \t\t12000 \t\t|")
        print("| \t5. Seblak Sosis+Bakso \t\t12000 \t\t|")
        print("| \t6. Seblak Sosis+Bakso+Mie \t15000 \t\t|")
        print("| \t7. Seblak Spesial \t\t15000 \t\t|")
        print("| \t8. Seblak Komplit \t\t20000 \t\t|")
        print("=========================================================")
        print()

        makanan = int(input("Mau Seblak Apa (Masukkan angka) = "))
        print()
        jumlah = int(input("Berapa porsi (Masukkan angka)? = "))

        if makanan == 1:
            harga = obj.total(10000, jumlah)
        elif makanan == 2:
            harga = obj.total(10000, jumlah)
        elif makanan == 3:
            harga = obj.total(10000, jumlah)
        elif makanan == 4:
            harga = obj.total(12000, jumlah)
        elif makanan == 5:
            harga = obj.total(12000, jumlah)
        elif makanan == 6:
            harga = obj.total(15000, jumlah)
        elif makanan == 7:
            harga = obj.total(15000, jumlah)
        elif makanan == 8:
            harga = obj.total(20000, jumlah)

        print()
        print("=========================================")
        print("|\t\tDAFTAR MINUM\t\t|")
        print("|\t1. Es Jeruk\t\t7000\t|")
        print("|\t2. Es teh Manis\t\t5000\t|")
        print("|\t3. Air Putih\t\t3000\t|")
        print("|\t4. Teh Pucuk\t\t4000\t|")
        print("|\t5. Tidak memesan minuman\t|")
        print("=========================================")

        minum = int(input("Mau minum apa? = "))
        pcs = int(input("Berapa pcs? = "))

        if minum == 1:
            jeruk = obj.total(7000, pcs)
            total = obj.HasilAkhir(harga, jeruk)
        elif minum == 2:
            esteh = obj.total(5000, pcs)
            total = obj.HasilAkhir(harga, esteh)
        elif minum == 3:
            air = obj.total(3000, pcs)
            total = obj.HasilAkhir(harga, air)
        elif minum == 4:
            pucuk = obj.total(4000, pcs)
            total = obj.HasilAkhir(harga, pucuk)
        elif minum == 5:
            pass

    # Menghitung total harga

        if minum == 5:
            print("Total Pembayaran = ", harga)
        elif jumlah > 5:
            diskon = total-3000
            print("Total Pembayaran = ", diskon)
        elif jumlah < 5:
            print("Total Pembayaran = ", total)
        break


if __name__ == '__main__':
    main()
