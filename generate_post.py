import os
from google import genai
from datetime import datetime

# 1. Configureren
# We gebruiken de nieuwe Client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. SEO Strategie: Roulatie van onderwerpen
topics = [
    "Email Deliverability Best Practices",
    "Subject Line AI Generators vs Human Creativity",
    "GDPR and Email Marketing Updates",
    "Segmenting Audiences for Higher Open Rates",
    "The Psychology of the Click-Through Rate",
    "Email Design Trends: Dark Mode & Interactivity",
    "Automated Welcome Flows: The Ultimate Guide",
    "Win-Back Campaigns: Re-engaging Dormant Users",
    "Transactional vs Marketing Emails",
    "Integrating CRM with Email Automation Tools",
    "A/B Testing Strategies for Newsletters",
    "Mobile-First Email Design Strategies",
    "Reducing Churn Rate via Email Automation",
    "Cold Email Outreach Strategies",
    "Email Marketing KPIs you should track",
    "Newsletter Monetization Strategies",
    "Omnichannel Marketing: Email + SMS",
    "Cleaning your Email List: Why and How",
    "Hyper-personalization in Email Marketing",
    "B2B vs B2C Email Marketing Strategies",
    "The Impact of AI on Email Copywriting",
    "Avoiding the Spam Folder (SPF/DKIM)",
    "Drip Campaigns for SaaS Onboarding",
    "Holiday Email Marketing Calendars",
    "User Generated Content in Emails",
    "Interactive AMP Emails explained",
    "Video in Email Marketing",
    "Storytelling in Newsletters",
    "Lead Magnets that grow your Email List",
    "The Future of Email Marketing Automation"
]

# Kies een onderwerp gebaseerd op de dag van het jaar
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

# 4. Content genereren
try:
    # We gebruiken gemini-1.5-flash, dat is de stabiele gratis versie
    response = client.models.generate_content(
        model="gemini-1.5-flash", 
        contents=prompt
    )
    
    content = response.text
    
    # Check of de output begint met --- (clean up indien nodig)
    if "---" in content:
        start_index = content.find("---")
        content = content[start_index:]

    # 5. Opslaan
    safe_slug = topic.lower().replace(" ", "-").replace(":", "").replace("/", "")
    filename = f"_posts/{datetime.now().strftime('%Y-%m-%d')}-{safe_slug}.md"

    os.makedirs("_posts", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Succes! Blogpost aangemaakt: {filename}")

except Exception as e:
    print(f"Fout bij genereren: {e}")
    exit(1)
