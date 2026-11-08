import json
from pathlib import Path

DATA_FILE = Path("/Users/kiki/Documents/Web Develop/katalog-ceritakiki/data/products.json")
OUT_FILE = Path("/Users/kiki/Documents/Web Develop/katalog-ceritakiki/index.html")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    products = json.load(f)

json_str = json.dumps(products, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="id" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Katalog Spill & Rekomendasi Kiki (@kikipunyacerita)</title>
  <meta name="description" content="Koleksi rekomendasi produk Shopee Affiliate terkurasi oleh Kiki Rachmat (@kikipunyacerita) di Threads. Solusi praktis & anti-pusing untuk budak korporat, anak kos, dan pejuang commute.">
  <meta name="theme-color" content="#0a0a0f">
  
  <!-- OpenGraph Meta -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="Katalog Spill & Rekomendasi Kiki (@kikipunyacerita)">
  <meta property="og:description" content="100+ Barang Pilihan Solusi Anti-Pusing: Desk Setup, Kosan Hacks, Skincare Murah & Essentials.">
  <meta property="og:image" content="https://images.unsplash.com/photo-1512436991641-6745cdb1723f?q=80&w=1200&auto=format&fit=crop">
  <meta property="og:site_name" content="Kisah Komisi by Kiki Rachmat">

  <!-- Fonts & Tailwind -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
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
              light: '#fff5f1'
            }},
            dark: {{
              bg: '#090a10',
              surface: '#12141f',
              border: '#1f2335',
              hover: '#191c2c'
            }}
          }}
        }}
      }}
    }}
  </script>

  <style>
    /* Modern Container Queries & Styling rules adhering to modern-web-guidance */
    .card-container {{
      container-type: inline-size;
    }}
    
    .product-card {{
      position: relative;
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s ease, border-color 0.2s ease;
    }}
    
    .product-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 12px 30px -10px rgba(0, 0, 0, 0.5), 0 0 20px -5px rgba(238, 77, 45, 0.15);
    }}

    .product-card a.card-link::after {{
      content: "";
      position: absolute;
      inset: 0;
      border-radius: 1rem;
    }}

    /* Elevated controls above stretched link */
    .product-card a:not(.card-link), 
    .product-card button {{
      position: relative;
      z-index: 10;
    }}

    /* Smooth Custom Scrollbar */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #090a10;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #222638;
      border-radius: 9999px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #3b4261;
    }}

    /* Dynamic viewport container */
    .viewport-box {{
      min-height: 100dvh;
    }}

    /* Glow backdrop */
    .ambient-glow {{
      background: radial-gradient(circle at 50% 0%, rgba(238, 77, 45, 0.12) 0%, rgba(99, 102, 241, 0.08) 35%, transparent 70%);
    }}
  </style>
</head>
<body class="bg-dark-bg text-slate-100 font-sans antialiased selection:bg-shopee selection:text-white viewport-box flex flex-col ambient-glow">

  <!-- Toast Notification -->
  <aside id="toast" role="status" aria-live="polite" class="fixed bottom-6 right-6 z-50 transform translate-y-20 opacity-0 transition-all duration-300 pointer-events-none flex items-center gap-3 bg-slate-900/95 backdrop-blur-md text-white border border-slate-700/80 px-4 py-3 rounded-xl shadow-2xl">
    <span class="text-emerald-400 text-lg">✓</span>
    <span id="toast-text" class="text-sm font-medium">Link Shopee berhasil disalin!</span>
  </aside>

  <!-- Sticky Top Banner / Brand -->
  <header class="border-b border-dark-border/60 bg-dark-bg/80 backdrop-blur-xl sticky top-0 z-40">
    <div class="max-w-4xl mx-auto px-4 py-3.5 flex items-center justify-between">
      <div class="flex items-center gap-2.5">
        <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-shopee via-orange-500 to-amber-400 flex items-center justify-center font-bold text-white text-xs shadow-md shadow-shopee/20">
          KK
        </div>
        <div>
          <h1 class="font-bold text-sm tracking-tight text-white flex items-center gap-1.5">
            @kikipunyacerita
            <svg class="w-4 h-4 text-sky-400 fill-current inline-block" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
          </h1>
          <p class="text-[11px] text-slate-400">Kurasi Spill & Rekomendasi Threads</p>
        </div>
      </div>

      <div class="flex items-center gap-2">
        <a href="https://www.threads.net/@kikipunyacerita" target="_blank" rel="noopener noreferrer" class="text-xs px-3 py-1.5 rounded-lg bg-dark-surface hover:bg-dark-hover border border-dark-border text-slate-200 transition font-medium flex items-center gap-1.5">
          <span>Threads</span>
          <span class="text-slate-400 text-[10px]">↗</span>
        </a>
        <a href="https://www.threads.net/@kikiirch" target="_blank" rel="noopener noreferrer" class="text-xs px-3 py-1.5 rounded-lg bg-dark-surface hover:bg-dark-hover border border-dark-border text-slate-400 hover:text-slate-200 transition font-medium hidden sm:inline-flex items-center gap-1">
          <span>Akun Utama</span>
          <span class="text-slate-400 text-[10px]">↗</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Profile & Hero Bio -->
  <section class="max-w-4xl mx-auto px-4 pt-8 pb-6 text-center">
    <div class="relative inline-block mb-4">
      <div class="w-24 h-24 rounded-full p-1 bg-gradient-to-tr from-shopee via-purple-500 to-indigo-500 shadow-xl shadow-shopee/10 mx-auto">
        <div class="w-full h-full rounded-full bg-dark-surface border-2 border-dark-bg flex items-center justify-center text-2xl font-black text-white">
          ✨
        </div>
      </div>
      <span class="absolute bottom-1 right-1 bg-emerald-500 w-4 h-4 rounded-full border-2 border-dark-bg" title="Aktif di Threads"></span>
    </div>

    <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-white mb-2">
      Koleksi Spill & Solusi Anti-Pusing
    </h2>
    <p class="text-sm sm:text-base text-slate-400 max-w-xl mx-auto leading-relaxed mb-6">
      Kurasi 100 barang penunjang hidup anak rantau, pejuang kosan, dan budak korporat. Harga ramah kantong di bawah 100rb, rating toko 4.8+, dan lolos kurasi nyata.
    </p>

    <!-- Key Metrics Badges -->
    <div class="flex flex-wrap items-center justify-center gap-2 sm:gap-3 text-xs">
      <div class="px-3 py-1.5 rounded-full bg-dark-surface/90 border border-dark-border text-slate-300 flex items-center gap-1.5 shadow-sm">
        <span class="text-orange-400 font-bold">100</span>
        <span>Produk Terverifikasi</span>
      </div>
      <div class="px-3 py-1.5 rounded-full bg-dark-surface/90 border border-dark-border text-slate-300 flex items-center gap-1.5 shadow-sm">
        <span class="text-amber-400">★ 4.8+</span>
        <span>Rating Shopee</span>
      </div>
      <div class="px-3 py-1.5 rounded-full bg-dark-surface/90 border border-dark-border text-slate-300 flex items-center gap-1.5 shadow-sm">
        <span class="text-emerald-400 font-bold">95%</span>
        <span>Di Bawah Rp 90.000</span>
      </div>
    </div>
  </section>

  <!-- Sticky Filter & Search Control Panel -->
  <section class="sticky top-[57px] z-30 bg-dark-bg/95 backdrop-blur-xl border-y border-dark-border/80 py-3 transition-all">
    <div class="max-w-4xl mx-auto px-4 space-y-3">
      
      <!-- Search Input & Sort Options -->
      <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-2.5">
        <div class="relative flex-1">
          <svg class="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          <input 
            type="search" 
            id="searchInput" 
            placeholder="Cari barang spill (kipas, diffuser, kabel, tawas, snack)..." 
            class="w-full pl-10 pr-10 py-2.5 rounded-xl bg-dark-surface border border-dark-border focus:border-shopee focus:ring-1 focus:ring-shopee text-sm text-white placeholder-slate-500 outline-none transition"
            autocomplete="off"
          >
          <button id="clearSearchBtn" class="hidden absolute right-3 top-1/2 -translate-y-1/2 text-slate-500 hover:text-slate-300 text-xs bg-slate-800 rounded-full w-5 h-5 flex items-center justify-center">✕</button>
        </div>

        <div class="flex items-center gap-2">
          <select id="sortSelect" class="w-full sm:w-auto px-3 py-2.5 rounded-xl bg-dark-surface border border-dark-border text-xs text-slate-300 focus:border-shopee focus:ring-1 focus:ring-shopee outline-none transition cursor-pointer">
            <option value="default">Urutkan: Rekomendasi</option>
            <option value="price_asc">Harga: Termurah</option>
            <option value="price_desc">Harga: Tertinggi</option>
            <option value="sales">Terlaris (10RB+)</option>
          </select>
        </div>
      </div>

      <!-- Category Filter Pills -->
      <div class="flex items-center gap-1.5 overflow-x-auto pb-1 no-scrollbar text-xs">
        <button data-cat="all" class="cat-pill active px-3.5 py-1.5 rounded-lg whitespace-nowrap font-medium transition bg-shopee text-white shadow-sm shadow-shopee/20">
          🌟 Semua (100)
        </button>
        <button data-cat="Rumah Tangga & Kosan" class="cat-pill px-3.5 py-1.5 rounded-lg whitespace-nowrap font-medium transition bg-dark-surface hover:bg-dark-hover border border-dark-border text-slate-300">
          🏠 Kosan & Kamar (34)
        </button>
        <button data-cat="Skincare & Perawatan" class="cat-pill px-3.5 py-1.5 rounded-lg whitespace-nowrap font-medium transition bg-dark-surface hover:bg-dark-hover border border-dark-border text-slate-300">
          💆 Skincare & Grooming (27)
        </button>
        <button data-cat="Elektronik & Gadget" class="cat-pill px-3.5 py-1.5 rounded-lg whitespace-nowrap font-medium transition bg-dark-surface hover:bg-dark-hover border border-dark-border text-slate-300">
          💻 Desk & Gadget (14)
        </button>
        <button data-cat="Camilan & Makanan" class="cat-pill px-3.5 py-1.5 rounded-lg whitespace-nowrap font-medium transition bg-dark-surface hover:bg-dark-hover border border-dark-border text-slate-300">
          🍿 Camilan & Relaks (14)
        </button>
        <button data-cat="Fashion & Outfit" class="cat-pill px-3.5 py-1.5 rounded-lg whitespace-nowrap font-medium transition bg-dark-surface hover:bg-dark-hover border border-dark-border text-slate-300">
          🎒 Daily Essentials (11)
        </button>
      </div>

    </div>
  </section>

  <!-- Live Status & Counter -->
  <div class="max-w-4xl mx-auto px-4 pt-4 flex items-center justify-between text-xs text-slate-400">
    <span id="resultsCount">Menampilkan 100 rekomendasi</span>
    <span class="text-[11px] text-slate-500">Klik kartu untuk langsung menuju Shopee</span>
  </div>

  <!-- Product Catalog Grid -->
  <main class="max-w-4xl mx-auto px-4 py-4 flex-1">
    <div id="productGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5 card-container">
      <!-- Populated via Client-Side JS -->
    </div>

    <!-- Empty State -->
    <div id="emptyState" class="hidden py-16 text-center">
      <div class="text-4xl mb-3">🔍</div>
      <h3 class="text-base font-bold text-white mb-1">Barang tidak ditemukan</h3>
      <p class="text-xs text-slate-400 mb-4">Coba cari dengan kata kunci lain (contoh: kipas, sandal, sabun, charger)</p>
      <button id="resetSearchBtn" class="text-xs px-4 py-2 rounded-lg bg-dark-surface border border-dark-border text-shopee font-medium hover:bg-dark-hover transition">
        Reset Pencarian
      </button>
    </div>
  </main>

  <!-- Footer -->
  <footer class="border-t border-dark-border bg-dark-bg py-8 mt-12 text-center text-xs text-slate-500">
    <div class="max-w-4xl mx-auto px-4 space-y-2">
      <p class="font-medium text-slate-400">Koleksi Rekomendasi Resmi Kiki Rachmat (@kikipunyacerita)</p>
      <p class="text-[11px]">Dikurasi dan dipantau secara otomatis oleh <span class="text-slate-300">Zura Personal AI</span> • Shopee Affiliate Program</p>
      <p class="text-[10px] text-slate-600">Hak Cipta © 2026 Kiki Rachmat. Seluruh hak cipta dilindungi undang-undang.</p>
    </div>
  </footer>

  <!-- Raw Products JSON Data -->
  <script id="product-data" type="application/json">
    {json_str}
  </script>

  <script>
    // Client-side Application Logic
    const rawData = JSON.parse(document.getElementById('product-data').textContent);
    let currentCategory = 'all';
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
    const toastText = document.getElementById('toast-text');

    function showToast(msg) {{
      toastText.textContent = msg;
      toast.classList.remove('translate-y-20', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');
      setTimeout(() => {{
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('translate-y-20', 'opacity-0');
      }}, 2400);
    }}

    function copyToClipboard(url, name) {{
      if (navigator.clipboard && window.isSecureContext) {{
        navigator.clipboard.writeText(url).then(() => {{
          showToast(`Link "${{name.slice(0, 25)}}..." disalin!`);
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
        showToast('Link Shopee berhasil disalin!');
      }} catch (e) {{
        showToast('Gagal menyalin link otomatis.');
      }}
      document.body.removeChild(ta);
    }}

    function getCategoryIcon(cat) {{
      switch(cat) {{
        case 'Elektronik & Gadget': return '💻';
        case 'Rumah Tangga & Kosan': return '🏠';
        case 'Skincare & Perawatan': return '💆';
        case 'Camilan & Makanan': return '🍿';
        case 'Fashion & Outfit': return '🎒';
        default: return '🛍️';
      }}
    }}

    function renderProducts() {{
      let filtered = rawData.filter(p => {{
        const matchCat = currentCategory === 'all' || p.category === currentCategory;
        const q = searchQuery.toLowerCase();
        const matchQuery = !q || 
          p.name.toLowerCase().includes(q) || 
          p.category.toLowerCase().includes(q) || 
          p.shop.toLowerCase().includes(q);
        return matchCat && matchQuery;
      }});

      // Sorting
      if (currentSort === 'price_asc') {{
        filtered.sort((a, b) => a.price_num - b.price_num);
      }} else if (currentSort === 'price_desc') {{
        filtered.sort((a, b) => b.price_num - a.price_num);
      }} else if (currentSort === 'sales') {{
        filtered.sort((a, b) => (b.sales.includes('10RB+') ? 1 : 0) - (a.sales.includes('10RB+') ? 1 : 0));
      }}

      countEl.textContent = `Menampilkan ${{filtered.length}} dari ${{rawData.length}} rekomendasi`;

      if (filtered.length === 0) {{
        grid.innerHTML = '';
        emptyState.classList.remove('hidden');
        return;
      }}

      emptyState.classList.add('hidden');

      grid.innerHTML = filtered.map(p => {{
        const icon = getCategoryIcon(p.category);
        const trackingUrl = p.affiliate_url + (p.affiliate_url.includes('?') ? '&' : '?') + 'sub_id1=katalog_bio';
        const cleanName = p.name.replace(/"/g, '&quot;');

        return `
          <article class="product-card group flex flex-col justify-between bg-dark-surface/90 hover:bg-dark-hover border border-dark-border hover:border-shopee/40 rounded-2xl p-4 shadow-sm transition">
            <div>
              <!-- Header Region: Badge & Category -->
              <header class="flex items-center justify-between gap-2 mb-2.5">
                <span class="inline-flex items-center gap-1 text-[11px] font-semibold px-2.5 py-0.5 rounded-full bg-slate-800 text-slate-300 border border-slate-700/60">
                  <span>${{icon}}</span>
                  <span>${{p.category.split('&')[0].trim()}}</span>
                </span>
                <span class="text-[10px] font-bold text-shopee bg-shopee/10 px-2 py-0.5 rounded-md border border-shopee/20 whitespace-nowrap">
                  ${{p.badge}}
                </span>
              </header>

              <!-- Title & Stretched Card Link -->
              <h3 class="text-sm font-semibold text-slate-100 group-hover:text-white line-clamp-2 leading-snug mb-2">
                <a href="${{trackingUrl}}" target="_blank" rel="noopener noreferrer" class="card-link hover:underline focus:outline-none">
                  ${{p.name}}
                </a>
              </h3>

              <!-- Shop & Sales Info -->
              <div class="flex items-center gap-2 text-[11px] text-slate-400 mb-3">
                <span class="truncate max-w-[140px] text-slate-300 font-medium">🏪 ${{p.shop}}</span>
                <span>•</span>
                <span class="text-amber-400/90 whitespace-nowrap font-mono text-[10px]">${{p.sales}}</span>
              </div>
            </div>

            <!-- Footer Region: Price & Elevated Action Controls -->
            <footer class="pt-3 border-t border-dark-border/60 flex items-center justify-between gap-2">
              <div>
                <span class="text-[10px] text-slate-500 uppercase tracking-wider block font-mono">Harga Spesial</span>
                <span class="text-base font-extrabold text-emerald-400 font-mono tracking-tight">${{p.price_formatted}}</span>
              </div>

              <div class="flex items-center gap-1.5">
                <button 
                  onclick="copyToClipboard('${{trackingUrl}}', '${{cleanName}}')" 
                  title="Salin link affiliate"
                  class="p-2 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700/60 transition text-xs flex items-center justify-center"
                  aria-label="Salin Link Shopee"
                >
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
                </button>

                <a 
                  href="${{trackingUrl}}" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  class="px-3.5 py-1.5 rounded-xl bg-gradient-to-r from-shopee to-orange-500 hover:from-shopee-hover hover:to-orange-600 text-white font-bold text-xs shadow-md shadow-shopee/25 transition flex items-center gap-1"
                >
                  <span>Beli</span>
                  <span class="text-[10px]">↗</span>
                </a>
              </div>
            </footer>
          </article>
        `;
      }}).join('');
    }}

    // Category Pill Event Listeners
    document.querySelectorAll('.cat-pill').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.cat-pill').forEach(b => {{
          b.classList.remove('active', 'bg-shopee', 'text-white', 'shadow-sm', 'shadow-shopee/20');
          b.classList.add('bg-dark-surface', 'border', 'border-dark-border', 'text-slate-300');
        }});
        btn.classList.add('active', 'bg-shopee', 'text-white', 'shadow-sm', 'shadow-shopee/20');
        btn.classList.remove('bg-dark-surface', 'border', 'border-dark-border', 'text-slate-300');
        currentCategory = btn.getAttribute('data-cat');
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
      currentCategory = 'all';
      currentSort = 'default';
      sortSelect.value = 'default';
      clearBtn.classList.add('hidden');
      document.querySelectorAll('.cat-pill').forEach(b => {{
        if (b.getAttribute('data-cat') === 'all') {{
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

    // Keyboard shortcut '/' to search
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

print(f"✅ Generated production HTML with 100 products at {OUT_FILE}")
