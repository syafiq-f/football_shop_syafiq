-----------------------------------------------------------------------------------------------------------------
TUGAS 2
-----------------------------------------------------------------------------------------------------------------
NOMOR 1 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)?

bikin fonasi appsnya dulu jadi harus memanggil django-admin startproject football_shop jadi nanti muncul struktur appsnya kayak setting, urls sama manage
didlem django itu bikin lagi app baru namanya main
nah main itu masukin ke installed apps di setting
Definisikan model Product di models.py jadi dibuat tipe2 datanya per model/attriut itu gimana
migrasiin buat mengubah definisi model jadi tabel main_product di database
buat viewsnya (basically ini kayak bikin isi dari variablesnya apa aja yang nanti bakal ditampilin.
ngehubungin url keview
bikin templatenya deh di main.html jadi kayak did design apa aja yang bakal ada di webnya terus di fill sama variable yang ada di view
NOMOR 2 Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. (https://www.canva.com/design/DAGyi0GQxyE/VgBOXY1-47SITHk6BlI1uQ/edit?utm_content=DAGyi0GQxyE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

NOMOR 3 Jelaskan peran settings.py dalam proyek Django! Menurut saya setting ini seperti dasar atau konfigurasi utama dari proyek yang bakal dibuat karena semua pengaturan pentingnya itu ada di file ini. Seperti contohnya databasenya mau pake apa, installed appsnya apa aja, alur request dan responnya, dan masih banyak lagi. setiap kali server Django dijalankan, semua perilakunya akan mengikuti instruksi yang sudah ditulis di dalam settings.py. jadi seperti terminal sih semua yang dilakukan harus based on settingsnya.

NOMOR 4 Bagaimana cara kerja migrasi database di Django? migrasi ini seperti penyamaan apa yang telah kita kerjakan di kode dengan isi tabel di database. Jadi ketika ada perubahan maka database jg akan menyesuaikan. makemigrations, command ini nyuruh Django buat bikin file catatan perubahan selanjutnya migrate, ini pengeksekusiannya dan database beneran diubah sesuai model terbaru.

NOMOR 5 Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? Menurut saya Django dipilih karena strukturnya jelas dan lengkap, jadi gampang dipahami untuk pemula. Waktu ngerjain tugas tadi, saya bisa lihat alur dari model → view → template dengan lebih teratur.

NOMOR 6 Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

------------------------------------------------------------------------------------------------------------------
TUGAS 3
------------------------------------------------------------------------------------------------------------------
NOMOR 1
Karena menurut saya data itu tidak jalan sengan sendirinya, maka kita sebagai programmer perlu menentukan alurnya sendiri dengan sangat jelas seperti bagaimana datanya itu diterima, lalu setelah diterima mau ditaruh dimana, dan bagaimana caranya itu data akan muncul kembali ke website. Itu semua harus dipikirkan alurnya dan kodenya supaya precise dan rapih sehingga tidak bingung untuk alur kodenya

NOMOR 2
neurut saya yang lebih baik dari sego bagaimana cara penggunaannya adalah json, kenapa? json menawarkan penggunaan kode yang lebih familiar dan mudah dibaca oleh pemula seperti saya karena mirip sekali dengan dictionary. Sedangkan xml itu formatnya lebih kompleks seperti html sehingga perlu banyak penyesuaian dan pembelajaran untuk penggunaannya

NOMOR 3
is_valid() itu fungsi untuk prevent agar jawaban yang diinput itu sesuai dengan apa yang diset pada tipe datanya, sehingga tidak akan error dan terdapat kesalahan tipe data. Seperti contohnya di bagian harga tentunya kita expect untuk mendapatkan sebuah angka/integer dan untuk prevent error maka diperlukan is_valid supaya sesuai dengan kemauan.

NOMOR 4
dari pengertiannya sendiri, csrf merupakan Cross-Site Request Forgery. Based on https://portswigger.net/web-security/csrf dia itu seperti aksi prevent kejahatan dari luar.

NOMOR 5
Sekarang saya sudah lumayan paham cara pebngerjaannya
1. Karena sudah di setup pemrograman djanggonya maka hanya perlu menambahkan method2 yang perlu ditambahkan di views
2. Karena sudah dibuat functionnya maka tinggal ditambahkan path/urls untuk setiap fungsi. Anggepannya setalah kita buat fungsi, harus tau fungsi tersebut akan mengarahkan websitenya kemana.
3. Baru buat teplates atau tampilan akhirnya kira kira akan seperti bagaimana

-----------------------------------------------------------------------------------------------------------------
TUGAS 4
-----------------------------------------------------------------------------------------------------------------
NOMOR 1
berdsarkan web berikut, https://docs.djangoproject.com/en/5.2/topics/auth/default/
autehtication form merupakan form bawaan dari djanggo yang memungkinkan programer untuk menginisiasikan kode agar pengguna web dapat melangsungkan proses login. dan form ini akan menerima request berupa post dari data2 pengguna seperti username dan password.

Plus :
untuk pemakaiannya bisa lebih gampang karena bisa langsung import dan taruh kodenya
Minus : 
kurang fleksibel dalam artian jika kita mau kustomisasi field seperti login pake email dkk maka perlu subclass/override atau custom backend

NOMOR 2
Authentication adalah proses verifikasi sebuah user, biasanya akan diminta data pribadi seperti username, nama, ataupun password. Sedangkan Authorization adalah penentu apa yang bisa dilakukan user didalam website. Misal saat membuat akun maka kita harus dapat dibedakan apakah kita misal dalam kasus shopee pembeli atau penjual? proses pembuatan akunnya adalah authentication, namun akan ada perbedaan limit dari penjual dan pembeli dimana penjual hanya bisa melihat barang sedangkan penjual bisa menambahkan barang dagangannya. Limitasi tersebut dinamakian Authorization

Penerapan Autehntication : 
Authentication bisa diterapkan dengan mengimport form bawaan django dan ditaruh ke dalam fungsi login jadi ketika kita login maka akan disimpan kedalam form tersebut data datanya

Penerapan Authorization :
Authorization dapat dilakukan dengan mengubah kode di htmlnya dengn menggunakan conditionals lalu kalo semisal suatu fungsi bukanlah milik author based on current username yang sedang login maka tidak akan ditampilkan fitur tersebut.

NOMOR 3
Jadi kalo cookies itu dia menyimpan datanya di bagian kliennya tapi kurang aman karena datanya ke ekspos plus ada batasan ukurannya, makannya dia informasinya biasanya sedikit doang tapi disimpannya bisa lamaa. Sedangkan session itu nyimpen datanya di server jadi lebih aman dan bisa lebih banyak datanya dan fleksibel di tipe data yang kompleks, hanya saja memerlukan koneksi yang kuat dan kalau kebanyakan server bakal membebani servernya.

NOMOR 4
Cookiesgak terlalu aman secRa default karena rentan terhadap serangan seperti CSRF, di mana penyerang dapat memanfaatkan session cookie pengguna tanpa sepengetahuan pengguna. salah satu cara django menangani risiko ini dengan middleware CSRF yang secara otomatis menambahkan token unik pada setiap form POST, lalu memverifikasinya di server untuk memastikan permintaan memang berasal dari user yang benar atau terverifikasi.

NOMOR 5
Chechklist 1 :
Tentunya dengan membuat fungsi batru yakni login logout dan regist di views py, add path di urls dan buat htmlnya untuk membuat tampilan fungsinya. Untuk memungkinkan pengaksesannya itu dengan menyelipkan form login_required bawaan python sehingga fungsi2 yang memang hanya bisa dibuka ketika user login itu ditampilkan ketika user sudah login.

Checklist 2 :
Saya melakukannya secara manual yakni runservernya dan menambahkan akun serta dummynya masing masinhg

Checklist 3 :
Denngan menambahkan kode user dibagian models yang artinya models dalam case ini kan product yah nah product satu ini hanya dimiliki oleh user yang bersangkutan, lebih jelasnya     #artinya setiap produk dimiliki oleh satu user (relasi many-to-one).
    #kalau user dihapus, semua produk miliknya juga ikut dihapus.
    #biar produk yang sudah ada sebelumnya (yang belum punya user) tidak error waktu migrasi. Field ini bisa kosong.
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

Checklist 4 :
Menganti main htmlnya agar bisa diketahui siapa yang sedang login ditambah dengan login required di masing masing function di views.py

