import os
import time
import requests # Nieuwe, betere bibliotheek
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

# 3. De Verbeterde Image Downloader
def download_image_robust(prompt_text, save_path):
    print(f"🎨 Start genereren afbeelding voor: {prompt_text}")
    
    # Pollinations URL constructie
    # We gebruiken een 'seed' zodat het plaatje elke keer anders is, maar wel consistent per dag
    clean_prompt = prompt_text.replace(" ", "%20")
    url = f"https://image.pollinations.ai/prompt/futuristic%20minimal%20tech%20illustration%20{clean_prompt}?width=1200&height=630&nologo=true&seed={day_of_year}"
    
    try:
        # We doen alsof we een browser zijn (User-Agent) om blokkades te voorkomen
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            
            # CRUCIALE CHECK: Bestaat het bestand nu echt?
            if os.path.exists(save_path) and os.path.getsize(save_path) > 0:
                print(f"✅ Afbeelding succesvol opgeslagen in: {save_path}")
                return True
            else:
                print(f"❌ Bestand lijkt leeg of niet aangemaakt: {save_path}")
                return False
        else:
            print(f"❌ Server gaf foutmelding: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Fout bij downloaden: {e}")
        return False

# 4. Paden instellen (In de ROOT images map)
safe_slug = topic.lower().replace(" ", "-").replace(":", "").replace("/", "")
date_str = datetime.now().strftime('%Y-%m-%d')

# Mapnamen
post_filename = f"_posts/{date_str}-{safe_slug}.md"
image_folder = "images" # Gewoon 'images' in de root
image_filename = f"{image_folder}/{date_str}-{safe_slug}.jpg"
image_public_path = f"/{image_filename}" # Dit komt in de HTML

# Zorg dat de mappen bestaan
os.makedirs("_posts", exist_ok=True)
os.makedirs(image_folder, exist_ok=True)

# 5. EERST de afbeelding proberen
success = download_image_robust(topic, image_filename)

if not success:
    print("⚠️ LET OP: Afbeelding genereren mislukt. We gaan door, maar gebruiken een fallback of geen plaatje.")
    # Optioneel: Je kunt hier 'exit(1)' doen als je wilt dat het script stopt zonder plaatje.
    # Voor nu laten we hem doorgaan, maar check de logs!

# 6. Tekst Genereren
prompt = f"""
Act as a World-Class SEO Copywriter.
Write a blog post for Jeffrey Overmeer's blog about: '{topic}'.

TARGET AUDIENCE: Marketing Managers & SaaS Founders.
LANGUAGE: Fluent American English.
TONE: Professional, Authoritative, yet Accessible.

REQUIREMENTS:
1.  **Structure**: Markdown. H2 (##) and H3 (###).
2.  **Key Takeaways**: Start with a bulleted list of 3-5 key insights.
3.  **Visuals**: Include at least one Markdown comparison table.
4.  **FAQ**: Add a "Frequently Asked Questions" section at the end.
5.  **Length**: 1000+ words.

IMPORTANT: Start with this EXACT Frontmatter:
---
layout: post
title: "[Create a click-worthy title for {topic}]"
titleshort: "[Short title max 40 chars]"
featured: 0
date: {date_str}
label: email, marketing, automation
permalink: /generated-post-{date_str}
tags: email, marketing, automation, ai, tech
yearreview: false
author: Jeffrey Overmeer
published: true
thumbnail: "{image_public_path}"
description: "[Meta-description max 160 chars]"
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
