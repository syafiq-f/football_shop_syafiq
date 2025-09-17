-----------------------------------------------------------------------------------------------------------------
TUGAS 1
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
TUGAS 2
------------------------------------------------------------------------------------------------------------------
NOMOR 1
Karena menurut saya data itu tidak jalan sengan sendirinya, maka kita sebagai programmer perlu menentukan alurnya sendiri dengan sangat jelas seperti bagaimana datanya itu diterima, lalu setelah diterima mau ditaruh dimana, dan bagaimana caranya itu data akan muncul kembali ke website. Itu semua harus dipikirkan alurnya dan kodenya supaya precise dan rapih sehingga tidak bingung untuk alur kodenya

NOMOR 2
neurut saya yang lebih baik dari sego bagaimana cara penggunaannya adalah json, kenapa? json menawarkan penggunaan kode yang lebih familiar dan mudah dibaca oleh pemula seperti saya karena mirip sekali dengan dictionary. Sedangkan xml itu formatnya lebih kompleks seperti html sehingga perlu banyak penyesuaian dan pembelajaran untuk penggunaannya

NOMOR 3
is_valid() itu fungsi untuk prevent agar jawaban yang diinput itu sesuai dengan apa yang diset pada tipe datanya, sehingga tidak akan error dan terdapat kesalahan tipe data. Seperti contohnya di bagian harga tentunya kita expect untuk mendapatkan sebuah angka/integer dan untuk prevent error maka diperlukan is_valid supaya sesuai dengan kemauan.

NOMOR 4
dari pengertiannya sendiri, csrf merupakan Cross-Site Request Forgery. Based on https://portswigger.net/web-security/csrf dia itu seperti aksi prevent kejahatan dari luar

NOMOR 5
Sekarang saya sudah lumayan paham cara pebngerjaannya
1. Karena sudah di setup pemrograman djanggonya maka hanya perlu menambahkan method2 yang perlu ditambahkan di views
2. Karena sudah dibuat functionnya maka tinggal ditambahkan path/urls untuk setiap fungsi. Anggepannya setalah kita buat fungsi, harus tau fungsi tersebut akan mengarahkan websitenya kemana.
3. Baru buat teplates atau tampilan akhirnya kira kira akan seperti bagaimana

