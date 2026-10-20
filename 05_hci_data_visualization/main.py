# Nama : Rifqi Reis Ramadhan
# NPM  : G1A025003

anggaran = {
    "Kost & Kamar":      750,
    "Konsumsi Harian":   950,
    "Kuota Internet":    120,
    "Transportasi":      180,
    "Modul & Fotokopi":   90,
    "Kebutuhan Pribadi": 210,
}


def tampilkan_tabel():
    if not anggaran:
        print("\n[INFO] Belum ada data pengeluaran yang tercatat.")
        return

    total = sum(anggaran.values())
    print("\n" + "-" * 52)
    print(f"{'No':<4}{'Kategori Pengeluaran':<24}{'Jumlah (Ribu)':>14}{'Porsi':>10}")
    print("-" * 52)
    for i, (kategori, nominal) in enumerate(anggaran.items(), 1):
        rasio = (nominal / total) * 100
        print(f"{i:<4}{kategori:<24}Rp {nominal:>9,}{rasio:>9.1f}%")
    print("-" * 52)
    print(f"{'Total Pengeluaran':<28}Rp {total:>9,}{'100.0%':>10}")


def visualisasi_grafik():
    if not anggaran:
        print("\n[INFO] Data kosong, tidak dapat membuat grafik.")
        return

    total = sum(anggaran.values())
    print("\nGrafik Batang Alokasi Pengeluaran (1 '#' = 25 ribu rupiah):")
    for kategori, nominal in sorted(anggaran.items(), key=lambda x: x[1], reverse=True):
        panjang_batang = nominal // 25
        bar = "#" * panjang_batang
        flag = " [Dominan]" if (nominal / total) >= 0.25 else ""
        print(f"{kategori:<19} | {bar:<42} Rp {nominal:,}k{flag}")


def statistik_anggaran():
    if not anggaran:
        print("\n[INFO] Data tidak tersedia.")
        return

    total = sum(anggaran.values())
    rerata = total / len(anggaran)
    maks_kat = max(anggaran, key=lambda k: anggaran[k])
    min_kat = min(anggaran, key=lambda k: anggaran[k])

    print("\nRingkasan Statistik Anggaran:")
    print(f"- Total belanja bulanan : Rp {total:,} ribu")
    print(f"- Rata-rata per pos     : Rp {rerata:,.1f} ribu")
    print(f"- Pos belanja terbesar  : {maks_kat} (Rp {anggaran[maks_kat]:,} ribu)")
    print(f"- Pos belanja terhemat  : {min_kat} (Rp {anggaran[min_kat]:,} ribu)")


def tambah_ubah_pos():
    nama = input("Nama pos pengeluaran : ").strip()
    if not nama:
        print("[PERINGATAN] Nama pos tidak boleh dibiarkan kosong.")
        return

    input_nominal = input("Nominal biaya (dalam ribu Rp) : ").strip()
    if not input_nominal.isdigit() or int(input_nominal) <= 0:
        print("[PERINGATAN] Nominal harus berupa angka bulat positif.")
        return

    nilai = int(input_nominal)
    anggaran[nama] = nilai
    print(f"[SUKSES] Pos '{nama}' sebesar Rp {nilai:,} ribu berhasil disimpan.")


def hapus_pos():
    nama = input("Masukkan pos yang ingin dihapus : ").strip()
    if nama not in anggaran:
        print(f"[PERINGATAN] Pos '{nama}' tidak terdaftar dalam data.")
        return

    konfirmasi = input(f"Apakah yakin ingin menghapus pos '{nama}'? (y/n): ").strip().lower()
    if konfirmasi == "y":
        del anggaran[nama]
        print(f"[SUKSES] Pos '{nama}' berhasil dihapus.")
    else:
        print("[INFO] Operasi penghapusan dibatalkan.")


AKSI = {
    "1": ("Tampilkan tabel pengeluaran", tampilkan_tabel),
    "2": ("Lihat grafik batang alokasi", visualisasi_grafik),
    "3": ("Ringkasan statistik anggaran", statistik_anggaran),
    "4": ("Tambah / ubah pos pengeluaran", tambah_ubah_pos),
    "5": ("Hapus pos pengeluaran", hapus_pos),
}

while True:
    print("\n" + "=" * 46)
    print("   MONITOR ANGGARAN & PENGELUARAN MAHASISWA   ")
    print("=" * 46)
    for kode, (label, _) in AKSI.items():
        print(f" [{kode}] {label}")
    print(" [0] Selesai / Keluar")

    opsi = input("\nPilih opsi [0-5]: ").strip()
    if opsi == "0":
        print("\nSesi selesai. Program ditutup.")
        break
    elif opsi in AKSI:
        AKSI[opsi][1]()
    else:
        print("[PERINGATAN] Menu tidak valid. Silakan pilih antara 0 hingga 5.")
