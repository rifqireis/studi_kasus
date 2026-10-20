# Nama : Rifqi Reis Ramadhan
# NPM  : G1A025003

import multiprocessing as mp
import random
import time

TITIK_PEMANTAUAN = {
    "Liku Sembilan Atas":   (62, 65),
    "Liku Sembilan Bawah":  (57, 68),
    "Tanjung Heran KM 38":  (53, 70),
    "Taba Penanjung":       (46, 74),
    "Perbatasan Kepahiang": (50, 72),
    "Ujung Karang":         (38, 80),
}

ITERASI = 3_000_000


def hitung_risiko_longsor(parameter):
    lokasi, rerata_hujan, ambang_batas, total_sample, seed = parameter
    rng = random.Random(seed)
    kejadian = 0
    for _ in range(total_sample):
        curah = rng.expovariate(1.0 / rerata_hujan)
        if curah > ambang_batas:
            kejadian += 1
    probabilitas = (kejadian / total_sample) * 100
    return lokasi, probabilitas


def siapkan_pekerjaan():
    return [
        (lokasi, hujan, ambang, ITERASI, idx)
        for idx, (lokasi, (hujan, ambang)) in enumerate(TITIK_PEMANTAUAN.items())
    ]


if __name__ == "__main__":
    print("=" * 66)
    print("SIMULASI RISIKO LONGSOR JALUR BENGKULU - KEPAHIANG (HPC BENCHMARK)")
    print("=" * 66)
    print(f"Core CPU aktif        : {mp.cpu_count()}")
    print(f"Sampel Monte Carlo    : {ITERASI:,} per titik\n")

    t0 = time.perf_counter()
    hasil_serial = [hitung_risiko_longsor(item) for item in siapkan_pekerjaan()]
    durasi_serial = time.perf_counter() - t0

    t1 = time.perf_counter()
    with mp.Pool() as pool:
        hasil_paralel = pool.map(hitung_risiko_longsor, siapkan_pekerjaan())
    durasi_paralel = time.perf_counter() - t1

    print(f"{'Titik Lokasi':<24}{'Peluang Longsor':>17}   Tingkat Risiko")
    print("-" * 58)
    for lokasi, prob in sorted(hasil_paralel, key=lambda x: x[1], reverse=True):
        kategori = "TINGGI" if prob >= 30 else "SEDANG" if prob >= 20 else "RENDAH"
        print(f"{lokasi:<24}{prob:>16.2f}%   {kategori}")

    print("\nHasil Benchmarking Komputasi")
    print(f"- Waktu eksekusi serial  : {durasi_serial:.2f} detik")
    print(f"- Waktu eksekusi paralel : {durasi_paralel:.2f} detik")
    print(f"- Akselerasi (Speedup)   : {durasi_serial / durasi_paralel:.2f}x lipat")
    print(f"- Validasi konsistensi   : {'Valid' if hasil_serial == hasil_paralel else 'Tidak Sesuai'}")
