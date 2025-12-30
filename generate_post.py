import os
import time
import requests
import random
import re # Nodig voor schoonmaken bestandsnamen
from google import genai
from datetime import datetime

# 1. Configureren
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. Thema's
themes = [
    "Advanced HTML CSS techniques for Email Developers",
    "Technical Email Deliverability Protocols",
    "SQL Data Scripting for Marketing Automation",
    "API Integrations Webhooks in Email Marketing",
    "Future Trends in Email Technology",
    "Strategic Email Marketing for SaaS",
    "Customer Data Platforms CDP Segmentation",
    "Dark Mode Accessibility in Email Coding"
]

todays_theme = random.choice(themes)

# Functie 1: Onderwerp Bedenken
def get_ai_topic(theme):
    print(f"🧠 Onderwerp bedenken voor: {theme}...")
    # We vragen om een titel ZONDER gekke tekens voor de veiligheid
    prompt = f"Generate a blog title about '{theme}'. Keep it professional. No colons (:), no questions marks (?). Just a statement."
    try:
        resp = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return resp.text.strip().replace('"', '').replace(":", "")
    except:
        return theme

topic = get_ai_topic(todays_theme)
print(f"💡 Gekozen onderwerp: {topic}")

# Functie 2: Strenge Bestandsnaam Schoonmaak (Hufterproof)
def clean_filename(text):
    # Alles naar kleine letters
    text = text.lower()
    # Vervang spaties door streepjes
    text = text.replace(" ", "-")
    # Verwijder ALLES wat geen letter, cijfer of streepje is (dus weg met ?!@.:,)
    text = re.sub(r'[^a-z0-9-]', '', text)
    # Voorkom dubbele streepjes
    text = re.sub(r'-+', '-', text)
    return text[:50] # Max 50 tekens

safe_slug = clean_filename(topic)
date_str = datetime.now().strftime('%Y-%m-%d')

# Paden
post_filename = f"_posts/{date_str}-{safe_slug}.md"
image_folder = "images"
image_filename = f"{image_folder}/{date_str}-{safe_slug}.jpg"
# Let op: GitHub Pages wil vaak de relative path vanaf root
image_public_path = f"/{image_filename}" 

os.makedirs("_posts", exist_ok=True)
os.makedirs(image_folder, exist_ok=True)

# 3. Image Genereren
def download_image_robust(prompt_text, save_path):
    print(f"🎨 Afbeelding genereren...")
    try:
        clean_prompt = prompt_text.replace(" ", "%20")
        seed = random.randint(0, 9999)
        # Model 'flux' geeft vaak betere, schonere resultaten
        url = f"https://image.pollinations.ai/prompt/abstract%20tech%203d%20{clean_prompt}?width=1200&height=630&nologo=true&seed={seed}&model=flux"
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
        return False
    except:
        return False

download_image_robust(topic, image_filename)

# 4. Content Genereren (VEILIGE METHODE)
# We laten Python de header schrijven, niet de AI.

prompt = f"""
Act as a Senior Email Campaign Developer.
Write a blog post content about: '{topic}'.

DO NOT write the Frontmatter (YAML). I will add that myself.
Start directly with the Introduction.

REQUIREMENTS:
1. Deep Dive Technical Content.
2. Use Markdown (H2, H3).
3. Include a Comparison Table.
4. Include a FAQ section.
"""

models_to_try = [
    "gemini-3-pro-preview",
    "gemini-2.0-flash-exp",
    "gemini-2.5-flash",
    "gemini-flash-latest"
]

content_body = None

print(f"📝 Start schrijven...")

for model_name in models_to_try:
    try:
        response = client.models.generate_content(model=model_name, contents=prompt)
        content_body = response.text
        # Soms doet AI toch eigenwijs de header erbij, die slopen we eruit
        if "---" in content_body[:50]:
            parts = content_body.split("---")
            if len(parts) > 2:
                content_body = parts[2].strip() # Pak alles NA de tweede ---
        
        print(f"✅ Gelukt met {model_name}")
        break 
    except Exception as e:
        time.sleep(1)

# 5. Opslaan met Python-Generated Frontmatter (100% Veilig)
if content_body:
    # Hier bouwen we de header zelf, zodat er geen syntax fouten in komen
    final_post = f"""---
layout: post
title: "{topic}"
titleshort: "{topic[:40]}..."
date: {date_str}
label: development
permalink: /generated-post-{date_str}-{random.randint(100,999)}
tags: email, automation, tech, ai
yearreview: false
author: Jeffrey Overmeer
published: true
thumbnail: "{image_public_path}"
description: "A technical deep-dive into {topic} for email developers."
---

{content_body}
"""
    
    with open(post_filename, "w", encoding="utf-8") as f:
        f.write(final_post)
    print(f"🎉 Opgeslagen: {post_filename}")
else:
    exit(1)
