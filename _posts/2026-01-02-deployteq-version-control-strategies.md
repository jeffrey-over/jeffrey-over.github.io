---
layout: post
title: "Deployteq Version Control: Stop the 'Backup_Final_V2' Madness"
titleshort: "Deployteq Version Control Strategies"
date: 2026-01-02
label: development
permalink: /deployteq-version-control-strategies
tags: deployteq, workflow, git, automation, development
yearreview: false
author: Jeffrey Overmeer
published: true
thumbnail: "/images/2026-01-02-deployteq-version-control-strategies.jpg"
description: "Deployteq lacks native version control. Here are 3 professional strategies to manage your code and campaigns using Git, DTAP folders, and API automation."
---

If you are a developer working with Deployteq (or similar Marketing Automation platforms like Salesforce Marketing Cloud), you know the pain. You are building complex logic, intricate Smarty templates, and critical data flows, but the environment feels more like a database GUI than a developer workspace.

There is no `git commit` button. There is no `git blame` to see who broke the header. There is no easy rollback.

Instead, we often resort to the "Save As" panic maneuver:
* `Campaign_Xmas_Backup`
* `Campaign_Xmas_Backup_Fixed`
* `Campaign_Xmas_FINAL_Jeff_V3`

This approach is error-prone, clutters your workspace, and is a nightmare for collaboration. In this article, I will share three strategies to implement professional version control in Deployteq, ranging from a disciplined manual workflow to fully automated API backups.

### The Core Problem: GUI vs. IDE

Deployteq is built for marketers to drag and drop campaigns. It stores the "current state" of an object in a database. As developers, we think in "versions" and "diffs" over time. Since the platform doesn't provide this natively, we must build an **"External Master"** workflow.

Here are the three most effective ways to do it.

---

### Strategy 1: The "Code-First" Method (Git as Source of Truth)

This is the most robust method for handling templates, HTML, and extensive Smarty logic. The golden rule here is simple: **Deployteq is for execution, VS Code is for editing.**

**How it works:**
1.  **Create a Git Repository:** Set up a repo (GitHub/GitLab) specifically for your Deployteq assets.
2.  **Local Development:** You write your HTML emails and Smarty functions locally in your IDE (like VS Code). This gives you the benefit of syntax highlighting, linters, and Copilot.
3.  **Commit First, Paste Later:** Before you put *anything* into Deployteq, you commit it to Git.
    * `git commit -m "Refactored loop logic for order confirmation"`
4.  **Copy-Paste:** Only after the commit do you copy the code and paste it into the Deployteq source editor.

**Pros:**
* Full version history and easy rollbacks.
* Ability to work on feature branches without breaking production.
* Code reviews (Pull Requests) are possible before "going live."

**Cons:**
* Requires discipline; the manual copy-paste step is tedious.

---

### Strategy 2: The DTAP Folder Structure (For Visual Flows)

While Strategy 1 works for code, you cannot easily copy-paste a visual campaign flow (the "balls" and connectors). For campaign orchestrations, you need a disciplined folder structure that mimics a professional **DTAP** street (Development, Test, Acceptance, Production).

Stop naming things "Backup". Structure your folders like this:

#### `01_DEVELOPMENT`
* **Purpose:** The sandbox. Break things here.
* **Naming:** `DEV_WelcomeCampaign_V2`
* **Rule:** No real customer data triggers (use test lists).

#### `02_STAGING` (or TEST)
* **Purpose:** The version currently being reviewed by the marketer or client.
* **Naming:** `TEST_WelcomeCampaign_V2`
* **Rule:** Matches production settings but sends to internal seed lists.

#### `99_PRODUCTION`
* **Purpose:** The live environment.
* **Rule:** **Read-only.** You never "quickly fix" something here.
* **Workflow:** If a fix is needed, you duplicate PROD back to DEV, fix it, test it, and then replace the PROD version.

#### `ZZ_ARCHIVE`
* **Purpose:** The graveyard of old versions.
* **Rule:** When a new version goes to PROD, move the old one here with a timestamp in the name (e.g., `ARCHIVE_20251230_WelcomeCampaign`).

---

### Strategy 3: The API Snapshot Script (The "Pro" Move)

Since we are developers, why not automate the backup process? If you forget to copy-paste your code to Git (Strategy 1), you are lost. Unless you have a script that does it for you.

You can write a Python script that runs nightly (e.g., via GitHub Actions) to fetch your templates via the Deployteq API and commit changes to a repository automatically.

**The Workflow:**
1.  Script connects to Deployteq API.
2.  Iterates through all Email Templates / Content blocks.
3.  Downloads the Source HTML/Smarty.
4.  Saves them to a file (e.g., `/backups/template_123.html`).
5.  Git detects changes ("diffs") and pushes them.

**Python Concept Code:**

{% raw %}
```python
import os
import requests
# automated_backup.py

API_URL = "[https://api.deployteq.com/v1](https://api.deployteq.com/v1)"
HEADERS = {"Authorization": f"Bearer {os.getenv('DEPLOYTEQ_TOKEN')}"}

def backup_templates():
    # 1. Get list of all templates
    # (Note: Check specific Deployteq API docs for exact endpoints)
    templates = requests.get(f"{API_URL}/content/templates", headers=HEADERS).json()
    
    for tmpl in templates:
        tmpl_id = tmpl['id']
        tmpl_name = tmpl['name'].replace(" ", "_")
        
        # 2. Get the source code
        source = requests.get(f"{API_URL}/content/templates/{tmpl_id}/source", headers=HEADERS).text
        
        # 3. Save to file
        filename = f"backups/{tmpl_name}.html"
        
        # Only write if changed (Git handles the diff, but efficient IO is good)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(source)
            print(f"Backed up: {tmpl_name}")

if __name__ == "__main__":
    backup_templates()
{% endraw %}

The Result: If you make a mistake in Deployteq on Tuesday, you can check your GitHub repo on Wednesday morning and see exactly what lines changed during the night. It's a safety net that costs zero effort once set up.

Conclusion: What is the best approach?

For a robust professional environment, I recommend a hybrid approach:

Use Strategy 1 (VS Code + Git) for your complex Smarty logic, headers, and footers. These are code files and should be treated as such.

Use Strategy 2 (DTAP Folders) for your Campaign Flows. It keeps the Deployteq interface clean and prevents "accidental" edits to live campaigns.

Consider Strategy 3 if you are working in an Enterprise environment where compliance and disaster recovery are critical.

Deployteq is a powerful engine, but it needs a developer's touch to keep the engine room organized. Stop creating backups named FINAL_FINAL_V2 and start managing your versions like a pro.
