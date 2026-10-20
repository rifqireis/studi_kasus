# Nama : Rifqi Reis Ramadhan
# NPM  : G1A025003

import statistics

penjualan = {
    "Lempuk Durian":   [115, 128, 142, 156, 175, 198],
    "Sirup Kalamansi": [85, 90, 94, 98, 104, 112],
    "Kue Tat":         [150, 145, 155, 152, 148, 153],
    "Keripik Enggano": [70, 68, 62, 58, 55, 48],
}
periode = ["Jul", "Agu", "Sep", "Okt", "Nov", "Des"]


def hitung_regresi(data_y):
    x = list(range(1, len(data_y) + 1))
    x_bar = statistics.mean(x)
    y_bar = statistics.mean(data_y)
    pembilang = sum((xi - x_bar) * (yi - y_bar) for xi, yi in zip(x, data_y))
    penyebut = sum((xi - x_bar) ** 2 for xi in x)
    b = pembilang / penyebut
    a = y_bar - (b * x_bar)
    return a, b


print("=" * 62)
print("ANALISIS PENJUALAN SENTRA OLEH-OLEH KHAS BENGKULU (SEMESTER 2)")
print("=" * 62)

print("\n1. Statistik Ringkasan Penjualan")
print(f"{'Produk':<18}{'Total':>7}{'Rata-rata':>11}{'Median':>9}{'Stdev':>8}")
print("-" * 53)
for nama, data in penjualan.items():
    print(f"{nama:<18}{sum(data):>7}{statistics.mean(data):>11.1f}"
          f"{statistics.median(data):>9.1f}{statistics.stdev(data):>8.1f}")

print("\n2. Evaluasi Kinerja Produk")
tertinggi = max(penjualan, key=lambda k: sum(penjualan[k]))
print(f"- Produk paling laris akumulatif : {tertinggi} ({sum(penjualan[tertinggi])} kemasan)")

for nama, data in penjualan.items():
    persen = ((data[-1] - data[0]) / data[0]) * 100
    print(f"- Tren pertumbuhan {nama:<16}: {persen:>+6.1f}% (Jul ke Des)")

total_per_bulan = [sum(penjualan[p][i] for p in penjualan) for i in range(len(periode))]
idx_puncak = total_per_bulan.index(max(total_per_bulan))
print(f"- Bulan penjualan puncak : {periode[idx_puncak]} ({max(total_per_bulan)} item terjual)")

print("\n3. Proyeksi Penjualan Bulan Januari (Regresi Linear)")
for nama, data in penjualan.items():
    a, b = hitung_regresi(data)
    t_lanjut = len(data) + 1
    estimasi = a + (b * t_lanjut)
    arah = "meningkat" if b > 1 else "menurun" if b < -1 else "stagnan"
    print(f"- {nama:<17}: {estimasi:>5.0f} unit (kecenderungan {arah}, {b:+.2f}/bln)")

print("\n4. Rekomendasi Kebijakan Pengadaan & Promosi")
for nama, data in penjualan.items():
    _, b = hitung_regresi(data)
    if b > 4:
        print(f"* {nama}: Permintaan tinggi, prioritaskan pasokan stok tambahan.")
    elif b < 0:
        print(f"* {nama}: Permintaan menurun, evaluasi ulang harga atau adakan bundling diskon.")
    else:
        print(f"* {nama}: Penjualan stabil, pertahankan jumlah pasokan saat ini.")
