# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

**Latar Belakang Bisnis:**
Perusahaan Edutech adalah organisasi yang fokus pada penyediaan solusi pendidikan digital untuk siswa dan institusi pendidikan. Dalam menghadapi tantangan untuk meningkatkan efisiensi dan hasil pembelajaran, perusahaan ini memerlukan analisis mendalam tentang performa siswa dan efektivitas berbagai aspek program pendidikan yang mereka tawarkan.

### Permasalahan Bisnis

1. **Pengaruh Beasiswa Terhadap Kelulusan:**
   - Bagaimana penerimaan beasiswa mempengaruhi tingkat kelulusan siswa?
   - Apakah siswa yang menerima beasiswa memiliki tingkat kelulusan yang lebih tinggi dibandingkan dengan yang tidak menerima beasiswa?

2. **Distribusi Course Terhadap Status Kelulusan:**
   - Bagaimana distribusi course yang diambil mempengaruhi status kelulusan siswa?
   - Apakah ada perbedaan signifikan dalam tingkat kelulusan berdasarkan course yang diambil?

### Cakupan Proyek

- **Analisis Data:** 
  - Mengumpulkan dan memproses data terkait beasiswa, status kelulusan, dan course yang diambil oleh siswa.
  - Menganalisis pengaruh beasiswa terhadap status kelulusan.
  - Menganalisis distribusi course terhadap status kelulusan.

- **Business Dashboard:**
  - Pengaruh Beasiswa Terhadap Kelulusan: Menampilkan data perbandingan tingkat kelulusan siswa yang menerima beasiswa dan yang tidak menerima.
  - Distribusi Course Terhadap Kelulusan: Menyediakan gambaran tentang distribusi course yang diambil oleh siswa dan bagaimana course tersebut berkorelasi dengan status kelulusan.
  - Filter Dinamis: Pengguna dapat menyesuaikan filter seperti rentang waktu, kategori course, dan jenis beasiswa untuk analisis yang lebih mendalam.

- **Machine Learning Prototype:**
  - Mengembangkan prototype sistem machine learning untuk memprediksi kelulusan siswa berdasarkan beasiswa dan course yang diambil.

### Persiapan

**Sumber Data:**
- Data performa siswa tersedia di [CSV file](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv).

**Setup Environment:**
```bash
# Install required libraries
pip install pandas seaborn matplotlib streamlit scipy

# Start Streamlit app
streamlit run app.py
```

## Business Dashboard

**Deskripsi:**
Dashboard ini dirancang untuk memberikan wawasan tentang pengaruh beasiswa terhadap kelulusan dan distribusi course terhadap status kelulusan siswa. Dashboard menyediakan visualisasi interaktif untuk memudahkan analisis dan pengambilan keputusan.

## Menjalankan Sistem Machine Learning

**Deskripsi:**
Prototype sistem machine learning ini digunakan untuk memprediksi kemungkinan kelulusan siswa berdasarkan data yang ada. Prototype ini dapat digunakan untuk memberikan rekomendasi lebih lanjut kepada siswa dan manajemen pendidikan.

**Cara Menjalankan:**
1. Pastikan semua dependensi terinstall.
2. Jalankan script Python untuk memuat model dan melakukan prediksi.

## Conclusion

**Konklusi:**
1. Persentase Dropout Berdasarkan Usia dan Kualifikasi Pendidikan Sebelumnya: Siswa dalam kelompok usia muda dengan kualifikasi pendidikan rendah memiliki risiko dropout yang lebih tinggi.
2. Perbandingan Tingkat Kelulusan Beasiswa: Siswa yang menerima beasiswa cenderung memiliki tingkat kelulusan yang lebih tinggi dibandingkan dengan yang tidak menerima beasiswa.
3. Hubungan Jumlah Unit Mata Kuliah dan Kelulusan Tepat Waktu: Siswa yang menyelesaikan lebih banyak unit mata kuliah pada semester pertama cenderung lebih mungkin untuk lulus tepat waktu.
### Rekomendasi Action Items

1. **Evaluasi Program Beasiswa:**
   - Tinjau dan sesuaikan kebijakan beasiswa berdasarkan hasil analisis untuk meningkatkan tingkat kelulusan.

2. **Pengembangan Course:**
   - Identifikasi course yang memiliki dampak signifikan terhadap kelulusan dan pertimbangkan penambahan atau penyesuaian course untuk meningkatkan hasil akademik siswa.

##### Login metabase
email : acari.panca21@gmail.com
password : root123