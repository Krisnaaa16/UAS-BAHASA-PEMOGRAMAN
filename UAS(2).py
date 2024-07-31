def menu():
    print("\nPilih bangun datar untuk dihitung:")
    print("1. Segi Empat")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Keluar")
    choice = int(input("Masukkan pilihan (1-5): "))
    return choice

def luas_segi_empat(sisi):
    return sisi * sisi

def keliling_segi_empat(sisi):
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def luas_lingkaran(jari_jari):
    return 3.14 * jari_jari * jari_jari

def keliling_lingkaran(jari_jari):
    return 2 * 3.14 * jari_jari

def hitung_luas_keliling():
    while True:
        choice = menu()

        if choice == 1:
            sisi = float(input("Masukkan sisi segi empat: "))
            luas = luas_segi_empat(sisi)
            keliling = keliling_segi_empat(sisi)
            print(f"Luas Segi Empat: {luas}")
            print(f"Keliling Segi Empat: {keliling}")

        elif choice == 2:
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            luas = luas_persegi_panjang(panjang, lebar)
            keliling = keliling_persegi_panjang(panjang, lebar)
            print(f"Luas Persegi Panjang: {luas}")
            print(f"Keliling Persegi Panjang: {keliling}")

        elif choice == 3:
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            sisi1 = float(input("Masukkan sisi pertama: "))
            sisi2 = float(input("Masukkan sisi kedua: "))
            sisi3 = float(input("Masukkan sisi ketiga: "))
            luas = luas_segitiga(alas, tinggi)
            keliling = keliling_segitiga(sisi1, sisi2, sisi3)
            print(f"Luas Segitiga: {luas}")
            print(f"Keliling Segitiga: {keliling}")

        elif choice == 4:
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            luas = luas_lingkaran(jari_jari)
            keliling = keliling_lingkaran(jari_jari)
            print(f"Luas Lingkaran: {luas}")
            print(f"Keliling Lingkaran: {keliling}")

        elif choice == 5:
            print("Terima kasih telah menggunakan program ini.")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    hitung_luas_keliling()
