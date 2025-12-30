import os
import time
import requests
import random
import re
from google import genai
from datetime import datetime

# 1. Configureren
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. Thema's (Oneindige inspiratie)
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

# Functie: Onderwerp Bedenken (STRENG!)
def get_strict_topic(theme):
    print(f"🧠 Onderwerp bedenken voor: {theme}...")
    # Instructie: Geen lijstjes, geen "Here is...", alleen de titel.
    prompt = f"""
    Create ONE single, professional blog title about '{theme}'.
    The title must be under 60 characters.
    Do NOT generate a list.
    Do NOT write "Here is a title".
    Output ONLY the title text.
    """
    try:
        resp = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        text = resp.text.strip()
        
        # VEILIGHEID: Als de AI toch een lijst maakt (met enters), pakken we alleen regel 1
        if "\n" in text:
            text = text.split("\n")[0]
            
        # Verwijder quotes en dubbele punten voor de zekerheid
        text = text.replace('"', '').replace(":", "").replace("*", "")
        
        # Verwijder nummering als AI dat doet (bijv "1. Titel")
        text = re.sub(r'^\d+\.\s*', '', text)
        
        return text
    except:
        return theme # Fallback

topic = get_strict_topic(todays_theme)
print(f"💡 Gekozen titel: {topic}")

# Functie: Bestandsnaam schoonmaken
def clean_filename(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9-]', '-', text) # Vervang alles wat geen letter/cijfer is door streepje
    text = re.sub(r'-+', '-', text) # Geen dubbele streepjes
    text = text.strip('-')
    return text[:50]

safe_slug = clean_filename(topic)
date_str = datetime.now().strftime('%Y-%m-%d')

# Paden
post_filename = f"_posts/{date_str}-{safe_slug}.md"
image_folder = "images"
image_filename = f"{image_folder}/{date_str}-{safe_slug}.jpg"
image_public_path = f"/{image_filename}"

os.makedirs("_posts", exist_ok=True)
os.makedirs(image_folder, exist_ok=True)

# 3. Image Genereren (Zonder Tekst)
def download_image_robust(prompt_text, save_path):
    print(f"🎨 Afbeelding genereren...")
    try:
        # We gebruiken de slug in de prompt, die is korter en bevat geen leestekens
        short_prompt = prompt_text.replace("-", " ")
        
        # PROMPT: Abstract, 3D, Gradient, Geen tekst
        # We voegen 'abstract' en 'shapes' toe en 'text' in de seed logic
        clean_prompt = f"abstract 3d tech shapes representing {short_prompt}, minimalist, gradient lighting, 8k render, no text, no letters"
        encoded_prompt = clean_prompt.replace(" ", "%20")
        
        seed = random.randint(0, 9999)
        # Model 'flux' is het beste voor abstract
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1200&height=630&nologo=true&seed={seed}&model=flux"
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
        return False
    except:
        return False

download_image_robust(safe_slug, image_filename) # We gebruiken de slug voor de image prompt (korter = beter)

# 4. Content Genereren
prompt = f"""
Act as a Senior Email Developer.
Write a blog post about: '{topic}'.

DO NOT write the Frontmatter. Start with the Introduction.

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
        # Clean up als AI toch frontmatter start
        if "---" in content_body[:50]:
            parts = content_body.split("---")
            if len(parts) > 2:
                content_body = parts[2].strip()
        print(f"✅ Gelukt met {model_name}")
        break 
    except Exception as e:
        time.sleep(1)

# 5. Opslaan (Veilige Frontmatter)
if content_body:
    # We bouwen de YAML handmatig en heel strikt op
    # Let op de dubbele quotes rondom strings om YAML errors te voorkomen
    final_post = f"""---
layout: post
title: "{topic}"
titleshort: "{topic[:30]}..."
date: {date_str}
label: development
permalink: /generated-post-{date_str}-{random.randint(100,999)}
tags: email, automation, tech, ai
yearreview: false
author: Jeffrey Overmeer
published: true
thumbnail: "{image_public_path}"
description: "A technical deep-dive into {topic}."
---

{content_body}
"""
    
    with open(post_filename, "w", encoding="utf-8") as f:
        f.write(final_post)
    print(f"🎉 Opgeslagen: {post_filename}")
else:
    exit(1)
