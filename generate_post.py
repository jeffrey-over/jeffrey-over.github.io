import os
import time
import random
import json
import requests
from datetime import datetime
import google.generativeai as genai

# =========================
# 1. CONFIG
# =========================

if "GEMINI_API_KEY" not in os.environ:
    raise RuntimeError("GEMINI_API_KEY ontbreekt")

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# ✅ ENIGE STABIELE MODELLEN HIER
CANDIDATE_MODELS = [
    "gemini-pro"
]

# =========================
# 2. SEO STRATEGIE
# =========================

seo_structures = [
    "The Ultimate Guide to {tech} for Developers",
    "Advanced {tech} Tutorial: Step-by-Step",
    "Why {tech} is the future of Email Marketing"
]

tech_keywords = [
    "Email SQL Queries",
    "Salesforce Marketing Cloud",
    "Liquid Scripting",
    "SSJS"
]

topic = random.choice(seo_structures).replace(
    "{tech}", random.choice(tech_keywords)
)

print(f"🎯 Strategie: {topic}")

# =========================
# 3. PROMPT
# =========================

prompt = f"""
Act as a Senior Technical Content Writer & SEO Specialist.

Write a COMPLETE blog post about:
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
- FAQ section

TECH RULE:
Liquid / Jinja code MUST be wrapped in {{% raw %}} and {{% endraw %}}.
"""

# =========================
# 4. GENERATE
# =========================

def generate():
    for model_name in CANDIDATE_MODELS:
        try:
            print(f"👉 Proberen met model: {model_name}")
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.6,
                    "max_output_tokens": 8192
                }
            )
            print("✅ Gelukt")
            return response.text
        except Exception as e:
            print(f"⚠️ Fout: {e}")
            time.sleep(10)
    return None

raw = generate()
if not raw:
    raise RuntimeError("❌ API faalde")

# =========================
# 5. PARSE JSON
# =========================

try:
    data = json.loads(raw)
except json.JSONDecodeError:
    with open("error_dump.txt", "w") as f:
        f.write(raw)
    raise RuntimeError("JSON parsing faalde")

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
# 7. SAVE
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

path = f"_posts/{date}-{slug}.md"
with open(path, "w", encoding="utf-8") as f:
    f.write(post)

print(f"🎉 Succes! Post opgeslagen: {path}")
