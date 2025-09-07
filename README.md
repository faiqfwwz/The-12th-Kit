# The 12th Kit
The 12th player's kit.

### Author
- Name: Ahmad Faiq Fawwaz Abdussalam
- NPM: 2406397706
- Class: PBP C

### Deployment
You can access the web here: [The 12th Kit Web](https://ahmad-faiq41-the12thkit.pbp.cs.ui.ac.id/)

---

## Tugas Individu 2 - PBP Ganjil 2025/2026

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. **Membuat sebuah proyek Django baru.**
   - Membuat direktori baru yaitu direktori The-12th-Kit dan inisiasi proyek Django dengan menjalankan `django-admin startproject the_12th_kit .`.

2. **Membuat aplikasi dengan nama `main` pada proyek tersebut.**
   - Setelah inisiasi proyek Django, buat aplikasi `main` dengan menjalankan `python manage.py startapp main`.

3. **Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.**
   - Buka `settings.py` dalam direktori proyek `the_12th_kit`, kemudian tambahkan `main` ke dalam variabel `INSTALLED_APPS`.

4. **Membuat model pada aplikasi `main` dengan nama `Product`.**
   - Pada `models.py` di dalam aplikasi `main`, buat model `Product` yang memiliki atribut `name`,`price`,`description`,`thumbnail`,`category`, dan `is_featured`.

5. **Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML yang menampilkan nama aplikasi serta nama dan kelas.**
   - Pada `views.py`, buat fungsi bernama `show_main` yang akan *render template* HTML yang berisi nama aplikasi, nama lengkap, dan kelas.

6. **Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.**
   - Pada `urls.py` di dalam aplikasi `main`, tambahkan rute baru dengan menambahkan `path('', show_main, name='show_main')` ke dalam `urlpatterns` yang akan memetakan URL ke fungsi yang udah dibuat di `views.py`.

7. **Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**
   - Setelah aplikasi dibuat dan siap untuk di-*deploy*, lakukan *deployment* ke proyek yang sudah dibuat di Pacil Web Service (PWS).

8. **Membuat sebuah `README.md` yang berisi tautan menuju aplikasi PWS yang sudah di-*deploy*, serta jawaban dari beberapa pertanyaan berikut.**
   - Terakhir, buat `README.md` yang berisi tautan dan penjelasan dari beberapa pertanyaan.