import os
import time
from google import genai
from datetime import datetime

# 1. Configureren
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. Onderwerpen
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

# 4. De "Slimme" Generator (Nu met Gemini 3 Pro bovenaan!)
models_to_try = [
    "gemini-3-pro-preview",      # Jouw voorkeur (Het allerbeste model)
    "gemini-2.0-flash-exp",      # Vaak gratis & super slim
    "gemini-2.5-flash",          # Nieuwe stabiele versie
    "gemini-flash-latest",       # Veilige fallback
    "gemini-1.5-flash"           # Oude fallback
]

generated_content = None

print(f"Start genereren voor onderwerp: {topic}")

for model_name in models_to_try:
    print(f"Proberen met model: {model_name}...")
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        generated_content = response.text
        print(f"✅ SUCCES! Content gegenereerd met {model_name}")
        break 
    except Exception as e:
        print(f"❌ Mislukt met {model_name}: {e}")
        # Geen pauze nodig bij 404, wel bij 429, dus korte sleep is veilig
        time.sleep(1)

# 5. Opslaan
if generated_content:
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
    print("\n⚠️ Helaas, alle modellen faalden.")
    # Print nogmaals de lijst om te debuggen als het misgaat
    try:
        print("Beschikbare modellen voor jouw key:")
        for m in client.models.list():
            print(f"- {m.name}")
    except:
        pass
    exit(1)
