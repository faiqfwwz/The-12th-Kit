# The 12th Kit
The 12th player's kit.

### Author
- Name: Ahmad Faiq Fawwaz Abdussalam
- NPM: 2406397706
- Class: PBP C

### Deployment
You can access the web here: [The 12th Kit Web](https://ahmad-faiq41-the12thkit.pbp.cs.ui.ac.id/)

### Archive
<details>
<summary>Tugas Individu 2</summary>

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
</details>

---

## Tugas Individu 3 - PBP Ganjil 2025/2026

### Jelaskan mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?

*Data delivery* sangat penting dalam pengimplementasian sebuah platform karena memastikan data mengalir tepat waktu, efisien, dan aman antar komponen platform. Tanpa *data delivery* platform tidak dapat berfungsi secara maksimal, karena data yang dibutuhkan tidak dapat dialirkan/dikirimkan dengan benar.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Keduanya digunakan untuk pertukaran data dan pada dasarnya tidak ada yang absolut lebih baik. Namun, JSON kerap dipandang lebih unggul daripada XML sehingga lebih populer karena alasan berikut:

   - **Keringkasan**: Struktur JSON umumnya lebih padat dibanding XML (tanpa tag pembuka/penutup), sehingga lebih mudah dibaca dan ditulis.
   - **Integrasi dengan JavaScript**: Representasi JSON cocok dengan objek dan *array* di JavaScript, sehingga implementasinya dalam pengembangan *web* menjadi lebih sederhana.
   - ***Parsing* lebih cepat**: Proses baca JSON umumnya lebih singkat, cocok untuk kebutuhan *real-time*.

### Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Fungsi *method* `is_valid()` adalah memastikan data yang di-*input* pengguna melalui *form* sudah valid. *Method* ini akan mengecek data yang di-*input* sudah sesuai ketentuan yang telah ditentukan (misalnya nama tidak boleh melebihi panjang maksimal). Tanpa `is_valid()` kita tidak bisa memastikan data yang masuk ke *database* itu aman dan valid. Oleh karena itu, *method* ini penting untuk menjaga keamanan aplikasi dan integritas data.

### Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` bertujuan untuk mencegah serangan CSRF (Cross-Site Request Forgery), yaitu serangan siber di mana penyerang membuat pengguna yang terautentikasi untuk mengirimnkan *request* yang berbahaya. Tanpa `csrf_token`, penyerang bisa manipulasi *form* untuk melakukan aksi yang berbahaya seperti mengubah data. Oleh karena itu, `csrf_token` penting untuk mendeteksi *request* yang diterima benar-benar berasal dari pengguna yang sah.

### Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).

1. **Membuat *form* untuk menambahkan produk baru**
   - Buat berkas `forms.py` pada direktori `main` 
      ```python
      from django.forms import ModelForm
      from main.models import Product

      class ProductForm(ModelForm):
         class Meta:
            model = Product
            fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "stock", "brand", "league", "team", "season"]
      ```
   - Buat fungsi baru di `views.py` untuk input *form*
      ```python
      def create_product(request):
         form = ProductForm(request.POST or None)

         if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

         context = {'form': form}
         return render(request, "create_product.html", context)

      def show_product(request, id):
         product = get_object_or_404(Product, id=id)

         context = {
            'product' : product
         }

      return render(request, "product_detail.html", context)
      ```
   - Tambahkan path URL di `urls.py`
      ```python
      from django.urls import path
      from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id

      app_name = 'main'

      urlpatterns = [
         path('', show_main, name='show_main'),
         path('create-product/', create_product, name='create_product'),
         path('product/<str:id>/', show_product, name='show_product'),
      ]
      ```
   - Modifikasi template `main.html`, kemudian buat `create_product.html` dan `product_detail.html`

2. **Buat 4 fungsi untuk melihat produk yang sudah ditambahkan dalam format XML, JSON, XML by *ID*, dan JSON by *ID***

   - Buat 4 fungsi baru di `views.py`
      ```python
      def show_xml(request):
         product_list = Product.objects.all()
         xml_data = serializers.serialize("xml", product_list)
         return HttpResponse(xml_data, content_type="application/xml")

      def show_json(request):
         product_list = Product.objects.all()
         json_data = serializers.serialize("json", product_list)
         return HttpResponse(json_data, content_type="application/json")

      def show_xml_by_id(request, product_id):
         try:
            product_item = Product.objects.filter(pk=product_id)
            xml_data = serializers.serialize("xml", product_item)
            return HttpResponse(xml_data, content_type="application/xml")
         except Product.DoesNotExist:
            return HttpResponse(status=404)

      def show_json_by_id(request, product_id):
         try:   
            product_item = Product.objects.filter(pk=product_id)
            json_data = serializers.serialize("json", [product_item])
            return HttpResponse(json_data, content_type="application/json")
         except Product.DoesNotExist:
            return HttpResponse(status=404)      
      ```
   - Tambahkan routing URL di `urls.py`
      ```python
      from django.urls import path
      from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id

      app_name = 'main'

      urlpatterns = [
         path('', show_main, name='show_main'),
         path('create-product/', create_product, name='create_product'),
         path('product/<str:id>/', show_product, name='show_product'),
         path('xml/', show_xml, name='show_xml'),
         path('json/', show_json, name='show_json'),
         path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
         path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
      ]
      ```

### Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Tidak ada.

### Hasil akses URL pada Postman

**XML**
![XML](https://github.com/user-attachments/assets/4b484b6e-85d3-4d39-bc44-e636e6188746)

**JSON**
![JSON](https://github.com/user-attachments/assets/59568a98-29bb-4ba8-8cc3-5dac57ddd87f)

**XML by *ID***
![XMLbyID](https://github.com/user-attachments/assets/28a8b1ce-a28b-4a9d-827c-24fb062a0e14)

**JSON by *ID***
![JSONbyID](https://github.com/user-attachments/assets/ac1e95d5-0ae3-4209-830f-fd72cc69ec9b)