# Proyek Analisis Data E-Commerce

Proyek ini bertujuan untuk melakukan analisis data pada dataset e-commerce yang mencakup berbagai aspek transaksi dan informasi terkait dari toko online.

## Struktur Direktori

- `dashboard/`: Folder untuk aplikasi dashboard dan berkas terkait.
  - `dashboard • Streamlit.pdf`: Dokumen panduan atau dokumentasi terkait dashboard Streamlit.
  - `dashboard.py`: Berkas Python untuk mengatur aplikasi dashboard.

- `dataset/`: Folder yang berisi dataset yang digunakan dalam proyek.
  - `customers_dataset.csv`: Dataset informasi pelanggan.
  - `geolocation_dataset.csv`: Dataset informasi geolokasi.
  - `order_items_dataset.csv`: Dataset rincian item pesanan.
  - `order_payments_dataset.csv`: Dataset informasi pembayaran pesanan.
  - `order_reviews_dataset.csv`: Dataset ulasan pesanan.
  - `orders_dataset.csv`: Dataset informasi pesanan.
  - `product_category_name_translation.csv`: Dataset terjemahan nama kategori produk.
  - `products_dataset.csv`: Dataset informasi produk.
  - `sellers_dataset.csv`: Dataset informasi penjual.

- `Proyek_Analisis_Data.ipynb`: Notebook Jupyter Python untuk analisis data utama.

- `README.md`: Dokumen ini, memberikan deskripsi proyek dan panduan penggunaan.

- `requirements.txt`: Berkas yang berisi daftar paket Python yang diperlukan untuk menjalankan proyek.

## Panduan Penggunaan

1. **Persiapan Lingkungan:**
   - Pastikan Python telah terinstal.
   - Instal semua paket yang diperlukan dengan menjalankan perintah berikut di terminal:
     ```
     pip install -r requirements.txt
     ```

2. **Eksplorasi Data:**
   - Buka notebook `Proyek_Analisis_Data.ipynb` untuk menjalankan analisis data pada dataset yang tersedia.

3. **Penggunaan Dashboard:**
   - Untuk melihat dan berinteraksi dengan visualisasi data, jalankan `dashboard.py` dengan perintah:
     ```
     cd dashboard
     streamlint run dashboard.py
     ```
   - Ikuti panduan pada `dashboard • Streamlit.pdf` untuk petunjuk lebih lanjut mengenai penggunaan aplikasi dashboard.
