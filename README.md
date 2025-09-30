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

<details>
<summary>Tugas Individu 3</summary>

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
</details>

<details>
<summary>Tugas Individu 4</summary>

## Tugas Individu 4 - PBP Ganjil 2025/2026

### Apa itu Django `AuthenticationForm`? Jelaskan juga kelebihan dan kekurangannya.

`AuthenticationForm` adalah form bawaan Django untuk login user. Form ini merupakan bagian dari Django's authentication system dan terletak di `django.contrib.auth.forms`. Form ini menyediakan field username dan password, melakukan validasi kredensial lewat authentication backends, serta mengembalikan user yang lolos autentikasi. Kelebihannya itu siap pakai dan terintegrasi, serta aman secara default. Kekurangannya hanya terbatas pada username dan password dan tidak mendukung 2FA. Namun, form ini dapat mudah dikostumisasi sesuai dengan kebutuhan.

### Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

- Autentikasi: Proses verifikasi identitas User biasanya melalui kombinasi username dan password. Django menyediakan sistem autentikasi bawaan di `django.contrib.auth`, contoh mekanismenya yaitu `login()` untuk membuat sesi dan menempelkan user ke `request.user`.
- Otorisasi: Proses menentukan hak akses setelah user berhasil diautentikasi. Misalnya, user biasa boleh membaca produk, tetapi hanya admin yang bisa menambah atau menghapus. Django mengatur otorisasi berbasis permissions dan groups. Kemudian, ada juga decorators untuk function-based views, contohnya `@login_required` yang membatasi akses view hanya untuk pengguna yang sudah login. Jika belum, redirect ke halaman login.

### Apa saja kelebihan dan kekurangan *session* dan *cookies* dalam konteks menyimpan state di aplikasi web?

- Session: Kelebihannya yaitu lebih aman karena data sensitif tidak disimpan di client (client hanya menerima session ID), server juga dapat menyimpan data dengan jumlah besar dan mengubah atau menghapus session kapan pun. Untuk kekurangannya yaitu bisa membuat beban storage semakin banyak dan bergantung pada cookie.
- Cookie: Kelebihannya yaitu disimpan di client jadi tidak perlu storage di server. Cookies juga merupakan stateless server sehingga cocok untuk arsitektur skala besar. Kekurangannya yaitu ukurannya terbatas dan rentan dilihat dan dimanipulasi.

###  Apakah penggunaan *cookies* aman secara *default* dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Cookies tidak sepenuhnya aman secara default karena berpotensi mengalami pencurian, manipulasi, penyadapan jika tidak menggunakan HTTPS, serta rawan disalahgunakan untuk serangan CSRF, sebab cookies selalu ikut terkirim di setiap request. Untuk mengatasi hal ini, Django menyediakan mekanisme keamanan bawaan seperti menyimpan session data di server, hanya `sessionid` yang dikirim sebagai cookie. Kemudian, ada juga CSRF token `{% csrf_token %}` yang dapat mencegah serangan CSRF meski cookie `sessionid` otomatis terkirim.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Implementasi registrasi, login, dan logout.

   - Menambahkan fungsi registrasi, login, dan logout di `views.py`.
      ```python
      from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
      from django.contrib.auth import authenticate, login
      from django.contrib import messages

      def register(request):
         form = UserCreationForm()

         if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  form.save()
                  messages.success(request, 'Your account has been successfully created!')
                  return redirect('main:login')
         context = {'form':form}
         return render(request, 'register.html', context)

      def login_user(request):
         if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                  user = form.get_user()
                  login(request, user)
                  return redirect('main:show_main')

         else:
            form = AuthenticationForm(request)
         context = {'form': form}
         return render(request, 'login.html', context)

      def logout_user(request):
         logout(request)
         return redirect('main:login')
      ```

   - Modifikasi template html.
      - `register.html`
         ```html
         {% extends 'base.html' %}

         {% block meta %}
         <title>Register</title>
         {% endblock meta %}

         {% block content %}

         <div>
         <h1>Register</h1>

         <form method="POST">
            {% csrf_token %}
            <table>
               {{ form.as_table }}
               <tr>
               <td></td>
               <td><input type="submit" name="submit" value="Daftar" /></td>
               </tr>
            </table>
         </form>

         {% if messages %}
         <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
         </ul>
         {% endif %}
         </div>

         {% endblock content %}
         ```
      - `login.html`
         ```html
         {% extends 'base.html' %}

         {% block meta %}
         <title>Login</title>
         {% endblock meta %}

         {% block content %}
         <div class="login">
         <h1>Login</h1>

         <form method="POST" action="">
            {% csrf_token %}
            <table>
               {{ form.as_table }}
               <tr>
               <td></td>
               <td><input class="btn login_btn" type="submit" value="Login" /></td>
               </tr>
            </table>
         </form>

         {% if messages %}
         <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
         </ul>
         {% endif %} Don't have an account yet?
         <a href="{% url 'main:register' %}">Register Now</a>
         </div>

         {% endblock content %}
         ```
      - `main.html`
         ```html
         <a href="{% url 'main:logout' %}">
         <button>Logout</button>
         </a>
         ```
   - Tambahkan path URL ke dalam `urlpatterns`.
      ```python
      urlpatterns = [
         path('', show_main, name='show_main'),
         path('create-product/', create_product, name='create_product'),
         path('product/<str:id>/', show_product, name='show_product'),
         path('xml/', show_xml, name='show_xml'),
         path('json/', show_json, name='show_json'),
         path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
         path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
         path('register/', register, name='register'),
         path('login/', login_user, name='login'),
         path('logout/', logout_user, name='logout'),
      ]  
      ```

2. Implementasi data dari cookies.

   - Modifikasi `views.py`
      ```python
      import datetime
      from django.http import HttpResponseRedirect
      from django.urls import reverse

      # Ubah blok kode if form.is_valid() di login_user
      if form.is_valid():
         user = form.get_user()
         login(request, user)
         response = HttpResponseRedirect(reverse("main:show_main"))
         response.set_cookie('last_login', str(datetime.datetime.now()))
         return response

      # Tambahkan 'last_login': request.COOKIES.get('last_login', 'Never') pada context show_main
      context = {
            'npm' : '2406397706',
            'name': 'Ahmad Faiq Fawwaz Abdussalam',
            'class': 'PBP C',
            'product_list': product_list,
            'last_login': request.COOKIES.get('last_login', 'Never')
         }
      
      # Ubah fungsi logout_user untuk menghapus cookie last_login setelah melakukan logout
      def logout_user(request):
         logout(request)
         response = HttpResponseRedirect(reverse('main:login'))
         response.delete_cookie('last_login')
         return response
      ```
   
   - Modifikasi `main.html` untuk menampilkan data waktu terakhir pengguna login.
      ```html
      <h5>Sesi terakhir login: {{ last_login }}</h5>
      ```

3. Menghubungkan model `Product` dengan `User`.

   - Modifikasi `models.py` kemudian makemigrations dan migrate.
      ```python
      from django.contrib.auth.models import User

      class Product(models.Model):
         user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
      ```
   
   - Modifikasi `views.py`.
      ```python
      def create_product(request):
         form = ProductForm(request.POST or None)

         if form.is_valid() and request.method == "POST":
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            return redirect('main:show_main')

         context = {'form': form}
         return render(request, "create_product.html", context)

      @login_required(login_url='/login')
      def show_main(request):
         filter_type = request.GET.get("filter", "all")

         if filter_type == "all":
            product_list = Product.objects.all()
         else:
            product_list = Product.objects.filter(user=request.user)

         context = {
            'npm' : '2406397706',
            'name': request.user.username,
            'class': 'PBP C',
            'product_list': product_list,
            'last_login': request.COOKIES.get('last_login', 'Never')
         }

         return render(request, "main.html", context)
      ```
   
   - Modifikasi templates yang sesuai.
      - `main.html`
         ```html
         <a href="?filter=all">
            <button type="button">All Products</button>
         </a>
         <a href="?filter=my">
            <button type="button">My Products</button>
         </a>
         ```
      - `product_detail.html`
         ```html
         {% if product.user %}
         <p>Added by: {{ product.user.username }}</p>
         {% else %}
         <p>Added by: Anonymous</p>
         {% endif %}
         ```

4. Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.

   - faiqfwwz
   ![faiqfwwz](https://github.com/user-attachments/assets/9c208af5-847c-40c1-99ac-69cd6989b619)

   - ahmfaiq
   ![ahmfaiq](https://github.com/user-attachments/assets/a7453fb6-2e63-460b-880a-436e7f377c67)

5. Commit dan push ke github dan pws.
</details>

---

## Tugas Individu 5 - PBP Ganjil 2025/2026

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Agar tidak bingung ketika banyak aturan CSS yang menimpa satu sama lain pada sebuah elemen, CSS punya sistem prioritas yang disebut specificity. Urutan prioritasnya adalah seperti ini:

1. Inline styles (misalnya `<p id="intro" class="text" style="color: orange">...</p>`)
2. ID selectors (misalnya `#intro { color: green; }`)
3. Classes selector (misalnya `.text { color: blue; }`)
4. Element selector (misalnya `p { color: black; }`)
5. Dengan menggunakan `!important`, sebuah properti dapat mengesampingkan seluruh aturan prioritas yang telah ditetapkan, karena ia langsung diberikan prioritas tertinggi.

### Mengapa *responsive design* menjadi konsep yang penting dalam pengembangan aplikasi *web*? Berikan contoh aplikasi yang sudah dan belum menerapkan *responsive design*, serta jelaskan mengapa!

Responsive design memungkinkan web dapat menyesuaikan diri dengan berbagai ukuran dan orientasi layar perangkat pengguna. Oleh karena itu, responsive design penting karena pengguna mengakses web dari berbagai perangkat seperti dekstop, tablet, dan smartphone. Jika desainnya tidak responsif, maka pengguna bisa saja mengalami kesulitan seperti teks tidak terbaca di layar yang lebih kecil.

Contoh aplikasi yang sudah menerapkan responsive design adalah X (Twitter) Web yang sudah menyesuaikan tampilan berdasarkan ukuran layar pengguna. Contoh aplikasi yang belum menerapkan responsive design adalah SIAK-NG yang jika diakses melalui smartphone, maka pengguna akan kesulitan membaca teks dan mengakses tombol yang ada.

### Jelaskan perbedaan antara *margin*, *border*, dan *padding*, serta cara untuk mengimplementasikan ketiga hal tersebut!

![Box Model CSS](https://pbp-fasilkom-ui.github.io/ganjil-2026/assets/images/t4-1-833b8ee0d0dd53959be9b66d452cd1d6.png)

1. Margin: ruang di luar kotak (memisahkan elemen dari elemen lain, tidak punya warna/latarnya)
2. Border: garis/bingkai yang mengelilingi kotak (punya ketebalan, jenis garis, dan warna)
3. Padding: ruang di dalam border yang mendorong isi (teks/gambar) menjauh dari tepi kotak

#### Contoh implementasi
```css
div {
    margin: 20px;
    border: 2px solid;    
    padding: 10px;
}
```

### Jelaskan konsep *flex box* dan *grid layout* beserta kegunaannya!

#### Flex box
Sistem layout satu dimensi yang mengatur elemen sepanjang satu sumbu (baris atau kolom) dengan mudah. Flex box cocok untuk meratakan, mendistribusikan ruang, dan membuat komponen adaptif seperti navbar, deret tombol, atau kartu yang tingginya seragam.

#### Grid layout
Sistem dua dimensi yang memungkinkan kita mendefinisikan kolom dan baris sekaligus, menempatkan elemen secara presisi (termasuk area grid), sehingga ideal untuk kerangka halaman kompleks seperti galeri atau dashboard.

###  Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial)!

1. Implementasi fungsi menghapus dan mengedit product

   - Tambah fungsi di `views.py`
      ```python
      def edit_product(request, id):
         product = get_object_or_404(Product, pk=id)
         form = ProductForm(request.POST or None, instance=product)
         if form.is_valid() and request.method == 'POST':
            form.save()
            return redirect('main:show_main')

         context = {
            'form': form
         }

         return render(request, "edit_product.html", context)

      def delete_product(request, id):
         product = get_object_or_404(Product, pk=id)
         product.delete()
         return HttpResponseRedirect(reverse('main:show_main'))
      ```
   
   - Tambahkan routing URL di `urls.py`
      ```python
      path('product/<uuid:id>/edit', edit_product, name='edit_product'),
      path('product/<uuid:id>/delete', delete_product, name='delete_product'),
      ```
   
2. Kustomisasi desain template yang sudah dibuat sebelumnya menggunakan Tailwind

   - Inisiasi tailwind
      - `base.html`
      ```html
      {% load static %}
      <!DOCTYPE html>
      <html lang="en">
      <head>
         <meta charset="UTF-8" />
         <meta name="viewport" content="width=device-width, initial-scale=1.0" />
         {% block meta %} {% endblock meta %}
         <script src="https://cdn.tailwindcss.com"></script>
         <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
      </head>
      <body>
         {% block content %} {% endblock content %}
      </body>
      </html>
      ```

      - Konfigurasi static files
      ```python
      MIDDLEWARE = [
         'django.middleware.security.SecurityMiddleware',
         'whitenoise.middleware.WhiteNoiseMiddleware', 
         ...
      ]
      STATIC_URL = '/static/'
      if DEBUG:
         STATICFILES_DIRS = [
            BASE_DIR / 'static' # merujuk ke /static root project pada mode development
         ]
      else:
         STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
      ```

      - Menambahkan `global.css`
      ```css
      /* Palette B variables */
      :root{
      --brand-navy:   #0A192F;
      --brand-surface:#FFFFFF;
      --brand-accent: #00FF88; /* neon green */
      --brand-muted:  #F3F4F6;
      --brand-border: #E5E7EB;
      }

      /* Inputs */
      .form-style form input,
      .form-style form textarea,
      .form-style form select {
      width: 100%;
      padding: 0.5rem;
      border: 2px solid var(--brand-border);
      border-radius: 0.375rem;
      background: var(--brand-surface);
      }

      /* Focus state (neon ring) */
      .form-style form input:focus,
      .form-style form textarea:focus,
      .form-style form select:focus {
      outline: none;
      border-color: var(--brand-accent);
      /* sedikit transparan agar lembut */
      box-shadow: 0 0 0 3px rgba(0, 255, 136, 0.35);
      }

      /* Checkbox base */
      .form-style input[type="checkbox"] {
      width: 1.25rem;
      height: 1.25rem;
      padding: 0;
      border: 2px solid var(--brand-border);
      border-radius: 0.375rem;
      background-color: var(--brand-surface);
      cursor: pointer;
      position: relative;
      appearance: none;
      -webkit-appearance: none;
      -moz-appearance: none;
      }

      /* Checkbox checked */
      .form-style input[type="checkbox"]:checked {
      background-color: var(--brand-accent);
      border-color: var(--brand-accent);
      }

      /* Gunakan navy untuk centang agar kontras dgn neon */
      .form-style input[type="checkbox"]:checked::after {
      content: '✓';
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      color: var(--brand-navy);
      font-weight: bold;
      font-size: 0.875rem;
      }

      /* Checkbox focus */
      .form-style input[type="checkbox"]:focus {
      outline: none;
      border-color: var(--brand-accent);
      box-shadow: 0 0 0 3px rgba(0, 255, 136, 0.25);
      }

      /* (Opsional) Placeholder & label tones agar nyatu dengan palette */
      .form-style ::placeholder { color: #6B7280; }
      .form-style label { color: var(--brand-navy); }
      ```
   
   - Styling pada tiap template
      - [Card Product](https://github.com/faiqfwwz/The-12th-Kit/blob/master/main/templates/card_product.html)
      - [Create Product](https://github.com/faiqfwwz/The-12th-Kit/blob/master/main/templates/create_product.html)
      - [Edit Product](https://github.com/faiqfwwz/The-12th-Kit/blob/master/main/templates/edit_product.html)
      - [Login](https://github.com/faiqfwwz/The-12th-Kit/blob/master/main/templates/login.html)
      - [Main](https://github.com/faiqfwwz/The-12th-Kit/blob/master/main/templates/main.html)
      - [Product Detail](https://github.com/faiqfwwz/The-12th-Kit/blob/master/main/templates/product_detail.html)
      - [Register](https://github.com/faiqfwwz/The-12th-Kit/blob/master/main/templates/register.html)