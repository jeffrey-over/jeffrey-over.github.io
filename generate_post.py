import os
import time
import requests
import random
import re
from google import genai
from datetime import datetime
from google.genai import types

# 1. Configureren
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# LIJST MET MODELLEN (Van stabiel naar experimenteel)
# We gebruiken specifieke versienummers (-002) om 404 errors te voorkomen.
MODELS_TO_TRY = [
    "gemini-1.5-flash-002",  # Nieuwste stabiele Flash
    "gemini-1.5-flash-001",  # Vorige stabiele Flash
    "gemini-1.5-pro-002",    # Nieuwste stabiele Pro
    "gemini-2.0-flash-exp"   # Experimenteel (vaak rate limits)
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

print(f"🎯 SEO Doelwit: {base_prompt_theme}")

# --- CENTRALE GENERATIE FUNCTIE ---
def generate_content_robust(prompt_text, task_name="Content"):
    """
    Probeert content te genereren met verschillende modellen en retry-logica.
    """
    print(f"🔄 Genereren: {task_name}...")
    
    for model in MODELS_TO_TRY:
        try:
            # Probeer request
            response = client.models.generate_content(
                model=model, 
                contents=prompt_text
            )
            return response.text.strip()
            
        except Exception as e:
            error_msg = str(e)
            
            # Scenario 1: Rate Limit (429) -> Wacht en probeer ZELFDE model opnieuw
            if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                print(f"⏳ Rate limit op {model}. Wachten 30 seconden...")
                time.sleep(30)
                try:
                    # Tweede poging op zelfde model
                    response = client.models.generate_content(
                        model=model, 
                        contents=prompt_text
                    )
                    return response.text.strip()
                except Exception as e2:
                    print(f"⚠️ Tweede poging mislukt op {model}: {e2}")
                    continue # Ga naar volgende model in de lijst
            
            # Scenario 2: Model niet gevonden (404) -> Ga direct door
            elif "404" in error_msg or "NOT_FOUND" in error_msg:
                print(f"⚠️ Model {model} niet gevonden. Overslaan.")
                continue
                
            # Scenario 3: Andere fout
            else:
                print(f"❌ Fout met {model}: {e}")
                continue

    return None

# Functie: Strenge Titel Bedenken
def get_strict_topic(theme):
    prompt = f"""
    You are an SEO Specialist.
    Take this concept: "{theme}" and turn it into a high-ranking blog title.
    Rules:
    1. Use a "Long-tail keyword" approach.
    2. Keep it under 60 characters.
    3. Make it clickable (High CTR).
    4. NO lists, NO "Here is a title". Output ONLY the title text.
    """
    result = generate_content_robust(prompt, "SEO Titel")
    
    if result:
        text = result
        if "\n" in text: text = text.split("\n")[0]
        text = text.replace('"', '').replace(":", "").replace("*", "")
        text = re.sub(r'^\d+\.\s*', '', text)
        return text
    
    return theme # Fallback

# Functie: Tags Genereren
def get_smart_tags(theme):
    prompt = f"""
    Generate 5 relevant, lowercase, comma-separated keywords/tags for a blog post about: "{theme}".
    Output ONLY the tags (e.g.: email, automation, code). No numbering.
    """
    result = generate_content_robust(prompt, "Tags")
    if result:
        return result.lower()
    return "email, automation, tech, development"

# UITVOEREN
topic = get_strict_topic(base_prompt_theme)
post_tags = get_smart_tags(topic)

print(f"💡 Definitieve Titel: {topic}")
print(f"🏷️ Tags: {post_tags}")

# Functie: Slug Schoonmaken
def clean_slug(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9-]', '-', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    return text[:60]

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
        clean_prompt = f"3D render in Apple App Store editorial style of {short_prompt}. A clean high-quality composition, center stage glossy 3D icon relevant to topic, soft light airy gradient background white light blue soft grey, high fidelity, soft shadows, octane render, claymorphism elements, tech-minimalist aesthetic, no text"
        
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
body_prompt = f"""
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

IMPORTANT TECHNICAL RULE:
If you write code examples that contain Liquid or Jinja syntax (like `{{ variable }}` or `{{% if condition %}}`), you MUST wrap that specific code block in `{{% raw %}}` and `{{% endraw %}}` tags. Otherwise, the Jekyll build will fail.

DO NOT write Frontmatter.
"""

content_body = generate_content_robust(body_prompt, "Blogpost Content")

if content_body:
    # Strip eventuele markdown formatting die per ongeluk mee komt
    if "---" in content_body[:50]:
        parts = content_body.split("---")
        if len(parts) > 2:
            content_body = parts[2].strip()

    final_post = f"""---
layout: post
title: "{topic}"
titleshort: "{topic[:30]}..."
date: {date_str}
label: development
permalink: /{safe_slug}
tags: {post_tags}
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
    print("❌ Kon geen content genereren. Check je API key quota.")
    exit(1)
