import os
import time
from google import genai
from datetime import datetime

# 1. Configuration
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. SEO Strategy: Topic Rotation (English)
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

# Pick a topic based on the day of the year
day_of_year = datetime.now().timetuple().tm_yday
topic = topics[day_of_year % len(topics)]

# 3. The Ultimate SEO Prompt (English)
prompt = f"""
Act as a World-Class SEO Copywriter and Email Marketing Expert.
Write a comprehensive, high-ranking blog post for Jeffrey Overmeer's blog about: '{topic}'.

TARGET AUDIENCE: Marketing Managers, SaaS Founders, and Tech-savvy Marketers.
LANGUAGE: Fluent, engaging American English.
TONE: Professional, Authoritative, yet Accessible (E-E-A-T focused).

REQUIREMENTS:
1.  **Structure**: Use Markdown. Include H2 (##) and H3 (###) headers.
2.  **Key Takeaways**: Start the article (after the intro) with a bulleted list of 3-5 "Key Takeaways".
3.  **Visuals**: Include at least one Markdown comparison table.
4.  **Snippet Optimization**: Include a "Frequently Asked Questions" (FAQ) section at the end (Great for Google Featured Snippets).
5.  **Length**: Deep dive, high value (approx. 1000+ words).

IMPORTANT: The output MUST start with this exact Frontmatter block (YAML):
---
layout: post
title: "[Create a click-worthy, SEO-optimized title for {topic}]"
titleshort: "[Short title max 40 chars]"
featured: 0
date: {datetime.now().strftime('%Y-%m-%d')}
label: email, marketing, automation
permalink: /generated-post-{datetime.now().strftime('%Y-%m-%d')}
tags: email, marketing, automation, ai, tech
yearreview: false
author: Jeffrey Overmeer
published: true
thumbnail: "/images/email-marketing-default.png"
description: "[A compelling meta-description (max 160 chars) including the main keyword]"
---

After the frontmatter, write the full blog post.
"""

# 4. Smart Generator (Tries your best models first)
models_to_try = [
    "gemini-3-pro-preview",      # Top Tier
    "gemini-2.0-flash-exp",      # Experimental High Quality
    "gemini-2.5-flash",          # New Stable
    "gemini-flash-latest",       # Fallback Stable
    "gemini-1.5-flash"           # Old Fallback
]

generated_content = None

print(f"Starting generation for topic: {topic}")

for model_name in models_to_try:
    print(f"Trying model: {model_name}...")
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        generated_content = response.text
        print(f"✅ SUCCESS! Content generated using {model_name}")
        break 
    except Exception as e:
        print(f"❌ Failed with {model_name}: {e}")
        time.sleep(1)

# 5. Save File
if generated_content:
    # Cleanup if AI adds text before frontmatter
    if "---" in generated_content:
        start_index = generated_content.find("---")
        generated_content = generated_content[start_index:]

    # Create English slug
    safe_slug = topic.lower().replace(" ", "-").replace(":", "").replace("/", "")
    filename = f"_posts/{datetime.now().strftime('%Y-%m-%d')}-{safe_slug}.md"

    os.makedirs("_posts", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(generated_content)

    print(f"🎉 Blogpost saved: {filename}")

else:
    print("\n⚠️ All models failed. Check Quota or API Key.")
    exit(1)
