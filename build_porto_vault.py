import json
from pathlib import Path

DATA_FILE = Path("/Users/kiki/Documents/Web Develop/katalog-ceritakiki/data/products_enriched.json")
OUT_FILE = Path("/Users/kiki/Documents/Web Develop/katalog-ceritakiki/index.html")

CLEAN_NAMES = {
    1: ("Basreng Daun Jeruk Pedas 100g", "Camilan melek jam revisi numpuk"),
    2: ("Goojodoq Turbo Fan 100-Gear", "Penyelamat gerah desak-desakan di KRL"),
    3: ("Masker Duckbill 3-Ply (50 Pcs)", "Napas lega, proteksi polusi harian"),
    4: ("Tripod Selfie Stick 4-in-1 LED", "Setup konten & zoom meeting praktis"),
    5: ("Goojodoq Pocket Mini Fan 3000mAh", "Angin sejuk compact muat di saku"),
    6: ("Detergen Bubuk Sayang (5 Pack)", "Baju wangi segar jemuran kosan"),
    7: ("Uneed Gadget & Harddisk Hardcase", "Kabel charger & SSD rapi di ransel"),
    8: ("Pelindung Kabel Spiral 4-in-1", "Ujung kabel iPhone gak gampang sobek"),
    9: ("Buket Bunga Thumbelina Aesthetic", "Kado wisuda & anniversary awet"),
    10: ("4D Wave Soft Silicone iPhone Case", "Bodi HP aman benturan, grip mantap"),
    11: ("Inara Formal Shoulder Sling Bag", "Slingbag ringkas buat kerja & ngopi"),
    12: ("Calme Extrait De Parfum Vanilla Coffee", "Aroma vanilla coffee tahan seharian"),
    13: ("Clara Minimalist Leather Bag", "Tas bahu clean muat HP & dompet"),
    14: ("Buku: Is It Bad Or Good Habits", "Panduan bangun rutinitas positif"),
    15: ("Cloud Star Phone Charm Strap", "Gantungan HP aesthetic anti jatuh"),
    16: ("3D Cute Charger Adapter Protector", "Kepala charger aman dari lecet"),
    17: ("Achava Yuri Flat Casual Sandals", "Sandal empuk anti lecet jalan santai"),
    18: ("Magsafe Plating Metallic iPhone Case", "Proteksi ramping support wireless charge"),
    19: ("BiuBiu Clear Magnetic Magsafe Case", "Tampil bening tanpa kuning berbulan"),
    20: ("Silicone Sport Band for Apple Watch", "Strap lentur nyaman buat olahraga"),
    21: ("Organeez Clear Display Folder F4", "Dokumen kerja & sertifikat tersimpan rapi"),
    22: ("Laboré Barrier Revive Cream BiomeRepair", "Perbaiki skin barrier kering & kemerahan"),
    23: ("Deodorant Tawas Organik Spray 100ml", "Ketiak kering wangi alami tanpa residu"),
    24: ("Octarine Scandalusy Fruity Eau De Parfum", "Wangi fruity manis segar tahan lama"),
    25: ("Lem Perekat Kuku Palsu (24 Pcs)", "Nail art praktis tanpa ke salon"),
    26: ("Han River Hair Dryer 800W", "Rambut kering kilat 5 menit hemat daya"),
    27: ("Facetology Triple Care Sunscreen SPF40", "Sunscreen matte seringan air tanpa whitecast"),
    28: ("Deodorant Tawas Essential Oil Spray", "Penghilang bau badan formula essential oil"),
    29: ("Luxcrime Blur & Cover Two Way Cake", "Samarkan pori instan bebas kilap seharian"),
    30: ("Hanasui Mattedorable Lip Cream Boba", "Lip cream matte transferproof wangi boba"),
    31: ("Dove Pro-Ceramide Serum Body Wash", "Kulit lembab kenyal sehabis mandi"),
    32: ("Glow fx Beauty Serum Glow Bomb", "Serum pencerah bekas jerawat & kusam"),
    33: ("Giv White Mulberry Body Wash 800ml", "Sabun mandi wangi mewah refill hemat"),
    34: ("OMG Oh My Glam Mattelast Lip Cream", "Lip cream ringan tahan 12 jam no transfer"),
    35: ("Hanasui Blurry Tint Watery Stain", "Efek bibir blurry alami ala Korea"),
    36: ("MBK Deodorant Roll On & Bedak", "Bedak legendaris basmi keringat berlebih"),
    37: ("White Inc Alpha Glowhite Body Lotion", "Lotion pencerah kulit belang & kering"),
    38: ("Braven Code Masculine Eau De Parfum", "Wangi maskulin karismatik buat ngantor"),
    39: ("Miniso Natural Body Mist 150ml", "Semprot segar sehabis commute harian"),
    40: ("Kudan Halal Peel-Off Nail Polish", "Kutek mudah dikelupas tanpa aseton"),
    41: ("Sunny Travel Cosmetic Organizer Pouch", "Skincare & makeup rapi saat travelling"),
    42: ("Vitalis Extra Bloom Eau De Parfum", "Floral elegan tahan sampai sore"),
    43: ("Plastik Vacuum Sealer Embossed", "Makanan & frozen food kedap udara awet"),
    44: ("Ultrasonic Aroma Diffuser 500ml", "Kamar kosan wangi hotel bintang lima"),
    45: ("Paper Lunch Box Eco Kraft (50 Pcs)", "Kotak bekal ramah lingkungan anti bocor"),
    46: ("Cup Plastik Minuman Tebal Starindo", "Gelas kopi dingin tebal anti tumpah"),
    47: ("Standing Pouch Foil Ziplock", "Kemas snack & kopi kedap udara rapi"),
    48: ("Tumbler Thermos SUS316 Stainless", "Air es tahan dingin 12 jam hemat jajan"),
    49: ("Plastik Polymailer Packing Tebal", "Paket jualan aman dari hujan & sobek"),
    50: ("Handuk Mandi Merah Putih Katun", "Super serap air lembut di kulit"),
    51: ("Yonezawa Meja Setrika Duduk Lipat", "Setrika baju kosan hemat tempat"),
    52: ("Tumbler Smart LED Temperature Display", "Pantau suhu kopi hangat real-time"),
    53: ("Keset Kamar Mandi Memory Foam Diatomite", "Serap air seketika, lantai anti becek"),
    54: ("Venetian Horizontal Blind Minimalis", "Tirai jendela kosan estetik anti silau"),
    55: ("Nice Facial Tissue 2-Ply 180s", "Tisu lembut serbaguna meja kerja"),
    56: ("Technoplast Water Pitcher + 4 Gelas", "Teko air minum dingin siap sedia di kulkas"),
    57: ("Filter Kran Air Kapas Sekali Pakai", "Saring karat & kotoran air pam kosan"),
    58: ("Kain Lap Microfiber Halus Serbaguna", "Lap layar laptop & meja tanpa baret"),
    59: ("Talenan Kayu Jati Perhutani Asli", "Alas potong dapur kuat awet anti jamur"),
    60: ("Lazzen Rak Piring Wastafel Stainless", "Wastafel rapi, piring basah cepat tiris"),
    61: ("Goto Abel Alat Pel Peras Otomatis", "Ngepel lantai bersih tanpa peras tangan"),
    62: ("Linen & Room Spray Anti Bakteri 250ml", "Kasur wangi segar bebas bau apek"),
    63: ("Bantal Duduk Biskuit Memory Foam", "Alas kursi kerja anti pegal tulang ekor"),
    64: ("Kotak Sepatu Transparan Stackable", "Sepatu tersusun rapi bebas debu kosan"),
    65: ("Tifale Granite Milk Saucepan 20cm", "Panci mie rebus anti lengket mudah dicuci"),
    66: ("Technoplast Lovelo Punch Bowl Set", "Wadah es buah segar buat kumpul santai"),
    67: ("Netpot Jaring Hidroponik Tebal", "Pot tanaman sayur mini di balkon"),
    68: ("Overnight Oat & Salad Jar Portable", "Wadah sarapan sehat lengkap sendok"),
    69: ("Rak Bumbu Dapur Susun 3 Minimalis", "Bumbu dapur terorganisir rapi gak berantakan"),
    70: ("Mama Lemon Jeruk Nipis 920g (Isi 2)", "Rontokkan minyak piring sekali bilas"),
    71: ("Keset Dapur Long Runner 2-in-1", "Alas dapur anti selip tahan cipratan minyak"),
    72: ("Hiasan Dinding Metal Geometris", "Wall art modern hias ruang tamu kosan"),
    73: ("Collins Crunchy Chocolate Spread 1kg", "Selai coklat renyah nagih buat sarapan"),
    74: ("Makaroni Pipa Bantat Gurih 1kg", "Camilan renyah teman nonton film"),
    75: ("Nutrifarm Sari Lemon Murni 500ml", "Detox vitamin C alami setiap pagi"),
    76: ("Safiya Muesli Oatmeal Almond Apple 1kg", "Sarapan serat tinggi kenyang lebih lama"),
    77: ("PikuLabs Pure Ceremonial Matcha 100g", "Matcha murni tanpa gula booster fokus"),
    78: ("Kanzler Crispy Chicken Nugget 450g", "Nugget renyah ekstra daging penyelamat lapar"),
    79: ("Nutrifarm Organic Chia Seeds 70g", "Superfood kaya omega-3 untuk smoothies"),
    80: ("Troli Rak Susun Roda Serbaguna", "Rak beroda fleksibel geser sudut kosan"),
    81: ("Mama Lemon Sabun Cuci Piring Yuzu", "Basmi bau amis & sisa lemak bandel"),
    82: ("Organizer Pintu Kulkas Akrilik", "Rak botol saus kulkas tersusun rapi"),
    83: ("Chair Shape Mobile Phone Stand", "Dudukan HP estetik nonton santai di meja"),
    84: ("Rak Dapur Sudut Portable 3 Tingkat", "Maksimalkan ruang sudut sempit kosan"),
    85: ("Pure Water Baby Wipes Bebas Alkohol", "Tisu basah lembut ramah kulit sensitif"),
    86: ("Joodutp Filter Kran Air Kain 10 Pcs", "Air mandi lebih jernih bebas sedimen"),
    87: ("Nano Double Tape Bening Serbaguna", "Tempel hiasan dinding tanpa paku"),
    88: ("Foam Cleaner Pembersih Kerak Toilet", "Rontokkan kerak kloset tanpa sikat capek"),
    89: ("Stainless Ear Pick Set 6-in-1 + Pouch", "Korek kuping higienis tersimpan rapi"),
    90: ("Minyak Goreng Sunco Pouch Higienis", "Minyak goreng bening gorengan lebih crispy"),
    91: ("Foldable Desktop Phone & Tablet Stand", "Tinggi & sudut HP bisa diatur fleksibel"),
    92: ("SoSoft Sweet Peony Liquid Detergent", "Cucian wangi floral mewah ramah serat kain"),
    93: ("Elodie Rayon High-Waist Casual Pants", "Celana santai adem nyaman harian"),
    94: ("Ciptadent Maxi 12 Pasta Gigi 225g (Isi 2)", "Napas segar perlindungan gigi berlubang"),
    95: ("Dumpling Squishy Jumbo Anti Stress", "Mainan pencet pereda penat jam deadline"),
    96: ("Hohoisyou Self-Adhesive Eyelashes", "Bulu mata lentik natural tanpa lem repot"),
    97: ("Sandrinna Fine Fragrance Mist 90ml", "Parfum semprot fresh harian wangi mewah"),
    98: ("Mlan C-Curl Natural False Eyelashes", "Mata berdimensi natural ala douyin"),
    99: ("Wardah Colorfit Perfect Glow Cushion", "Coverage flawless hasil glowing natural"),
    100: ("Glad2Glow Waterproof Coverage Cushion", "Tutup noda bekas jerawat tahan air seharian"),
}

with open(DATA_FILE, "r", encoding="utf-8") as f:
    products = json.load(f)

for p in products:
    pid = p["id"]
    if pid in CLEAN_NAMES:
        clean_title, clean_hook = CLEAN_NAMES[pid]
        p["clean_title"] = clean_title
        p["clean_hook"] = clean_hook
    else:
        p["clean_title"] = p["name"][:40]
        p["clean_hook"] = p.get("hook", "")[:45]

# Top 3 Viral Bento Picks
viral_ids = [2, 44, 23] # Goojodoq Kipas (Hero), Aroma Diffuser, Tawas Deodorant
bento_items = [p for p in products if p["id"] in viral_ids]
bento_items.sort(key=lambda x: viral_ids.index(x["id"]))

html_template = f'''<!DOCTYPE html>
<html lang="id" class="theme-cream scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kiki Rachmat — Curated Essentials (@kikipunyacerita)</title>
  <meta name="description" content="Koleksi barang penunjang kerja, kosan, dan commute yang sering gue spill di Threads. Semua rating 4.8+ lolos kurasi tanpa gimmick.">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">

  <!-- OpenGraph -->
  <meta property="og:title" content="Kiki Rachmat — Curated Essentials">
  <meta property="og:description" content="100 barang penunjang kerja, kosan, dan commute terkurasi.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://katalog-ceritakiki.vercel.app">

  <!-- Google Fonts: Syne, Space Grotesk, JetBrains Mono (Identical to Porto Web) -->
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
            // Porto Web tokens
            background: '#0A0A0A',
            surface: '#111111',
            cream: '#F0ECE5',
            creamDark: '#E8E3DB',
            ink: '#111111',
            inkLight: '#555555',
            filmRed: '#C84B2F',
            filmRedLight: '#D9614A',
          }}
        }}
      }}
    }}
  </script>

  <style>
    :root {{
      --bg-cream: #F0ECE5;
      --bg-card: #FFFFFF;
      --border-cream: rgba(0, 0, 0, 0.08);
      --text-ink: #111111;
      --text-muted: #555555;
      --accent: #C84B2F;
    }}

    .theme-cream {{
      background-color: var(--bg-cream);
      color: var(--text-ink);
    }}

    .theme-cream .editorial-surface {{
      background-color: #FFFFFF;
      border-color: rgba(0, 0, 0, 0.08);
    }}

    .theme-cream .editorial-border {{
      border-color: rgba(0, 0, 0, 0.08);
    }}

    .theme-cream .editorial-text {{
      color: #111111;
    }}

    .theme-cream .editorial-muted {{
      color: #555555;
    }}

    .theme-cream .pill-active {{
      background-color: #111111;
      color: #F0ECE5;
      border-color: #111111;
    }}

    .theme-cream .pill-inactive {{
      background-color: rgba(255, 255, 255, 0.8);
      color: #555555;
      border-color: rgba(0, 0, 0, 0.1);
    }}

    /* Dark Mode Variant */
    .theme-dark {{
      background-color: #0A0A0A;
      color: #F0ECE5;
    }}

    .theme-dark .editorial-surface {{
      background-color: #121212;
      border-color: rgba(255, 255, 255, 0.08);
    }}

    .theme-dark .editorial-border {{
      border-color: rgba(255, 255, 255, 0.08);
    }}

    .theme-dark .editorial-text {{
      color: #FFFFFF;
    }}

    .theme-dark .editorial-muted {{
      color: #888888;
    }}

    .theme-dark .pill-active {{
      background-color: #FFFFFF;
      color: #0A0A0A;
      border-color: #FFFFFF;
    }}

    .theme-dark .pill-inactive {{
      background-color: rgba(255, 255, 255, 0.04);
      color: #888888;
      border-color: rgba(255, 255, 255, 0.08);
    }}

    /* Hardware Accelerated Video & Image Rendering (Porto Web globals.css) */
    img {{
      transform: translateZ(0);
      backface-visibility: hidden;
    }}

    .project-card {{
      position: relative;
      overflow: hidden;
      cursor: pointer;
      will-change: transform, opacity;
    }}

    .project-card img {{
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s ease;
      width: 100%;
      height: 100%;
    }}

    .project-card:hover img {{
      transform: scale(1.04);
    }}

    ::-webkit-scrollbar {{
      width: 4px;
    }}
    ::-webkit-scrollbar-track {{
      background: #0A0A0A;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #333333;
      border-radius: 9999px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #C84B2F;
    }}

    ::selection {{
      background: rgba(200, 75, 47, 0.25);
      color: #111111;
    }}
    .theme-dark ::selection {{
      color: #FFFFFF;
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
<body class="min-h-screen flex flex-col font-sans transition-colors duration-300">

  <!-- Toast Notification -->
  <aside id="toast" role="status" aria-live="polite" class="fixed bottom-6 right-6 z-50 transform translate-y-16 opacity-0 transition-all duration-300 pointer-events-none flex items-center gap-2.5 bg-[#111111] border border-white/10 px-4 py-3 rounded-full shadow-2xl text-xs font-mono text-white">
    <span class="text-[#C84B2F]">●</span>
    <span id="toast-text">Link Shopee disalin ke clipboard</span>
  </aside>

  <!-- Sticky Luxury Top Bar -->
  <header class="w-full border-b editorial-border sticky top-0 z-40 backdrop-blur-md bg-opacity-90 transition-colors">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex items-center justify-between">
      
      <!-- Brand Kicker -->
      <a href="https://kikirach.vercel.app" target="_blank" rel="noopener noreferrer" class="flex items-center gap-2 group">
        <span class="font-mono text-xs uppercase tracking-widest editorial-muted group-hover:editorial-text transition-colors">KIKI RACHMAT</span>
        <span class="text-gray-400">/</span>
        <span class="font-mono text-xs font-medium text-[#C84B2F]">@kikipunyacerita</span>
      </a>

      <!-- Right Controls: Threads & Theme Toggle -->
      <div class="flex items-center gap-3 font-mono text-xs">
        <a href="https://www.threads.net/@kikipunyacerita" target="_blank" rel="noopener noreferrer" class="hidden sm:inline-flex items-center gap-1 editorial-muted hover:editorial-text transition-colors">
          <span>Threads</span>
          <span class="text-[10px]">↗</span>
        </a>

        <!-- Minimalist Theme Switcher -->
        <button id="themeToggleBtn" aria-label="Toggle Theme" class="flex items-center gap-1.5 px-3 py-1.5 rounded-full border editorial-border text-[11px] editorial-muted hover:editorial-text transition-all bg-white/40 dark:bg-white/5">
          <span id="themeIndicator">●</span>
          <span id="themeLabel">CREAM</span>
        </button>
      </div>

    </div>
  </header>

  <!-- Cinematic Hero Section (Exact Porto Web HeroBio DNA) -->
  <section class="w-full bg-[#0A0A0A] text-[#F0ECE5] relative overflow-hidden py-16 sm:py-24 border-b border-white/10 select-none">
    
    <!-- Ambient luxury glow orb behind typography (#C84B2F/10 blur 140px) -->
    <div class="absolute top-1/2 left-1/3 -translate-x-1/2 -translate-y-1/2 w-[550px] h-[550px] bg-[#C84B2F]/15 rounded-full blur-[150px] pointer-events-none"></div>

    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Kicker Tag -->
      <div class="inline-flex items-center gap-2 mb-4 font-mono text-[11px] uppercase tracking-widest text-[#C84B2F]">
        <span>●</span>
        <span>Curated Vault • 100 Verified Objects</span>
      </div>

      <!-- Massive Syne Hero Headline -->
      <div class="max-w-4xl mb-6">
        <h1 class="text-white font-display font-black uppercase tracking-tighter leading-[0.88] text-5xl sm:text-7xl md:text-8xl">
          Kiki
        </h1>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-gray-100 via-gray-300 to-gray-500 font-display font-black uppercase tracking-tight leading-[0.9] text-3xl sm:text-5xl md:text-6xl block mt-1">
          Rachmat.
        </span>
      </div>

      <p class="font-sans text-gray-400 text-sm sm:text-base leading-relaxed max-w-2xl mb-8">
        Koleksi barang pilihan penunjang kerja, kosan, dan commute yang sering gue spill di Threads. Semua sudah melalui kurasi fungsi jelas, durabilitas tinggi, dan harga masuk akal tanpa gimmick.
      </p>

      <!-- Stats Bar in JetBrains Mono -->
      <div class="flex flex-wrap items-center gap-4 sm:gap-6 font-mono text-xs text-gray-500 pt-2 border-t border-white/10">
        <div><strong class="text-white font-bold text-sm">100</strong> OBJECTS ARCHIVED</div>
        <span class="text-gray-700">•</span>
        <div><strong class="text-white font-bold text-sm">4.8+</strong> SHOPEE RATING</div>
        <span class="text-gray-700">•</span>
        <div><strong class="text-white font-bold text-sm">&lt; 100K</strong> IMPULSE PRICE</div>
      </div>

    </div>
  </section>

  <!-- Bento Showcase: Top 3 Viral Highlights (Porto Web BentoShowcase style) -->
  <section class="w-full py-12 sm:py-16 border-b editorial-border">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex items-center justify-between mb-8 border-b editorial-border pb-4">
        <div>
          <span class="font-mono text-[10px] text-[#C84B2F] uppercase tracking-widest block font-bold">TOP VIRAL PICKS</span>
          <h2 class="font-display font-black uppercase text-2xl sm:text-3xl tracking-tight editorial-text">
            Sering Ditanyain di Threads
          </h2>
        </div>
        <span class="font-mono text-xs editorial-muted">03 FEATURED</span>
      </div>

      <!-- Bento Grid Layout: 1 Hero 2-col card + 2 1-col cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 sm:gap-8">
        
        <!-- Bento 1: Hero Card (Spans 2 columns) -->
        <article class="project-card group cursor-pointer flex flex-col md:col-span-2">
          <div class="overflow-hidden bg-[#0F0F0F] relative w-full aspect-[16/10] sm:aspect-[16/9] rounded-2xl sm:rounded-3xl border editorial-border shadow-sm group-hover:shadow-2xl transition-all duration-500">
            <img 
              src="{bento_items[0]['image_url']}" 
              alt="{bento_items[0]['clean_title']}"
              class="w-full h-full object-cover object-center filter grayscale contrast-110 group-hover:grayscale-0 group-hover:contrast-100 transition-all duration-700 ease-out group-hover:scale-105"
            >
            <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-between p-5 sm:p-7 pointer-events-none">
              <div class="flex items-center justify-between">
                <span class="px-3 py-1 rounded-full bg-black/60 backdrop-blur-md text-[10px] font-mono text-white/95 uppercase tracking-widest font-bold border border-white/15">
                  #1 VIRAL COMMUTE
                </span>
                <span class="inline-flex items-center gap-1.5 px-4 py-1.5 rounded-full bg-[#C84B2F] text-white text-[10px] font-mono font-bold uppercase tracking-wider shadow-xl transform translate-x-2 group-hover:translate-x-0 transition-transform duration-300">
                  <span>Beli di Shopee</span>
                  <span class="text-xs">↗</span>
                </span>
              </div>
              <div class="space-y-1 transform translate-y-2 group-hover:translate-y-0 transition-transform duration-300">
                <h3 class="text-white font-bold text-xl sm:text-2xl uppercase tracking-tight font-display">
                  {bento_items[0]['clean_title']}
                </h3>
                <p class="text-gray-300 text-xs font-mono">
                  {bento_items[0]['price_formatted']} • {bento_items[0]['shop']}
                </p>
              </div>
            </div>
            <a href="{bento_items[0]['affiliate_url']}" target="_blank" rel="noopener noreferrer" class="absolute inset-0 z-10" aria-label="Beli {bento_items[0]['clean_title']}"></a>
          </div>

          <div class="mt-3.5 flex items-baseline justify-between gap-2 px-1 w-full min-w-0">
            <div class="min-w-0 flex-1">
              <h3 class="font-bold text-base sm:text-lg uppercase editorial-text group-hover:text-[#C84B2F] transition-colors truncate font-display">
                {bento_items[0]['clean_title']}
              </h3>
              <p class="text-xs font-mono editorial-muted truncate mt-0.5">
                {bento_items[0]['clean_hook']}
              </p>
            </div>
            <span class="font-mono font-bold text-sm sm:text-base shrink-0 editorial-text">
              {bento_items[0]['price_formatted']}
            </span>
          </div>
        </article>

        <!-- Bento 2 & 3 Column -->
        <div class="flex flex-col gap-6 sm:gap-8">
          
          <!-- Bento 2: Aroma Diffuser -->
          <article class="project-card group cursor-pointer flex flex-col">
            <div class="overflow-hidden bg-[#0F0F0F] relative w-full aspect-[16/10] rounded-2xl sm:rounded-3xl border editorial-border shadow-sm group-hover:shadow-2xl transition-all duration-500">
              <img 
                src="{bento_items[1]['image_url']}" 
                alt="{bento_items[1]['clean_title']}"
                class="w-full h-full object-cover object-center filter grayscale contrast-110 group-hover:grayscale-0 group-hover:contrast-100 transition-all duration-700 ease-out group-hover:scale-105"
              >
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-between p-4 sm:p-5 pointer-events-none">
                <div class="flex items-center justify-between">
                  <span class="px-2.5 py-1 rounded-full bg-black/60 backdrop-blur-md text-[9px] font-mono text-white uppercase tracking-widest font-bold border border-white/15">
                    KOSAN LUXURY
                  </span>
                  <span class="inline-flex items-center gap-1 px-3 py-1 rounded-full bg-[#C84B2F] text-white text-[9px] font-mono font-bold uppercase tracking-wider shadow-xl">
                    <span>Beli</span>
                    <span>↗</span>
                  </span>
                </div>
                <div>
                  <h3 class="text-white font-bold text-base uppercase font-display">{bento_items[1]['clean_title']}</h3>
                  <p class="text-gray-300 text-xs font-mono">{bento_items[1]['price_formatted']}</p>
                </div>
              </div>
              <a href="{bento_items[1]['affiliate_url']}" target="_blank" rel="noopener noreferrer" class="absolute inset-0 z-10" aria-label="Beli {bento_items[1]['clean_title']}"></a>
            </div>

            <div class="mt-3 flex items-baseline justify-between gap-2 px-1 w-full min-w-0">
              <div class="min-w-0 flex-1">
                <h3 class="font-bold text-sm sm:text-base uppercase editorial-text group-hover:text-[#C84B2F] transition-colors truncate font-display">
                  {bento_items[1]['clean_title']}
                </h3>
                <p class="text-xs font-mono editorial-muted truncate mt-0.5">
                  {bento_items[1]['clean_hook']}
                </p>
              </div>
              <span class="font-mono font-bold text-sm shrink-0 editorial-text">
                {bento_items[1]['price_formatted']}
              </span>
            </div>
          </article>

          <!-- Bento 3: Tawas Deodorant -->
          <article class="project-card group cursor-pointer flex flex-col">
            <div class="overflow-hidden bg-[#0F0F0F] relative w-full aspect-[16/10] rounded-2xl sm:rounded-3xl border editorial-border shadow-sm group-hover:shadow-2xl transition-all duration-500">
              <img 
                src="{bento_items[2]['image_url']}" 
                alt="{bento_items[2]['clean_title']}"
                class="w-full h-full object-cover object-center filter grayscale contrast-110 group-hover:grayscale-0 group-hover:contrast-100 transition-all duration-700 ease-out group-hover:scale-105"
              >
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-between p-4 sm:p-5 pointer-events-none">
                <div class="flex items-center justify-between">
                  <span class="px-2.5 py-1 rounded-full bg-black/60 backdrop-blur-md text-[9px] font-mono text-white uppercase tracking-widest font-bold border border-white/15">
                    UNDER 10K
                  </span>
                  <span class="inline-flex items-center gap-1 px-3 py-1 rounded-full bg-[#C84B2F] text-white text-[9px] font-mono font-bold uppercase tracking-wider shadow-xl">
                    <span>Beli</span>
                    <span>↗</span>
                  </span>
                </div>
                <div>
                  <h3 class="text-white font-bold text-base uppercase font-display">{bento_items[2]['clean_title']}</h3>
                  <p class="text-gray-300 text-xs font-mono">{bento_items[2]['price_formatted']}</p>
                </div>
              </div>
              <a href="{bento_items[2]['affiliate_url']}" target="_blank" rel="noopener noreferrer" class="absolute inset-0 z-10" aria-label="Beli {bento_items[2]['clean_title']}"></a>
            </div>

            <div class="mt-3 flex items-baseline justify-between gap-2 px-1 w-full min-w-0">
              <div class="min-w-0 flex-1">
                <h3 class="font-bold text-sm sm:text-base uppercase editorial-text group-hover:text-[#C84B2F] transition-colors truncate font-display">
                  {bento_items[2]['clean_title']}
                </h3>
                <p class="text-xs font-mono editorial-muted truncate mt-0.5">
                  {bento_items[2]['clean_hook']}
                </p>
              </div>
              <span class="font-mono font-bold text-sm shrink-0 editorial-text">
                {bento_items[2]['price_formatted']}
              </span>
            </div>
          </article>

        </div>

      </div>

    </div>
  </section>

  <!-- Complete Archive Catalog (Exact Porto Web Filmography / Archive Section) -->
  <section class="w-full py-16 sm:py-24 flex-1" id="archive">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
      
      <!-- Section Header -->
      <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4 mb-8 sm:mb-10 border-b editorial-border pb-6">
        <div>
          <h2 class="editorial-text font-display font-black uppercase text-4xl sm:text-6xl tracking-tight leading-none">
            Archive
          </h2>
        </div>
        <p class="font-mono editorial-muted text-xs sm:text-sm shrink-0">
          <strong class="editorial-text font-bold" id="resultsCount">100</strong> OBJECTS ARCHIVED
        </p>
      </div>

      <!-- Controls: Category Pills & Search (Touch & Mobile Optimized) -->
      <div class="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-4 mb-8">
        
        <!-- Category Tabs (Rounded-full, exact Porto Web style) -->
        <div class="flex items-center gap-2 overflow-x-auto no-scrollbar pb-1.5 -mx-4 px-4 sm:mx-0 sm:px-0 font-mono text-xs">
          <button data-filter="all" class="filter-pill pill-active px-4 py-2 rounded-full whitespace-nowrap transition-all border shrink-0">
            All Works (100)
          </button>
          <button data-filter="Budak Korporat" class="filter-pill pill-inactive px-4 py-2 rounded-full whitespace-nowrap transition-all border shrink-0">
            Budak Korporat
          </button>
          <button data-filter="Penyelamat Kosan" class="filter-pill pill-inactive px-4 py-2 rounded-full whitespace-nowrap transition-all border shrink-0">
            Penyelamat Kosan
          </button>
          <button data-filter="Glow Up Murah" class="filter-pill pill-inactive px-4 py-2 rounded-full whitespace-nowrap transition-all border shrink-0">
            Glow Up & Care
          </button>
          <button data-filter="Camilan & Stress" class="filter-pill pill-inactive px-4 py-2 rounded-full whitespace-nowrap transition-all border shrink-0">
            Snack & Relaks
          </button>
          <button data-filter="Di Bawah 20rb" class="filter-pill pill-inactive px-4 py-2 rounded-full whitespace-nowrap transition-all border shrink-0">
            Under 20k
          </button>
        </div>

        <!-- Search Box (Exact Porto Web Filmography Search) -->
        <div class="relative w-full sm:w-72 shrink-0">
          <input 
            type="search" 
            id="searchInput" 
            placeholder="Cari solusi (kipas, diffuser, kabel)..." 
            class="w-full pl-9 pr-8 py-2.5 rounded-full editorial-surface border editorial-border editorial-text placeholder-gray-400 text-xs font-mono shadow-sm focus:outline-none focus:border-[#C84B2F] transition-all"
            autocomplete="off"
          >
          <span class="absolute left-3.5 top-1/2 -translate-y-1/2 text-gray-400 text-xs pointer-events-none">🔍</span>
          <button id="clearSearchBtn" class="hidden absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:editorial-text text-xs">✕</button>
        </div>

      </div>

      <!-- Product Cards Grid (3 Columns Desktop, 2 Columns Tablet, 1 Column Mobile) -->
      <div id="productGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
        <!-- Rendered by client-side JS -->
      </div>

      <!-- Empty State -->
      <div id="emptyState" class="hidden py-24 text-center">
        <p class="font-mono text-xs editorial-muted uppercase tracking-widest mb-2">[0 RESULTS]</p>
        <h3 class="text-2xl font-display font-bold editorial-text mb-2">Item Tidak Ditemukan</h3>
        <p class="text-xs editorial-muted mb-6 max-w-sm mx-auto">Coba cari dengan kata kunci lain atau reset filter kategori.</p>
        <button id="resetSearchBtn" class="font-mono text-xs px-5 py-2.5 rounded-full bg-[#111111] text-[#F0ECE5] dark:bg-white dark:text-black font-bold hover:opacity-90 transition shadow-sm">
          RESET FILTER
        </button>
      </div>

      <!-- Load More Button -->
      <div id="loadMoreContainer" class="mt-12 text-center">
        <button id="loadMoreBtn" class="px-8 py-3.5 rounded-full border editorial-border editorial-surface editorial-text font-mono text-xs font-bold uppercase tracking-wider hover:border-[#C84B2F] hover:text-[#C84B2F] transition-all shadow-sm">
          Load More Objects (+12)
        </button>
      </div>

    </div>
  </section>

  <!-- Clean Minimalist Footer (Exact ContactSection DNA) -->
  <footer class="w-full border-t editorial-border py-12 text-center font-mono text-xs editorial-muted transition-colors">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 space-y-2">
      <p class="editorial-text uppercase tracking-widest text-[11px] font-bold">KIKI RACHMAT • @KIKIPUNYACERITA</p>
      <p class="text-[11px]">Curated index for Threads audience. Links are Shopee affiliate redirects.</p>
      <p class="text-[10px] text-gray-400 pt-2">© 2026 Kiki Rachmat. All rights reserved.</p>
    </div>
  </footer>

  <!-- Product Data JSON -->
  <script id="product-data" type="application/json">
    {json.dumps(products, ensure_ascii=False)}
  </script>

  <!-- Client-Side Logic -->
  <script>
    const rawData = JSON.parse(document.getElementById('product-data').textContent);
    
    let activeFilter = 'all';
    let searchQuery = '';
    let visibleCount = 12;
    const PAGE_STEP = 12;

    const grid = document.getElementById('productGrid');
    const searchInput = document.getElementById('searchInput');
    const clearBtn = document.getElementById('clearSearchBtn');
    const countEl = document.getElementById('resultsCount');
    const emptyState = document.getElementById('emptyState');
    const resetBtn = document.getElementById('resetSearchBtn');
    const loadMoreContainer = document.getElementById('loadMoreContainer');
    const loadMoreBtn = document.getElementById('loadMoreBtn');
    const toast = document.getElementById('toast');
    const toastText = document.getElementById('toast-text');

    // Theme Switcher Logic
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const themeIndicator = document.getElementById('themeIndicator');
    const themeLabel = document.getElementById('themeLabel');
    const htmlEl = document.documentElement;

    function applyTheme(isDark) {{
      if (isDark) {{
        htmlEl.classList.remove('theme-cream');
        htmlEl.classList.add('theme-dark', 'dark');
        themeIndicator.textContent = '○';
        themeLabel.textContent = 'DARK';
        localStorage.setItem('katalog_theme', 'dark');
      }} else {{
        htmlEl.classList.remove('theme-dark', 'dark');
        htmlEl.classList.add('theme-cream');
        themeIndicator.textContent = '●';
        themeLabel.textContent = 'CREAM';
        localStorage.setItem('katalog_theme', 'cream');
      }}
    }}

    const savedTheme = localStorage.getItem('katalog_theme') || 'cream';
    applyTheme(savedTheme === 'dark');

    themeToggleBtn.addEventListener('click', () => {{
      const isCurrentlyDark = htmlEl.classList.contains('theme-dark');
      applyTheme(!isCurrentlyDark);
      updatePillsTheme();
    }});

    function updatePillsTheme() {{
      document.querySelectorAll('.filter-pill').forEach(btn => {{
        const isActive = btn.classList.contains('active-pill-marker');
        if (isActive) {{
          btn.className = 'filter-pill active-pill-marker pill-active px-4 py-2 rounded-full whitespace-nowrap transition-all border shrink-0';
        }} else {{
          btn.className = 'filter-pill pill-inactive px-4 py-2 rounded-full whitespace-nowrap transition-all border shrink-0';
        }}
      }});
    }}

    function showToast(text) {{
      toastText.textContent = text;
      toast.classList.remove('translate-y-16', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');
      setTimeout(() => {{
        toast.classList.add('translate-y-16', 'opacity-0');
        toast.classList.remove('translate-y-0', 'opacity-100');
      }}, 2400);
    }}

    function copyLink(url) {{
      navigator.clipboard.writeText(url).then(() => {{
        showToast('Link Shopee disalin ke clipboard');
      }}).catch(() => {{
        showToast('Gagal menyalin link');
      }});
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
        const indexStr = String(idx + 1).padStart(2, '0');
        const trackingUrl = `${{p.affiliate_url}}?utm_source=kikipunyacerita&utm_medium=bio_catalog&utm_campaign=item_${{p.id}}`;

        return `
          <article class="project-card group cursor-pointer flex flex-col w-full min-w-0">
            <!-- Living Visual Cover (Exact BentoShowcase Style) -->
            <div class="overflow-hidden bg-[#0F0F0F] relative w-full aspect-[16/10] rounded-2xl sm:rounded-3xl border editorial-border shadow-sm group-hover:shadow-2xl transition-all duration-500 group-hover:scale-[1.015]">
              <img 
                src="${{p.image_url}}" 
                alt="${{p.clean_title}}" 
                loading="lazy" 
                class="w-full h-full object-cover object-center filter grayscale contrast-110 group-hover:grayscale-0 group-hover:contrast-100 transition-all duration-700 ease-out group-hover:scale-105"
              >
              
              <!-- Luxury Vignette & Glass Overlay on Hover -->
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/25 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-between p-4 sm:p-5 pointer-events-none">
                <div class="flex items-center justify-between gap-2">
                  <span class="px-2.5 py-1 rounded-full bg-black/60 backdrop-blur-md text-[9px] font-mono text-white/95 uppercase tracking-widest font-bold border border-white/15 shadow-md">
                    #${{indexStr}} • ${{p.need_pill}}
                  </span>

                  <span class="inline-flex items-center gap-1 px-3 py-1 rounded-full bg-[#C84B2F] text-white text-[9px] font-mono font-bold uppercase tracking-wider shadow-xl transform translate-x-2 group-hover:translate-x-0 transition-transform duration-300">
                    <span>Beli</span>
                    <span class="text-[10px]">↗</span>
                  </span>
                </div>

                <div class="space-y-1 transform translate-y-2 group-hover:translate-y-0 transition-transform duration-300">
                  <h4 class="text-white font-bold text-sm sm:text-base uppercase tracking-tight line-clamp-1 font-display">
                    ${{p.clean_title}}
                  </h4>
                  <p class="text-gray-300 text-xs font-mono line-clamp-1">
                    ${{p.price_formatted}} • ${{p.shop}}
                  </p>
                </div>
              </div>

              <!-- Click opens Shopee Affiliate -->
              <a href="${{trackingUrl}}" target="_blank" rel="noopener noreferrer" class="absolute inset-0 z-10" aria-label="Beli ${{p.clean_title}}"></a>
            </div>

            <!-- Clean Metadata below card (Always Visible on Mobile/Desktop) -->
            <div class="mt-3.5 flex items-baseline justify-between gap-2 px-1 w-full min-w-0">
              <div class="min-w-0 flex-1">
                <h3 class="font-bold text-sm sm:text-base uppercase editorial-text group-hover:text-[#C84B2F] transition-colors truncate font-display">
                  ${{p.clean_title}}
                </h3>
                <p class="text-xs font-mono editorial-muted truncate mt-0.5">
                  ${{p.clean_hook}}
                </p>
              </div>
              
              <div class="flex items-center gap-2 shrink-0">
                <span class="font-mono font-bold text-xs sm:text-sm editorial-text">
                  ${{p.price_formatted}}
                </span>
                <button 
                  onclick="event.stopPropagation(); copyLink('${{p.affiliate_url}}')" 
                  aria-label="Salin Link"
                  class="p-1 rounded-md text-gray-400 hover:editorial-text transition-colors"
                  title="Salin Link Shopee"
                >
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
                </button>
              </div>
            </div>
          </article>
        `;
      }}).join('');

      // Load More Button visibility
      if (visibleCount >= filtered.length) {{
        loadMoreContainer.classList.add('hidden');
      }} else {{
        loadMoreContainer.classList.remove('hidden');
      }}
    }}

    // Filter Buttons
    document.querySelectorAll('.filter-pill').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.filter-pill').forEach(b => {{
          b.classList.remove('active-pill-marker', 'pill-active');
          b.classList.add('pill-inactive');
        }});
        btn.classList.add('active-pill-marker', 'pill-active');
        btn.classList.remove('pill-inactive');
        activeFilter = btn.getAttribute('data-filter');
        visibleCount = 12; // Reset pagination on category change
        renderProducts();
      }});
    }});

    // Search Input
    searchInput.addEventListener('input', (e) => {{
      searchQuery = e.target.value.trim();
      clearBtn.classList.toggle('hidden', !searchQuery);
      visibleCount = 12;
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

    // Load More Action
    loadMoreBtn.addEventListener('click', () => {{
      visibleCount += PAGE_STEP;
      renderProducts();
    }});

    // Keyboard Shortcut '/'
    document.addEventListener('keydown', (e) => {{
      if (e.key === '/' && document.activeElement !== searchInput) {{
        e.preventDefault();
        searchInput.focus();
      }}
    }});

    // Initial Marker
    document.querySelector('[data-filter="all"]').classList.add('active-pill-marker');
    renderProducts();
  </script>
</body>
</html>'''

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"✅ Generated Luxury Porto-Grade Catalog at {OUT_FILE}")
