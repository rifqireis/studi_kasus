# Nama : Rifqi Reis Ramadhan
# NPM  : G1A025003

import math
import random

DATASET = [
    ([3.85, 92, 9], "Lolos"),
    ([3.70, 88, 8], "Lolos"),
    ([3.45, 85, 7], "Lolos"),
    ([3.60, 90, 8], "Lolos"),
    ([3.90, 95, 10], "Lolos"),
    ([3.30, 82, 6], "Lolos"),
    ([3.55, 86, 7], "Lolos"),
    ([3.20, 80, 7], "Lolos"),
    ([3.75, 91, 9], "Lolos"),
    ([2.80, 60, 3], "Gagal"),
    ([2.65, 55, 2], "Gagal"),
    ([2.95, 68, 4], "Gagal"),
    ([2.40, 50, 2], "Gagal"),
    ([3.05, 62, 3], "Gagal"),
    ([2.50, 58, 1], "Gagal"),
    ([2.70, 65, 4], "Gagal"),
    ([2.30, 45, 1], "Gagal"),
    ([2.85, 59, 2], "Gagal"),
]


def cari_rentang(data):
    kolom = list(zip(*[fitur for fitur, _ in data]))
    return [(min(col), max(col)) for col in kolom]


def transform_minmax(fitur, rentang):
    return [(val - batas[0]) / (batas[1] - batas[0]) for val, batas in zip(fitur, rentang)]


def jarak(titik1, titik2):
    return math.sqrt(sum((a - b)**2 for a, b in zip(titik1, titik2)))


def klasifikasi_knn(data_latih, sample_uji, rentang, k=3):
    sample_norm = transform_minmax(sample_uji, rentang)
    jarak_list = []
    for fitur, label in data_latih:
        dist = jarak(transform_minmax(fitur, rentang), sample_norm)
        jarak_list.append((dist, label))

    jarak_list.sort(key=lambda item: item[0])
    tetangga = [lbl for _, lbl in jarak_list[:k]]
    return max(set(tetangga), key=tetangga.count)


print("=" * 64)
print("KLASIFIKASI KELAYAKAN BEASISWA TALENTA DIGITAL DENGAN KNN")
print("=" * 64)

random.seed(19)
data_acak = DATASET[:]
random.shuffle(data_acak)

split_idx = int(len(data_acak) * 0.7)
latih = data_acak[:split_idx]
uji = data_acak[split_idx:]
rentang_fitur = cari_rentang(latih)

print(f"Jumlah sampel latih : {len(latih)}")
print(f"Jumlah sampel uji   : {len(uji)}\n")

for k_val in (1, 3, 5):
    sukses = sum(klasifikasi_knn(latih, f, rentang_fitur, k_val) == l for f, l in uji)
    akurasi = (sukses / len(uji)) * 100
    print(f"Pengujian K = {k_val} | Tingkat Akurasi: {akurasi:.1f}%")

print("\nDetail Hasil Prediksi Data Uji (K = 3):")
print(f"{'IPK':>5}{'Logika':>8}{'Portofolio':>12}   {'Status Riil':<12}{'Hasil Model':<12}Kesesuaian")
print("-" * 60)
for f, aktual in uji:
    pred = klasifikasi_knn(latih, f, rentang_fitur, k=3)
    evaluasi = "Sesuai" if pred == aktual else "Keliru"
    print(f"{f[0]:>5.2f}{f[1]:>8}{f[2]:>12}   {aktual:<12}{pred:<12}{evaluasi}")

print("\nUji Prediksi Pendaftar Baru:")
pendaftar = [
    ([3.40, 84, 8], "Kandidat A"),
    ([2.75, 58, 3], "Kandidat B"),
    ([3.10, 78, 6], "Kandidat C"),
]
rentang_total = cari_rentang(DATASET)
for atribut, nama in pendaftar:
    keputusan = klasifikasi_knn(DATASET, atribut, rentang_total, k=3)
    print(f"- {nama} (IPK: {atribut[0]}, Tes: {atribut[1]}, Portofolio: {atribut[2]}) -> {keputusan}")
