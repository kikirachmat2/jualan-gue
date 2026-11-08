import json
from pathlib import Path

DATA_FILE = Path("/Users/kiki/Documents/Web Develop/katalog-ceritakiki/data/products.json")
OUT_FILE = Path("/Users/kiki/Documents/Web Develop/katalog-ceritakiki/data/products_enriched.json")

# Visual Image Mapping based on keywords
IMAGE_MAP = {
    'fan': 'https://images.unsplash.com/photo-1618941716939-553df3c6c278?auto=format&fit=crop&w=600&q=80',
    'snack': 'https://images.unsplash.com/photo-1599490659213-e2b9527bd087?auto=format&fit=crop&w=600&q=80',
    'mask': 'https://images.unsplash.com/photo-1584634731339-252c581abfc5?auto=format&fit=crop&w=600&q=80',
    'tripod': 'https://images.unsplash.com/photo-1512499617640-c74ae3a79d37?auto=format&fit=crop&w=600&q=80',
    'laundry': 'https://images.unsplash.com/photo-1582735689369-4fe89db7114c?auto=format&fit=crop&w=600&q=80',
    'case_tech': 'https://images.unsplash.com/photo-1544816155-12df9643f363?auto=format&fit=crop&w=600&q=80',
    'cable': 'https://images.unsplash.com/photo-1583863788434-e58a36330cf0?auto=format&fit=crop&w=600&q=80',
    'flower': 'https://images.unsplash.com/photo-1561181286-d3fee7d55364?auto=format&fit=crop&w=600&q=80',
    'phone_case': 'https://images.unsplash.com/photo-1601784551446-20c9e07cdbdb?auto=format&fit=crop&w=600&q=80',
    'bag': 'https://images.unsplash.com/photo-1548036328-c9fa89d128fa?auto=format&fit=crop&w=600&q=80',
    'perfume': 'https://images.unsplash.com/photo-1523293182086-7651a899d37f?auto=format&fit=crop&w=600&q=80',
    'book': 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=600&q=80',
    'keychain': 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=600&q=80',
    'sandal': 'https://images.unsplash.com/photo-1603808033192-082d6919d3e1?auto=format&fit=crop&w=600&q=80',
    'watch_strap': 'https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?auto=format&fit=crop&w=600&q=80',
    'folder': 'https://images.unsplash.com/photo-1586281380349-632531db7ed4?auto=format&fit=crop&w=600&q=80',
    'moisturizer': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=600&q=80',
    'deodorant': 'https://images.unsplash.com/photo-1608248597359-598d1a123f99?auto=format&fit=crop&w=600&q=80',
    'hair_dryer': 'https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=600&q=80',
    'sunscreen': 'https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?auto=format&fit=crop&w=600&q=80',
    'powder': 'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?auto=format&fit=crop&w=600&q=80',
    'lipstick': 'https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=600&q=80',
    'soap': 'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&w=600&q=80',
    'diffuser': 'https://images.unsplash.com/photo-1602928321679-560bb453f190?auto=format&fit=crop&w=600&q=80',
    'tumbler': 'https://images.unsplash.com/photo-1517256064527-09c73fc73e38?auto=format&fit=crop&w=600&q=80',
    'towel': 'https://images.unsplash.com/photo-1616627547584-bf28cee262db?auto=format&fit=crop&w=600&q=80',
    'iron_board': 'https://images.unsplash.com/photo-1582735689369-4fe89db7114c?auto=format&fit=crop&w=600&q=80',
    'bath_mat': 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=600&q=80',
    'pitcher': 'https://images.unsplash.com/photo-1544816155-12df9643f363?auto=format&fit=crop&w=600&q=80',
    'filter': 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=600&q=80',
    'cutting_board': 'https://images.unsplash.com/photo-1590794056226-79ef3a8147e1?auto=format&fit=crop&w=600&q=80',
    'dish_rack': 'https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=600&q=80',
    'mop': 'https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=600&q=80',
    'linen_spray': 'https://images.unsplash.com/photo-1608248597359-598d1a123f99?auto=format&fit=crop&w=600&q=80',
    'cushion': 'https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?auto=format&fit=crop&w=600&q=80',
    'shoe_box': 'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?auto=format&fit=crop&w=600&q=80',
    'saucepan': 'https://images.unsplash.com/photo-1584990347449-399a6132f8a4?auto=format&fit=crop&w=600&q=80',
    'oat_jar': 'https://images.unsplash.com/photo-1517673132405-a56a62b18caf?auto=format&fit=crop&w=600&q=80',
    'spice_rack': 'https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=600&q=80',
    'dishwashing': 'https://images.unsplash.com/photo-1585421514284-efb74c2b69ba?auto=format&fit=crop&w=600&q=80',
    'chocolate': 'https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=600&q=80',
    'lemon_juice': 'https://images.unsplash.com/photo-1534353473418-4cfa6c56fd38?auto=format&fit=crop&w=600&q=80',
    'muesli': 'https://images.unsplash.com/photo-1517673132405-a56a62b18caf?auto=format&fit=crop&w=600&q=80',
    'matcha': 'https://images.unsplash.com/photo-1536256263959-770b48d82b0a?auto=format&fit=crop&w=600&q=80',
    'nugget': 'https://images.unsplash.com/photo-1562967914-608f82629710?auto=format&fit=crop&w=600&q=80',
    'trolley': 'https://images.unsplash.com/photo-1595428774223-ef52624120d2?auto=format&fit=crop&w=600&q=80',
    'fridge_box': 'https://images.unsplash.com/photo-1584990347449-399a6132f8a4?auto=format&fit=crop&w=600&q=80',
    'phone_stand': 'https://images.unsplash.com/photo-1586105251261-72a756497a11?auto=format&fit=crop&w=600&q=80',
    'toilet_cleaner': 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=600&q=80',
    'squishy': 'https://images.unsplash.com/photo-1558882224-dda166733046?auto=format&fit=crop&w=600&q=80',
    'cushion_makeup': 'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?auto=format&fit=crop&w=600&q=80',
    'default': 'https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?auto=format&fit=crop&w=600&q=80'
}

def get_product_image_and_hook(name, price_num):
    nl = name.lower()
    
    if 'kipas' in nl:
        return IMAGE_MAP['fan'], "Penyelamat nyawa pas KRL Manggarai gerah parah", "Angin kencang 100 gear, baterai awet seharian."
    if 'basreng' in nl or 'makaroni' in nl:
        return IMAGE_MAP['snack'], "Obat ngantuk jam 3 sore pas revisi numpuk", "Pedas renyah daun jeruk bikin melek instan."
    if 'masker' in nl:
        return IMAGE_MAP['mask'], "Napas gak engap pas jalan kaki di polusi kota", "Bentuk 3D duckbill gak nempel bibir / makeup."
    if 'tongsis' in nl or 'tripod' in nl:
        return IMAGE_MAP['tripod'], "Bikin konten / selfie sendirian tanpa minta tolong", "Remote bluetooth + lampu LED 4-in-1 praktis."
    if 'detergen' in nl or 'sosoft' in nl:
        return IMAGE_MAP['laundry'], "Baju wangi segar walau dijemur di kosan sempit", "Hemat isi 5 sachet, busa melimpah gak apek."
    if 'ssd' in nl or 'powerbank' in nl or 'hardcase' in nl:
        return IMAGE_MAP['case_tech'], "Harddisk & kabel charger aman gak ketumpuk rusak", "Bahan hard EVA anti-bentur & shockproof."
    if 'pelindung kabel' in nl or 'cable' in nl:
        return IMAGE_MAP['cable'], "Ujung kabel charger gak gampang putus / terkelupas", "Set lengkap spiral + cover kepala charger awet."
    if 'buket' in nl:
        return IMAGE_MAP['flower'], "Kado wisuda & ultah pacar aesthetic gak bikin boncos", "Buket handmade rapi tahan lama selamanya."
    if 'case' in nl or 'magsafe' in nl:
        return IMAGE_MAP['phone_case'], "Bikin HP keliatan mewah & anti lecet pas jatuh", "Silicone tebal + lens protector kamera aman."
    if 'tas' in nl or 'slingbag' in nl:
        return IMAGE_MAP['bag'], "Tas ngantor / jalan simpel muat dompet & HP", "Bahan kulit sintetis awet, model clean elegan."
    if 'parfum' in nl or 'fragrance' in nl or 'calme' in nl or 'octarine' in nl or 'vitalis' in nl:
        return IMAGE_MAP['perfume'], "Wangi mewah elegan tahan seharian gak nusuk hidung", "Aroma vanilla coffee / fresh tahan 8-12 jam."
    if 'buku' in nl or 'habits' in nl:
        return IMAGE_MAP['book'], "Bacaan singkat ubah hidup biar gak overthinking terus", "Panduan praktis bangun kebiasaan produktif."
    if 'gantungan kunci' in nl:
        return IMAGE_MAP['keychain'], "Biar kunci kosan gak gampang keselip & hilang", "Aesthetic liontin cloud cocok buat casing & kunci."
    if 'sandal' in nl:
        return IMAGE_MAP['sandal'], "Kaki gak pegel jalan jauh di stasiun / kantor", "Sandal empuk tebal, anti selip pas lantai basah."
    if 'iwatch' in nl or 'strap' in nl:
        return IMAGE_MAP['watch_strap'], "Ganti look jam tangan biar gak bosen pas ngantor", "Bahan silicone lembut gak bikin gatal di kulit."
    if 'clear holder' in nl or 'map' in nl:
        return IMAGE_MAP['folder'], "Dokumen kerja & surat penting rapi anti lecek", "Map display 20/40 pocket tahan air tebal."
    if 'labore' in nl or 'moisturizer' in nl:
        return IMAGE_MAP['moisturizer'], "Perbaiki skin barrier pas kulit kering akibat AC", "Dermatologist approved, lembut buat kulit sensitif."
    if 'deodorant' in nl or 'tawas' in nl or 'mbk' in nl:
        return IMAGE_MAP['deodorant'], "Bebas bau badan seharian tanpa noda kuning kemeja", "Tawas organik alami 100% aman gak bikin hitam."
    if 'hair dryer' in nl:
        return IMAGE_MAP['hair_dryer'], "Keringin rambut kilat 5 menit sebelum berangkat kantor", "Angin kencang 800W hemat listrik gak ngerusak rambut."
    if 'sunscreen' in nl or 'facetology' in nl:
        return IMAGE_MAP['sunscreen'], "Wajah gak kusam & gak berminyak di bawah terik jalan", "SPF 40 PA+++ matte finish ringan tanpa whitecast."
    if 'two way cake' in nl or 'bedak' in nl or 'luxcrime' in nl:
        return IMAGE_MAP['powder'], "Pori-pori tersamarkan kilat touch-up 10 detik", "Blurring effect bebas minyak tahan 24 jam."
    if 'lip' in nl or 'hanasui' in nl or 'omg' in nl:
        return IMAGE_MAP['lipstick'], "Bibir gak pucat seharian walau minum kopi berkali-kali", "Matte transferproof ringan di bibir gak bikin kering."
    if 'body wash' in nl or 'sabun mandi' in nl or 'dove' in nl:
        return IMAGE_MAP['soap'], "Mandi segar wangi parfum lembut bikin rileks pikiran", "Kandungan serum melembapkan kulit seharian."
    if 'diffuser' in nl or 'summerspring' in nl:
        return IMAGE_MAP['diffuser'], "Kamar kos 3x3 auto wangi kamar hotel bintang 5", "Aroma wangi tahan sebulan bikin tidur nyenyak."
    if 'tumbler' in nl or 'thermos' in nl:
        return IMAGE_MAP['tumbler'], "Hemat ratusan ribu gak jajan es kopi terus di kantor", "Tahan es batu dingin 12-24 jam stainless food grade."
    if 'handuk' in nl:
        return IMAGE_MAP['towel'], "Handuk mandi super nyerap air gak gampang bau apek", "100% katun tebal lembut di kulit ukuran pas."
    if 'setrika' in nl:
        return IMAGE_MAP['iron_board'], "Baju rapi rapih di kosan tanpa makan tempat", "Papan setrika lipat meja bisa disimpan di kolong."
    if 'keset' in nl:
        return IMAGE_MAP['bath_mat'], "Lantai kamar mandi gak licin dan cepat kering", "Daya serap air instan anti-selip di lantai."
    if 'teko' in nl or 'pitcher' in nl:
        return IMAGE_MAP['pitcher'], "Bikin infused water / stok air minum dingin di kos", "Bahan food grade BPA free dapat set 8 gelas."
    if 'filter kran' in nl or 'penyaring' in nl:
        return IMAGE_MAP['filter'], "Air keran kosan kuning/keruh jadi bening higienis", "Filter kapas kerapatan tinggi saring karat & lumut."
    if 'talenan' in nl:
        return IMAGE_MAP['cutting_board'], "Masak praktis di kosan pake kayu jati estetik", "Kayu jati perhutani kuat gak gampang berjamur."
    if 'rak piring' in nl:
        return IMAGE_MAP['dish_rack'], "Wastafel sempit jadi luas dan piring cepat kering", "Stainless steel tebal anti karat muat banyak."
    if 'pel' in nl or 'mop' in nl:
        return IMAGE_MAP['mop'], "Ngepel kosan 5 menit tanpa capek peras kain tangan", "Sistem peras otomatis kain microfiber angkat debu."
    if 'linen spray' in nl or 'anti bau' in nl:
        return IMAGE_MAP['linen_spray'], "Kasur & sprei bebas tungau dan wangi segar tahan lama", "Semprot langsung ke kain hilangkan bakteri & apek."
    if 'bantal duduk' in nl or 'pillow' in nl:
        return IMAGE_MAP['cushion'], "Duduk berjam-jam kerja gak bikin pantat & pinggang tepos", "Bahan plush empuk bentuk biskuit estetik."
    if 'kotak sepatu' in nl:
        return IMAGE_MAP['shoe_box'], "Sepatu rapi tertata gak bikin kosan keliatan kumuh", "Kotak transparan tebal bisa ditumpuk hemat tempat."
    if 'panci' in nl or 'saucepan' in nl:
        return IMAGE_MAP['saucepan'], "Masak mie / sup di kosan anti lengket gampang dicuci", "Lapisan granite tebal elegan panas merata."
    if 'oat' in nl:
        return IMAGE_MAP['oat_jar'], "Sarapan sehat hemat praktis tinggal ambil di kulkas", "Wadah kaca kedap udara bonus sendok sarapan."
    if 'rak bumbu' in nl:
        return IMAGE_MAP['spice_rack'], "Dapur mini kosan jadi rapi tertata ala cafe", "Susun 3 tingkat muat bumbu, saus & skincare."
    if 'mama lemon' in nl or 'cuci piring' in nl:
        return IMAGE_MAP['dishwashing'], "Lemak minyak membandel hilang bersih kesat seketika", "Formula jeruk nipis anti bau amis wajan piring."
    if 'coklat' in nl:
        return IMAGE_MAP['chocolate'], "Olesan roti / camilan manis mood booster kerjaan", "Crunchy coklat asli lumer di mulut mantap."
    if 'lemon' in nl:
        return IMAGE_MAP['lemon_juice'], "Detox tubuh & daya tahan tubuh biar gak gampang drop", "100% sari lemon murni tanpa gula tinggal seduh."
    if 'muesli' in nl:
        return IMAGE_MAP['muesli'], "Kenyang tahan lama buat yang lagi diet defisit kalori", "Campuran oat, almond & freeze dried apple renyah."
    if 'matcha' in nl:
        return IMAGE_MAP['matcha'], "Bikin matcha latte cafe di rumah cuma modal belasan ribu", "100% pure matcha tanpa pemanis tambahan."
    if 'nugget' in nl:
        return IMAGE_MAP['nugget'], "Lauk darurat sahur / malam tanggal tua gampang digoreng", "Daging tebal crispy nagih favorit anak kos."
    if 'rak troli' in nl:
        return IMAGE_MAP['trolley'], "Barang kosan berserakan rapi tinggal dorong beroda", "Troli 4 susun fleksibel buat kamar & dapur."
    if 'pintu kulkas' in nl:
        return IMAGE_MAP['fridge_box'], "Kulkas kosan rapi gak ada sachet bumbu tumpah", "Organizer gantung pintu kulkas transparan."
    if 'holder hp' in nl or 'stand' in nl:
        return IMAGE_MAP['phone_stand'], "Nonton YouTube & video call gak perlu dipegang pegel", "Bisa dilipat pocket-size kokoh di atas meja."
    if 'pembersih toilet' in nl:
        return IMAGE_MAP['toilet_cleaner'], "WC kosan berkerak bersih kinclong tanpa disikat capek", "Busa aktif rontokkan noda kerak & hilangkan bau."
    if 'squishy' in nl:
        return IMAGE_MAP['squishy'], "Penyalur emosi pas meeting zoom bikin pusing", "Bahan empuk slow-rising super gemas anti-stress."
    if 'cushion' in nl:
        return IMAGE_MAP['cushion_makeup'], "Wajah flawless glowing natural dalam 1 menit", "Cover bekas jerawat tahan keringat & air seharian."

    return IMAGE_MAP['default'], "Barang andalan solusi praktis pengeluaran hemat", "Rating tinggi terbukti dipakai banyak warganet."

def get_value_anchor(price_num):
    if price_num <= 10000:
        return "⚡ Lebih murah dari 1x parkir mobil"
    if price_num <= 25000:
        return "💸 Lebih murah dari segelas kopi susu"
    if price_num <= 50000:
        return "✨ Modal sekali makan siang, kepake berbulan-bulan"
    if price_num <= 100000:
        return "💎 Investasi kenyamanan hidup sehari-hari"
    return "🔥 Kualitas premium harga pabrik Shopee"

def get_need_pill(cat, name, price_num):
    nl = name.lower()
    if price_num <= 20000:
        return "Di Bawah 20rb"
    if any(k in nl for k in ['kipas', 'kabel', 'ssd', 'stand', 'holder', 'powerbank', 'tripod', 'strap', 'smartwatch']):
        return "Budak Korporat"
    if any(k in nl for k in ['diffuser', 'handuk', 'keset', 'setrika', 'troli', 'panci', 'rak', 'kulkas', 'toilet', 'pel', 'detergen']):
        return "Penyelamat Kosan"
    if any(k in nl for k in ['parfum', 'sunscreen', 'lip', 'cushion', 'deodorant', 'tawas', 'hair dryer', 'moisturizer', 'bedak']):
        return "Glow Up Murah"
    if any(k in nl for k in ['basreng', 'coklat', 'lemon', 'muesli', 'matcha', 'nugget', 'squishy']):
        return "Camilan & Stress"
    return "Penyelamat Kosan"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    products = json.load(f)

enriched = []
for p in products:
    img, hook, note = get_product_image_and_hook(p['name'], p['price_num'])
    anchor = get_value_anchor(p['price_num'])
    need_pill = get_need_pill(p['category'], p['name'], p['price_num'])

    # Highlight top 3 heroes
    is_hero = p['id'] in [2, 45, 84]  # 2: Goojodoq Kipas Turbo, 45: Summerspring Diffuser, 84: Stand Holder HP 2k

    item = dict(p)
    item['image_url'] = img
    item['hook'] = hook
    item['curator_note'] = note
    item['value_anchor'] = anchor
    item['need_pill'] = need_pill
    item['is_hero'] = is_hero
    enriched.append(item)

with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(enriched, f, indent=2, ensure_ascii=False)

print(f"✅ Enriched {len(enriched)} products with psychological hooks, images, and anchors at {OUT_FILE}")
