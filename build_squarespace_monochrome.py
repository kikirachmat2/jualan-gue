import json
from pathlib import Path

DATA_FILE = Path("/Users/kiki/Documents/Web Develop/katalog-ceritakiki/data/products_enriched.json")
OUT_FILE = Path("/Users/kiki/Documents/Web Develop/katalog-ceritakiki/index.html")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    products = json.load(f)

html_template = f'''<!DOCTYPE html>
<html lang="id" class="scroll-smooth bg-[#000000] text-[#ffffff]">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kiki Rachmat — Curated Essentials (@kikipunyacerita)</title>
  <meta name="description" content="Cinematic monochrome catalog of curated essentials for work, living, and commute.">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">

  <!-- OpenGraph -->
  <meta property="og:title" content="Kiki Rachmat — Curated Essentials">
  <meta property="og:description" content="A purely achromatic, cinematic gallery of 100 verified essentials.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://katalog-ceritakiki.vercel.app">

  <!-- Clarkson Substitute: Inter (300, 400, 500) & Clarkson Serif Substitute: Playfair Display (400) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;1,400&display=swap" rel="stylesheet">

  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            clarkson: ['"Inter"', 'system-ui', '-apple-system', 'sans-serif'],
            serif: ['"Playfair Display"', 'Georgia', 'serif'],
          }},
          colors: {{
            obsidian: '#000000',
            paper: '#ffffff',
            charcoal: '#2f2f2f',
            ash: '#898989',
            fog: '#dddddd',
            slate: '#999999',
          }},
          letterSpacing: {{
            'display': '-0.06em',
            'heading': '-0.05em',
            'heading-sm': '-0.04em',
            'subheading': '-0.02em',
            'body-sm': '-0.01em',
            'caption': '-0.001em',
          }},
          borderRadius: {{
            'card': '8px',
            'pill': '100px',
            'btn': '0px',
          }}
        }}
      }}
    }}
  </script>

  <style>
    :root {{
      --color-obsidian: #000000;
      --color-paper: #ffffff;
      --color-charcoal: #2f2f2f;
      --color-ash: #898989;
      --color-fog: #dddddd;
      --color-slate: #999999;
      --font-clarkson: 'Inter', system-ui, -apple-system, sans-serif;
    }}

    body {{
      font-family: var(--font-clarkson);
      background-color: var(--color-obsidian);
      color: var(--color-paper);
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    /* Squarespace Whisper-Light Display Headings */
    .text-display {{
      font-size: clamp(2.8rem, 6.5vw, 4.5rem);
      font-weight: 300;
      line-height: 0.93;
      letter-spacing: -0.06em;
    }}

    .text-heading {{
      font-size: clamp(2rem, 4vw, 2.5rem);
      font-weight: 300;
      line-height: 1.0;
      letter-spacing: -0.05em;
    }}

    .text-heading-sm {{
      font-size: 26px;
      font-weight: 300;
      line-height: 1.2;
      letter-spacing: -0.04em;
    }}

    .text-subheading {{
      font-size: 20px;
      font-weight: 300;
      line-height: 1.2;
      letter-spacing: -0.02em;
    }}

    /* Ghost Button — 0px radius, 1px border */
    .ghost-btn {{
      background: transparent;
      border: 1px solid #ffffff;
      color: #ffffff;
      font-size: 14px;
      font-weight: 400;
      text-transform: uppercase;
      letter-spacing: 0em;
      padding: 16px 32px;
      border-radius: 0px;
      transition: all 0.25s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
    }}
    .ghost-btn:hover {{
      background: #ffffff;
      color: #000000;
    }}

    /* Filled Button — 0px radius */
    .filled-btn {{
      background: #ffffff;
      border: 1px solid #ffffff;
      color: #000000;
      font-size: 13px;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.02em;
      padding: 12px 24px;
      border-radius: 0px;
      transition: all 0.25s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      cursor: pointer;
    }}
    .filled-btn:hover {{
      background: #dddddd;
      border-color: #dddddd;
    }}

    .filled-charcoal-btn {{
      background: #2f2f2f;
      border: 1px solid #2f2f2f;
      color: #ffffff;
      font-size: 13px;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.02em;
      padding: 14px 32px;
      border-radius: 0px;
      transition: all 0.25s ease;
      cursor: pointer;
    }}
    .filled-charcoal-btn:hover {{
      background: #000000;
      border-color: #000000;
    }}

    /* Pill Tabs — 100px radius */
    .pill-tab {{
      border-radius: 100px;
      padding: 8px 18px;
      font-size: 14px;
      font-weight: 400;
      letter-spacing: -0.01em;
      transition: all 0.2s ease;
      white-space: nowrap;
      cursor: pointer;
      border: none;
    }}
    .pill-tab.active {{
      background-color: #dddddd;
      color: #000000;
    }}
    .pill-tab.inactive {{
      background-color: transparent;
      color: #000000;
    }}
    .pill-tab.inactive:hover {{
      color: #898989;
    }}

    /* Dark Feature Card — 8px radius, NO drop shadow */
    .dark-card {{
      border-radius: 8px;
      position: relative;
      overflow: hidden;
      background: #111111;
      aspect-ratio: 3 / 4;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 24px sm:32px;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .dark-card:hover {{
      transform: translateY(-4px);
    }}

    /* Subtle custom scrollbar */
    ::-webkit-scrollbar {{
      width: 4px;
    }}
    ::-webkit-scrollbar-track {{
      background: #000000;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #2f2f2f;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #898989;
    }}

    .no-scrollbar::-webkit-scrollbar {{
      display: none;
    }}
    .no-scrollbar {{
      -ms-overflow-style: none;
      scrollbar-width: none;
    }}
  </style>
</head>
<body class="selection:bg-[#ffffff] selection:text-[#000000]">

  <!-- Minimalist Toast Notification -->
  <aside id="toast" role="status" aria-live="polite" class="fixed bottom-8 right-8 z-50 transform translate-y-20 opacity-0 transition-all duration-300 pointer-events-none bg-[#2f2f2f] text-[#ffffff] px-6 py-3 rounded-[0px] border border-[#898989]/30 text-[13px] uppercase tracking-wider font-clarkson">
    Link Shopee disalin ke clipboard
  </aside>

  <!-- Transparent Navigation Bar (Transitions to Obsidian on scroll) -->
  <nav id="navbar" class="fixed top-0 left-0 right-0 z-40 transition-colors duration-300 py-6 px-6 sm:px-12 flex items-center justify-between">
    
    <!-- Wordmark Logo -->
    <a href="https://kikirach.vercel.app" target="_blank" rel="noopener noreferrer" class="flex items-center gap-2 text-[#ffffff] no-underline tracking-[-0.03em] font-light text-[15px] sm:text-[17px]">
      <span class="font-normal uppercase tracking-[0.05em] text-[13px]">KIKI RACHMAT</span>
      <span class="text-[#898989]">/</span>
      <span class="text-[#898989] text-[13px]">@kikipunyacerita</span>
    </a>

    <!-- Center Nav Items (Hidden on small mobile) -->
    <div class="hidden md:flex items-center gap-8 text-[13px] uppercase tracking-[0.04em] text-[#ffffff] font-normal">
      <a href="#collection" class="text-[#ffffff] hover:text-[#898989] transition-colors no-underline">The Collection</a>
      <a href="#stats" class="text-[#ffffff] hover:text-[#898989] transition-colors no-underline">Overview</a>
      <a href="https://www.threads.net/@kikipunyacerita" target="_blank" rel="noopener noreferrer" class="text-[#898989] hover:text-[#ffffff] transition-colors no-underline">Threads ↗</a>
    </div>

    <!-- Right Side: Threads CTA -->
    <div class="flex items-center gap-4">
      <a href="https://www.threads.net/@kikipunyacerita" target="_blank" rel="noopener noreferrer" class="hidden sm:inline-block text-[13px] uppercase tracking-[0.02em] text-[#ffffff] hover:underline no-underline">
        Log In
      </a>
      <a href="#collection" class="filled-btn">
        Explore 100
      </a>
    </div>

  </nav>

  <!-- 1. FULL-BLEED PHOTOGRAPHIC HERO (Squarespace Style) -->
  <section class="relative min-h-[100svh] h-screen w-full flex flex-col justify-center items-center text-center px-6 sm:px-12 overflow-hidden">
    
    <!-- Cinematic Full-Bleed Photography Background -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=2000&q=85" 
        alt="Atmospheric architecture"
        class="w-full h-full object-cover filter brightness-[0.4] contrast-125 scale-105"
      >
      <!-- Atmospheric black gradient wash -->
      <div class="absolute inset-0 bg-gradient-to-b from-[#000000]/60 via-transparent to-[#000000]"></div>
    </div>

    <!-- Centered Editorial Content -->
    <div class="relative z-10 max-w-4xl mx-auto flex flex-col items-center">
      
      <p class="text-[13px] uppercase tracking-[0.1em] text-[#898989] mb-4">
        Curated Affiliate Index
      </p>

      <!-- Headline: Clarkson 300 at 72px with -0.06em tracking -->
      <h1 class="text-display text-[#ffffff] text-center mb-6 max-w-3xl">
        A curated vault makes it real.
      </h1>

      <p class="font-normal text-[15px] sm:text-[18px] text-[#898989] max-w-xl leading-relaxed mb-10 text-center">
        100 barang penunjang kerja, kosan, dan commute yang sering gue spill di Threads. Semua rating 4.8+ lolos kurasi tanpa gimmick.
      </p>

      <!-- Ghost Button: 1px #ffffff border, Clarkson 400 14px uppercase, 0px radius -->
      <div class="flex flex-col items-center gap-4">
        <a href="#collection" class="ghost-btn">
          Explore The Collection
        </a>
        <p class="text-[13px] text-[#898989] font-normal tracking-tight">
          Verified Shopee links • Direct impulse curation
        </p>
      </div>

    </div>

    <!-- Scroll Indicator Arrow -->
    <div class="absolute bottom-8 left-1/2 -translate-x-1/2 z-10 text-[#898989] text-[13px] tracking-widest uppercase">
      ↓
    </div>

  </section>

  <!-- 2. BLACK STAT DISPLAY BAND (#000000 Full-width, 80px vertical padding) -->
  <section id="stats" class="w-full bg-[#000000] border-t border-[#2f2f2f]/60 py-20 px-6 sm:px-12">
    <div class="max-w-[1200px] mx-auto grid grid-cols-1 md:grid-cols-3 gap-12 sm:gap-8 text-center">
      
      <!-- Stat 1 -->
      <div class="flex flex-col items-center">
        <div class="font-light text-[72px] sm:text-[84px] text-[#ffffff] leading-none tracking-[-0.06em] mb-3">
          100<sup class="text-[32px] text-[#898989] font-light">.</sup>
        </div>
        <p class="text-[12px] uppercase tracking-[0.08em] text-[#898989] font-normal">
          Verified Curated Objects
        </p>
      </div>

      <!-- Stat 2 -->
      <div class="flex flex-col items-center">
        <div class="font-light text-[72px] sm:text-[84px] text-[#ffffff] leading-none tracking-[-0.06em] mb-3">
          4.8<sup class="text-[32px] text-[#898989] font-light">★</sup>
        </div>
        <p class="text-[12px] uppercase tracking-[0.08em] text-[#898989] font-normal">
          Minimum Shopee Rating
        </p>
      </div>

      <!-- Stat 3 -->
      <div class="flex flex-col items-center">
        <div class="font-light text-[72px] sm:text-[84px] text-[#ffffff] leading-none tracking-[-0.06em] mb-3">
          &lt;100k
        </div>
        <p class="text-[12px] uppercase tracking-[0.08em] text-[#898989] font-normal">
          Impulse Price Threshold
        </p>
      </div>

    </div>
  </section>

  <!-- 3. LIGHT SECTION: THE COLLECTION (#ffffff Paper Canvas, 80-120px padding) -->
  <section id="collection" class="w-full bg-[#ffffff] text-[#000000] py-24 sm:py-32 px-6 sm:px-12">
    <div class="max-w-[1200px] mx-auto">

      <!-- Section Header (Centered): Clarkson 300, 48px, tracking -0.05em -->
      <div class="text-center max-w-2xl mx-auto mb-16">
        <h2 class="text-heading text-[#000000] mb-4">
          The Collection.
        </h2>
        <p class="text-[15px] text-[#898989] leading-relaxed max-w-[480px] mx-auto">
          Setiap barang dipilih berdasarkan fungsi nyata dan ketahanan pakai. Filter berdasarkan skenario harian atau cari langsung.
        </p>
      </div>

      <!-- Category Filter Row + Search Bar (Pill tabs 100px radius, active #dddddd) -->
      <div class="flex flex-col lg:flex-row items-center justify-between gap-6 mb-12">
        
        <!-- Pill Category Tabs Row -->
        <div class="flex items-center gap-2 overflow-x-auto no-scrollbar max-w-full pb-2">
          <button data-filter="all" class="pill-tab active">
            All Objects (100)
          </button>
          <button data-filter="Budak Korporat" class="pill-tab inactive">
            Budak Korporat
          </button>
          <button data-filter="Penyelamat Kosan" class="pill-tab inactive">
            Penyelamat Kosan
          </button>
          <button data-filter="Glow Up Murah" class="pill-tab inactive">
            Glow Up & Care
          </button>
          <button data-filter="Camilan & Stress" class="pill-tab inactive">
            Snack & Relaks
          </button>
          <button data-filter="Di Bawah 20rb" class="pill-tab inactive">
            Under 20k
          </button>
        </div>

        <!-- Minimal Search Box: 8px border-radius, #ffffff, 1px #dddddd border -->
        <div class="relative w-full lg:w-72">
          <input 
            type="search" 
            id="searchInput" 
            placeholder="Search items..." 
            class="w-full pl-9 pr-8 py-2.5 rounded-[8px] bg-[#ffffff] border border-[#dddddd] text-[#000000] placeholder-[#898989] text-[14px] focus:outline-none focus:border-[#000000] transition-colors"
            autocomplete="off"
          >
          <span class="absolute left-3 top-1/2 -translate-y-1/2 text-[#898989] text-[13px] pointer-events-none">🔍</span>
          <button id="clearSearchBtn" class="hidden absolute right-3 top-1/2 -translate-y-1/2 text-[#898989] hover:text-[#000000] text-[12px]">✕</button>
        </div>

      </div>

      <!-- Active Filter Counter -->
      <div class="flex items-center justify-between text-[12px] uppercase tracking-[0.06em] text-[#898989] mb-8 pb-3 border-b border-[#dddddd]">
        <span><strong id="resultsCount" class="text-[#000000]">100</strong> Items Listed</span>
        <span>Tap Card to Open Shopee →</span>
      </div>

      <!-- Dark Feature Card Grid: 4-Column Grid, 24px Gap, 8px Radius, NO Shadows -->
      <div id="productGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <!-- Injected via Client-side JS -->
      </div>

      <!-- Empty State -->
      <div id="emptyState" class="hidden py-24 text-center">
        <p class="text-[12px] uppercase tracking-widest text-[#898989] mb-2">[0 RESULTS]</p>
        <h3 class="text-[26px] font-light text-[#000000] mb-2">Item Tidak Ditemukan</h3>
        <p class="text-[14px] text-[#898989] mb-6">Coba cari kata kunci lain atau reset filter kategori.</p>
        <button id="resetSearchBtn" class="filled-charcoal-btn">
          Reset Filter
        </button>
      </div>

      <!-- Load More Button -->
      <div id="loadMoreContainer" class="mt-16 text-center">
        <button id="loadMoreBtn" class="filled-charcoal-btn">
          Load More Objects (+16)
        </button>
      </div>

    </div>
  </section>

  <!-- 4. BLACK FOOTER BAND (#000000 Full-width) -->
  <footer class="w-full bg-[#000000] text-[#ffffff] py-20 px-6 sm:px-12 border-t border-[#2f2f2f]">
    <div class="max-w-[1200px] mx-auto flex flex-col md:flex-row items-center justify-between gap-8">
      
      <div>
        <h3 class="font-light text-[22px] tracking-[-0.03em] mb-1">
          Kiki Rachmat
        </h3>
        <p class="text-[13px] text-[#898989]">
          @kikipunyacerita • Curated Shopee Affiliate Directory
        </p>
      </div>

      <div class="flex items-center gap-6 text-[13px] uppercase tracking-[0.04em] text-[#898989]">
        <a href="https://www.threads.net/@kikipunyacerita" target="_blank" rel="noopener noreferrer" class="hover:text-[#ffffff] transition-colors no-underline">Threads ↗</a>
        <a href="https://kikirach.vercel.app" target="_blank" rel="noopener noreferrer" class="hover:text-[#ffffff] transition-colors no-underline">Portfolio ↗</a>
        <a href="#collection" class="hover:text-[#ffffff] transition-colors no-underline">Back to Top ↑</a>
      </div>

    </div>

    <div class="max-w-[1200px] mx-auto mt-12 pt-8 border-t border-[#2f2f2f]/60 text-center text-[12px] text-[#898989] uppercase tracking-widest">
      © 2026 Kiki Rachmat. Purely Achromatic. All Rights Reserved.
    </div>
  </footer>

  <!-- Product Data JSON -->
  <script id="product-data" type="application/json">
    {json.dumps(products, ensure_ascii=False)}
  </script>

  <!-- Client-Side Architecture -->
  <script>
    const rawData = JSON.parse(document.getElementById('product-data').textContent);

    let activeFilter = 'all';
    let searchQuery = '';
    let visibleCount = 16;
    const PAGE_STEP = 16;

    const grid = document.getElementById('productGrid');
    const searchInput = document.getElementById('searchInput');
    const clearBtn = document.getElementById('clearSearchBtn');
    const countEl = document.getElementById('resultsCount');
    const emptyState = document.getElementById('emptyState');
    const resetBtn = document.getElementById('resetSearchBtn');
    const loadMoreContainer = document.getElementById('loadMoreContainer');
    const loadMoreBtn = document.getElementById('loadMoreBtn');
    const toast = document.getElementById('toast');
    const navbar = document.getElementById('navbar');

    // Scroll Navbar Transition
    window.addEventListener('scroll', () => {{
      if (window.scrollY > 80) {{
        navbar.classList.add('bg-[#000000]', 'border-b', 'border-[#2f2f2f]');
      }} else {{
        navbar.classList.remove('bg-[#000000]', 'border-b', 'border-[#2f2f2f]');
      }}
    }});

    function showToast() {{
      toast.classList.remove('translate-y-20', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');
      setTimeout(() => {{
        toast.classList.add('translate-y-20', 'opacity-0');
        toast.classList.remove('translate-y-0', 'opacity-100');
      }}, 2200);
    }}

    function copyLink(url) {{
      navigator.clipboard.writeText(url).then(showToast).catch(showToast);
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
          p.clean_title.toLowerCase().includes(q) || 
          p.clean_hook.toLowerCase().includes(q) ||
          p.category.toLowerCase().includes(q) || 
          p.shop.toLowerCase().includes(q);
        
        return matchCategory && matchQuery;
      }});

      countEl.textContent = filtered.length;

      if (filtered.length === 0) {{
        grid.innerHTML = '';
        emptyState.classList.remove('hidden');
        loadMoreContainer.classList.add('hidden');
        return;
      }}

      emptyState.classList.add('hidden');

      const itemsToShow = filtered.slice(0, visibleCount);

      grid.innerHTML = itemsToShow.map((p, idx) => {{
        const trackingUrl = `${{p.affiliate_url}}?utm_source=kikipunyacerita&utm_medium=squarespace_gallery&utm_campaign=item_${{p.id}}`;

        return `
          <article class="dark-card group">
            <!-- Full-Bleed Background Image (8px Radius clipping) -->
            <img 
              src="${{p.image_url}}" 
              alt="${{p.clean_title}}" 
              loading="lazy" 
              class="absolute inset-0 w-full h-full object-cover filter brightness-[0.6] group-hover:brightness-[0.72] group-hover:scale-105 transition-all duration-700 ease-out"
            >
            <div class="absolute inset-0 bg-gradient-to-t from-[#000000] via-[#000000]/40 to-transparent"></div>

            <!-- Top Row: Category label & Copy link -->
            <div class="relative z-10 flex items-center justify-between">
              <span class="text-[11px] text-[#898989] uppercase tracking-[0.06em] font-normal">
                ${{p.need_pill}}
              </span>
              <button 
                onclick="event.stopPropagation(); copyLink('${{p.affiliate_url}}')" 
                class="text-[#898989] hover:text-[#ffffff] transition-colors p-1"
                title="Salin link Shopee"
                aria-label="Salin link"
              >
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
              </button>
            </div>

            <!-- Bottom Block: White heading (Clarkson 300, 20px), Ash body (13px), Arrow indicator (→) -->
            <div class="relative z-10 pt-4">
              <h3 class="font-light text-[20px] text-[#ffffff] tracking-[-0.02em] leading-snug line-clamp-2 mb-1.5">
                ${{p.clean_title}}
              </h3>
              
              <p class="text-[13px] text-[#898989] leading-relaxed line-clamp-1 mb-4">
                ${{p.clean_hook}}
              </p>

              <div class="flex items-center justify-between pt-3 border-t border-white/10">
                <span class="font-medium text-[14px] text-[#ffffff] tracking-tight">
                  ${{p.price_formatted}}
                </span>
                <span class="text-[#ffffff] text-[16px] group-hover:translate-x-1.5 transition-transform duration-300">
                  →
                </span>
              </div>
            </div>

            <!-- Stretched Clickable Overlay -->
            <a href="${{trackingUrl}}" target="_blank" rel="noopener noreferrer" class="absolute inset-0 z-20" aria-label="Beli ${{p.clean_title}}"></a>
          </article>
        `;
      }}).join('');

      if (visibleCount >= filtered.length) {{
        loadMoreContainer.classList.add('hidden');
      }} else {{
        loadMoreContainer.classList.remove('hidden');
      }}
    }}

    // Pill Tab Category Switching
    document.querySelectorAll('.pill-tab').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.pill-tab').forEach(b => {{
          b.classList.remove('active');
          b.classList.add('inactive');
        }});
        btn.classList.add('active');
        btn.classList.remove('inactive');
        activeFilter = btn.getAttribute('data-filter');
        visibleCount = 16;
        renderProducts();
      }});
    }});

    // Search Input Logic
    searchInput.addEventListener('input', (e) => {{
      searchQuery = e.target.value.trim();
      clearBtn.classList.toggle('hidden', !searchQuery);
      visibleCount = 16;
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
      clearBtn.classList.add('hidden');
      document.querySelector('[data-filter="all"]').click();
    }});

    loadMoreBtn.addEventListener('click', () => {{
      visibleCount += PAGE_STEP;
      renderProducts();
    }});

    renderProducts();
  </script>
</body>
</html>'''

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"✅ Generated Squarespace Cinematic Monochrome Catalog at {OUT_FILE}")
