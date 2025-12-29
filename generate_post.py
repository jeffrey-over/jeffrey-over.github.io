import os
import time
from google import genai
from google.genai import types
from datetime import datetime

# 1. Configureren
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. SEO Strategie: Onderwerpen
topics = [
    "Email Deliverability Best Practices 2026",
    "Subject Line AI Generators vs Human Creativity",
    "GDPR and Email Marketing: A 2026 Update",
    "Segmenting Audiences for Higher Open Rates",
    "The Psychology of the Click-Through Rate",
    "Email Design Trends: Dark Mode & Interactivity",
    "Automated Welcome Flows: The Ultimate Guide",
    "Win-Back Campaigns: Re-engaging Dormant Users",
    "Transactional vs Marketing Emails: The Differences",
    "Integrating CRM with Email Automation Tools",
    "A/B Testing Strategies for Newsletters",
    "Mobile-First Email Design Strategies",
    "Reducing Churn Rate via Email Automation",
    "Cold Email Outreach: Does it still work?",
    "Email Marketing KPIs you should track",
    "Newsletter Monetization Strategies",
    "Omnichannel Marketing: Email + SMS",
    "Cleaning your Email List: Why and How",
    "Hyper-personalization in Email Marketing",
    "B2B vs B2C Email Marketing Strategies",
    "The Impact of AI on Email Copywriting",
    "Avoiding the Spam Folder: Technical Guide (SPF/DKIM)",
    "Drip Campaigns for SaaS Onboarding",
    "Holiday Email Marketing Calendars",
    "User Generated Content in Emails",
    "Interactive AMP Emails explained",
    "Video in Email Marketing: Pros and Cons",
    "Storytelling in Newsletters",
    "Lead Magnets that grow your Email List",
    "The Future of Email Marketing Automation"
]

day_of_year = datetime.now().timetuple().tm_yday
topic = topics[day_of_year % len(topics)]

# 3. De Prompt
prompt = f"""
Je bent een Senior SEO Specialist en Content Marketer.
Schrijf een technische, diepgaande blogpost voor Jeffrey Overmeer's blog over: '{topic}'.

DOEL: Ranken in Google op long-tail keywords rondom dit topic.
TOON: Professioneel, behulpzaam, expert-niveau.
STRUCTUUR: Markdown. Gebruik H2 (##) en H3 (###).

BELANGRIJK: De output MOET beginnen met deze exacte Frontmatter block (YAML):
---
layout: post
title: "[Bedenk een pakkende, SEO-titel voor {topic}]"
titleshort: "[Korte versie van de titel max 40 tekens]"
featured: 0
date: {datetime.now().strftime('%Y-%m-%d')}
label: email, marketing, automation
permalink: /generated-post-{datetime.now().strftime('%Y-%m-%d')}
tags: email, marketing, automation, ai, tech
yearreview: false
author: Jeffrey Overmeer
published: true
thumbnail: "/images/email-marketing-default.png"
description: "[Een sterke meta-description van max 160 tekens]"
---

Schrijf daarna de blogpost. 
- Begin met een sterke introductie.
- Gebruik tussenkopjes.
- Verwerk een vergelijkingstabel (markdown table) in de tekst.
- Eindig met een conclusie.
"""

# 4. De "Slimme" Generator (Probeert meerdere modellen)
models_to_try = [
    "gemini-1.5-flash",       # Standaard alias
    "gemini-1.5-flash-001",   # Specifieke versie 1
    "gemini-1.5-flash-002",   # Specifieke versie 2
    "gemini-1.5-pro",         # Probeer Pro als Flash faalt
    "gemini-2.0-flash-exp"    # Experimenteel (als laatste redmiddel)
]

generated_content = None
used_model = None

print(f"Start genereren voor onderwerp: {topic}")

for model_name in models_to_try:
    print(f"Proberen met model: {model_name}...")
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        generated_content = response.text
        used_model = model_name
        print(f"✅ SUCCES! Content gegenereerd met {model_name}")
        break # Stop de loop, we hebben beet!
    except Exception as e:
        print(f"❌ Mislukt met {model_name}: {e}")
        time.sleep(1) # Even wachten voor de volgende poging

# 5. Opslaan (of foutmelding printen als ALLES faalt)
if generated_content:
    # Cleanup frontmatter indien nodig
    if "---" in generated_content:
        start_index = generated_content.find("---")
        generated_content = generated_content[start_index:]

    safe_slug = topic.lower().replace(" ", "-").replace(":", "").replace("/", "")
    filename = f"_posts/{datetime.now().strftime('%Y-%m-%d')}-{safe_slug}.md"

    os.makedirs("_posts", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(generated_content)

    print(f"🎉 Blogpost opgeslagen: {filename}")

else:
    print("\n⚠️ ALLE POGINGEN MISLUKT. DEBUG INFO:")
    print("Beschikbare modellen voor deze API key:")
    try:
        # Dit print alle modellen die JIJ mag gebruiken in de log
        for m in client.models.list():
            print(f"- {m.name}")
    except Exception as list_err:
        print(f"Kon modellenlijst niet ophalen: {list_err}")
    
    # Laat de action falen zodat je een mail krijgt
    exit(1)
