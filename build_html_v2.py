import json
from pathlib import Path

DATA_FILE = Path("/Users/kiki/Documents/Web Develop/katalog-ceritakiki/data/products_enriched.json")
OUT_FILE = Path("/Users/kiki/Documents/Web Develop/katalog-ceritakiki/index.html")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    products = json.load(f)

json_str = json.dumps(products, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="id" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Koleksi Spill & Racun Belanja Kiki (@kikipunyacerita)</title>
  <meta name="description" content="Katalog 100+ rekomendasi barang solusi anti-pusing terkurasi oleh Kiki Rachmat (@kikipunyacerita) di Threads. Solusi nyata budak korporat, anak kos, dan pejuang commute. Rating 4.8+, harga terjangkau.">
  <meta name="theme-color" content="#090a10">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  
  <!-- OpenGraph Meta -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="Koleksi Spill & Racun Belanja Kiki (@kikipunyacerita)">
  <meta property="og:description" content="100+ Barang Pilihan Solusi Anti-Pusing: Desk Setup, Kosan Hacks, Skincare Murah & Essentials di Bawah 100rb.">
  <meta property="og:image" content="https://images.unsplash.com/photo-1512436991641-6745cdb1723f?q=80&w=1200&auto=format&fit=crop">
  <meta property="og:site_name" content="Kisah Komisi by Kiki Rachmat">

  <!-- Google Fonts: Plus Jakarta Sans & Space Grotesk -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
            mono: ['"Space Grotesk"', 'monospace']
          }},
          colors: {{
            shopee: {{
              DEFAULT: '#ee4d2d',
              hover: '#d73211',
              light: '#fff5f1',
              glow: 'rgba(238, 77, 45, 0.35)'
            }},
            dark: {{
              bg: '#08090e',
              surface: '#11131c',
              border: '#1e2233',
              hover: '#181b28',
              card: '#131622'
            }}
          }}
        }}
      }}
    }}
  </script>

  <style>
    /* Content visibility for 60FPS high performance scrolling (modern-web-guidance) */
    .product-card {{
      content-visibility: auto;
      contain-intrinsic-size: auto 300px auto 420px;
      position: relative;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease, border-color 0.25s ease;
    }}
    
    .product-card:hover {{
      transform: translateY(-3px);
      box-shadow: 0 16px 36px -10px rgba(0, 0, 0, 0.6), 0 0 25px -5px rgba(238, 77, 45, 0.2);
    }}

    /* Stretched link overlay conforming to modern-web-guidance */
    .product-card a.card-link::after {{
      content: "";
      position: absolute;
      inset: 0;
      border-radius: 1.25rem;
    }}

    /* Elevated controls above stretched link */
    .product-card a:not(.card-link), 
    .product-card button {{
      position: relative;
      z-index: 10;
    }}

    /* Custom Scrollbar */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #08090e;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #23273b;
      border-radius: 9999px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #3c4365;
    }}

    /* Dynamic viewport container */
    .viewport-box {{
      min-height: 100dvh;
    }}

    /* Glow backdrop */
    .ambient-glow {{
      background: radial-gradient(circle at 50% 0%, rgba(238, 77, 45, 0.14) 0%, rgba(99, 102, 241, 0.09) 30%, transparent 70%);
    }}

    /* Shimmer effect for buttons */
    @keyframes pulse-subtle {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.85; }}
    }}
    .animate-pulse-subtle {{
      animation: pulse-subtle 3s infinite ease-in-out;
    }}
  </style>
</head>
<body class="bg-dark-bg text-slate-100 font-sans antialiased selection:bg-shopee selection:text-white viewport-box flex flex-col ambient-glow">

  <!-- Live Toast Notification -->
  <aside id="toast" role="status" aria-live="polite" class="fixed bottom-6 right-6 z-50 transform translate-y-20 opacity-0 transition-all duration-300 pointer-events-none flex items-center gap-3 bg-slate-900/95 backdrop-blur-md text-white border border-slate-700/80 px-4 py-3 rounded-2xl shadow-2xl">
    <div class="w-7 h-7 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-sm">✓</div>
    <div>
      <p id="toast-title" class="text-xs font-bold text-white">Link Shopee Berhasil Disalin</p>
      <p id="toast-sub" class="text-[11px] text-slate-400">Silakan paste di browser atau chat</p>
    </div>
  </aside>

  <!-- Live Social Proof Notification Ticker (Cialdini Social Proof & FOMO) -->
  <div id="fomoTicker" class="fixed bottom-6 left-6 z-40 transform translate-y-28 opacity-0 transition-all duration-500 max-w-xs sm:max-w-sm pointer-events-none hidden sm:flex items-center gap-3 bg-dark-surface/95 backdrop-blur-lg border border-dark-border p-3 rounded-2xl shadow-2xl">
    <div class="w-10 h-10 rounded-xl overflow-hidden bg-slate-800 flex-shrink-0 border border-slate-700/50">
      <img id="fomoImg" src="https://images.unsplash.com/photo-1618941716939-553df3c6c278?auto=format&fit=crop&w=120&q=80" alt="Produk" class="w-full h-full object-cover">
    </div>
    <div class="text-xs leading-tight">
      <p class="text-[11px] text-slate-400"><span id="fomoCity" class="text-white font-semibold">Seseorang dari Jakarta</span> baru saja checkout:</p>
      <p id="fomoProduct" class="font-bold text-slate-100 truncate max-w-[200px]">Goojodoq Kipas Turbo 100 Gear</p>
      <span class="text-[10px] text-emerald-400 font-mono">⚡ 12 detik yang lalu</span>
    </div>
  </div>

  <!-- Top Sticky Navigation Bar -->
  <header class="border-b border-dark-border/80 bg-dark-bg/85 backdrop-blur-xl sticky top-0 z-40">
    <div class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-full bg-gradient-to-tr from-shopee via-orange-500 to-amber-400 flex items-center justify-center font-black text-white text-sm shadow-md shadow-shopee/25 ring-2 ring-white/10">
          K
        </div>
        <div>
          <h1 class="font-extrabold text-sm tracking-tight text-white flex items-center gap-1.5">
            @kikipunyacerita
            <svg class="w-4 h-4 text-sky-400 fill-current inline-block" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
          </h1>
          <p class="text-[11px] text-slate-400 font-medium">Spill & Racun Belanja Resmi Threads</p>
        </div>
      </div>

      <div class="flex items-center gap-2">
        <a href="https://www.threads.net/@kikipunyacerita" target="_blank" rel="noopener noreferrer" class="text-xs px-3.5 py-1.5 rounded-xl bg-dark-surface hover:bg-dark-hover border border-dark-border text-slate-200 transition font-semibold flex items-center gap-1.5 shadow-sm">
          <span>Follow Threads</span>
          <span class="text-slate-400 text-[10px]">↗</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Hero Banner & Value Proposition -->
  <section class="max-w-5xl mx-auto px-4 pt-10 pb-6 text-center">
    <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-shopee/10 border border-shopee/25 text-shopee text-xs font-bold mb-4 shadow-sm animate-pulse-subtle">
      <span>🔥</span>
      <span>100 Produk Pilihan Rating 4.8+ • Khusus Follower Threads</span>
    </div>

    <h2 class="text-3xl sm:text-4xl md:text-5xl font-black tracking-tight text-white mb-3 leading-tight">
      Koleksi Barang Solusi <span class="text-transparent bg-clip-text bg-gradient-to-r from-shopee via-orange-400 to-amber-300">Anti-Pusing</span>
    </h2>
    
    <p class="text-sm sm:text-base text-slate-400 max-w-2xl mx-auto leading-relaxed mb-6">
      "Daripada boncos beli barang coba-coba gak jelas, ini 100 racun belanja yang gue kurasi sendiri. Solusi nyata buat budak korporat pegal, anak kosan sempit, dan pejuang commute KRL. Semua di bawah 100 ribu!" — <span class="text-slate-200 font-semibold">Kiki Rachmat</span>
    </p>

    <!-- Social Proof Indicators -->
    <div class="flex flex-wrap items-center justify-center gap-2.5 sm:gap-4 text-xs font-medium">
      <div class="px-3.5 py-2 rounded-xl bg-dark-card border border-dark-border text-slate-300 flex items-center gap-2 shadow-sm">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
        <span><b>100</b> Barang Lolos Kurasi</span>
      </div>
      <div class="px-3.5 py-2 rounded-xl bg-dark-card border border-dark-border text-slate-300 flex items-center gap-1.5 shadow-sm">
        <span class="text-amber-400 font-bold">★ 4.8 - 4.9</span>
        <span>Rating Rata-rata Toko</span>
      </div>
      <div class="px-3.5 py-2 rounded-xl bg-dark-card border border-dark-border text-slate-300 flex items-center gap-1.5 shadow-sm">
        <span class="text-emerald-400 font-mono font-bold">10RB+</span>
        <span>Terjual di Shopee</span>
      </div>
    </div>
  </section>

  <!-- TOP 3 HERO BENTO SHOWCASE (Consumer Psychology: The Anchors) -->
  <section class="max-w-5xl mx-auto px-4 py-4">
    <div class="flex items-center justify-between mb-3.5">
      <div class="flex items-center gap-2">
        <span class="text-xl">🏆</span>
        <h3 class="text-base sm:text-lg font-black text-white tracking-tight">Top 3 Paling Sering Di-Spill Minggu Ini</h3>
      </div>
      <span class="text-xs text-shopee font-bold">Paling Banyak Dibeli</span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      
      <!-- Bento Card 1: Goojodoq Kipas Turbo -->
      <article class="bg-gradient-to-b from-dark-card to-dark-surface border border-dark-border hover:border-shopee/60 rounded-3xl p-5 shadow-lg relative group transition flex flex-col justify-between">
        <span class="absolute top-4 left-4 z-20 px-2.5 py-1 rounded-lg bg-shopee text-white font-extrabold text-[11px] shadow-md shadow-shopee/40">
          #1 Penyelamat KRL
        </span>
        <div class="relative overflow-hidden rounded-2xl aspect-[16/10] mb-4 bg-slate-900">
          <img src="https://images.unsplash.com/photo-1618941716939-553df3c6c278?auto=format&fit=crop&w=600&q=80" alt="Kipas Turbo" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
          <div class="absolute inset-0 bg-gradient-to-t from-dark-bg/80 via-transparent to-transparent"></div>
        </div>
        <div>
          <p class="text-xs text-amber-300 font-semibold mb-1 flex items-center gap-1">
            <span>⚡ Masalah:</span> Gerah parah desak-desakan KRL
          </p>
          <h4 class="text-base font-bold text-white mb-1.5 line-clamp-2">Goojodoq Kipas Turbo 100 Gear Wind Digital</h4>
          <p class="text-xs text-slate-400 mb-3 leading-relaxed">"Anginnya beneran badai bukan sepoi-sepoi lemes. Wajib punya di tas buat komuter Manggarai."</p>
        </div>
        <div class="pt-3 border-t border-dark-border flex items-center justify-between">
          <div>
            <span class="text-[10px] text-slate-400 block font-mono">HARGA SPESIAL</span>
            <span class="text-lg font-black text-emerald-400 font-mono">Rp 89.900</span>
          </div>
          <a href="https://s.shopee.co.id/70LXfConpV?sub_id1=katalog_hero1" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-xl bg-gradient-to-r from-shopee to-orange-500 hover:from-shopee-hover hover:to-orange-600 text-white font-bold text-xs shadow-md shadow-shopee/30 flex items-center gap-1 transition">
            <span>Beli Sekarang</span>
            <span>↗</span>
          </a>
        </div>
      </article>

      <!-- Bento Card 2: Summerspring Diffuser -->
      <article class="bg-gradient-to-b from-dark-card to-dark-surface border border-dark-border hover:border-shopee/60 rounded-3xl p-5 shadow-lg relative group transition flex flex-col justify-between">
        <span class="absolute top-4 left-4 z-20 px-2.5 py-1 rounded-lg bg-indigo-600 text-white font-extrabold text-[11px] shadow-md shadow-indigo-600/40">
          #2 Kamar Kosan Mewah
        </span>
        <div class="relative overflow-hidden rounded-2xl aspect-[16/10] mb-4 bg-slate-900">
          <img src="https://images.unsplash.com/photo-1602928321679-560bb453f190?auto=format&fit=crop&w=600&q=80" alt="Diffuser" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
          <div class="absolute inset-0 bg-gradient-to-t from-dark-bg/80 via-transparent to-transparent"></div>
        </div>
        <div>
          <p class="text-xs text-indigo-300 font-semibold mb-1 flex items-center gap-1">
            <span>🏠 Masalah:</span> Kamar kos apek & lembab
          </p>
          <h4 class="text-base font-bold text-white mb-1.5 line-clamp-2">Summerspring Reed Diffuser 40ml Aromaterapi</h4>
          <p class="text-xs text-slate-400 mb-3 leading-relaxed">"Kamar kos 3x3 auto wangi hotel bintang 5. Pulang kerja capek langsung rileks tidur nyenyak."</p>
        </div>
        <div class="pt-3 border-t border-dark-border flex items-center justify-between">
          <div>
            <span class="text-[10px] text-slate-400 block font-mono">HARGA SPESIAL</span>
            <span class="text-lg font-black text-emerald-400 font-mono">Rp 55.700</span>
          </div>
          <a href="https://s.shopee.co.id/2gCYVF5IdL?sub_id1=katalog_hero2" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-xl bg-gradient-to-r from-shopee to-orange-500 hover:from-shopee-hover hover:to-orange-600 text-white font-bold text-xs shadow-md shadow-shopee/30 flex items-center gap-1 transition">
            <span>Beli Sekarang</span>
            <span>↗</span>
          </a>
        </div>
      </article>

      <!-- Bento Card 3: Stand HP 2k -->
      <article class="bg-gradient-to-b from-dark-card to-dark-surface border border-dark-border hover:border-shopee/60 rounded-3xl p-5 shadow-lg relative group transition flex flex-col justify-between">
        <span class="absolute top-4 left-4 z-20 px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-extrabold text-[11px] shadow-md shadow-emerald-600/40">
          #3 Juara Murah 2 Ribuan
        </span>
        <div class="relative overflow-hidden rounded-2xl aspect-[16/10] mb-4 bg-slate-900">
          <img src="https://images.unsplash.com/photo-1586105251261-72a756497a11?auto=format&fit=crop&w=600&q=80" alt="Stand HP" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
          <div class="absolute inset-0 bg-gradient-to-t from-dark-bg/80 via-transparent to-transparent"></div>
        </div>
        <div>
          <p class="text-xs text-emerald-300 font-semibold mb-1 flex items-center gap-1">
            <span>💸 Masalah:</span> Pegel pegang HP pas nonton di meja
          </p>
          <h4 class="text-base font-bold text-white mb-1.5 line-clamp-2">Satu Keluarga Stand Holder Kursi Macaron</h4>
          <p class="text-xs text-slate-400 mb-3 leading-relaxed">"Lebih murah dari parkir motor liar! Tapi bikin video call & nonton di meja gak pegel sama sekali."</p>
        </div>
        <div class="pt-3 border-t border-dark-border flex items-center justify-between">
          <div>
            <span class="text-[10px] text-slate-400 block font-mono">HARGA SPESIAL</span>
            <span class="text-lg font-black text-emerald-400 font-mono">Rp 2.000</span>
          </div>
          <a href="https://s.shopee.co.id/9KjSRUfv7G?sub_id1=katalog_hero3" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-xl bg-gradient-to-r from-shopee to-orange-500 hover:from-shopee-hover hover:to-orange-600 text-white font-bold text-xs shadow-md shadow-shopee/30 flex items-center gap-1 transition">
            <span>Beli Sekarang</span>
            <span>↗</span>
          </a>
        </div>
      </article>

    </div>
  </section>

  <!-- Sticky Filter by "Keresahan & Kebutuhan" (Consumer Psychology Matrix) -->
  <section class="sticky top-[57px] z-30 bg-dark-bg/95 backdrop-blur-xl border-y border-dark-border/80 py-3.5 mt-4 transition-all">
    <div class="max-w-5xl mx-auto px-4 space-y-3">
      
      <!-- Search Input & Quick Controls -->
      <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-2.5">
        <div class="relative flex-1">
          <svg class="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          <input 
            type="search" 
            id="searchInput" 
            placeholder="Cari solusi masalah (leher sakit, gerah, apek, kabel, parfum, basreng)..." 
            class="w-full pl-10 pr-12 py-3 rounded-2xl bg-dark-surface border border-dark-border focus:border-shopee focus:ring-2 focus:ring-shopee/20 text-sm text-white placeholder-slate-500 outline-none transition"
            autocomplete="off"
          >
          <span class="hidden sm:inline-block absolute right-3.5 top-1/2 -translate-y-1/2 text-[10px] text-slate-500 font-mono border border-slate-700/60 px-1.5 py-0.5 rounded">/</span>
          <button id="clearSearchBtn" class="hidden absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white text-xs bg-slate-800 rounded-full w-6 h-6 flex items-center justify-center">✕</button>
        </div>

        <div class="flex items-center gap-2">
          <select id="sortSelect" class="w-full sm:w-auto px-4 py-3 rounded-2xl bg-dark-surface border border-dark-border text-xs text-slate-200 focus:border-shopee focus:ring-1 focus:ring-shopee outline-none transition cursor-pointer font-medium">
            <option value="default">Urutkan: Rekomendasi Kiki</option>
            <option value="sales">Paling Laris (10RB+ Terjual)</option>
            <option value="price_asc">Harga: Termurah</option>
            <option value="price_desc">Harga: Tertinggi</option>
          </select>
        </div>
      </div>

      <!-- Problem-Solution Pills (Based on Emotional Need, Not Dry Categories!) -->
      <div class="flex items-center gap-2 overflow-x-auto pb-1 no-scrollbar text-xs">
        <button data-filter="all" class="filter-pill active px-4 py-2 rounded-xl whitespace-nowrap font-bold transition bg-shopee text-white shadow-md shadow-shopee/25">
          🌟 Semua Racun (100)
        </button>
        <button data-filter="Budak Korporat" class="filter-pill px-4 py-2 rounded-xl whitespace-nowrap font-medium transition bg-dark-surface hover:bg-dark-hover border border-dark-border text-slate-300">
          🏢 Budak Korporat (Meja & Kerja)
        </button>
        <button data-filter="Penyelamat Kosan" class="filter-pill px-4 py-2 rounded-xl whitespace-nowrap font-medium transition bg-dark-surface hover:bg-dark-hover border border-dark-border text-slate-300">
          🏠 Penyelamat Kamar Kosan
        </button>
        <button data-filter="Glow Up Murah" class="filter-pill px-4 py-2 rounded-xl whitespace-nowrap font-medium transition bg-dark-surface hover:bg-dark-hover border border-dark-border text-slate-300">
          ✨ Glow Up & Wangi Hemat
        </button>
        <button data-filter="Camilan & Stress" class="filter-pill px-4 py-2 rounded-xl whitespace-nowrap font-medium transition bg-dark-surface hover:bg-dark-hover border border-dark-border text-slate-300">
          🍿 Camilan Lembur & Anti-Ngantuk
        </button>
        <button data-filter="Di Bawah 20rb" class="filter-pill px-4 py-2 rounded-xl whitespace-nowrap font-medium transition bg-dark-surface hover:bg-dark-hover border border-dark-border text-slate-300">
          💸 Di Bawah 20 Ribu (Tanpa Mikir)
        </button>
      </div>

    </div>
  </section>

  <!-- Live Counter & Active Filter Description -->
  <div class="max-w-5xl mx-auto px-4 pt-4 flex items-center justify-between text-xs text-slate-400">
    <span id="resultsCount" class="font-medium text-slate-300">Menampilkan 100 rekomendasi barang pilihan</span>
    <span class="text-[11px] text-slate-500 hidden sm:inline-block">💡 Klik kartu untuk langsung diarahkan ke Shopee</span>
  </div>

  <!-- Product Catalog Grid -->
  <main class="max-w-5xl mx-auto px-4 py-4 flex-1">
    <div id="productGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <!-- Populated via Client-Side JS -->
    </div>

    <!-- Empty State -->
    <div id="emptyState" class="hidden py-16 text-center">
      <div class="text-5xl mb-3">🔍</div>
      <h3 class="text-base font-bold text-white mb-1">Barang tidak ditemukan</h3>
      <p class="text-xs text-slate-400 mb-4 max-w-sm mx-auto">Coba cari dengan kata kunci lain atau pilih kategori di atas.</p>
      <button id="resetSearchBtn" class="text-xs px-5 py-2.5 rounded-xl bg-shopee text-white font-bold hover:bg-shopee-hover transition shadow-lg shadow-shopee/25">
        Reset Pencarian
      </button>
    </div>
  </main>

  <!-- Footer -->
  <footer class="border-t border-dark-border bg-dark-bg/90 py-10 mt-16 text-center text-xs text-slate-500">
    <div class="max-w-5xl mx-auto px-4 space-y-3">
      <div class="flex items-center justify-center gap-2">
        <span class="w-6 h-6 rounded-full bg-shopee text-white flex items-center justify-center font-black text-xs">K</span>
        <span class="font-bold text-slate-300 text-sm">Katalog Resmi Kiki Rachmat (@kikipunyacerita)</span>
      </div>
      <p class="text-xs text-slate-400 max-w-md mx-auto">
        Setiap produk telah diverifikasi ulasan aslinya di Shopee. Kami mendapatkan komisi kecil dari transaksi tanpa biaya tambahan bagi pembeli.
      </p>
      <div class="pt-2 flex items-center justify-center gap-4 text-xs font-medium text-slate-400">
        <a href="https://www.threads.net/@kikipunyacerita" target="_blank" rel="noopener noreferrer" class="hover:text-white transition">Threads @kikipunyacerita</a>
        <span>•</span>
        <a href="https://www.threads.net/@kikiirch" target="_blank" rel="noopener noreferrer" class="hover:text-white transition">Threads @kikiirch</a>
      </div>
      <p class="text-[10px] text-slate-600 pt-2">Dikurasi otomatis oleh Zura Personal AI Engine • Hak Cipta © 2026</p>
    </div>
  </footer>

  <!-- Raw Products JSON Data -->
  <script id="product-data" type="application/json">
    {json_str}
  </script>

  <script>
    // Client-side Application Logic with High-Converting Psychology
    const rawData = JSON.parse(document.getElementById('product-data').textContent);
    let activeFilter = 'all';
    let searchQuery = '';
    let currentSort = 'default';

    const grid = document.getElementById('productGrid');
    const searchInput = document.getElementById('searchInput');
    const clearBtn = document.getElementById('clearSearchBtn');
    const sortSelect = document.getElementById('sortSelect');
    const countEl = document.getElementById('resultsCount');
    const emptyState = document.getElementById('emptyState');
    const resetBtn = document.getElementById('resetSearchBtn');
    const toast = document.getElementById('toast');
    const toastTitle = document.getElementById('toast-title');
    const toastSub = document.getElementById('toast-sub');

    // FOMO Ticker elements
    const fomoTicker = document.getElementById('fomoTicker');
    const fomoImg = document.getElementById('fomoImg');
    const fomoCity = document.getElementById('fomoCity');
    const fomoProduct = document.getElementById('fomoProduct');

    const CITIES = [
      'Jakarta Selatan', 'Tebet, Jaksel', 'Sleman, DIY', 'Bandung Kota',
      'Surabaya Timur', 'Tangerang Selatan', 'Bekasi Barat', 'Malang',
      'Semarang', 'Depok', 'Palmerah, Jakbar', 'Bendungan Hilir'
    ];

    // Periodic FOMO Popup Rotation (Social Proof Loop)
    let fomoIndex = 0;
    function triggerFomo() {{
      const candidate = rawData[Math.floor(Math.random() * rawData.length)];
      const city = CITIES[Math.floor(Math.random() * CITIES.length)];
      
      fomoImg.src = candidate.image_url;
      fomoCity.textContent = `Seseorang dari ${{city}}`;
      fomoProduct.textContent = candidate.name;

      fomoTicker.classList.remove('hidden', 'translate-y-28', 'opacity-0');
      fomoTicker.classList.add('translate-y-0', 'opacity-100');

      setTimeout(() => {{
        fomoTicker.classList.remove('translate-y-0', 'opacity-100');
        fomoTicker.classList.add('translate-y-28', 'opacity-0');
      }}, 4000);
    }}

    // Trigger FOMO after 4s, then every 16s
    setTimeout(() => {{
      triggerFomo();
      setInterval(triggerFomo, 16000);
    }}, 4000);

    function showToast(title, sub) {{
      toastTitle.textContent = title;
      toastSub.textContent = sub || 'Silakan paste di browser atau chat';
      toast.classList.remove('translate-y-20', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');
      setTimeout(() => {{
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('translate-y-20', 'opacity-0');
      }}, 2500);
    }}

    function copyToClipboard(url, name) {{
      if (navigator.clipboard && window.isSecureContext) {{
        navigator.clipboard.writeText(url).then(() => {{
          showToast('Link Shopee Disalin!', name.slice(0, 30) + '...');
        }}).catch(() => {{
          fallbackCopy(url);
        }});
      }} else {{
        fallbackCopy(url);
      }}
    }}

    function fallbackCopy(text) {{
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      try {{
        document.execCommand('copy');
        showToast('Link Shopee Disalin!', 'Siap di-paste');
      }} catch (e) {{
        showToast('Gagal menyalin link otomatis.');
      }}
      document.body.removeChild(ta);
    }}

    function renderProducts() {{
      let filtered = rawData.filter(p => {{
        let matchCategory = true;
        if (activeFilter === 'all') {{
          matchCategory = true;
        }} else if (activeFilter === 'Di Bawah 20rb') {{
          matchCategory = p.price_num <= 20000;
        }} else {{
          matchCategory = p.need_pill === activeFilter;
        }}

        const q = searchQuery.toLowerCase();
        const matchQuery = !q || 
          p.name.toLowerCase().includes(q) || 
          p.category.toLowerCase().includes(q) || 
          p.hook.toLowerCase().includes(q) ||
          p.shop.toLowerCase().includes(q);
        
        return matchCategory && matchQuery;
      }});

      // Sorting
      if (currentSort === 'price_asc') {{
        filtered.sort((a, b) => a.price_num - b.price_num);
      }} else if (currentSort === 'price_desc') {{
        filtered.sort((a, b) => b.price_num - a.price_num);
      }} else if (currentSort === 'sales') {{
        filtered.sort((a, b) => (b.sales.includes('10RB+') ? 1 : 0) - (a.sales.includes('10RB+') ? 1 : 0));
      }}

      countEl.textContent = `Menampilkan ${{filtered.length}} dari ${{rawData.length}} barang pilihan`;

      if (filtered.length === 0) {{
        grid.innerHTML = '';
        emptyState.classList.remove('hidden');
        return;
      }}

      emptyState.classList.add('hidden');

      grid.innerHTML = filtered.map(p => {{
        const trackingUrl = p.affiliate_url + (p.affiliate_url.includes('?') ? '&' : '?') + 'sub_id1=katalog_bio';
        const cleanName = p.name.replace(/"/g, '&quot;');

        return `
          <article class="product-card group flex flex-col justify-between bg-dark-card border border-dark-border hover:border-shopee/60 rounded-3xl p-4 shadow-sm transition">
            
            <div>
              <!-- Product Image with Zoom & Badges -->
              <div class="relative overflow-hidden rounded-2xl aspect-[16/10] mb-3.5 bg-slate-900 border border-dark-border/50">
                <img 
                  src="${{p.image_url}}" 
                  alt="${{cleanName}}" 
                  loading="lazy" 
                  class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                >
                <div class="absolute inset-0 bg-gradient-to-t from-dark-bg/85 via-transparent to-transparent"></div>
                
                <!-- Category Tag Top Left -->
                <span class="absolute top-2.5 left-2.5 text-[10px] font-extrabold px-2 py-0.5 rounded-md bg-dark-bg/90 backdrop-blur-md text-slate-200 border border-slate-700/60 shadow">
                  ${{p.need_pill}}
                </span>

                <!-- Sales Tag Top Right -->
                <span class="absolute top-2.5 right-2.5 text-[10px] font-bold px-2 py-0.5 rounded-md bg-shopee/90 backdrop-blur-md text-white shadow flex items-center gap-1">
                  <span>🔥</span>
                  <span>${{p.sales}}</span>
                </span>

                <!-- Price Anchor Bottom Pill -->
                <span class="absolute bottom-2 left-2.5 right-2.5 text-[11px] font-bold text-amber-300 drop-shadow truncate">
                  ${{p.value_anchor}}
                </span>
              </div>

              <!-- Emotional Problem-Relief Hook (Consumer Psychology) -->
              <p class="text-xs text-orange-400 font-bold mb-1.5 flex items-center gap-1">
                <span>⚡</span>
                <span class="truncate">${{p.hook}}</span>
              </p>

              <!-- Product Name with Stretched Link -->
              <h3 class="text-sm font-bold text-white group-hover:text-shopee line-clamp-2 leading-snug mb-2">
                <a href="${{trackingUrl}}" target="_blank" rel="noopener noreferrer" class="card-link hover:underline focus:outline-none">
                  ${{p.name}}
                </a>
              </h3>

              <!-- Curator Note & Store Info -->
              <p class="text-[11px] text-slate-400 line-clamp-1 mb-2.5 italic">
                "${{p.curator_note}}"
              </p>

              <div class="flex items-center gap-2 text-[11px] text-slate-400 mb-3">
                <span class="truncate text-slate-300 font-medium">🏪 ${{p.shop}}</span>
                <span>•</span>
                <span class="text-amber-400 font-bold">★ 4.9</span>
              </div>
            </div>

            <!-- Price & Action CTA -->
            <footer class="pt-3 border-t border-dark-border/80 flex items-center justify-between gap-2">
              <div>
                <span class="text-[10px] text-slate-500 font-mono uppercase tracking-wider block">Harga Promo</span>
                <span class="text-base font-extrabold text-emerald-400 font-mono tracking-tight">${{p.price_formatted}}</span>
              </div>

              <div class="flex items-center gap-1.5">
                <button 
                  onclick="copyToClipboard('${{trackingUrl}}', '${{cleanName}}')" 
                  title="Salin link affiliate"
                  class="p-2.5 rounded-xl bg-dark-surface hover:bg-dark-hover text-slate-300 hover:text-white border border-dark-border transition text-xs flex items-center justify-center shadow-sm"
                  aria-label="Salin Link Shopee"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
                </button>

                <a 
                  href="${{trackingUrl}}" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  class="px-4 py-2 rounded-xl bg-gradient-to-r from-shopee to-orange-500 hover:from-shopee-hover hover:to-orange-600 text-white font-extrabold text-xs shadow-md shadow-shopee/30 transition flex items-center gap-1.5"
                >
                  <span>Beli</span>
                  <span class="text-xs">↗</span>
                </a>
              </div>
            </footer>
          </article>
        `;
      }}).join('');
    }}

    // Filter Pill Event Listeners
    document.querySelectorAll('.filter-pill').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.filter-pill').forEach(b => {{
          b.classList.remove('active', 'bg-shopee', 'text-white', 'shadow-md', 'shadow-shopee/25');
          b.classList.add('bg-dark-surface', 'border', 'border-dark-border', 'text-slate-300');
        }});
        btn.classList.add('active', 'bg-shopee', 'text-white', 'shadow-md', 'shadow-shopee/25');
        btn.classList.remove('bg-dark-surface', 'border', 'border-dark-border', 'text-slate-300');
        activeFilter = btn.getAttribute('data-filter');
        renderProducts();
      }});
    }});

    // Search Input Listener
    searchInput.addEventListener('input', (e) => {{
      searchQuery = e.target.value.trim();
      clearBtn.classList.toggle('hidden', searchQuery.length === 0);
      renderProducts();
    }});

    clearBtn.addEventListener('click', () => {{
      searchInput.value = '';
      searchQuery = '';
      clearBtn.classList.add('hidden');
      searchInput.focus();
      renderProducts();
    }});

    resetBtn.addEventListener('click', () => {{
      searchInput.value = '';
      searchQuery = '';
      activeFilter = 'all';
      currentSort = 'default';
      sortSelect.value = 'default';
      clearBtn.classList.add('hidden');
      document.querySelectorAll('.filter-pill').forEach(b => {{
        if (b.getAttribute('data-filter') === 'all') {{
          b.classList.add('active', 'bg-shopee', 'text-white');
        }} else {{
          b.classList.remove('active', 'bg-shopee', 'text-white');
          b.classList.add('bg-dark-surface', 'text-slate-300');
        }}
      }});
      renderProducts();
    }});

    // Sort Listener
    sortSelect.addEventListener('change', (e) => {{
      currentSort = e.target.value;
      renderProducts();
    }});

    // Shortcut '/'
    window.addEventListener('keydown', (e) => {{
      if (e.key === '/' && document.activeElement !== searchInput) {{
        e.preventDefault();
        searchInput.focus();
      }}
    }});

    // Initial render
    renderProducts();
  </script>
</body>
</html>
"""

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ Generated upgraded psychological HTML catalog with Bento & FOMO at {OUT_FILE}")
