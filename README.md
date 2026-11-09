# Jualan Gue — Katalog Shopee Affiliate

Website kurasi produk rekomendasi Shopee Affiliate dengan performa tinggi, zero bloat, static pre-rendering, dan motion animasi premium.

---

## 🛠️ Arsitektur & Build Otomatis

Website ini menggunakan arsitektur **Static HTML Pre-rendered**:
- Data master produk berada di `data/products_verified.json`.
- Skrip generator `build_site.py` membaca data, menyusun markup HTML 92 kartu produk dan slider Hero secara statis ke `index.html`.
- Setiap kali branch di-push atau di-deploy ke Vercel, Vercel otomatis menjalankan:
  ```bash
  python3 build_site.py
  ```
  yang terkonfigurasi pada `vercel.json` dan `package.json` (`npm run build`).

---

## 💻 Menjalankan & Membangun Secara Lokal

1. **Jalankan Build Script (menghasilkan `index.html`):**
   ```bash
   python3 build_site.py
   # atau
   npm run build
   ```

2. **Jalankan Lokal Server:**
   ```bash
   npm start
   # atau
   python3 -m http.server 8080
   ```
   Buka peramban di `http://localhost:8080`.

---

## 📦 Menambah / Menyembunyikan Produk

### A. Menyembunyikan Produk (Hide)
Jika ada produk yang stoknya habis, anomali harga (mis. harga satuan per lembar kardus), atau link tidak aktif:
1. Buka `data/products.json` dan temukan produk berdasarkan `id`.
2. Ubah atau tambahkan field:
   ```json
   "hidden": true
   ```
3. Sinkronkan ke `data/products_verified.json` (hanya produk dengan `"hidden": false` atau tanpa flag hidden yang masuk ke sini).
4. Jalankan `python3 build_site.py` untuk mengupdate `index.html`.

### B. Menambah Produk Baru
1. Masukkan entri baru ke `data/products.json` dengan struktur:
   ```json
   {
     "id": 101,
     "name": "Nama Produk Lengkap Sesuai Shopee",
     "category": "Elektronik & Gadget",
     "price": 50000,
     "price_formatted": "Rp 50.000",
     "priceCheckedAt": "2026-11-08T19:36:49+07:00",
     "priceSource": "Shopee Affiliate Export CSV",
     "affiliate_url": "https://s.shopee.co.id/...",
     "sales": "10RB+ Terjual",
     "sales_bucket": "10RB+ Terjual",
     "glow_color": "rgb(238, 77, 45)",
     "image_url": "assets/products_real/md/101.webp"
   }
   ```
2. Pastikan file gambar WebP sudah tersedia di `assets/products_real/md/101.webp`, `sm/101.webp`, dan `lg/101.webp`.
3. Jalankan `python3 build_site.py`.

---

## 🎯 Aturan Kejujuran Data

- **Harga:** Field `priceCheckedAt` mencatat waktu ekspor CSV dari Shopee. Tidak mengklaim harga realtime kecuali jika divalidasi langsung via API/CDP.
- **Hero "Produk Terlaris":** Hanya menampilkan produk yang memiliki bukti penjualan bucket resmi `10RB+` di data ekspor Shopee. Label bucket ditampilkan apa adanya ("10RB+ Terjual").
- **Aset Gambar:** 100% foto produk asli yang ditarik dari CDN Shopee. Dilarang memasukkan foto stok / Unsplash.
