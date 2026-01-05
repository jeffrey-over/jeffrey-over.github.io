import os
import time
import requests
import random
import re
import json
from google import genai
from datetime import datetime

# 1. Configureren
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# We gebruiken Flash omdat die grote context (input/output) goedkoop en snel aankan
MODEL_NAME = "gemini-1.5-flash"

# 2. SEO Strategie
seo_structures = [
    "Comparison: {tech} vs {tech} for Enterprise",
    "How to fix {tech} issues in 2026",
    "The Ultimate Guide to {tech} for Developers",
    "Top 5 Mistakes Developers make with {tech}",
    "Advanced {tech} Tutorial: Step-by-Step",
    "Why {tech} is the future of Email Marketing",
    "Implementing {tech}: A Technical Walkthrough"
]

tech_keywords = [
    "Selligent Marketing Cloud", "Deployteq", "Salesforce Marketing Cloud",
    "Liquid Scripting", "AMP for Email", "Dark Mode Email Coding",
    "BIMI and DMARC", "Email SQL Queries", "JSON-LD in Email",
    "CSS Grid for Email", "Outlook Rendering", "Email API Webhooks",
    "Server-side Javascript (SSJS)", "MJML framework", "Litmus testing"
]

# Kies structuur en tech
chosen_structure = random.choice(seo_structures)
chosen_tech = random.choice(tech_keywords)

if "{tech} vs {tech}" in chosen_structure:
    tech2 = random.choice([t for t in tech_keywords if t != chosen_tech])
    base_prompt_theme = chosen_structure.replace("{tech}", chosen_tech, 1).replace("{tech}", tech2)
else:
    base_prompt_theme = chosen_structure.replace("{tech}", chosen_tech)

print(f"🎯 Strategie: {base_prompt_theme}")

# 3. De Alles-in-één Prompt
full_prompt = f"""
Act as a Senior Technical Content Writer & SEO Specialist.
I need a complete blog post based on the topic: "{base_prompt_theme}".

Output MUST be valid JSON only. Do not add markdown formatting like ```json ... ```. 
Just the raw JSON object.

Structure the JSON as follows:
{{
    "title": "The optimized, high-CTR blog title (max 60 chars)",
    "slug": "url-friendly-kebab-case-slug",
    "description": "SEO meta description (max 160 chars)",
    "tags": "comma, separated, lowercase, list, of, 5, tags",
    "content": "The full blog post content in Markdown format..."
}}

CONTENT REQUIREMENTS:
1. **Intro**: Problem definition.
2. **Body**: Technical deep dive (Code, SQL, Logic).
3. **Structure**: Comparison Table is MANDATORY.
4. **FAQ**: "People Also Ask" section at end.
5. **Length**: 1000+ words.

IMPORTANT TECHNICAL RULE:
Inside the "content" field, if you write code examples with Liquid/Jinja syntax (like {{{{ variable }}}} or {{% if %}}), you MUST wrap that code block in {{% raw %}} and {{% endraw %}} tags.
"""

def generate_full_post():
    print(f"🚀 Start 'Single-Shot' generatie met {MODEL_NAME}...")
    
    # Retry logica
    for attempt in range(1, 4):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=full_prompt,
                config={
                    'response_mime_type': 'application/json' # Forceer JSON modus
                }
            )
            return response.text
        except Exception as e:
            print(f"⚠️ Poging {attempt} mislukt: {e}")
            time.sleep(10 * attempt)
    return None

# Voer de call uit
raw_json = generate_full_post()

if not raw_json:
    print("❌ API Faalde volledig.")
    exit(1)

# JSON Parsen en opruimen
try:
    # Soms zet de AI er toch ```json omheen, dit filteren we
    clean_json = raw_json.replace("```json", "").replace("```", "").strip()
    data = json.loads(clean_json)
    
    title = data.get("title", base_prompt_theme)
    slug = data.get("slug", "blog-post").lower()
    description = data.get("description", "")
    tags = data.get("tags", "email, tech")
    body = data.get("content", "")
    
    print(f"✅ Data succesvol ontvangen: {title}")

except json.JSONDecodeError as e:
    print(f"❌ JSON Parse Error: {e}")
    # Fallback: sla de ruwe tekst op zodat je het handmatig kunt redden
    with open("error_dump.txt", "w") as f:
        f.write(raw_json)
    exit(1)


# 4. Afbeelding Genereren (op basis van de nieuwe titel)
date_str = datetime.now().strftime('%Y-%m-%d')
image_folder = "images"
image_filename = f"{image_folder}/{date_str}-{slug}.jpg"
image_public_path = f"/{image_filename}"

os.makedirs("_posts", exist_ok=True)
os.makedirs(image_folder, exist_ok=True)

def download_image(prompt_text, save_path):
    print(f"🎨 Afbeelding genereren voor: {prompt_text}")
    try:
        clean_prompt = f"3D render in Apple App Store editorial style of {prompt_text}. clean high-quality composition, glossy 3D icon, soft light gradient background, no text"
        encoded = clean_prompt.replace(" ", "%20")
        seed = random.randint(0, 9999)
        url = f"[https://image.pollinations.ai/prompt/](https://image.pollinations.ai/prompt/){encoded}?width=1200&height=630&nologo=true&seed={seed}&model=flux"
        
        resp = requests.get(url, timeout=30)
        if resp.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(resp.content)
            return True
    except:
        return False

download_image(slug.replace("-", " "), image_filename)

# 5. Opslaan als Jekyll Post
final_post_content = f"""---
layout: post
title: "{title}"
titleshort: "{title[:30]}..."
date: {date_str}
label: development
permalink: /{slug}
tags: {tags}
yearreview: false
author: Jeffrey Overmeer
published: true
thumbnail: "{image_public_path}"
description: "{description}"
---

{body}
"""

post_path = f"_posts/{date_str}-{slug}.md"
with open(post_path, "w", encoding="utf-8") as f:
    f.write(final_post_content)

print(f"🎉 Succes! Post opgeslagen: {post_path}")
