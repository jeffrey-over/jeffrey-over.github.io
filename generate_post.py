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

# LIJST MET MOGELIJKE MODELLEN (Op volgorde van voorkeur)
# We proberen ze één voor één tot er een werkt.
CANDIDATE_MODELS = [
    "gemini-1.5-flash-002",  # Nieuwste stabiele versie
    "gemini-1.5-flash-001",  # Vorige stabiele versie
    "gemini-1.5-flash",      # Algemene alias
    "gemini-1.5-pro-002",    # Pro versie (stabiel)
    "gemini-1.5-pro-001",    # Pro versie (oud)
    "gemini-2.0-flash-exp"   # Experimenteel (als laatste redmiddel)
]

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
    print(f"🚀 Start 'Single-Shot' generatie...")
    
    for model_name in CANDIDATE_MODELS:
        print(f"👉 Proberen met model: {model_name}...")
        
        # Retry logica per model (alleen voor rate limits)
        for attempt in range(1, 3):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=full_prompt,
                    config={
                        'response_mime_type': 'application/json' 
                    }
                )
                print(f"✅ Gelukt met {model_name}!")
                return response.text
                
            except Exception as e:
                error_str = str(e)
                
                # CASE 1: Model bestaat niet (404) -> Direct door naar volgende model in lijst
                if "404" in error_str or "NOT_FOUND" in error_str:
                    print(f"⚠️ {model_name} niet gevonden (404).")
                    break # Break de retry loop, ga naar volgende model
                
                # CASE 2: Rate Limit (429) -> Wachten en nog eens proberen
                elif "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                    wait_time = attempt * 10
                    print(f"⏳ Rate limit op {model_name}. Wachten {wait_time}s...")
                    time.sleep(wait_time)
                    continue # Probeer zelfde model nog eens
                
                # CASE 3: Andere fout -> Loggen en volgende
                else:
                    print(f"❌ Error met {model_name}: {e}")
                    break
                    
    return None

# Voer de call uit
raw_json = generate_full_post()

if not raw_json:
    print("❌ API Faalde volledig op ALLE modellen.")
    exit(1)

# JSON Parsen en opruimen
try:
    clean_json = raw_json.replace("```json", "").replace("```", "").strip()
    data = json.loads(clean_json)
    
    title = data.get("title", base_prompt_theme)
    slug = data.get("slug", "blog-post").lower()
    description = data.get("description", "")
    tags = data.get("tags", "email, tech")
    body = data.get("content", "")
    
    print(f"✅ Data geparsed: {title}")

except json.JSONDecodeError as e:
    print(f"❌ JSON Parse Error: {e}")
    with open("error_dump.txt", "w") as f:
        f.write(raw_json)
    exit(1)


# 4. Afbeelding Genereren
date_str = datetime.now().strftime('%Y-%m-%d')
image_folder = "images"
image_filename = f"{image_folder}/{date_str}-{slug}.jpg"
image_public_path = f"/{image_filename}"

os.makedirs("_posts", exist_ok=True)
os.makedirs(image_folder, exist_ok=True)

def download_image(prompt_text, save_path):
    print(f"🎨 Afbeelding genereren...")
    try:
        clean_prompt = f"3D render in Apple App Store editorial style of {prompt_text}. clean high-quality composition, glossy 3D icon, soft light gradient background, no text"
        encoded = clean_prompt.replace(" ", "%20")
        seed = random.randint(0, 9999)
        url = f"https://image.pollinations.ai/prompt/{encoded}?width=1200&height=630&nologo=true&seed={seed}&model=flux"
        
        resp = requests.get(url, timeout=30)
        if resp.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(resp.content)
            return True
    except:
        return False

download_image(slug.replace("-", " "), image_filename)

# 5. Opslaan
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
