import json
from pathlib import Path

DATA_FILE = Path("/Users/kiki/Documents/Web Develop/katalog-ceritakiki/data/products_enriched.json")
OUT_FILE = Path("/Users/kiki/Documents/Web Develop/katalog-ceritakiki/index.html")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    products = json.load(f)

# Simplify and tighten hooks: MAX 6-8 WORDS! Zero fluff!
SIMPLIFIED_HOOKS = {
    'kipas': 'Angin kencang penyelamat KRL',
    'basreng': 'Camilan pedas melek jam 3 sore',
    'masker': 'Napas lega gak nempel makeup',
    'tongsis': 'Tripod bluetooth 4-in-1 fleksibel',
    'detergen': 'Baju wangi segar jemur kosan',
    'ssd': 'Hardcase pelindung kabel & gadget',
    'pelindung kabel': 'Ujung kabel aman gak gampang robek',
    'buket': 'Kado wisuda aesthetic tahan lama',
    'case': 'Bodi HP aman dari benturan',
    'tas': 'Slingbag simpel muat HP & dompet',
    'parfum': 'Wangi vanilla tahan seharian',
    'buku': 'Panduan bangun kebiasaan baru',
    'gantungan kunci': 'Gantungan kunci liontin lucu',
    'sandal': 'Sandal empuk anti selip harian',
    'strap': 'Silicone strap nyaman seharian',
    'holder': 'Map dokumen rapi anti lecek',
    'moisturizer': 'Perbaiki skin barrier kering',
    'tawas': 'Deodorant tawas alami anti bau',
    'dryer': 'Rambut kering kilat 5 menit',
    'sunscreen': 'Sunscreen matte bebas kilap',
    'bedak': 'Touch up kilat samarkan pori',
    'lip': 'Lip cream matte transferproof',
    'body wash': 'Sabun mandi lembut wangi mewah',
    'diffuser': 'Kamar kos wangi hotel mewah',
    'tumbler': 'Tahan dingin es 12 jam hemat',
    'handuk': 'Handuk mandi lembut super serap',
    'setrika': 'Meja setrika lipat hemat tempat',
    'keset': 'Lantai cepat kering anti selip',
    'teko': 'Pitcher air dingin plus 8 gelas',
    'filter': 'Saring air keruh jadi bening',
    'talenan': 'Kayu jati perhutani kuat awet',
    'rak piring': 'Wastafel rapi piring cepat kering',
    'pel': 'Pel peras otomatis tanpa capek',
    'linen': 'Semprot kasur wangi bebas tungau',
    'bantal': 'Bantal duduk empuk anti pegal',
    'sepatu': 'Kotak sepatu transparan tumpuk',
    'panci': 'Panci mie anti lengket granite',
    'oat': 'Wadah overnight oat bonus sendok',
    'bumbu': 'Rak susun 3 bumbu dapur rapi',
    'cuci piring': 'Bersihkan minyak lemak seketika',
    'coklat': 'Selai coklat crunchy nagih',
    'lemon': 'Sari lemon murni detox harian',
    'muesli': 'Sereal oat sehat kenyang lama',
    'matcha': 'Pure matcha powder no sugar',
    'nugget': 'Lauk darurat sahur crispy nikmat',
    'troli': 'Troli roda serbaguna hemat ruang',
    'kulkas': 'Organizer pintu kulkas rapi',
    'phone': 'Stand HP nonton gak pegel',
    'toilet': 'Busa rontokkan kerak tanpa sikat',
    'squishy': 'Squishy empuk pelepas stress',
    'cushion': 'Cover bekas jerawat natural'
}

def get_short_hook(name):
    nl = name.lower()
    for k, v in SIMPLIFIED_HOOKS.items():
        if k in nl:
            return v
    return "Solusi praktis harga ramah kantong"

# Clean short title: Max 50 chars!
def get_clean_title(name):
    clean = name.split('|')[0].split('-')[0].strip()
    if len(clean) > 48:
        clean = clean[:45] + '...'
    return clean

for p in products:
    p['clean_title'] = get_clean_title(p['name'])
    p['short_hook'] = get_short_hook(p['name'])

json_str = json.dumps(products, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="id" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Kiki Rachmat — Curated Essentials (@kikipunyacerita)</title>
  <meta name="description" content="Katalog 100 produk pilihan solusi hidup anak rantau, kerja kantor, dan kosan. Dikurasi oleh Kiki Rachmat (@kikipunyacerita) di Threads.">
  <meta name="theme-color" content="#0A0A0A">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  
  <!-- OpenGraph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="Kiki Rachmat — Curated Essentials (@kikipunyacerita)">
  <meta property="og:description" content="100 barang solusi nyata meja kerja, kosan & commute di bawah 100k.">

  <!-- Typography matching Porto Web: Syne, Space Grotesk, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Space+Grotesk:wght@400;500;600;700&family=Syne:wght@700;800;900&display=swap" rel="stylesheet">
  
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            display: ['"Syne"', 'sans-serif'],
            sans: ['"Space Grotesk"', 'system-ui', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace']
          }},
          colors: {{
            bg: '#0A0A0A',
            surface: '#121212',
            surfaceBorder: 'rgba(255, 255, 255, 0.08)',
            surfaceHover: '#181818',
            accent: '#EE4D2D',
            accentHover: '#D73211'
          }}
        }}
      }}
    }}
  </script>

  <style>
    body {{
      background-color: #0A0A0A;
      color: #EDEDED;
      font-family: 'Space Grotesk', system-ui, sans-serif;
    }}

    .font-display {{
      font-family: 'Syne', sans-serif;
    }}

    .font-mono {{
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Containment for high performance scrolling (modern-web-guidance) */
    .product-card {{
      content-visibility: auto;
      contain-intrinsic-size: auto 300px auto 380px;
      position: relative;
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.2s ease, background-color 0.2s ease;
    }}

    .product-card:hover {{
      transform: translateY(-2px);
      border-color: rgba(255, 255, 255, 0.2);
    }}

    /* Stretched link pattern adhering to modern-web-guidance */
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

    /* Minimalist hairline borders */
    .hairline-border {{
      border: 1px solid rgba(255, 255, 255, 0.08);
    }}

    ::-webkit-scrollbar {{
      width: 5px;
    }}
    ::-webkit-scrollbar-track {{
      background: #0A0A0A;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #222222;
      border-radius: 9999px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #333333;
    }}
  </style>
</head>
<body class="selection:bg-accent/20 selection:text-accent min-h-screen flex flex-col">

  <!-- Minimalist Toast -->
  <aside id="toast" role="status" aria-live="polite" class="fixed bottom-6 right-6 z-50 transform translate-y-16 opacity-0 transition-all duration-200 pointer-events-none flex items-center gap-2.5 bg-[#161616] border border-white/10 px-4 py-2.5 rounded-xl shadow-2xl text-xs font-mono">
    <span class="text-accent">●</span>
    <span id="toast-text" class="text-white">Link Shopee disalin</span>
  </aside>

  <!-- Editorial Top Bar -->
  <header class="border-b border-white/[0.08] bg-[#0A0A0A]/90 backdrop-blur-md sticky top-0 z-40">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 py-4 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs uppercase tracking-widest text-gray-500">KIKI RACHMAT</span>
        <span class="text-gray-700">/</span>
        <span class="font-mono text-xs text-gray-300">@kikipunyacerita</span>
      </div>

      <div class="flex items-center gap-3 font-mono text-xs">
        <a href="https://www.threads.net/@kikipunyacerita" target="_blank" rel="noopener noreferrer" class="text-gray-400 hover:text-white transition flex items-center gap-1">
          <span>Threads</span>
          <span class="text-[10px]">↗</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Editorial Hero Section (Porto Web Vibe) -->
  <section class="w-full border-b border-white/[0.08]">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 pt-12 sm:pt-16 pb-10">
      <div class="max-w-3xl">
        <div class="inline-flex items-center gap-2 mb-4 font-mono text-[11px] uppercase tracking-widest text-accent">
          <span>●</span>
          <span>Curated Index • 100 Verified Items</span>
        </div>

        <h1 class="text-4xl sm:text-5xl md:text-6xl font-display font-black text-white uppercase tracking-tight leading-[0.95] mb-5">
          Curated<br/>Essentials.
        </h1>

        <p class="font-sans text-gray-400 text-sm sm:text-base leading-relaxed max-w-xl mb-6">
          Koleksi barang penunjang kerja, kosan, dan commute yang sering gue spill di Threads. Semua rating 4.8+ dan lolos filter kualitas tanpa gimmick.
        </p>

        <div class="flex items-center gap-4 font-mono text-xs text-gray-500">
          <div><span class="text-white font-bold">100</span> ITEMS</div>
          <span>•</span>
          <div><span class="text-white font-bold">4.8+</span> SHOPEE RATING</div>
          <span>•</span>
          <div><span class="text-white font-bold">&lt; 100K</span> IMPULSE PRICE</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Clean Minimalist Controls & Search Bar -->
  <section class="w-full sticky top-[57px] z-30 bg-[#0A0A0A]/95 backdrop-blur-md border-b border-white/[0.08] py-4">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 space-y-3.5">
      
      <!-- Search & Sort Row -->
      <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
        <div class="relative flex-1">
          <input 
            type="search" 
            id="searchInput" 
            placeholder="Cari solusi (kipas, diffuser, kabel, tawas, basreng)..." 
            class="w-full pl-4 pr-10 py-2.5 rounded-xl bg-surface hairline-border focus:border-white/30 text-xs sm:text-sm text-white placeholder-gray-500 outline-none transition font-sans"
            autocomplete="off"
          >
          <span class="hidden sm:inline-block absolute right-3 top-1/2 -translate-y-1/2 text-[10px] text-gray-500 font-mono border border-white/10 px-1.5 py-0.5 rounded">/</span>
          <button id="clearSearchBtn" class="hidden absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white text-xs">✕</button>
        </div>

        <div class="flex items-center gap-2">
          <select id="sortSelect" class="w-full sm:w-auto px-3.5 py-2.5 rounded-xl bg-surface hairline-border text-xs text-gray-300 focus:border-white/30 outline-none transition cursor-pointer font-mono">
            <option value="default">SORT: REKOMENDASI</option>
            <option value="sales">SORT: TERLARIS (10K+)</option>
            <option value="price_asc">SORT: HARGA TERMURAH</option>
            <option value="price_desc">SORT: HARGA TERTINGGI</option>
          </select>
        </div>
      </div>

      <!-- Monochrome Category Filter Pills -->
      <div class="flex items-center gap-1.5 overflow-x-auto pb-0.5 no-scrollbar font-mono text-xs">
        <button data-filter="all" class="filter-pill active px-3.5 py-1.5 rounded-lg whitespace-nowrap transition bg-white text-black font-bold">
          ALL (100)
        </button>
        <button data-filter="Budak Korporat" class="filter-pill px-3.5 py-1.5 rounded-lg whitespace-nowrap transition bg-surface hover:bg-surfaceHover border border-white/[0.08] text-gray-400 hover:text-white">
          DESK & KERJA
        </button>
        <button data-filter="Penyelamat Kosan" class="filter-pill px-3.5 py-1.5 rounded-lg whitespace-nowrap transition bg-surface hover:bg-surfaceHover border border-white/[0.08] text-gray-400 hover:text-white">
          KAMAR KOSAN
        </button>
        <button data-filter="Glow Up Murah" class="filter-pill px-3.5 py-1.5 rounded-lg whitespace-nowrap transition bg-surface hover:bg-surfaceHover border border-white/[0.08] text-gray-400 hover:text-white">
          SELF-CARE
        </button>
        <button data-filter="Camilan & Stress" class="filter-pill px-3.5 py-1.5 rounded-lg whitespace-nowrap transition bg-surface hover:bg-surfaceHover border border-white/[0.08] text-gray-400 hover:text-white">
          SNACK & RELAKS
        </button>
        <button data-filter="Di Bawah 20rb" class="filter-pill px-3.5 py-1.5 rounded-lg whitespace-nowrap transition bg-surface hover:bg-surfaceHover border border-white/[0.08] text-gray-400 hover:text-white">
          UNDER 20K
        </button>
      </div>

    </div>
  </section>

  <!-- Counter Header -->
  <div class="w-full max-w-5xl mx-auto px-4 sm:px-6 pt-6 flex items-center justify-between font-mono text-xs text-gray-500">
    <span id="resultsCount">100 ITEMS LISTED</span>
    <span class="text-[11px] uppercase tracking-wider text-gray-400">TAP CARD TO OPEN SHOPEE ↗</span>
  </div>

  <!-- Editorial Product Grid -->
  <main class="w-full max-w-5xl mx-auto px-4 sm:px-6 py-6 flex-1">
    <div id="productGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-5">
      <!-- Populated via Client-Side JS -->
    </div>

    <!-- Empty State -->
    <div id="emptyState" class="hidden py-24 text-center">
      <p class="font-mono text-xs text-gray-500 uppercase tracking-widest mb-2">[0 RESULTS]</p>
      <h3 class="text-xl font-display font-bold text-white mb-2">Item Tidak Ditemukan</h3>
      <p class="text-xs text-gray-400 mb-5 max-w-sm mx-auto">Coba cari dengan kata kunci lain atau reset filter kategori.</p>
      <button id="resetSearchBtn" class="font-mono text-xs px-4 py-2 rounded-lg bg-white text-black font-bold hover:bg-gray-200 transition">
        RESET FILTER
      </button>
    </div>
  </main>

  <!-- Clean Minimalist Footer -->
  <footer class="w-full border-t border-white/[0.08] bg-[#0A0A0A] py-12 mt-12 text-center font-mono text-xs text-gray-500">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 space-y-2">
      <p class="text-gray-400 uppercase tracking-widest text-[11px]">KIKI RACHMAT • @KIKIPUNYACERITA</p>
      <p class="text-[11px]">Curated index for Threads audience. Links are Shopee affiliate redirects.</p>
      <p class="text-[10px] text-gray-600 pt-2">© 2026 Kiki Rachmat. All rights reserved.</p>
    </div>
  </footer>

  <!-- Raw Products JSON Data -->
  <script id="product-data" type="application/json">
    {json_str}
  </script>

  <script>
    // Clean, High-Speed Client Controller
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
    const toastText = document.getElementById('toast-text');

    function showToast(text) {{
      toastText.textContent = text;
      toast.classList.remove('translate-y-16', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');
      setTimeout(() => {{
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('translate-y-16', 'opacity-0');
      }}, 2000);
    }}

    function copyToClipboard(url, name) {{
      const fallback = () => {{
        const ta = document.createElement('textarea');
        ta.value = url;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        try {{
          document.execCommand('copy');
          showToast('Link disalin ke clipboard');
        }} catch(e) {{
          showToast('Gagal menyalin link');
        }}
        document.body.removeChild(ta);
      }};

      if (navigator.clipboard && window.isSecureContext) {{
        navigator.clipboard.writeText(url).then(() => {{
          showToast('Link disalin ke clipboard');
        }}).catch(fallback);
      }} else {{
        fallback();
      }}
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
          p.short_hook.toLowerCase().includes(q) ||
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

      countEl.textContent = `${{filtered.length}} ITEMS LISTED`;

      if (filtered.length === 0) {{
        grid.innerHTML = '';
        emptyState.classList.remove('hidden');
        return;
      }}

      emptyState.classList.add('hidden');

      grid.innerHTML = filtered.map((p, idx) => {{
        const trackingUrl = p.affiliate_url + (p.affiliate_url.includes('?') ? '&' : '?') + 'sub_id1=katalog_bio';
        const cleanName = p.name.replace(/"/g, '&quot;');
        const indexNumber = String(idx + 1).padStart(2, '0');

        return `
          <article class="product-card group flex flex-col justify-between bg-surface hairline-border hover:border-white/20 rounded-2xl p-4 transition-all">
            
            <div>
              <!-- Image Container with Clean Aspect Ratio -->
              <div class="relative overflow-hidden rounded-xl aspect-[16/10] mb-3 bg-[#161616]">
                <img 
                  src="${{p.image_url}}" 
                  alt="${{cleanName}}" 
                  loading="lazy" 
                  class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300 filter brightness-95 group-hover:brightness-100"
                >
                <div class="absolute inset-0 bg-gradient-to-t from-surface via-transparent to-transparent opacity-80"></div>

                <!-- Index Number & Category Pill Top Left -->
                <div class="absolute top-2.5 left-2.5 flex items-center gap-1.5 font-mono text-[10px] text-gray-300 bg-black/60 backdrop-blur-md px-2 py-0.5 rounded-md border border-white/10">
                  <span>#${{indexNumber}}</span>
                  <span>•</span>
                  <span>${{p.need_pill}}</span>
                </div>

                <!-- Sales Tag Top Right -->
                <div class="absolute top-2.5 right-2.5 font-mono text-[10px] text-gray-300 bg-black/60 backdrop-blur-md px-2 py-0.5 rounded-md border border-white/10">
                  ${{p.sales.replace(' Terjual', '')}} SOLD
                </div>
              </div>

              <!-- Punchy 1-Line Problem Hook (No walls of text!) -->
              <p class="font-mono text-[11px] text-accent font-medium mb-1 truncate">
                ${{p.short_hook}}
              </p>

              <!-- Product Title with Stretched Link -->
              <h3 class="text-sm font-sans font-semibold text-white group-hover:text-accent line-clamp-2 leading-snug mb-2 transition-colors">
                <a href="${{trackingUrl}}" target="_blank" rel="noopener noreferrer" class="card-link focus:outline-none">
                  ${{p.name}}
                </a>
              </h3>

              <!-- Store Info -->
              <p class="font-mono text-[10px] text-gray-500 truncate mb-3">
                ${{p.shop}}
              </p>
            </div>

            <!-- Price & Clean CTA Row -->
            <footer class="pt-3 border-t border-white/[0.06] flex items-center justify-between gap-2">
              <div>
                <span class="font-mono text-base font-bold text-white tracking-tight">
                  ${{p.price_formatted}}
                </span>
              </div>

              <div class="flex items-center gap-1.5">
                <button 
                  onclick="copyToClipboard('${{trackingUrl}}', '${{cleanName}}')" 
                  title="Salin Link"
                  class="p-2 rounded-lg bg-white/[0.04] hover:bg-white/[0.1] text-gray-400 hover:text-white border border-white/10 transition text-xs flex items-center justify-center cursor-pointer"
                  aria-label="Salin Link"
                >
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
                </button>

                <a 
                  href="${{trackingUrl}}" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  class="font-mono text-xs px-3.5 py-1.5 rounded-lg bg-accent hover:bg-accentHover text-white font-bold transition flex items-center gap-1 shadow-sm"
                >
                  <span>BELI</span>
                  <span class="text-[10px]">↗</span>
                </a>
              </div>
            </footer>
          </article>
        `;
      }}).join('');
    }}

    // Filter Buttons
    document.querySelectorAll('.filter-pill').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.filter-pill').forEach(b => {{
          b.classList.remove('active', 'bg-white', 'text-black', 'font-bold');
          b.classList.add('bg-surface', 'border', 'border-white/[0.08]', 'text-gray-400');
        }});
        btn.classList.add('active', 'bg-white', 'text-black', 'font-bold');
        btn.classList.remove('bg-surface', 'border', 'border-white/[0.08]', 'text-gray-400');
        activeFilter = btn.getAttribute('data-filter');
        renderProducts();
      }});
    }});

    // Search Input
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
          b.classList.add('active', 'bg-white', 'text-black', 'font-bold');
        }} else {{
          b.classList.remove('active', 'bg-white', 'text-black', 'font-bold');
          b.classList.add('bg-surface', 'text-gray-400');
        }}
      }});
      renderProducts();
    }});

    // Sort
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

    renderProducts();
  </script>
</body>
</html>
"""

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ Generated Editorial Swiss/Porto-grade HTML catalog at {OUT_FILE}")
