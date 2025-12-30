import os
import time
import requests
import random
from google import genai
from datetime import datetime

# 1. Configureren
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. De Brede Thema's (Hieruit kiest de AI elke dag een invalshoek)
# Dit raakt nooit op, want de AI verzint telkens iets nieuws binnen deze kaders.
themes = [
    "Advanced HTML/CSS techniques for Email Developers",
    "Technical Email Deliverability & Protocols (DMARC/BIMI)",
    "SQL & Data Scripting for Marketing Automation (Selligent/Marketing Cloud)",
    "API Integrations & Webhooks in Email Marketing",
    "Future Trends in Email Technology (AMP, AI, Interactivity)",
    "Strategic Email Marketing for SaaS & B2B",
    "Customer Data Platforms (CDP) & Segmentation Logic",
    "Dark Mode & Accessibility in Email Coding"
]

# Kies een willekeurig thema voor vandaag
todays_theme = random.choice(themes)

# Functie om de AI eerst een UNIEK onderwerp te laten verzinnen
def get_ai_topic(theme):
    print(f"🧠 Onderwerp bedenken binnen thema: {theme}...")
    topic_prompt = f"""
    Generate a unique, specific, and highly technical blog post title about: '{theme}'.
    Target audience: Senior Email Developers and Marketing Automation Specialists.
    The title must be catchy, professional, and suitable for 2026.
    Output ONLY the title, nothing else.
    """
    try:
        # We gebruiken Flash voor deze snelle vraag
        resp = client.models.generate_content(model="gemini-2.5-flash", contents=topic_prompt)
        return resp.text.strip().replace('"', '')
    except:
        return theme # Fallback als het misgaat

# We genereren nu het onderwerp 'live'
topic = get_ai_topic(todays_theme)
print(f"💡 AI heeft gekozen: {topic}")

# 3. Image Downloader
def download_image_robust(prompt_text, save_path):
    print(f"🎨 Afbeelding genereren...")
    base_prompt = f"abstract 3d composition representing {prompt_text}, futuristic, clean, minimalist, iso, high quality, 8k, no text, blurred background"
    clean_prompt = base_prompt.replace(" ", "%20")
    # Random seed toevoegen voor variatie
    seed = random.randint(0, 9999) 
    url = f"https://image.pollinations.ai/prompt/{clean_prompt}?width=1200&height=630&nologo=true&seed={seed}&model=flux"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
        return False
    except:
        return False

# 4. Paden instellen
safe_slug = topic.lower().replace(" ", "-").replace(":", "").replace("/", "")[:50] # Max lengte slug
date_str = datetime.now().strftime('%Y-%m-%d')

post_filename = f"_posts/{date_str}-{safe_slug}.md"
image_folder = "images"
image_filename = f"{image_folder}/{date_str}-{safe_slug}.jpg"
image_public_path = image_filename 

os.makedirs("_posts", exist_ok=True)
os.makedirs(image_folder, exist_ok=True)

# 5. Image genereren
download_image_robust(topic, image_filename)

# 6. Tekst Genereren (Met DYNAMISCHE Tags/Labels)
prompt = f"""
Act as a Senior Email Campaign Developer.
Write a deep-dive technical blog post about: '{topic}'.

TARGET: Senior Developers & CRM Specialists.
LANGUAGE: Fluent American English.

REQUIREMENTS:
1.  **Deep Dive**: Include code snippets (HTML/CSS/SQL/Liquid) or technical diagrams where possible.
2.  **Structure**: Markdown with H2/H3.
3.  **Table**: Include a comparison or feature table.
4.  **FAQ**: Include a technical FAQ.

IMPORTANT: You must generate the Frontmatter yourself based on the content.
Start with this EXACT format, but fill in the brackets dynamically:
---
layout: post
title: "{topic}"
titleshort: "[Generate a short version max 40 chars]"
featured: 0
date: {date_str}
label: [Generate 1 or 2 main categories, e.g. 'development, strategy']
permalink: /generated-post-{date_str}
tags: [Generate 5-7 specific tags, e.g. 'sql, liquid, selligent, css']
yearreview: false
author: Jeffrey Overmeer
published: true
thumbnail: "{image_public_path}"
description: "[Generate a compelling meta-description max 160 chars]"
---

After frontmatter, write the full post.
"""

models_to_try = [
    "gemini-3-pro-preview",
    "gemini-2.0-flash-exp",
    "gemini-2.5-flash",
    "gemini-flash-latest"
]

generated_content = None

print(f"📝 Start schrijven...")

for model_name in models_to_try:
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        generated_content = response.text
        print(f"✅ Gelukt met {model_name}")
        break 
    except Exception as e:
        time.sleep(1)

# 7. Opslaan
if generated_content:
    if "---" in generated_content:
        start_index = generated_content.find("---")
        generated_content = generated_content[start_index:]

    with open(post_filename, "w", encoding="utf-8") as f:
        f.write(generated_content)
    print(f"🎉 Opgeslagen: {post_filename}")
else:
    exit(1)
