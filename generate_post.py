import os
import time
import requests
import random
import re
from google import genai
from datetime import datetime

# 1. Configureren
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

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
    # Zorg voor 2 verschillende techs bij een vergelijking
    tech2 = random.choice([t for t in tech_keywords if t != chosen_tech])
    base_prompt_theme = chosen_structure.replace("{tech}", chosen_tech, 1).replace("{tech}", tech2)
else:
    base_prompt_theme = chosen_structure.replace("{tech}", chosen_tech)

print(f"🎯 SEO Doelwit: {base_prompt_theme}")

# Functie: Strenge Titel Bedenken
def get_strict_topic(theme):
    print(f"🧠 Titel optimaliseren voor Google...")
    prompt = f"""
    You are an SEO Specialist.
    Take this concept: "{theme}" and turn it into a high-ranking blog title.
    
    Rules:
    1. Use a "Long-tail keyword" approach.
    2. Keep it under 60 characters.
    3. Make it clickable (High CTR).
    4. NO lists, NO "Here is a title". Output ONLY the title text.
    """
    try:
        resp = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        text = resp.text.strip()
        if "\n" in text: text = text.split("\n")[0]
        text = text.replace('"', '').replace(":", "").replace("*", "")
        text = re.sub(r'^\d+\.\s*', '', text)
        return text
    except:
        return theme

topic = get_strict_topic(base_prompt_theme)
print(f"💡 Definitieve Titel: {topic}")

# Functie: Slug Schoonmaken (voor URL en Bestandsnaam)
def clean_slug(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9-]', '-', text) # Alleen letters/cijfers/streepjes
    text = re.sub(r'-+', '-', text) # Geen dubbele streepjes
    text = text.strip('-')
    return text[:60] # Iets langer voor goede SEO URL

safe_slug = clean_slug(topic)
date_str = datetime.now().strftime('%Y-%m-%d')

# Paden
post_filename = f"_posts/{date_str}-{safe_slug}.md"
image_folder = "images"
image_filename = f"{image_folder}/{date_str}-{safe_slug}.jpg"
image_public_path = f"/{image_filename}"

os.makedirs("_posts", exist_ok=True)
os.makedirs(image_folder, exist_ok=True)

# 3. Image Genereren
def download_image_robust(prompt_text, save_path):
    print(f"🎨 Afbeelding genereren...")
    try:
        short_prompt = prompt_text.replace("-", " ")
        clean_prompt = f"abstract 3d tech visualization of {short_prompt}, data streams, code snippets style, minimalist, blue and purple gradient, 8k, no text"
        encoded_prompt = clean_prompt.replace(" ", "%20")
        seed = random.randint(0, 9999)
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

download_image_robust(safe_slug, image_filename)

# 4. Content Genereren
prompt = f"""
Act as a Senior Technical Content Writer.
Write a blog post about: '{topic}'.

GOAL: Rank #1 on Google for this topic.
STRATEGY: Answer the user's search intent immediately.

REQUIREMENTS:
1. **Intro**: Start with the problem definition ("Are you struggling with...?").
2. **Body**: Technical deep dive (Code, SQL, Logic).
3. **Structure**: Comparison Table is MANDATORY.
4. **FAQ**: Include "People Also Ask" style questions at the end.
5. **Length**: 1000+ words.

DO NOT write Frontmatter.
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
        if "---" in content_body[:50]:
            parts = content_body.split("---")
            if len(parts) > 2:
                content_body = parts[2].strip()
        print(f"✅ Gelukt met {model_name}")
        break 
    except Exception as e:
        time.sleep(1)

# 5. Opslaan (Met SEO Permalink Fix)
if content_body:
    # HIER IS DE WIJZIGING: permalink gebruikt nu {safe_slug}
    final_post = f"""---
layout: post
title: "{topic}"
titleshort: "{topic[:30]}..."
date: {date_str}
label: development
permalink: /{safe_slug}
tags: email, automation, tech, seo
yearreview: false
author: Jeffrey Overmeer
published: true
thumbnail: "{image_public_path}"
description: "Learn about {topic} in this technical deep dive for email developers."
---

{content_body}
"""
    
    with open(post_filename, "w", encoding="utf-8") as f:
        f.write(final_post)
    print(f"🎉 Opgeslagen: {post_filename}")
else:
    exit(1)
