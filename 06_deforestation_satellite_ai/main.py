# Nama : Rifqi Reis Ramadhan
# NPM  : G1A025003

import random

random.seed(42)
DIMENSI = 20


def hitung_ndvi(nir, red):
    return (nir - red) / (nir + red)


def generate_citra_awal():
    return [[(random.uniform(0.48, 0.58), random.uniform(0.04, 0.08)) for _ in range(DIMENSI)]
            for _ in range(DIMENSI)]


def injeksi_gangguan(grid, baris_range, kolom_range, target_nir, target_red):
    for r in baris_range:
        for c in kolom_range:
            grid[r][c] = (
                target_nir + random.uniform(-0.02, 0.02),
                target_red + random.uniform(-0.01, 0.01)
            )


t0_citra = generate_citra_awal()
t1_citra = [baris[:] for baris in t0_citra]

injeksi_gangguan(t1_citra, range(1, 8), range(2, 8), 0.26, 0.13)      # Blok teratur -> Perkebunan Kelapa Sawit
injeksi_gangguan(t1_citra, [4], range(11, 19), 0.24, 0.16)           # Pola linear memanjang -> Koridor Jalan Angkut
injeksi_gangguan(t1_citra, range(13, 19), range(3, 9), 0.11, 0.12)    # Lahan terbuka galian tandus -> Pertambangan Terbuka
injeksi_gangguan(t1_citra, range(10, 12), range(13, 15), 0.23, 0.11)  # Spot kecil terisolasi -> Perambahan Liar

AMBANG_PENURUNAN = 0.30
mask_alert = [
    [hitung_ndvi(*t0_citra[r][c]) - hitung_ndvi(*t1_citra[r][c]) > AMBANG_PENURUNAN for c in range(DIMENSI)]
    for r in range(DIMENSI)
]


def identifikasi_kluster(mask):
    terekam = set()
    daftar_kluster = []
    for r in range(DIMENSI):
        for c in range(DIMENSI):
            if mask[r][c] and (r, c) not in terekam:
                antrean = [(r, c)]
                terekam.add((r, c))
                anggota = []
                while antrean:
                    curr_r, curr_c = antrean.pop()
                    anggota.append((curr_r, curr_c))
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < DIMENSI and 0 <= nc < DIMENSI:
                            if mask[nr][nc] and (nr, nc) not in terekam:
                                terekam.add((nr, nc))
                                antrean.append((nr, nc))
                daftar_kluster.append(anggota)
    return daftar_kluster


def ekstrak_geometri(piksel_list):
    baris_list = [p[0] for p in piksel_list]
    kolom_list = [p[1] for p in piksel_list]
    h = max(baris_list) - min(baris_list) + 1
    w = max(kolom_list) - min(kolom_list) + 1
    return {
        "luas_hektar": len(piksel_list) * 0.09,
        "rasio_aspek": max(h, w) / min(h, w),
        "densitas": len(piksel_list) / (h * w),
        "rerata_ndvi": sum(hitung_ndvi(*t1_citra[y][x]) for y, x in piksel_list) / len(piksel_list),
        "titik_tengah": (sum(baris_list) // len(baris_list), sum(kolom_list) // len(kolom_list))
    }


def klasifikasi_pemicu(geo):
    if geo["rasio_aspek"] >= 4.0:
        return "Koridor Jalan Angkut", "Bentuk geometri linier memanjang"
    if geo["rerata_ndvi"] < 0.12:
        return "Pertambangan Terbuka", "NDVI anjlok ekstrem (singkapan tanah/batuan)"
    if geo["luas_hektar"] >= 3.0 and geo["densitas"] > 0.85:
        return "Perkebunan Kelapa Sawit", "Hamparan luas dengan batas blok teratur"
    return "Perambahan Liar", "Bukaan sporadis skala kecil di pedalaman"


print("=" * 72)
print("SISTEM DETEKSI DAN ATRIBUSI DEFORESTASI SATELIT (KAWASAN BENGKULU)")
print("=" * 72)

print("Matriks Deteksi Perubahan Tutupan Kanopi (. = Utuh, # = Alert):\n")
for baris in mask_alert:
    print("  " + " ".join("#" if cell else "." for cell in baris))

kluster_deforestasi = identifikasi_kluster(mask_alert)
print(f"\nTeridentifikasi {len(kluster_deforestasi)} kluster perubahan tutupan lahan:\n")
print(f"{'No':<4}{'Centroid':<11}{'Luas (Ha)':>10}{'Rerata NDVI':>13}   {'Prediksi Driver':<25}Karakteristik")
print("-" * 88)

total_luasan = 0.0
for i, kluster in enumerate(kluster_deforestasi, 1):
    ciri = ekstrak_geometri(kluster)
    label, keterangan = klasifikasi_pemicu(ciri)
    total_luasan += ciri["luas_hektar"]
    print(f"{i:<4}{str(ciri['titik_tengah']):<11}{ciri['luas_hektar']:>8.2f} ha"
          f"{ciri['rerata_ndvi']:>12.2f}   {label:<25}{keterangan}")

cakupan_total = (DIMENSI * DIMENSI) * 0.09
print(f"\nAkumulasi deforestasi terdeteksi : {total_luasan:.2f} ha dari total pantauan {cakupan_total:.1f} ha")
