# Tugas 6 Studi Kasus dengan Python

| | |
|---|---|
| **Nama** | Rifqi Reis Ramadhan |
| **NPM** | G1A025003 |
| **Program Studi** | Teknik Informatika |
| **Universitas** | Universitas Bengkulu |

Repositori ini memuat implementasi 6 studi kasus pemrograman Python. Setiap modul mandiri berada di direktori masing-masing dan dirancang menggunakan pustaka standar bawaan Python (standard library) tanpa memerlukan dependensi eksternal.

## Struktur Direktori

```
studikasus/
├── README.md
├── 01_data_analytics_ai/main.py
├── 02_hpc_infrastructure/main.py
├── 03_gis_career/main.py
├── 04_machine_learning/main.py
├── 05_hci_data_visualization/main.py
└── 06_deforestation_satellite_ai/main.py
```

## Petunjuk Menjalankan Program

Jalankan perintah berikut dari direktori utama tugas menggunakan Python (versi 3.8 atau lebih baru):

```bash
python 01_data_analytics_ai/main.py
python 02_hpc_infrastructure/main.py
python 03_gis_career/main.py
python 04_machine_learning/main.py
python 05_hci_data_visualization/main.py
python 06_deforestation_satellite_ai/main.py
```

---

## 1. Make Sense of Data with Analytics and AI

**Direktori:** `01_data_analytics_ai`

**Kasus:** Analisis tren penjualan produk sentra oleh-oleh khas Bengkulu (Lempuk Durian, Sirup Kalamansi, Kue Tat, Keripik Enggano) selama semester 2 dan proyeksi penjualan bulan berikutnya.

**Cakupan Solusi:**
1. Menghitung ringkasan statistik deskriptif (total, rata-rata, median, standar deviasi).
2. Mengekstraksi insight bisnis: produk terlaris, laju pertumbuhan, dan periode penjualan tertinggi.
3. Memproyeksikan penjualan bulan Januari menggunakan formula regresi linear kuadrat terkecil.
4. Memberikan rekomendasi operasional stok dan strategi pemasaran berdasarkan kemiringan tren.

**Konsep:** Analisis data deskriptif, regresi linear, inferensi berbasis tren.

---

## 2. Bridging Global Infrastructure to Address Local Challenges in HPC

**Direktori:** `02_hpc_infrastructure`

**Kasus:** Simulasi Monte Carlo estimasi probabilitas tanah longsor di 6 titik rawan jalur lintas pegunungan Bengkulu - Kepahiang (kawasan Liku Sembilan) berbasis curah hujan stokastik dan ambang kestabilan lereng.

**Cakupan Solusi:**
1. Menjalankan 3.000.000 iterasi sampel acak per lokasi pemantauan.
2. Mengelompokkan status kerentanan wilayah menjadi TINGGI, SEDANG, dan RENDAH.
3. Melakukan komparasi performa eksekusi mode Serial (single-core) versus mode Paralel (`multiprocessing.Pool`).
4. Menghitung rasio akselerasi komputasi (*speedup*).

**Konsep:** High Performance Computing (HPC), simulasi Monte Carlo, *parallel processing*, *multiprocessing*.

---

## 3. Career and Competition in Industrial Era with GIS

**Direktori:** `03_gis_career`

**Kasus:** Analisis kedekatan spasial dan optimasi pemilihan lokasi magang industri serta karir geospasial bagi lulusan Informatika di wilayah Bengkulu.

**Cakupan Solusi:**
1. Memodelkan data geospasial titik instansi dan mitra industri (koordinat lintang dan bujur).
2. Menghitung jarak geodesik di permukaan bumi menggunakan formula Haversine.
3. Mengkalkulasi orientasi arah mata angin relatif terhadap titik acuan kampus Fakultas Teknik UNIB.
4. Memfilter instansi dalam radius jangkauan prioritas (10 km).
5. Memberikan rekomendasi penempatan terbaik dengan pembobotan nilai insentif berbanding jarak tempuh.

**Konsep:** Sistem Informasi Geografis (GIS), trigonometri sferis (Haversine), penentuan azimuth kompas, analisis kedekatan (*proximity analysis*).

---

## 4. Introduction to Machine Learning

**Direktori:** `04_machine_learning`

**Kasus:** Klasifikasi kelayakan seleksi penerima Beasiswa Prestasi & Talenta Digital Mahasiswa menggunakan algoritma K-Nearest Neighbors (KNN) murni dari nol.

**Cakupan Solusi:**
1. Melakukan pemisahan dataset (*train-test split*) menjadi data latih (70%) dan data uji (30%).
2. Melakukan normalisasi data fitur menggunakan metode *Min-Max Scaling*.
3. Mengembangkan algoritma klasifikasi KNN berbasis jarak Euclidean dan mekanisme *majority voting*.
4. Mengukur performa akurasi pada beberapa nilai parameter K (K = 1, 3, dan 5).
5. Menguji prediksi klasifikasi terhadap berkas pendaftar baru.

**Konsep:** Supervised learning, klasifikasi KNN, normalisasi data, metrik jarak Euclidean, evaluasi model.

---

## 5. Human-Computer Interaction & Data Visualization

**Direktori:** `05_hci_data_visualization`

**Kasus:** Aplikasi terminal interaktif monitor alokasi anggaran dan pengeluaran bulanan mahasiswa yang menerapkan prinsip-prinsip User-Centered Design.

**Fitur:**
- `[1]` Tabel ringkasan pos pengeluaran dan persentase porsi alokasi.
- `[2]` Visualisasi grafik batang horizontal berbasis karakter teks dengan deteksi pos dominan.
- `[3]` Ringkasan statistik (total belanja, rata-rata, pos pengeluaran tertinggi & terendah).
- `[4]` Penambahan atau pembaruan pos anggaran dengan validasi input numerik positif.
- `[5]` Penghapusan pos dengan dialog konfirmasi pencegahan galat (*error prevention*).
- `[0]` Keluar dari program.

**Prinsip HCI:**
- **Konsistensi & visibilitas navigasi:** Struktur menu modular yang mudah dipahami.
- **Umpan balik responsif:** Notifikasi status hasil operasi (`[SUKSES]`, `[PERINGATAN]`, `[INFO]`).
- **Validasi masukan data:** Pencegahan kesalahan input non-numerik dan nilai kosong.
- **Pencegahan kesalahan (*Error Prevention*):** Dialog konfirmasi sebelum aksi penghapusan permanen.

**Konsep:** Desain antarmuka pengguna (CLI), usability, visualisasi data berbasis teks.

---

## 6. Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI

**Direktori:** `06_deforestation_satellite_ai`

**Kasus:** Deteksi spasial kehilangan tutupan kanopi hutan dari citra satelit multispektral (NIR & Red) serta identifikasi faktor penyebab langsung (*direct drivers*) deforestasi di lanskap Bengkulu.

**Cakupan Solusi:**
1. Memodelkan citra satelit simulasi multi-temporal (kondisi sebelum dan sesudah kejadian).
2. Menghitung indeks vegetasi *Normalized Difference Vegetation Index* (NDVI).
3. Mendeteksi piksel perubahan signifikan (*alert*) dengan ambang batas penurunan NDVI > 0.30.
4. Mengelompokkan piksel alert yang bertetangga menjadi kesatuan kluster spasial (*connected-component labeling*).
5. Mengekstraksi karakteristik geometris (luas hektar, rasio aspek, kerapatan poligon, rata-rata residual NDVI).
6. Mengatribusikan penyebab deforestasi menggunakan penalaran berbasis aturan (*rule-based inference*):
   - **Koridor Jalan Angkut:** Geometri linier memanjang dengan rasio aspek tinggi.
   - **Pertambangan Terbuka:** Penurunan ekstrem NDVI (singkapan tanah tandus/batuan).
   - **Perkebunan Kelapa Sawit:** Hamparan luas dengan batas blok rapi teratur.
   - **Perambahan Liar:** Bukaan sporadis berukuran kecil di pedalaman hutan.

**Konsep:** Penginderaan jauh (*remote sensing*), indeks vegetasi NDVI, segmentasi citra, ekstraksi fitur spasial, *rule-based reasoning*.
