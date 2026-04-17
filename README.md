# Refactoring Sistem Validasi Registrasi Mahasiswa

## Analisis Kode Awal

### 1. Pelanggaran SRP (Single Responsibility Principle)
Class `ValidatorManager` menangani lebih dari satu tanggung jawab:
- Validasi jumlah SKS
- Validasi mata kuliah prasyarat

Perubahan pada salah satu aturan validasi dapat memengaruhi logic lainnya.

### 2. Pelanggaran OCP (Open/Closed Principle)
Penambahan aturan validasi baru (misalnya validasi IPK) mengharuskan:
- Mengubah method yang sudah ada
- Menambahkan if/else baru

Class tidak tertutup terhadap perubahan.

### 3. Pelanggaran DIP (Dependency Inversion Principle)
Class `ValidatorManager` bergantung langsung pada:
- Logic konkret validasi
- Tidak menggunakan abstraksi

Hal ini menyebabkan ketergantungan kuat (tight coupling).

---

## Solusi Refactoring

- Setiap jenis validasi dipisah ke class sendiri (SRP)
- Menggunakan interface `IValidationRule` (OCP & DIP)
- `RegistrationService` hanya bergantung pada abstraksi
