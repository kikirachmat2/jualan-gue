# Jualan Gue — Premium Curated Affiliate Catalog

Katalog affiliate Shopee yang bersih, mewah, dan berorientasi konversi tinggi.

- **Production URL:** [https://jualan-gue.vercel.app](https://jualan-gue.vercel.app)
- **Repository:** [https://github.com/kikirachmat2/jualan-gue](https://github.com/kikirachmat2/jualan-gue)

---

## 📁 Struktur Data & Cara Menambah Produk

Data produk tersimpan di folder `data/`:
1. `data/products.json`: Sumber data mentah hasil ekspor link Shopee.
2. `data/products_enriched.json`: Data yang digunakan langsung oleh `index.html`.

### Cara Menambah Produk / Kategori Baru:
Buka `data/products_enriched.json` lalu tambahkan objek produk:

```json
{
  "id": 101,
  "name": "Nama Produk Lengkap dari Shopee",
  "clean_title": "Nama Produk Ringkas (1-2 Baris)",
  "category": "Elektronik & Gadget",
  "price_num": 149000,
  "price_formatted": "Rp 149.000",
  "original_price_num": 199000,
  "original_price_formatted": "Rp 199.000",
  "sales": "10RB+ Terjual",
  "rating": 4.9,
  "priority": 10,
  "product_url": "https://shopee.co.id/product/...",
  "affiliate_url": "https://s.shopee.co.id/...",
  "image_url": "https://images.unsplash.com/... atau URL foto produk CDN"
}
```

#### Field Keterangan:
- `clean_title`: Judul pendek bersih (maksimal 2 baris).
- `category`: Otomatis membuat chip kategori jika nama kategori baru.
- `priority`: Angka integer (misal `10`, `5`, `1`). Semakin tinggi angkanya, produk akan otomatis naik ke baris teratas dalam kategorinya.
- `original_price_num` *(opsional)*: Jika diisi lebih besar dari `price_num`, sistem akan otomatis menghitung persen diskon asli dan menampilkan harga coret.
- `rating` *(opsional)*: Angka rating bintang (misal `4.9`). Jika kosong, sistem hanya menampilkan jumlah terjual tanpa mengarang rating.
- `sales`: Format teks asli (misal `"10RB+ Terjual"`).

Setelah mengubah file data, lakukan commit dan push ke GitHub `main`:
```bash
git add data/products_enriched.json
git commit -m "feat: tambah produk baru"
git push origin main
```
Vercel akan otomatis men-deploy versi terbaru dalam hitungan detik.
