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

### Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
![Django Flow](https://github.com/user-attachments/assets/dc4cf68b-9e91-4f61-930c-3f0a1e788d76)

### Jelaskan peran `settings.py` dalam proyek Django!

Dalam proyek Django, `settings.py` berperan sebagai pusat konfigurasi yang mengatur jalannya aplikasi. File ini berisi pengaturan penting seperti `DEBUG`, `ALLOWED_HOSTS`, `INSTALLED_APPS`, `MIDDLEWARE`, serta konfigurasi *database*. Singkatnya, `settings.py` adalah “otak” proyek Django yang mengendalikan hampir semua aspek teknis aplikasi agar dapat berjalan sesuai kebutuhan.

### Bagaimana cara kerja migrasi database di Django?

Migrasi di Django adalah mekanisme sinkronisasi antara model (`models.py`) dengan struktur *database*. Pertama `makemigrations` menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam *database*. Lalu `migrate` akan mengaplikasikan perubahan model yang ada di dalam berkas migrasi ke *database*.

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django sering dipakai sebagai permulaan pembelajaran karena mudah, lengkap, dan terstruktur. Django dibuat dengan bahasa Python yang gampang dipahami oleh pemula, *framework* yang sudah menyediakan banyak fitur bawaan sehingga kita bisa fokus ke pengembangan, pola MVT (Model-View-Template) yang terstruktur, serta dokumentasi yang jelas dan komunitas yang besar.

### Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Tidak ada.