NOMOR 1
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)?
1. bikin fonasi appsnya dulu jadi harus memanggil django-admin startproject football_shop jadi nanti muncul struktur appsnya kayak setting, urls sama manage
2. didlem django itu bikin lagi app baru namanya main
3. nah main itu masukin ke installed apps di setting
4. Definisikan model Product di models.py jadi dibuat tipe2 datanya per model/attriut itu gimana
5. migrasiin buat mengubah definisi model jadi tabel main_product di database
6. buat viewsnya (basically ini kayak bikin isi dari variablesnya apa aja yang nanti bakal ditampilin.
7. ngehubungin url keview
8. bikin templatenya deh di main.html jadi kayak did design apa aja yang bakal ada di webnya terus di fill sama variable yang ada di view

NOMOR 2
Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
(https://www.canva.com/design/DAGyi0GQxyE/VgBOXY1-47SITHk6BlI1uQ/edit?utm_content=DAGyi0GQxyE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

NOMOR 3
Jelaskan peran settings.py dalam proyek Django!
Menurut saya setting ini seperti dasar atau konfigurasi utama dari proyek yang bakal dibuat karena semua pengaturan pentingnya itu ada di file ini.
Seperti contohnya databasenya mau pake apa, installed appsnya apa aja, alur request dan responnya, dan masih banyak lagi.
setiap kali server Django dijalankan, semua perilakunya akan mengikuti instruksi yang sudah ditulis di dalam settings.py.
jadi seperti terminal sih semua yang dilakukan harus based on settingsnya.

NOMOR 4
Bagaimana cara kerja migrasi database di Django?
migrasi ini seperti penyamaan apa yang telah kita kerjakan di kode dengan isi tabel di database. Jadi ketika ada perubahan maka database jg akan menyesuaikan.
makemigrations, command ini nyuruh Django buat bikin file catatan perubahan
selanjutnya  migrate, ini pengeksekusiannya dan database beneran diubah sesuai model terbaru.


NOMOR 5
Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya Django dipilih karena strukturnya jelas dan lengkap, jadi gampang dipahami untuk pemula. Waktu ngerjain tugas tadi, saya bisa lihat alur dari model → view → template dengan lebih teratur.

NOMOR 6
Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
