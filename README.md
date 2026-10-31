# Pertemuan 13 - Debugging, Tracing, dan Testing

**Nama:** Hana Karimah Ghoziyah  
**NIM:** 2225250165  
**Kelas:** 3B

## 1. Tujuan Praktik

Praktik ini bertujuan untuk memahami proses tracing, debugging, dan testing pada program. Kegiatan dilakukan dengan menelusuri jalannya program, menemukan kesalahan, memperbaiki kode, dan menguji kembali hasilnya.

## 2. Tracing Program

Tracing dilakukan dengan mengikuti perubahan nilai variabel selama program dijalankan.

Contoh program:

```python
total = 1

for i in range(1, 5):
    total = total * i

print(total)
```

Tabel tracing:

| Iterasi | Nilai i | Total sebelum | Total sesudah |
|---|---:|---:|---:|
| Awal | - | - | 1 |
| 1 | 1 | 1 | 1 |
| 2 | 2 | 1 | 2 |
| 3 | 3 | 2 | 6 |
| 4 | 4 | 6 | 24 |

**Output:** `24`

Berdasarkan tracing tersebut, nilai `total` berubah pada setiap iterasi hingga menghasilkan 24.

## 3. Bug Report dan Perbaikan

Program yang diuji merupakan program pengolahan nilai mahasiswa yang memiliki tiga fungsi, yaitu menghitung rata-rata nilai, menentukan status kelulusan, dan mencari nilai tertinggi.

### Bug 1: Perhitungan Rata-rata

- Gejala: hasil rata-rata tidak sesuai dengan jumlah data.
- Lokasi: fungsi `hitung_rata_rata()`.
- Penyebab: program membagi jumlah nilai dengan angka tetap 5.
- Perbaikan: mengganti angka 5 dengan `len(nilai)` dan menambahkan penanganan data kosong.

### Bug 2: Status Kelulusan

- Gejala: nilai 60 dinyatakan tidak lulus.
- Lokasi: fungsi `status()`.
- Penyebab: menggunakan operator `>` sehingga nilai harus lebih besar dari 60.
- Perbaikan: mengganti operator `>` menjadi `>=`.

### Bug 3: Nilai Tertinggi

- Gejala: hasil nilai tertinggi selalu 0.
- Lokasi: fungsi `nilai_tertinggi()`.
- Penyebab: menggunakan perbandingan `<` dan nilai awal 0.
- Perbaikan: menggunakan nilai pertama sebagai nilai awal dan mengganti operator `<` menjadi `>`.

## 4. Test Case

| ID | Input | Expected Result |
|---|---|---|
| T1 | Rata-rata `[80, 60, 90, 70]` | 75.0 |
| T2 | Rata-rata `[100, 80]` | 90.0 |
| T3 | Status nilai 60 | Lulus |
| T4 | Status nilai 59 | Tidak lulus |
| T5 | Nilai tertinggi `[80, 60, 90, 70]` | 90 |
| T6 | Rata-rata `[]` | 0 |
| T7 | Nilai tertinggi `[]` | None |

## 5. Hasil Retest

Pengujian ulang dilakukan setelah program diperbaiki untuk memastikan seluruh fungsi berjalan sesuai hasil yang diharapkan. Pengujian dilakukan menggunakan tujuh test case, termasuk pengujian data kosong.

| ID | Expected Result | Actual Result | Status |
|---|---|---|---|
| T1 | 75.0 | 75.0 | PASS |
| T2 | 90.0 | 90.0 | PASS |
| T3 | Lulus | Lulus | PASS |
| T4 | Tidak lulus | Tidak lulus | PASS |
| T5 | 90 | 90 | PASS |
| T6 | 0 | 0 | PASS |
| T7 | None | None | PASS |

Berdasarkan hasil pengujian, seluruh tujuh test case berhasil memperoleh hasil sesuai dengan yang diharapkan. Dengan demikian, perbaikan program tidak menunjukkan adanya kesalahan pada pengujian tersebut.

## 6. Kuis Formatif

**1. Apa perbedaan syntax error, runtime error, dan logical error?**

Syntax error adalah kesalahan penulisan kode. Runtime error terjadi ketika program sedang dijalankan. Logical error terjadi ketika program berjalan, tetapi hasilnya tidak sesuai dengan yang diharapkan.

**2. Apa fungsi traceback?**

Traceback digunakan untuk menunjukkan informasi kesalahan, termasuk lokasi dan urutan pemanggilan fungsi yang menyebabkan error.

**3. Kapan Step Into digunakan?**

Step Into digunakan ketika ingin masuk ke dalam fungsi yang dipanggil dan menelusuri perintah di dalam fungsi tersebut.

**4. Apa perbedaan Step Over dan Step Into?**

Step Over menjalankan satu baris tanpa masuk ke dalam fungsi yang dipanggil. Step Into masuk ke dalam fungsi agar perintah di dalamnya dapat diperiksa.

**5. Mengapa nilai batas perlu dimasukkan dalam test case?**

Nilai batas perlu diuji untuk memastikan program menangani kondisi tepat pada batas dengan benar, misalnya nilai kelulusan 60.

**6. Apa perbedaan expected result dan actual result?**

Expected result adalah hasil yang diharapkan, sedangkan actual result adalah hasil yang benar-benar diperoleh ketika program dijalankan.

**7. Apa yang dimaksud regresi setelah perbaikan?**

Regresi adalah munculnya kembali kesalahan atau munculnya kesalahan baru setelah program diperbaiki.

**8. Mengapa debugging perlu diawali dengan reproduksi masalah?**

Agar kesalahan dapat diamati kembali sehingga penyebabnya lebih mudah ditemukan dan diperiksa.

**9. Mengapa perubahan kode sebaiknya minimal saat memperbaiki bug?**

Agar perbaikan lebih terarah dan mengurangi kemungkinan munculnya kesalahan baru pada bagian lain program.

**10. Apa manfaat commit khusus bertipe fix pada GitHub?**

Commit bertipe fix membantu mencatat perubahan yang dilakukan untuk memperbaiki bug sehingga riwayat perbaikan program lebih mudah ditelusuri.

## 7. Refleksi

Teknik debugging yang paling membantu adalah tracing dan breakpoint karena dapat digunakan untuk mengetahui proses jalannya program serta melihat perubahan nilai variabel. Step Over membantu menjalankan program baris demi baris, sedangkan Step Into dapat digunakan untuk menelusuri perintah di dalam fungsi.

Testing membantu memastikan bahwa program sudah berjalan sesuai harapan setelah diperbaiki. Melalui kegiatan ini, saya belajar menemukan penyebab kesalahan, memperbaiki kode, dan melakukan pengujian ulang.

## 8. Cara Menjalankan Program

Jalankan program melalui terminal VS Code dengan perintah:

```bash
python3 latihan/01_trace_loop.py
python3 latihan/02_trace_fungsi.py
python3 latihan/03_test_case.py
python3 latihan/04_debug_breakpoint.py
python3 praktik/praktik_4_debugging.py
```

Program kasus dapat dijalankan dengan perintah:

```bash
python3 kasus/kasus_01_batas_kelulusan.py
python3 kasus/kasus_02_rata_rata.py
python3 kasus/kasus_03_file_nilai.py
```