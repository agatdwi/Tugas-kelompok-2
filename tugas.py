# Class produk: nge-wrap info barang biar rapi dan reusable
class Produk:
    def __init__(self, nama: str, harga: int):
        self.nama = nama   # nama produk
        self.harga = harga # harga produk (int)

    def __str__(self):
        # tampilan produk ketika di-print
        return f"{self.nama} - Rp{self.harga}"


# Class toko: tempat nyimpen stok produk yang *bisa dibeli*
class Toko:
    def __init__(self):
        # list produk yang tersedia — ini bisa dikembangin jadi ambil dari database
        self.daftar_produk = [
            Produk("Indomie Goreng", 3500),
            Produk("Roti Tawar", 12000),
            Produk("Teh Kotak", 5000),
            Produk("Beras 1kg", 15000),
            Produk("Minyak Goreng 1L", 14000),
        ]

    def tampilkan_produk(self):
        # show barang yang toko jual
        print("\n=== Produk Toko ===")
        for i, produk in enumerate(self.daftar_produk, start=1):
            print(f"{i}. {produk}")
        print("===================\n")

    def pilih_produk(self, nomor: int):
        # cek kalau nomor valid
        if 1 <= nomor <= len(self.daftar_produk):
            return self.daftar_produk[nomor - 1]
        return None  # kalau salah nomor, balikin None


# Class keranjang: urus barang masuk/keluar dari belanja user
class KeranjangBelanja:
    def __init__(self):
        self.item = []  # nampung produk yang user beli

    def tambah_produk(self, produk: Produk):
        self.item.append(produk)
        print(f"✔ {produk.nama} berhasil ditambahkan!")

    def hapus_produk(self, nama_produk: str):
        for produk in self.item:
            if produk.nama.lower() == nama_produk.lower():
                self.item.remove(produk)
                print(f"✘ {produk.nama} berhasil dihapus!")
                return
        print("⚠ Produk tidak ditemukan.")

    def tampilkan_keranjang(self):
        if not self.item:
            print("🛒 Keranjang masih kosong.")
            return

        print("\n=== Isi Keranjang ===")
        for i, produk in enumerate(self.item, start=1):
            print(f"{i}. {produk}")
        print("=====================\n")

    def hitung_total(self):
        total = sum([p.harga for p in self.item])
        print(f"💰 Total Belanja: Rp{total}")
        return total


# Menu UI — interaksi user disini
def tampilkan_menu():
    print("\nMENU")
    print("1. Lihat Produk Toko")
    print("2. Tambah Produk ke Keranjang")
    print("3. Hapus Produk dari Keranjang")
    print("4. Lihat Keranjang")
    print("5. Hitung Total")
    print("6. Keluar")
    print("#################")


def main():
    toko = Toko()                # objek toko dengan daftar produk siap pakai
    keranjang = KeranjangBelanja()  # keranjang user

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            # user liat dulu produk apa yang ada di toko
            toko.tampilkan_produk()

        elif pilihan == "2":
            toko.tampilkan_produk()
            try:
                nomor = int(input("Masukkan nomor produk yang ingin dibeli: "))
                produk = toko.pilih_produk(nomor)
                if produk:
                    keranjang.tambah_produk(produk)
                else:
                    print("⚠ Nomor produk tidak valid.")
            except ValueError:
                print("⚠ Harus angka!")

        elif pilihan == "3":
            nama = input("Nama produk yang mau dihapus: ")
            keranjang.hapus_produk(nama)

        elif pilihan == "4":
            keranjang.tampilkan_keranjang()

        elif pilihan == "5":
            keranjang.hitung_total()

        elif pilihan == "6":
            print("👋 Makasih sudah belanja! Sampai ketemu lagi!")
            break

        else:
            print("⚠ Pilihan salah!")


if __name__ == "__main__":
    main()
