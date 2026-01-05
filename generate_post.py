import os
import time
import random
import json
import requests
from datetime import datetime
from google import genai

# =========================
# 1. CONFIG
# =========================

if "GEMINI_API_KEY" not in os.environ:
    raise RuntimeError("GEMINI_API_KEY ontbreekt")

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# ✅ CORRECTE MODELNAMEN VOOR google.genai
CANDIDATE_MODELS = [
    "gemini-1.5-flash",
    "gemini-1.5-pro"
]

# =========================
# 2. SEO STRATEGIE
# =========================

seo_structures = [
    "Advanced {tech} Tutorial: Step-by-Step",
    "Why {tech} is the future of Email Marketing",
    "The Ultimate Guide to {tech} for Developers",
    "Top 5 Mistakes Developers Make with {tech}"
]

tech_keywords = [
    "Salesforce Marketing Cloud",
    "Liquid Scripting",
    "AMP for Email",
    "SSJS",
    "Email SQL Queries"
]

structure = random.choice(seo_structures)
tech = random.choice(tech_keywords)
topic = structure.replace("{tech}", tech)

print(f"🎯 Strategie: {topic}")

# =========================
# 3. PROMPT
# =========================

prompt = f"""
Act as a Senior Technical Content Writer & SEO Specialist.

Create a COMPLETE blog post for:
"{topic}"

OUTPUT RULES:
- Output ONLY valid JSON
- No markdown fences
- No explanations

JSON FORMAT:
{{
  "title": "SEO title (max 60 chars)",
  "slug": "kebab-case-slug",
  "description": "meta description (max 160 chars)",
  "tags": "comma, separated, lowercase",
  "content": "Full blog post in Markdown"
}}

CONTENT RULES:
- 1000+ words
- Mandatory comparison table
- Technical deep dive
- FAQ / People Also Ask section

TECH RULE:
Liquid / Jinja code MUST be wrapped in {{% raw %}} and {{% endraw %}}.
"""

# =========================
# 4. GENERATIE
# =========================

def generate():
    for model in CANDIDATE_MODELS:
        print(f"👉 Proberen met model: {model}")
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config={
                    "temperature": 0.6,
                    "max_output_tokens": 8192,
                    "response_mime_type": "application/json"
                }
            )
            print(f"✅ Gelukt met {model}")
            return response.text
        except Exception as e:
            print(f"⚠️ Fout met {model}: {e}")
            time.sleep(10)

    return None

raw = generate()
if not raw:
    raise RuntimeError("❌ API faalde op alle modellen")

# =========================
# 5. JSON PARSE
# =========================

try:
    data = json.loads(raw)
except json.JSONDecodeError:
    with open("error_dump.txt", "w") as f:
        f.write(raw)
    raise RuntimeError("❌ JSON parsing faalde")

title = data["title"]
slug = data["slug"]
description = data["description"]
tags = data["tags"]
content = data["content"]

# =========================
# 6. IMAGE
# =========================

def download_image(prompt, path):
    seed = random.randint(0, 9999)
    url = (
        "https://image.pollinations.ai/prompt/"
        f"{prompt.replace(' ', '%20')}"
        f"?width=1200&height=630&seed={seed}&model=flux&nologo=true"
    )
    r = requests.get(url, timeout=30)
    if r.status_code == 200:
        with open(path, "wb") as f:
            f.write(r.content)

date = datetime.now().strftime("%Y-%m-%d")
os.makedirs("_posts", exist_ok=True)
os.makedirs("images", exist_ok=True)

image_path = f"images/{date}-{slug}.jpg"
download_image(slug.replace("-", " "), image_path)

# =========================
# 7. OPSLAAN
# =========================

post = f"""---
layout: post
title: "{title}"
date: {date}
permalink: /{slug}
tags: {tags}
author: Jeffrey Overmeer
published: true
thumbnail: "/{image_path}"
description: "{description}"
---

{content}
"""

post_path = f"_posts/{date}-{slug}.md"
with open(post_path, "w", encoding="utf-8") as f:
    f.write(post)

print(f"🎉 Succes! Post opgeslagen: {post_path}")
