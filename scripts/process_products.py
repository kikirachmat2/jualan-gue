#!/usr/bin/env python3
"""
scripts/process_products.py
Local pipeline to process Shopee products from CSV/JSON into verified static JSON:
1. Normalizes prices (flags anomalies under Rp 1.000 or units/grosir items).
2. Sets multi-photo galleries per product (3-4 photos per product type).
3. Calculates smart ranking score for Hero Carousel & Grid placement.
4. Generates data/products_verified.json ready for instant 0ms site consumption.
"""

import os
import re
import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENRICHED_JSON = BASE_DIR / "data/products_enriched.json"
OUT_JSON = BASE_DIR / "data/products_verified.json"

# High-resolution product galleries (3-4 photos per product type)
PRODUCT_GALLERIES = {
    'fan': [
        'https://images.unsplash.com/photo-1618941716939-553df3c6c278?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1591147139475-e66699318b38?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1544816155-12df9643f363?auto=format&fit=crop&w=600&q=80'
    ],
    'snack': [
        'https://images.unsplash.com/photo-1599490659213-e2b9527bd087?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1566478989037-eec170784d0b?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1621996346565-e3d5d6281699?auto=format&fit=crop&w=600&q=80'
    ],
    'mask': [
        'https://images.unsplash.com/photo-1584634731339-252c581abfc5?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1586942593568-29361efcd571?auto=format&fit=crop&w=600&q=80'
    ],
    'tripod': [
        'https://images.unsplash.com/photo-1512499617640-c74ae3a79d37?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?auto=format&fit=crop&w=600&q=80'
    ],
    'perfume': [
        'https://images.unsplash.com/photo-1523293182086-7651a899d37f?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1547887537-6158d64c35b3?auto=format&fit=crop&w=600&q=80'
    ],
    'tumbler': [
        'https://images.unsplash.com/photo-1517256064527-09c73fc73e38?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1602143407151-7111542de6e8?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1577705998148-6da4f3963bc8?auto=format&fit=crop&w=600&q=80'
    ],
    'skincare': [
        'https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=600&q=80'
    ],
    'home': [
        'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1582735689369-4fe89db7114c?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=600&q=80'
    ],
    'fashion': [
        'https://images.unsplash.com/photo-1548036328-c9fa89d128fa?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1603808033192-082d6919d3e1?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=600&q=80'
    ]
}

def determine_gallery(name, category, default_img):
    n = name.lower()
    c = category.lower()
    base = []
    if 'kipas' in n or 'fan' in n:
        base = PRODUCT_GALLERIES['fan']
    elif 'basreng' in n or 'snack' in n or 'makanan' in c or 'camilan' in c or 'cokelat' in n:
        base = PRODUCT_GALLERIES['snack']
    elif 'masker' in n or 'duckbill' in n:
        base = PRODUCT_GALLERIES['mask']
    elif 'tripod' in n or 'tongsis' in n or 'led' in n:
        base = PRODUCT_GALLERIES['tripod']
    elif 'parfum' in n or 'perfume' in n:
        base = PRODUCT_GALLERIES['perfume']
    elif 'tumbler' in n or 'botol' in n or 'mug' in n:
        base = PRODUCT_GALLERIES['tumbler']
    elif 'skincare' in c or 'serum' in n or 'moisturizer' in n or 'sunscreen' in n:
        base = PRODUCT_GALLERIES['skincare']
    elif 'rumah' in c or 'kosan' in c or 'sprei' in n or 'rak' in n:
        base = PRODUCT_GALLERIES['home']
    elif 'tas' in n or 'baju' in n or 'sandal' in n or 'fashion' in c:
        base = PRODUCT_GALLERIES['fashion']
    else:
        base = PRODUCT_GALLERIES['home']
    
    res = [default_img] if default_img else []
    for g in base:
        if g not in res:
            res.append(g)
    return res[:4]

def main():
    with open(ENRICHED_JSON, encoding='utf-8') as f:
        products = json.load(f)

    anomalies = []
    processed = []

    for p in products:
        name = p.get('name', '')
        raw_price = p.get('price_num', 0)
        cat = p.get('category', 'Lainnya')
        sales = p.get('sales', '')

        # Price sanity check
        is_anomaly = False
        anomaly_reason = ""
        
        # Wholesale single-unit items (e.g. Lunch Box 417 / Lem kuku 349)
        if raw_price < 1000:
            is_anomaly = True
            anomaly_reason = f"Harga satuan kemasan/grosir (Rp {raw_price})"
            anomalies.append({
                'id': p.get('id'),
                'name': name,
                'price': raw_price,
                'reason': anomaly_reason
            })

        # Calculate sales number
        sales_num = 0
        if sales:
            m = re.search(r'(\d+)', sales)
            if m:
                sales_num = int(m.group(1))
                if 'RB' in sales.upper():
                    sales_num *= 1000

        # Multi-photo gallery
        images = p.get('images')
        if not images or len(images) == 0:
            images = determine_gallery(name, cat, p.get('image_url'))

        # Clean title
        clean_title = p.get('clean_title') or name

        # Format price with unit note if anomaly
        price_display = p.get('price_formatted')
        if is_anomaly and 'satuan' not in clean_title.lower() and 'pcs' not in clean_title.lower():
            clean_title = f"{clean_title} (Satuan)"

        # Priority calculation: Priority * 1000000 + Sales
        score = (p.get('priority', 0) * 1000000) + sales_num
        if p.get('original_price_num') and p['original_price_num'] > raw_price:
            disc = round(((p['original_price_num'] - raw_price) / p['original_price_num']) * 100)
            score += disc * 100

        processed.append({
            'id': p.get('id'),
            'product_id': p.get('product_id'),
            'name': name,
            'clean_title': clean_title,
            'category': cat,
            'price_num': raw_price,
            'price_formatted': price_display,
            'original_price_num': p.get('original_price_num'),
            'original_price_formatted': p.get('original_price_formatted'),
            'sales': sales,
            'sales_num': sales_num,
            'rating': p.get('rating') or 4.9,
            'shop': p.get('shop', 'Shopee Star Seller'),
            'affiliate_url': p.get('affiliate_url'),
            'product_url': p.get('product_url'),
            'images': images,
            'image_url': images[0],
            'score': score,
            'is_anomaly': is_anomaly,
            'anomaly_reason': anomaly_reason
        })

    # Save to data/products_verified.json
    with open(OUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(processed, f, indent=2, ensure_ascii=False)

    print(f"SUCCESS: Processed {len(processed)} products.")
    print(f"Anomalies detected & annotated: {len(anomalies)}")
    print(f"Data saved to {OUT_JSON}")

if __name__ == '__main__':
    main()
