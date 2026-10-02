# Laporan Praktikum Sistem Operasi - Modul 1
## Running Modul (Rules & Tools Setup)

### Identitas Praktikan
| Item | Keterangan |
|------|------------|
| **Nama** | Nuevalen Refitra Alswando |
| **NIM** | 103072430008 |
| **Kelas** | IF-04-01 |
| **Asisten Praktikum** | [Isi Nama Asisten Anda] |
| **Tanggal Praktikum** | [Isi Tanggal Praktikum, misal: 12 September 2025] |

---

## 1. Tujuan Praktikum
Berdasarkan modul praktikum Sistem Operasi Semester Ganjil 2025/2026, tujuan dari Modul 1 adalah:
1. Praktikan mengetahui aturan, sistem pelaksanaan, sistem penilaian, dan sanksi pelanggaran selama praktikum di Laboratorium Informatika.
2. Praktikan mengetahui *tools* yang akan digunakan selama 16 pertemuan dan memastikan *tools* tersebut telah terinstal serta berfungsi dengan baik untuk mengurangi kendala teknis.

---

## 2. Persiapan Tools
Sebelum memulai praktikum, dilakukan pengecekan dan instalasi *tools* wajib yang akan digunakan selama praktikum Sistem Operasi, yaitu:

### 2.1 Oracle VM VirtualBox
Virtualisasi yang digunakan untuk menjalankan sistem operasi tamu (Ubuntu dan Xinu).
- **Status:** Terinstall
- **Versi:** [Isi Versi VirtualBox Anda, misal: 6.1.x] *(Sesuai rekomendasi modul)*
- **Link Download:** [virtualbox.org](https://www.virtualbox.org/wiki/Download_Old_Builds)

### 2.2 Xinu OS
Sistem operasi *embedded* yang akan dipelajari. File berformat `.ova` yang akan diimpor menjadi *Virtual Machine* pada modul selanjutnya.
- **Status:** File `.ova` telah diunduh
- **Lokasi File:** `C:/` (atau direktori yang ditentukan)
- **Link Download:** [Xinu Book and Code](https://www.cs.purdue.edu/homes/comer/downloads/Xinu_Book_And_Code/VirtualBox/)

### 2.3 Ubuntu
Sistem operasi Linux yang dijalankan di dalam VirtualBox sebagai lingkungan pengembangan (*Development-System*).
- **Status:** Terinstall dan dapat dijalankan di VirtualBox
- **Password Lab PC:** `praktikan`

### 2.4 Sourcetrail
*Software cross-platform* untuk mengeksplorasi dan memahami *source code* C/C++ secara visual.
- **Status:** Terinstall
- **Link Download:** [Sourcetrail Releases](https://github.com/CoatiSoftware/Sourcetrail/releases)

---

## 3. Langkah Kerja
Berikut adalah langkah-langkah yang dilakukan selama praktikum Modul 1:

1. **Briefing Aturan Praktikum**
   - Mendengarkan penjelasan asisten mengenai tata tertib laboratorium di Gedung TULT Lantai 6 & 7.
   - Memahami sistem penilaian, kewajiban kehadiran minimal 75%, aturan keterlambatan (≤ 5 menit diperbolehkan, ≥ 30 menit tidak diperbolehkan), dan sanksi pelanggaran (misal: pengurangan nilai 20% jika lupa menghapus file).
   - Memahami alur 16 modul praktikum, mulai dari Instalasi Xinu hingga Keamanan Linux.

2. **Pengecekan dan Instalasi VirtualBox**
   - Memastikan Oracle VM VirtualBox sudah terinstal di komputer laboratorium/personal.
   - Jika belum, melakukan unduh dan instalasi versi 6.1 sesuai panduan modul.

3. **Persiapan File Xinu OS**
   - Mengunduh file `xinu-vbox-appliances.tar.gz` atau file `.ova` dari link yang disediakan.
   - Mengekstrak file tersebut dan memastikan file `development-system.ova` dan `backend.ova` tersedia.

4. **Pengecekan Ubuntu**
   - Membuka aplikasi VirtualBox dan menjalankan *Virtual Machine* Ubuntu.
   - Melakukan *login* menggunakan password `praktikan` untuk memastikan VM berjalan normal.

5. **Instalasi Sourcetrail**
   - Mengunduh *installer* Sourcetrail.
   - Melakukan instalasi dan membuka aplikasi untuk memastikan *software* dapat berjalan sebagai persiapan membaca *source code* Xinu di Modul 4.

---

## 4. Hasil dan Pembahasan

### 4.1 Tampilan Oracle VM VirtualBox
Berikut adalah tampilan awal Oracle VM VirtualBox Manager yang telah terinstal dengan baik. Terlihat daftar *Virtual Machine* (termasuk Ubuntu) yang siap digunakan.

![Tampilan VirtualBox](assets/virtualbox_home.png)  
*Gambar 1: Tampilan awal Oracle VM VirtualBox Manager.*

### 4.2 Ketersediaan File Xinu OS
File image Xinu (`.ova`) telah berhasil diunduh dan disimpan di direktori yang sesuai (misalnya drive `C:/`) sebagai persiapan untuk proses *Import Appliance* pada Modul 2.

![File Xinu OS](assets/xinu_ova_file.png)  
*Gambar 2: Tampilan direktori yang berisi file `development-system.ova` dan `backend.ova`.*

### 4.3 Tampilan Ubuntu yang Berjalan
Berikut adalah tangkapan layar saat *Virtual Machine* Ubuntu dijalankan di dalam VirtualBox. Proses *login* berhasil dilakukan menggunakan password `praktikan`, menandakan lingkungan pengembangan siap digunakan.

![Tampilan Ubuntu](assets/ubuntu_running.png)  
*Gambar 3: Tampilan desktop Ubuntu yang berjalan di dalam VirtualBox.*

### 4.4 Verifikasi Instalasi Sourcetrail
Berikut adalah tangkapan layar aplikasi Sourcetrail yang telah berhasil diinstal. *Software* ini akan digunakan untuk menavigasi dan memahami struktur *source code* Xinu yang kompleks pada modul selanjutnya.

![Tampilan Sourcetrail](assets/sourcetrail_home.png)  
*Gambar 4: Tampilan antarmuka Sourcetrail saat pertama kali dibuka.*

---

## 5. Kesimpulan
Berdasarkan praktikum Modul 1 ini, dapat disimpulkan bahwa:
1. Praktikan telah memahami aturan main, sistem penilaian, tata tertib, dan sanksi yang berlaku di Laboratorium Informatika Universitas Telkom (Gedung TULT Lantai 6 & 7).
2. Keempat *tools* utama praktikum, yaitu **Oracle VM VirtualBox**, **File Xinu OS (.ova)**, **Ubuntu**, dan **Sourcetrail**, telah berhasil diverifikasi keberadaannya dan berfungsi dengan baik.
3. Kesiapan *tools* ini sangat penting sebagai fondasi untuk kelancaran praktikum pada Modul 2 (Instalasi Xinu) dan modul-modul selanjutnya yang berfokus pada eksplorasi kernel, proses, dan sinkronisasi.

---