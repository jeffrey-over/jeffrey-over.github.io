import os
import time
import urllib.parse
import urllib.request
from google import genai
from datetime import datetime

# 1. Configuration
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. Topic Rotation
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

# 3. Image Generation Function (No API Key needed)
def download_image(prompt_text, save_path):
    print(f"🎨 Generating image for: {prompt_text}...")
    try:
        # Create a safe URL prompt
        encoded_prompt = urllib.parse.quote(f"futuristic clean minimal tech illustration about {prompt_text}, soft lighting, high quality, 4k")
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1200&height=630&nologo=true&seed={day_of_year}"
        
        # Download the image
        urllib.request.urlretrieve(image_url, save_path)
        print(f"✅ Image saved to {save_path}")
        return True
    except Exception as e:
        print(f"❌ Image generation failed: {e}")
        return False

# 4. Determine Filenames
safe_slug = topic.lower().replace(" ", "-").replace(":", "").replace("/", "")
date_str = datetime.now().strftime('%Y-%m-%d')
post_filename = f"_posts/{date_str}-{safe_slug}.md"
image_filename = f"images/{date_str}-{safe_slug}.jpg"
image_public_path = f"/{image_filename}" # This goes into the frontmatter

# Ensure directories exist
os.makedirs("_posts", exist_ok=True)
os.makedirs("images", exist_ok=True)

# 5. Generate and Download Image FIRST
download_image(topic, image_filename)

# 6. Generate Text Content
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

# 7. AI Generation Loop
models_to_try = [
    "gemini-3-pro-preview",
    "gemini-2.0-flash-exp",
    "gemini-2.5-flash",
    "gemini-flash-latest",
    "gemini-1.5-flash"
]

generated_content = None

print(f"📝 Starting text generation for: {topic}")

for model_name in models_to_try:
    print(f"Trying model: {model_name}...")
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        generated_content = response.text
        print(f"✅ SUCCESS! Text generated using {model_name}")
        break 
    except Exception as e:
        print(f"❌ Failed with {model_name}: {e}")
        time.sleep(1)

# 8. Save Content
if generated_content:
    if "---" in generated_content:
        start_index = generated_content.find("---")
        generated_content = generated_content[start_index:]

    with open(post_filename, "w", encoding="utf-8") as f:
        f.write(generated_content)

    print(f"🎉 Blogpost saved: {post_filename}")
else:
    print("⚠️ All models failed.")
    exit(1)
