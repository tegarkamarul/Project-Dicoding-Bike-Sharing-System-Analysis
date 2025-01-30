# Project-Dicoding-Bike-Sharing-System-Analysis

## Tentang Dataset
Dataset yang digunakan adalah dataset dari Perusahaan Capital Bike Sharing System yang berfokus pada sistem peminjaman sepeda. Data ini dikumpulkan selama 2 tahun dari 2011 sampai 2012. Dalam dataset ini terdapatdua data yaitu data hour dan day. Perbedaan dari kedua dataset ini hanya pada waktu pencatatan data. Data hour di catat setiap jam sedangkan data day dicatat setiap hari. Dalam kedua data set ini terdapat 17 kolom yang berisi sebagai berikut.
- instant : Record index
- dteday : Tanggal waktu pengambilan data
- season : Musim saat pengambilan data
- yr : Tahun waktu pengambilan data
- mnth : Bulan waktu pengambilan data
- hr : Jam waktu pengambilan data
- holiday : keterangan apakah saat pengambilan data hari libur atau tidak
- weekday : Nama hari dalam satu minggu
- workingday : keterangan apakah saat pengambilan data hari kerja atau tidak
- weathersit : Cuaca saat pengambilan data
- temp : Suhu saat pengambilan data
- atemp : Suhu yang dirasakan saat pengembilan data
- hum : Kelembapan saat pengambilan data
- windspeed : Kecepatan angin saat pengambilan data
- casual : Jumlah pengguna casual atau biasa
- registered : Jumlah penguna terdaftar
- cnt : Total seluruh pengguna bike sharing

Walaupun pada akhir dari proses pembersihan data terdapat beberapa kolom yang saya ubah hasilnya menjadi seperti ini.
- date : Tanggal waktu pengambilan data
- season : Musim saat pengambilan data
- yearr : Tahun waktu pengambilan data
- month : Bulan waktu pengambilan data
- hour : Jam waktu pengambilan data
- holiday : keterangan apakah saat pengambilan data hari libur atau tidak
- weekday : keterangan apakah ini hari weekday atau weekend
- workingday : keterangan apakah saat pengambilan data hari kerja, hari libur atau weekend
- weather : Cuaca saat pengambilan data
- temperatur : Suhu saat pengambilan data
- feeling temperatur : Suhu yang dirasakan saat pengembilan data
- humidity : Kelembapan saat pengambilan data
- windspeed : Kecepatan angin saat pengambilan data
- casual : Jumlah pengguna casual atau biasa
- registered : Jumlah penguna terdaftar
- total_user : Total seluruh pengguna bike sharing
- day_of_week : Nama hari saat pengambilan data

Untuk melihat sumber data mentahnya bisa klin link [**disini**](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset/data)

## Tentang Berkas Pengumpulan
```
.
├── dashboard
│   |── clean_daydata.csv
|   |── clean_hourdata.csv
|   |── dashboard.py
|   └── logo.png
├── data
│   ├── day.csv
|   |── hour.csv
|   └── Readme.txt
├── notebook.ipynb
├── README.md
└── requirements.txt
```
Berikut adalah struktur dari folder Submission_TegarKamarulzaman yang merupakan tugas saya. Untuk data pada folder data merupakan data mentah sedangkan data pada folder dashboar merupakan data hasil pembersihan dari proses analisis pada file notebook. file notebook berisi proses dan langkah - langkah analisis data sedangkan file requirement berisi library atau packages apa saja yang digunakan dalam proses pembuatan tugas.
## Tata Cara Menjalankan Dashboard
1. Pastikan anda sudah menginstal python yang menjadi bahasa utama dalam pembuatan dashboard. Jika belum anda bisa mengunjungi link [**berikut.**](https://www.python.org/downloads/windows/)
2. Buka Terminal atau CMD lalu pastikan bahwa anda sudah berada di path dari folder submission.
3. Install Packages dan Library yang dibutuhkan dengan mengetik perintah berikut:
```
pip install -r requirements.txt
```
4. Setelah itu masuk ke folder dashboard dengan perintah:

``` 
cd dashboard
```
5. Running Dashboard dengan perintah:
```
streamlit run dashboard.py
```
6. Maka tampilan dashboard akan muncul secara otomatis

Berikut penjelasan dari saya. Terima kasih.
