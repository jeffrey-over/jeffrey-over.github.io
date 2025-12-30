import os
import time
import requests
from google import genai
from datetime import datetime

# 1. Configureren
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. Onderwerpen: Deep Dives & Developer Focus
topics = [
    # --- ESP Vergelijkingen & Tech ---
    "Selligent Marketing Cloud vs Salesforce: A Developer's Perspective",
    "Deployteq Data Model: Best Practices for Campaign Developers",
    "Migrating from Mailchimp to Enterprise ESPs: Technical Pitfalls",
    "Klaviyo vs Braze: Which one scales better for E-commerce?",
    "Spotler vs Deployteq: A Technical Feature Showdown",
    "The Hidden Features of Selligent Cortex every Developer should know",
    "Marketing Cloud AMPScript vs Selligent Smart Content: A Comparison",
    
    # --- Coding & Development ---
    "Advanced Liquid Scripting Hacks for Personalization",
    "Dark Mode Email Coding: The Ultimate 2026 Cheat Sheet",
    "Interactive Email with AMP: Building Forms inside Gmail",
    "CSS Grid in Email: Is it safe to use yet?",
    "Debugging HTML Emails: Tools & Techniques for Professionals",
    "Mastering SQL for Advanced Segmentation in Marketing Automation",
    "API Triggered Campaigns: A Technical Implementation Guide",
    "Dynamic Content Blocks: Server-side vs Client-side Rendering",
    
    # --- Strategie & "Low Hanging Fruit" ---
    "Low Hanging Fruit: Birthday Automations 2.0 (Beyond the coupon)",
    "Win-Back Flows that actually convert: A Data-Driven Approach",
    "The 'Abandoned Browse' Flow: Implementation Guide",
    "Replenishment Campaigns: Calculating the perfect timing with Data",
    "Loyalty Program Integration in Email: Technical Best Practices",
    "Surprise & Delight: Automating Random Rewards safely",
    
    # --- Deliverability & Data ---
    "BIMI & VMC Certificates: Is it worth the investment?",
    "DMARC Enforcement: A Step-by-Step Guide for Marketers",
    "Warm-up Strategies for Dedicated IP Addresses",
    "Feedback Loops & Whitelisting: The Technical Details",
    "Handling Hard Bounces: Automating List Hygiene via API",
    
    # --- Future & AI ---
    "AI-Generated Subject Lines vs Human Creativity: A/B Test Results",
    "Predictive Churn Modeling using Email Data",
    "Hyper-Personalization at Scale: The role of AI in 2026",
    "The End of Open Rates: New KPIs for Campaign Developers"
]

# Kies random onderwerp op basis van de dag
day_of_year = datetime.now().timetuple().tm_yday
topic = topics[day_of_year % len(topics)]

# 3. Image Downloader (Abstract & Clean)
def download_image_robust(prompt_text, save_path):
    print(f"🎨 Start genereren afbeelding voor: {prompt_text}")
    
    # Prompt: Abstract, Tech, Geen tekst
    base_prompt = f"abstract 3d composition representing {prompt_text}, futuristic, clean, minimalist, iso, high quality, 8k, no text, blurred background"
    clean_prompt = base_prompt.replace(" ", "%20")
    
    url = f"https://image.pollinations.ai/prompt/{clean_prompt}?width=1200&height=630&nologo=true&seed={day_of_year}&model=flux"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            
            if os.path.exists(save_path) and os.path.getsize(save_path) > 0:
                print(f"✅ Afbeelding opgeslagen: {save_path}")
                return True
        print(f"❌ Server fout: {response.status_code}")
        return False
            
    except Exception as e:
        print(f"❌ Fout bij downloaden: {e}")
        return False

# 4. Paden
safe_slug = topic.lower().replace(" ", "-").replace(":", "").replace("/", "")
date_str = datetime.now().strftime('%Y-%m-%d')

post_filename = f"_posts/{date_str}-{safe_slug}.md"
image_folder = "images"
image_filename = f"{image_folder}/{date_str}-{safe_slug}.jpg"
image_public_path = image_filename 

os.makedirs("_posts", exist_ok=True)
os.makedirs(image_folder, exist_ok=True)

# 5. Download Image
download_image_robust(topic, image_filename)

# 6. Content Genereren
prompt = f"""
Act as a Senior Email Campaign Developer & Technical Marketer.
Write a high-level, technical blog post for Jeffrey Overmeer's blog about: '{topic}'.

TARGET AUDIENCE: Experienced Email Marketers, CRM Specialists, and Developers.
LANGUAGE: Fluent American English.
TONE: Authoritative, Technical, Insightful (Show expertise).

REQUIREMENTS:
1.  **Deep Dive**: Go beyond basics. Discuss code, data structures, or strategy nuances.
2.  **Comparison Table**: If applicable, compare tools/methods (e.g. "Pros/Cons" or "Feature Matrix").
3.  **Code/Snippets**: If the topic allows, include a (pseudo)code block or SQL example.
4.  **Key Takeaways**: Start with 3 bullet points for quick scanning.
5.  **FAQ**: End with a technical FAQ section.
6.  **Length**: 1000+ words.

IMPORTANT: Start with this EXACT Frontmatter:
---
layout: post
title: "[Technical SEO Title for {topic}]"
titleshort: "[Short title max 40 chars]"
featured: 0
date: {date_str}
label: email, development, automation
permalink: /generated-post-{date_str}
tags: email, marketing, development, selligent, deployteq, tech
yearreview: false
author: Jeffrey Overmeer
published: true
thumbnail: "{image_public_path}"
description: "[Technical meta-description max 160 chars]"
---

After frontmatter, write the full post.
"""

models_to_try = [
    "gemini-3-pro-preview",
    "gemini-2.0-flash-exp",
    "gemini-2.5-flash",
    "gemini-flash-latest",
    "gemini-1.5-flash"
]

generated_content = None

print(f"📝 Start tekst generatie voor: {topic}")

for model_name in models_to_try:
    print(f"Poging met model: {model_name}...")
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        generated_content = response.text
        print(f"✅ Tekst gegenereerd met {model_name}")
        break 
    except Exception as e:
        print(f"❌ Mislukt met {model_name}: {e}")
        time.sleep(1)

# 7. Opslaan
if generated_content:
    if "---" in generated_content:
        start_index = generated_content.find("---")
        generated_content = generated_content[start_index:]

    with open(post_filename, "w", encoding="utf-8") as f:
        f.write(generated_content)

    print(f"🎉 Blogpost opgeslagen: {post_filename}")
else:
    print("⚠️ Alle modellen faalden.")
    exit(1)
