import json
import html
import re

with open("data/products_verified.json") as f:
    products = json.load(f)

# Hero items
hero_items = [p for p in products if p.get("is_hero")]
if not hero_items:
    hero_items = products[:5]

# Group by categories
cats = {}
for p in products:
    c = p.get("category", "Lainnya")
    cats.setdefault(c, []).append(p)

def slugify(text):
    return re.sub(r"[^\w\-]+", "", re.sub(r"\s+", "-", text.lower()))

chips_html = ['<button class="category-chip active" data-cat="all">Semua</button>']
for cat in sorted(cats.keys()):
    chips_html.append(f'<button class="category-chip" data-cat="{html.escape(cat)}">{html.escape(cat)}</button>')
chips_str = "\n        ".join(chips_html)

sections_html = []
for cat in sorted(cats.keys()):
    items = cats[cat]
    sec_id = f"cat-{slugify(cat)}"
    cards_html = []
    for p in items:
        pid = p["id"]
        img_src = p["image_url"]
        p_name = html.escape(p["name"])
        p_price = html.escape(p["price_formatted"])
        p_aff = html.escape(p["affiliate_url"])
        
        card = f'''
          <a href="{p_aff}" target="_blank" rel="noopener sponsored" class="product-card" data-cat="{html.escape(cat)}">
            <div class="card-media">
              <img class="card-img" src="{img_src}" alt="{p_name}" loading="lazy" decoding="async" width="480" height="600" />
            </div>
            <div class="card-info">
              <div class="card-title">{p_name}</div>
              <div class="card-bottom-row">
                <span class="card-price">{p_price}</span>
                <div class="card-buy-btn" aria-label="Beli di Shopee">
                  <svg viewBox="0 0 24 24"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg>
                </div>
              </div>
            </div>
          </a>'''
        cards_html.append(card)

    sec_html = f'''
      <section class="category-section" id="{sec_id}" data-cat="{html.escape(cat)}">
        <div class="category-header">
          <h2 class="category-name">{html.escape(cat)}</h2>
          <span class="category-count">{len(items)} Produk</span>
        </div>
        <div class="product-grid">
          {"".join(cards_html)}
        </div>
      </section>'''
    sections_html.append(sec_html)

grid_str = "\n".join(sections_html)
h0 = hero_items[0]
hero_json = json.dumps(hero_items)

story_segments = "".join([f'<div class="story-segment" data-idx="{i}"><div class="story-fill" id="story-fill-{i}"></div></div>' for i in range(len(hero_items))])

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <title>Jualan Gue — Rekomendasi Produk Shopee Pilihan</title>
  <meta name="description" content="Koleksi kurasi produk Shopee pilihan, terlaris, dan harga terbaik." />
  
  <meta name="theme-color" content="#EE4D2D" />
  <link rel="icon" type="image/svg+xml" href="favicon.svg" />
  <link rel="icon" type="image/png" sizes="32x32" href="favicon.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png" />
  <link rel="manifest" href="manifest.json" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet" />

  <script src="https://cdn.jsdelivr.net/npm/lenis@1.1.18/dist/lenis.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/Flip.min.js" defer></script>

  <style>
    :root {{
      --bg: #0B0B0D;
      --surface: #151518;
      --surface-hover: #1C1C22;
      --surface-glass: rgba(15, 15, 18, 0.85);
      --border: rgba(255, 255, 255, 0.06);
      --border-hover: rgba(255, 255, 255, 0.14);
      
      --text-main: #EDEDEE;
      --text-muted: #8E8E93;
      
      --shopee-orange: #EE4D2D;
      --shopee-gradient: linear-gradient(135deg, #F53D2D 0%, #FF7337 100%);
      --shopee-glow: rgba(238, 77, 45, 0.35);
      --shopee-border: rgba(238, 77, 45, 0.45);

      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-full: 9999px;

      --ease-primary: cubic-bezier(0.22, 1, 0.36, 1);
      --duration-press: 120ms;
      --duration-hover: 450ms;
      --duration-reveal: 900ms;
      --duration-hero: 1100ms;
    }}

    #scroll-progress-bar {{
      position: fixed;
      top: 0;
      left: 0;
      width: 0%;
      height: 2px;
      background: var(--shopee-gradient);
      box-shadow: 0 0 8px var(--shopee-orange);
      z-index: 9999;
      pointer-events: none;
      transition: width 0.05s linear;
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    html {{
      background-color: var(--bg);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    }}

    body {{
      min-height: 100vh;
      overflow-x: hidden;
      position: relative;
    }}

    .app-header {{
      position: sticky;
      top: 0;
      left: 0;
      right: 0;
      z-index: 1000;
      background: var(--surface-glass);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--border);
      transform: translateY(0);
      transition: transform 0.35s var(--ease-primary);
      will-change: transform;
    }}

    .app-header.nav-hidden {{
      transform: translateY(-100%);
    }}

    .header-inner {{
      max-width: 1440px;
      margin: 0 auto;
      height: 56px;
      display: flex;
      align-items: center;
      padding: 0 20px;
      gap: 16px;
    }}

    .category-scroll-container {{
      display: flex;
      align-items: center;
      gap: 8px;
      overflow-x: auto;
      scrollbar-width: none;
      position: relative;
      padding: 4px 0;
      width: 100%;
    }}
    .category-scroll-container::-webkit-scrollbar {{
      display: none;
    }}

    .category-chip {{
      appearance: none;
      border: none;
      background: transparent;
      color: var(--text-muted);
      font-size: 13.5px;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: var(--radius-full);
      cursor: pointer;
      white-space: nowrap;
      position: relative;
      z-index: 2;
      transition: color 0.25s ease;
      user-select: none;
    }}
    .category-chip:hover {{
      color: var(--text-main);
    }}
    .category-chip.active {{
      color: #FFFFFF;
    }}

    .chip-sliding-pill {{
      position: absolute;
      top: 4px;
      left: 0;
      height: calc(100% - 8px);
      background: var(--shopee-gradient);
      border-radius: var(--radius-full);
      box-shadow: 0 2px 14px var(--shopee-glow);
      z-index: 1;
      pointer-events: none;
      transition: transform 0.4s var(--ease-primary), width 0.4s var(--ease-primary);
      will-change: transform, width;
    }}

    .hero-container {{
      max-width: 1440px;
      margin: 24px auto 36px;
      padding: 0 20px;
      position: relative;
    }}

    .hero-section-title {{
      font-size: 20px;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
      color: var(--text-main);
    }}

    .hero-fire-icon {{
      width: 22px;
      height: 22px;
      display: inline-block;
      fill: url(#fireGradient);
      filter: drop-shadow(0 2px 6px rgba(238, 77, 45, 0.6));
    }}

    .hero-slider-wrap {{
      position: relative;
      border-radius: var(--radius-lg);
      background: var(--surface);
      border: 1px solid var(--border);
      overflow: hidden;
      box-shadow: 0 20px 48px rgba(0, 0, 0, 0.45);
    }}

    .hero-ambient-glow {{
      position: absolute;
      top: -30%;
      left: -20%;
      width: 140%;
      height: 160%;
      opacity: 0.38;
      filter: blur(80px);
      pointer-events: none;
      z-index: 0;
      transition: background 0.8s var(--ease-primary);
      will-change: background;
      background: radial-gradient(circle, {h0.get("glow_color", "rgb(238,77,45)")} 0%, rgba(238,77,45,0.4) 40%, transparent 70%);
    }}

    .hero-slide-stage {{
      position: relative;
      z-index: 1;
      display: grid;
      grid-template-columns: 1fr 1fr;
      align-items: center;
      min-height: 440px;
      padding: 40px;
      gap: 36px;
      cursor: pointer;
      text-decoration: none;
      color: inherit;
    }}

    @media (max-width: 860px) {{
      .hero-slide-stage {{
        grid-template-columns: 1fr;
        padding: 24px;
        gap: 20px;
        min-height: auto;
      }}
    }}

    .hero-image-wrap {{
      position: relative;
      display: flex;
      justify-content: center;
      align-items: center;
      perspective: 1000px;
    }}

    .hero-product-img {{
      width: 100%;
      max-width: 380px;
      aspect-ratio: 1 / 1;
      object-fit: cover;
      border-radius: var(--radius-md);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.08);
      transform: translateY(0);
      transition: transform 0.6s var(--ease-primary);
      will-change: transform;
    }}

    .hero-content {{
      display: flex;
      flex-direction: column;
      gap: 16px;
      z-index: 2;
    }}

    .hero-header-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .hero-order-num {{
      font-size: 54px;
      font-weight: 800;
      line-height: 1;
      color: transparent;
      -webkit-text-stroke: 1.5px rgba(255, 255, 255, 0.28);
      letter-spacing: -0.04em;
    }}

    .hero-category-tag {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--shopee-orange);
      background: rgba(238, 77, 45, 0.12);
      border: 1px solid var(--shopee-border);
      padding: 6px 12px;
      border-radius: var(--radius-full);
    }}

    .hero-title {{
      font-size: 26px;
      font-weight: 700;
      line-height: 1.35;
      color: #FFFFFF;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      letter-spacing: -0.02em;
    }}

    .hero-price-row {{
      display: flex;
      align-items: baseline;
      gap: 12px;
    }}

    .hero-price {{
      font-size: 32px;
      font-weight: 800;
      color: var(--shopee-orange);
      letter-spacing: -0.03em;
    }}

    .hero-cta {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: var(--shopee-gradient);
      color: #FFFFFF;
      font-size: 15px;
      font-weight: 700;
      padding: 14px 26px;
      border-radius: var(--radius-full);
      box-shadow: 0 4px 18px var(--shopee-glow);
      width: fit-content;
      transition: transform 0.25s var(--ease-primary), box-shadow 0.25s var(--ease-primary);
    }}

    .hero-slide-stage:hover .hero-cta {{
      transform: translateY(-2px) scale(1.03);
      box-shadow: 0 8px 24px rgba(238, 77, 45, 0.6);
    }}

    .hero-story-progress {{
      display: flex;
      gap: 8px;
      padding: 0 32px 20px;
      position: relative;
      z-index: 2;
    }}
    @media (max-width: 860px) {{
      .hero-story-progress {{
        padding: 0 20px 16px;
      }}
    }}

    .story-segment {{
      flex: 1;
      height: 3px;
      background: rgba(255, 255, 255, 0.15);
      border-radius: var(--radius-full);
      overflow: hidden;
      position: relative;
      cursor: pointer;
    }}

    .story-fill {{
      width: 0%;
      height: 100%;
      background: var(--shopee-gradient);
      box-shadow: 0 0 6px var(--shopee-orange);
      transition: width 0.1s linear;
    }}

    .content-container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 20px 60px;
    }}

    .category-section {{
      margin-bottom: 48px;
      scroll-margin-top: 80px;
    }}

    .category-header {{
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border);
    }}

    .category-name {{
      font-size: 20px;
      font-weight: 700;
      color: #FFFFFF;
      letter-spacing: -0.02em;
    }}

    .category-count {{
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .product-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
    }}

    @media (min-width: 768px) {{
      .product-grid {{
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
      }}
    }}

    @media (min-width: 1100px) {{
      .product-grid {{
        grid-template-columns: repeat(4, 1fr);
        gap: 22px;
      }}
    }}

    .product-card {{
      position: relative;
      background: var(--surface);
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: inherit;
      transform: translateY(0) scale(1);
      transition: transform var(--duration-hover) var(--ease-primary), 
                  border-color 0.3s ease, 
                  box-shadow var(--duration-hover) var(--ease-primary);
      will-change: transform;
      --mx: 50%;
      --my: 50%;
    }}

    .product-card::before {{
      content: '';
      position: absolute;
      inset: 0;
      border-radius: inherit;
      background: radial-gradient(400px circle at var(--mx) var(--my), rgba(238, 77, 45, 0.16), transparent 70%);
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.35s ease;
      z-index: 3;
    }}

    .product-card:hover {{
      transform: translateY(-6px);
      border-color: var(--shopee-border);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.4), 0 0 20px rgba(238, 77, 45, 0.12);
    }}
    .product-card:hover::before {{
      opacity: 1;
    }}

    .product-card:active {{
      transform: scale(0.97);
      transition-duration: var(--duration-press);
    }}

    .card-media {{
      position: relative;
      width: 100%;
      aspect-ratio: 4 / 5;
      background: #111114;
      overflow: hidden;
    }}

    .card-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transform: scale(1);
      transition: transform var(--duration-hover) var(--ease-primary);
      will-change: transform;
    }}

    .product-card:hover .card-img {{
      transform: scale(1.06);
    }}

    .card-info {{
      padding: 14px;
      display: flex;
      flex-direction: column;
      flex: 1;
      justify-content: space-between;
      gap: 12px;
      position: relative;
      z-index: 2;
    }}

    .card-title {{
      font-size: 13.5px;
      font-weight: 600;
      line-height: 1.4;
      color: var(--text-main);
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      letter-spacing: -0.01em;
    }}

    .card-bottom-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }}

    .card-price {{
      font-size: 17px;
      font-weight: 800;
      color: var(--shopee-orange);
      letter-spacing: -0.02em;
    }}

    .card-buy-btn {{
      width: 36px;
      height: 36px;
      border-radius: var(--radius-full);
      background: rgba(238, 77, 45, 0.12);
      border: 1px solid var(--shopee-border);
      color: var(--shopee-orange);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.25s var(--ease-primary), background 0.25s ease, color 0.25s ease;
      flex-shrink: 0;
    }}

    .product-card:hover .card-buy-btn {{
      background: var(--shopee-gradient);
      color: #FFFFFF;
      box-shadow: 0 2px 10px var(--shopee-glow);
      transform: scale(1.08);
    }}

    .card-buy-btn svg {{
      width: 17px;
      height: 17px;
      stroke: currentColor;
      stroke-width: 2.2;
      fill: none;
      stroke-linecap: round;
      stroke-linejoin: round;
    }}

    @media (prefers-reduced-motion: reduce) {{
      *, *::before, *::after {{
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }}
      .hero-ambient-glow, .product-card::before {{
        display: none !important;
      }}
    }}
  </style>
</head>
<body>

  <div id="scroll-progress-bar"></div>

  <svg style="display: none;">
    <defs>
      <linearGradient id="fireGradient" x1="0%" y1="100%" x2="0%" y2="0%">
        <stop offset="0%" stop-color="#EE4D2D" />
        <stop offset="100%" stop-color="#FF7337" />
      </linearGradient>
    </defs>
  </svg>

  <header class="app-header" id="app-header">
    <div class="header-inner">
      <nav class="category-scroll-container" id="category-nav">
        <div class="chip-sliding-pill" id="chip-pill"></div>
        {chips_str}
      </nav>
    </div>
  </header>

  <main>
    <section class="hero-container">
      <div class="hero-section-title">
        <svg class="hero-fire-icon" viewBox="0 0 24 24">
          <path d="M12 23c-4.97 0-9-3.8-9-8.5 0-3.1 1.7-6 4.3-8.8.7-.7 1.7-.5 2.1.3.4.9.4 1.9.1 2.8 1.4-1.6 2.5-3.5 2.5-5.8 0-.6.5-1 1-1 .2 0 .4.1.6.2C17.2 6.1 21 10.4 21 14.5 21 19.2 16.97 23 12 23zM9.5 13.5c-.8.9-1.5 2-1.5 3 0 2.2 1.8 4 4 4s4-1.8 4-4c0-1.5-.9-2.9-2-4-.4-.4-1.1-.3-1.4.2-.6 1.1-1.6 1.6-2.5 1.4-.4-.1-.7-.3-.6-.6z"/>
        </svg>
        <span>Produk Terlaris</span>
      </div>

      <div class="hero-slider-wrap" id="hero-slider-wrap">
        <div class="hero-ambient-glow" id="hero-ambient"></div>
        
        <a id="hero-slide-link" class="hero-slide-stage" href="{html.escape(h0.get('affiliate_url'))}" target="_blank" rel="noopener sponsored">
          <div class="hero-image-wrap">
            <img id="hero-img" class="hero-product-img" src="{h0.get('image_url')}" alt="{html.escape(h0.get('name'))}" loading="eager" width="380" height="380" />
          </div>
          <div class="hero-content">
            <div class="hero-header-row">
              <span id="hero-order" class="hero-order-num">01</span>
              <span id="hero-category" class="hero-category-tag">{html.escape(h0.get('category'))}</span>
            </div>
            <h1 id="hero-title" class="hero-title">{html.escape(h0.get('name'))}</h1>
            <div class="hero-price-row">
              <span id="hero-price" class="hero-price">{html.escape(h0.get('price_formatted'))}</span>
            </div>
            <div class="hero-cta">
              <span>Beli di Shopee</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <line x1="7" y1="17" x2="17" y2="7"></line>
                <polyline points="7 7 17 7 17 17"></polyline>
              </svg>
            </div>
          </div>
        </a>

        <div class="hero-story-progress" id="hero-progress-container">
          {story_segments}
        </div>
      </div>
    </section>

    <div class="content-container" id="grid-container">
      {grid_str}
    </div>
  </main>

  <script>
    const heroItems = {hero_json};
    let currentHeroIndex = 0;
    let heroTimer = null;
    let heroProgress = 0;
    let isHeroPaused = false;
    let lenisInstance = null;

    document.addEventListener('DOMContentLoaded', () => {{
      setupHeroStorySlider();
      setupChipNavigation();
      setupCardInteractions();

      if (typeof Lenis !== 'undefined') {{
        lenisInstance = new Lenis({{
          duration: 1.1,
          easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
          smoothWheel: true,
          syncTouch: false
        }});

        if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {{
          gsap.registerPlugin(ScrollTrigger, Flip);
          lenisInstance.on('scroll', ScrollTrigger.update);
          gsap.ticker.add((time) => {{
            lenisInstance.raf(time * 1000);
          }});
          gsap.ticker.lagSmoothing(0);
        }} else {{
          function raf(time) {{
            lenisInstance.raf(time);
            requestAnimationFrame(raf);
          }}
          requestAnimationFrame(raf);
        }}

        const progressBar = document.getElementById('scroll-progress-bar');
        const header = document.getElementById('app-header');
        let lastScrollY = 0;

        lenisInstance.on('scroll', () => {{
          const scrollY = window.scrollY || document.documentElement.scrollTop;
          const docHeight = document.documentElement.scrollHeight - window.innerHeight;
          const progress = docHeight > 0 ? (scrollY / docHeight) * 100 : 0;
          if (progressBar) progressBar.style.width = progress + '%';

          if (scrollY > 120) {{
            if (scrollY > lastScrollY + 6) {{
              header.classList.add('nav-hidden');
            }} else if (scrollY < lastScrollY - 6) {{
              header.classList.remove('nav-hidden');
            }}
          }} else {{
            header.classList.remove('nav-hidden');
          }}
          lastScrollY = scrollY;
        }});
      }}
    }});

    function setupHeroStorySlider() {{
      const container = document.getElementById('hero-progress-container');
      if (!container) return;

      container.querySelectorAll('.story-segment').forEach(seg => {{
        seg.addEventListener('click', () => {{
          const idx = parseInt(seg.getAttribute('data-idx'));
          goToHeroSlide(idx);
        }});
      }});

      startHeroStoryTimer();

      const heroWrap = document.getElementById('hero-slider-wrap');
      if (heroWrap) {{
        heroWrap.addEventListener('mouseenter', () => {{ isHeroPaused = true; }});
        heroWrap.addEventListener('mouseleave', () => {{ isHeroPaused = false; }});
        heroWrap.addEventListener('touchstart', () => {{ isHeroPaused = true; }}, {{ passive: true }});
        heroWrap.addEventListener('touchend', () => {{ isHeroPaused = false; }});
      }}
    }}

    function renderHeroSlide(index) {{
      const p = heroItems[index];
      if (!p) return;

      const link = document.getElementById('hero-slide-link');
      const img = document.getElementById('hero-img');
      const order = document.getElementById('hero-order');
      const cat = document.getElementById('hero-category');
      const title = document.getElementById('hero-title');
      const price = document.getElementById('hero-price');
      const ambient = document.getElementById('hero-ambient');

      link.href = p.affiliate_url;
      order.textContent = `0${{index + 1}}`;
      cat.textContent = p.category;
      title.textContent = p.name;
      price.textContent = p.price_formatted;
      img.src = p.image_url;

      const glow = p.glow_color || 'rgb(238, 77, 45)';
      ambient.style.background = `radial-gradient(circle, ${{glow}} 0%, rgba(238,77,45,0.4) 40%, transparent 70%)`;

      if (typeof gsap !== 'undefined') {{
        gsap.fromTo([order, cat, title, price], 
          {{ opacity: 0, y: 14 }}, 
          {{ opacity: 1, y: 0, duration: 0.5, stagger: 0.06, ease: "power2.out" }}
        );
        gsap.fromTo(img, 
          {{ opacity: 0.4, scale: 0.95 }}, 
          {{ opacity: 1, scale: 1, duration: 0.6, ease: "power2.out" }}
        );
      }}
    }}

    function goToHeroSlide(index) {{
      currentHeroIndex = index;
      heroProgress = 0;
      heroItems.forEach((_, i) => {{
        const bar = document.getElementById(`story-fill-${{i}}`);
        if (bar) bar.style.width = i < currentHeroIndex ? '100%' : '0%';
      }});
      renderHeroSlide(currentHeroIndex);
    }}

    function startHeroStoryTimer() {{
      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      clearInterval(heroTimer);
      heroTimer = setInterval(() => {{
        if (isHeroPaused) return;
        heroProgress += 2;
        const currentBar = document.getElementById(`story-fill-${{currentHeroIndex}}`);
        if (currentBar) currentBar.style.width = `${{heroProgress}}%`;

        if (heroProgress >= 100) {{
          heroProgress = 0;
          currentHeroIndex = (currentHeroIndex + 1) % heroItems.length;
          goToHeroSlide(currentHeroIndex);
        }}
      }}, 100);
    }}

    function setupChipNavigation() {{
      const chips = document.querySelectorAll('.category-chip');
      const pill = document.getElementById('chip-pill');

      function updatePill(activeChip) {{
        if (!activeChip || !pill) return;
        pill.style.width = activeChip.offsetWidth + 'px';
        pill.style.transform = `translateX(${{activeChip.offsetLeft}}px)`;
      }}

      updatePill(document.querySelector('.category-chip.active'));

      chips.forEach(chip => {{
        chip.addEventListener('click', () => {{
          chips.forEach(c => c.classList.remove('active'));
          chip.classList.add('active');
          updatePill(chip);

          const cat = chip.dataset.cat;
          filterCategoriesWithFlip(cat);
        }});
      }});
    }}

    function filterCategoriesWithFlip(selectedCat) {{
      const sections = document.querySelectorAll('.category-section');
      
      if (typeof Flip !== 'undefined') {{
        const state = Flip.getState(sections);

        sections.forEach(sec => {{
          if (selectedCat === 'all' || sec.dataset.cat === selectedCat) {{
            sec.style.display = 'block';
          }} else {{
            sec.style.display = 'none';
          }}
        }});

        Flip.from(state, {{
          duration: 0.6,
          ease: "power2.inOut",
          stagger: 0.05,
          onComplete: () => {{
            if (typeof ScrollTrigger !== 'undefined') ScrollTrigger.refresh();
          }}
        }});
      }} else {{
        sections.forEach(sec => {{
          sec.style.display = (selectedCat === 'all' || sec.dataset.cat === selectedCat) ? 'block' : 'none';
        }});
      }}

      if (selectedCat !== 'all' && lenisInstance) {{
        const targetSec = document.getElementById(`cat-${{slugify(selectedCat)}}`);
        if (targetSec) {{
          lenisInstance.scrollTo(targetSec, {{ offset: -70, duration: 1.1 }});
        }}
      }}
    }}

    function setupCardInteractions() {{
      const cards = document.querySelectorAll('.product-card');
      const isMobile = /Android|iPhone|iPad|iPod/i.test(navigator.userAgent);

      cards.forEach(card => {{
        card.addEventListener('pointerdown', () => {{
          if (navigator.vibrate) navigator.vibrate(8);
        }});

        if (!isMobile) {{
          card.addEventListener('mousemove', (e) => {{
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            card.style.setProperty('--mx', `${{x}}px`);
            card.style.setProperty('--my', `${{y}}px`);

            const cx = rect.width / 2;
            const cy = rect.height / 2;
            const rx = ((y - cy) / cy) * -2.5;
            const ry = ((x - cx) / cx) * 2.5;

            card.style.transform = `perspective(1000px) rotateX(${{rx}}deg) rotateY(${{ry}}deg) translateY(-6px)`;
          }});

          card.addEventListener('mouseleave', () => {{
            card.style.transform = '';
          }});
        }}
      }});
    }}

    function slugify(text) {{
      return text.toString().toLowerCase()
        .replace(/\\s+/g, '-')
        .replace(/[^\\w\\-]+/g, '')
        .replace(/\\-\\-+/g, '-')
        .replace(/^-+/, '')
        .replace(/-+$/, '');
    }}
  </script>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

print("index.html generated successfully!")
