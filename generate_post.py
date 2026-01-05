import os
import time
import requests
import random
import json
from datetime import datetime
from google import genai
from google.genai import types

# =========================
# 1. CONFIGURATIE
# =========================

if "GEMINI_API_KEY" not in os.environ:
    raise RuntimeError("❌ GEMINI_API_KEY ontbreekt in environment variables")

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# ✅ ENIGE GELDIGE & PUBLIEKE MODELLEN (EU-proof)
CANDIDATE_MODELS = [
    "models/gemini-1.5-flash",  # snel & goedkoop
    "models/gemini-1.5-pro",    # beste kwaliteit
    "models/gemini-1.0-pro"     # zeer stabiele fallback
]

# =========================
# 2. SEO STRATEGIE
# =========================

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

chosen_structure = random.choice(seo_structures)
chosen_tech = random.choice(tech_keywords)

if "{tech} vs {tech}" in chosen_structure:
    tech2 = random.choice([t for t in tech_keywords if t != chosen_tech])
    base_prompt_theme = chosen_structure.replace("{tech}", chosen_tech, 1).replace("{tech}", tech2)
else:
    base_prompt_theme = chosen_structure.replace("{tech}", chosen_tech)

print(f"🎯 Strategie: {base_prompt_theme}")

# =========================
# 3. PROMPT
# =========================

full_prompt = f"""
Act as a Senior Technical Content Writer & SEO Specialist.

Create a COMPLETE blog post for the topic:
"{base_prompt_theme}"

OUTPUT RULES (VERY IMPORTANT):
- Output ONLY valid JSON
- NO markdown wrappers
- NO explanations
- NO text outside JSON

JSON STRUCTURE:
{{
  "title": "SEO optimized title (max 60 chars)",
  "slug": "url-friendly-kebab-case",
  "description": "meta description (max 160 chars)",
  "tags": "comma, separated, lowercase, tags",
  "content": "FULL blog post in Markdown"
}}

CONTENT REQUIREMENTS:
1. Strong intro with problem definition
2. Deep technical body (code, logic, SQL where relevant)
3. MANDATORY comparison table
4. FAQ / People Also Ask section at the end
5. Minimum length: 1000 words

CRITICAL TECH RULE:
If you include Liquid / Jinja syntax ({{{{ }}}}, {{% if %}}, etc),
you MUST wrap those code blocks in {{% raw %}} and {{% endraw %}}.
"""

# =========================
# 4. GENERATIE FUNCTIE
# =========================

def generate_full_post():
    print("🚀 Start single-shot generatie...")

    for model_name in CANDIDATE_MODELS:
        print(f"👉 Proberen met model: {model_name}")

        for attempt in range(1, 3):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=[
                        {
                            "role": "user",
                            "parts": [{"text": full_prompt}]
                        }
                    ],
                    config=types.GenerateContentConfig(
                        temperature=0.6,
                        max_output_tokens=8192,
                        response_mime_type="application/json"
                    )
                )

                print(f"✅ Gelukt met {model_name}")
                return response.text

            except Exception as e:
                err = str(e)

                if "429" in err or "RESOURCE_EXHAUSTED" in err:
                    wait_time = 30 * attempt
                    print(f"⏳ Rate limit ({model_name}) → wachten {wait_time}s")
                    time.sleep(wait_time)
                    continue

                if "404" in err or "NOT_FOUND" in err:
                    print(f"⚠️ Model niet gevonden: {model_name}")
                    break

                print(f"❌ Error met {model_name}: {err}")
                break

    return None

# =========================
# 5. CONTENT GENEREREN
# =========================

raw_json = generate_full_post()

if not raw_json:
    raise RuntimeError("❌ API faalde op alle modellen")

try:
    data = json.loads(raw_json)
except json.JSONDecodeError as e:
    with open("error_dump.txt", "w", encoding="utf-8") as f:
        f.write(raw_json)
    raise RuntimeError(f"❌ JSON parse error: {e}")

title = data.get("title", base_prompt_theme)
slug = data.get("slug", "blog-post")
description = data.get("description", "")
tags = data.get("tags", "email,marketing")
body = data.get("content", "")

print(f"✅ Content geparsed: {title}")

# =========================
# 6. AFBEELDING GENEREREN
# =========================

def download_image(prompt_text, save_path):
    print("🎨 Afbeelding genereren...")
    try:
        clean_prompt = (
            f"3D render in Apple App Store editorial style of {prompt_text}, "
            "glossy 3D icon, soft gradient background, no text"
        )
        encoded = clean_prompt.replace(" ", "%20")
        seed = random.randint(0, 9999)

        url = (
            f"https://image.pollinations.ai/prompt/{encoded}"
            f"?width=1200&height=630&seed={seed}&nologo=true&model=flux"
        )

        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(r.content)
            return True
    except Exception:
        pass
    return False

date_str = datetime.now().strftime("%Y-%m-%d")

os.makedirs("_posts", exist_ok=True)
os.makedirs("images", exist_ok=True)

image_filename = f"images/{date_str}-{slug}.jpg"
download_image(slug.replace("-", " "), image_filename)

# =========================
# 7. OPSLAAN ALS JEKYLL POST
# =========================

final_post = f"""---
layout: post
title: "{title}"
date: {date_str}
permalink: /{slug}
tags: {tags}
author: Jeffrey Overmeer
published: true
thumbnail: "/{image_filename}"
description: "{description}"
---

{body}
"""

post_path = f"_posts/{date_str}-{slug}.md"
with open(post_path, "w", encoding="utf-8") as f:
    f.write(final_post)

print(f"🎉 Klaar! Post opgeslagen: {post_path}")
