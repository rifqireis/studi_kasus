# Nama : Rifqi Reis Ramadhan
# NPM  : G1A025003

import math

TITIK_ACUAN = ("Fakultas Teknik Universitas Bengkulu", -3.7583, 102.2745)

MITRA_GIS = [
    {"nama": "Studio Geodesi Pemetaan",   "bidang": "Drone Mapping Specialist", "lat": -3.7712, "lon": 102.2710, "insentif": 7_500_000},
    {"nama": "Kantor ATR/BPN Bengkulu",   "bidang": "Cadastral Surveyor",       "lat": -3.7932, "lon": 102.2641, "insentif": 5_000_000},
    {"nama": "DLHK Provinsi Bengkulu",    "bidang": "Forestry GIS Analyst",     "lat": -3.8050, "lon": 102.2850, "insentif": 5_800_000},
    {"nama": "Bappeda Provinsi Bengkulu", "bidang": "Spatial Database Admin",   "lat": -3.8185, "lon": 102.2980, "insentif": 5_500_000},
    {"nama": "BWS Sumatera VII",          "bidang": "GIS Hydrologist",          "lat": -3.8310, "lon": 102.3125, "insentif": 6_200_000},
    {"nama": "PT Palma Agro Lestari",     "bidang": "Smart Plantation GIS",     "lat": -3.4210, "lon": 102.5800, "insentif": 8_500_000},
]


def jarak_haversine(lat1, lon1, lat2, lon2):
    r = 6371.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lam = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lam / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return r * c


def hitung_arah(lat1, lon1, lat2, lon2):
    kompas = ["Utara", "Timur Laut", "Timur", "Tenggara", "Selatan", "Barat Daya", "Barat", "Barat Laut"]
    d_lon = lon2 - lon1
    d_lat = lat2 - lat1
    derajat = (math.degrees(math.atan2(d_lon, d_lat)) + 360) % 360
    return kompas[int((derajat + 22.5) // 45) % 8]


print("=" * 75)
print("ANALISIS SPASIAL PELUANG KARIR & MAGANG GEOSPASIAL (GIS) BENGKULU")
print("=" * 75)
print(f"Basis Lokasi : {TITIK_ACUAN[0]} [{TITIK_ACUAN[1]}, {TITIK_ACUAN[2]}]\n")

for mitra in MITRA_GIS:
    mitra["jarak"] = jarak_haversine(TITIK_ACUAN[1], TITIK_ACUAN[2], mitra["lat"], mitra["lon"])
    mitra["orientasi"] = hitung_arah(TITIK_ACUAN[1], TITIK_ACUAN[2], mitra["lat"], mitra["lon"])
    mitra["skor"] = (mitra["insentif"] / 1_000_000) - (mitra["jarak"] * 0.12)

print(f"{'Instansi / Perusahaan':<27}{'Posisi':<25}{'Jarak':>9}  {'Arah':<11}{'Insentif':>13}")
print("-" * 88)
for m in sorted(MITRA_GIS, key=lambda x: x["jarak"]):
    print(f"{m['nama']:<27}{m['bidang']:<25}{m['jarak']:>6.2f} km  {m['orientasi']:<11}Rp{m['insentif']:>11,}")

BATAS_RADIUS = 10.0
print(f"\nLokasi Prioritas (Radius <= {BATAS_RADIUS:.0f} km):")
for m in MITRA_GIS:
    if m["jarak"] <= BATAS_RADIUS:
        print(f"- {m['nama']} ({m['bidang']}) -> {m['jarak']:.2f} km")

terbaik = max(MITRA_GIS, key=lambda x: x["skor"])
print(f"\nRekomendasi Pilihan Teratas : {terbaik['bidang']} di {terbaik['nama']}")
print(f"Koordinat Tautan            : https://www.google.com/maps?q={terbaik['lat']},{terbaik['lon']}")
