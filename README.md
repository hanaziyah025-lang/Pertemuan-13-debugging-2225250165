# Pertemuan 13 - Debugging dan Testing

Nama: Hana Karimah Ghoziyah  
NIM: 2225250165  
Kelas: 3B

## Kasus

Program yang diuji adalah program pengolahan nilai mahasiswa yang memiliki tiga fungsi, yaitu menghitung rata-rata nilai, menentukan status kelulusan, dan mencari nilai tertinggi.

Pengujian dilakukan untuk menemukan kesalahan pada program, memperbaiki kesalahan, dan menguji kembali hasilnya.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| T1 | [80, 60, 90, 70] | 75.0 | 60.0 | Gagal |
| T2 | [100, 80] | 90.0 | 36.0 | Gagal |
| T3 | 60 | Lulus | Tidak lulus | Gagal |
| T4 | 59 | Tidak lulus | Tidak lulus | Lulus |
| T5 | [80, 60, 90, 70] | 90 | 0 | Gagal |

## Bug Report

### 1. Bug Perhitungan Rata-rata
- Gejala: Hasil rata-rata tidak sesuai dengan jumlah data.
- Lokasi: Fungsi `hitung_rata_rata()`.
- Akar penyebab: Program membagi jumlah nilai dengan angka tetap 5.
- Perbaikan: Mengganti angka 5 dengan `len(nilai)`.

### 2. Bug Status Kelulusan
- Gejala: Nilai 60 dinyatakan tidak lulus.
- Lokasi: Fungsi `status()`.
- Akar penyebab: Menggunakan operator `>` sehingga nilai harus lebih besar dari 60.
- Perbaikan: Mengganti operator `>` menjadi `>=`.

### 3. Bug Nilai Tertinggi
- Gejala: Hasil nilai tertinggi selalu 0.
- Lokasi: Fungsi `nilai_tertinggi()`.
- Akar penyebab: Menggunakan perbandingan `<` dan nilai awal 0.
- Perbaikan: Menggunakan nilai pertama sebagai nilai awal dan mengganti operator `<` menjadi `>`.

## Retest

Setelah program diperbaiki, dilakukan pengujian ulang menggunakan lima test case.

| ID | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|
| T1 | 75.0 | 75.0 | Berhasil |
| T2 | 90.0 | 90.0 | Berhasil |
| T3 | Lulus | Lulus | Berhasil |
| T4 | Tidak lulus | Tidak lulus | Berhasil |
| T5 | 90 | 90 | Berhasil |

Seluruh lima test case berhasil dijalankan dengan hasil sesuai harapan.

## Cara Menjalankan

Jalankan perintah berikut melalui terminal:

```bash
python3 praktik/praktik_4_debugging.py