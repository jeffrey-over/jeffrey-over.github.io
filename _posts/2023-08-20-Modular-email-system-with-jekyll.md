---
layout: post
title: "Building a Modular Email System with Jekyll"
date: 2023-08-20
label: email
permalink: /modular-email-system-with-jekyll
tags: design, email, developer, jekyll, tips
yearreview: false
author: Jeffrey Overmeer
published: true
thumbnail: "/images/modular.jpg"
description: "Discover the ultimate guide to crafting a powerful Email Design System. Learn how to unify brand aesthetics, design modular components, implement responsive layouts, and more. Elevate your email marketing with consistency and efficiency. A comprehensive tutorial for marketers and designers."
---

In this tutorial, we'll walk through the step-by-step process of building a modular email system using Jekyll. Jekyll is a static site generator commonly used for building websites, but it can also be utilized to generate emails. The modular system we'll build will make it easy to create reusable email components and assemble them into complete emails.

### Table of Contents
1. **Preparations**
   - Installing Jekyll
   - Setting up the Basic Structure

2. **Modular Email Components**
   - Header
   - Text Blocks
   - Images
   - Call-to-Action Buttons
   - Footer

3. **Creating Email Templates**
   - Template for Promotion Email
   - Template for Newsletter

4. **Generating Emails**
   - Using YAML Front Matter
   - Utilizing Includes

5. **Testing and Sending**
   - Testing Across Email Clients
   - Sending the Emails

### 1. Preparations
#### Installing Jekyll
Make sure you have Jekyll installed on your system. Use the following command to install Jekyll via RubyGems:

```
gem install jekyll
```

#### Setting up the Basic Structure
Create a new directory for your project and navigate into it:

```bash
mkdir modular_email_system
cd modular_email_system
```

Initialize a new Jekyll project:
```bash
jekyll new .
```


### 2. Modular Email Components

#### Header
Create a new file named `_header.html` in the _includes directory. This file will contain the code for the email header:

 <pre><code>&lt;table width="100%" cellpadding="0" cellspacing="0"&gt;
  &lt;tr&gt;
    &lt;td align="center"&gt;
      &lt;h1&gt;Our Amazing Emails&lt;/h1&gt;
    &lt;/td&gt;
  &lt;/tr&gt;
&lt;/table&gt;</code></pre>

#### Text Blocks
Create a new file named _text_block.html in the _includes directory. This file will contain the code for a reusable text block:


<pre><code>&lt;table width="100%" cellpadding="0" cellspacing="0"&gt;
  &lt;tr&gt;
    &lt;td&gt;
      &lt;p&gt;&#x7B;&#x7B; include.text &#x7D;&#x7D;&lt;/p&gt;
    &lt;/td&gt;
  &lt;/tr&gt;
&lt;/table&gt;</code></pre>

#### Images
Create a new file named `_image.html` in the _includes directory. This file will contain the code for inserting an image:

<pre><code>&lt;table width="100%" cellpadding="0" cellspacing="0"&gt;
  &lt;tr&gt;
    &lt;td align="center"&gt;
      &lt;img src="&#x7B;&#x7B; include.image_url &#x7D;&#x7D;" alt="&#x7B;&#x7B; include.image_alt &#x7D;&#x7D;" width="300"&gt;
    &lt;/td&gt;
  &lt;/tr&gt;
&lt;/table&gt;</code></pre>



#### Call-to-Action Buttons
Create a new file named `_cta_button.html` in the _includes directory. This file will contain the code for a call-to-action button:

<pre><code>&lt;table width="100%" cellpadding="0" cellspacing="0"&gt;
  &lt;tr&gt;
    &lt;td align="center"&gt;
      &lt;a href="&#x7B;&#x7B; include.button_url &#x7D;&#x7D;" style="background-color: #007bff; color: #ffffff; padding: 10px 20px; text-decoration: none;"&gt;
        &#x7B;&#x7B; include.button_text &#x7D;&#x7D;
      &lt;/a&gt;
    &lt;/td&gt;
  &lt;/tr&gt;
&lt;/table&gt;
</code></pre>

#### Footer
Create a new file named `_footer.html` in the _includes directory. This file will contain the code for the email footer:


<pre><code>&lt;table width="100%" cellpadding="0" cellspacing="0"&gt;
  &lt;tr&gt;
    &lt;td align="center"&gt;
      &lt;p&gt;&amp;copy; &#x7B;&#x7B; site.year &#x7D;&#x7D; Our Company. All rights reserved.&lt;/p&gt;
    &lt;/td&gt;
  &lt;/tr&gt;
&lt;/table&gt;
</code></pre>

### 3. Creating Email Templates

#### Template for Promotion Email
Create a new file named `promotion_email.html` in the _layouts directory. This file will serve as the template for a promotion email:

<pre><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
  &lt;title&gt;&#x7B;&#x7B; page.title &#x7D;&#x7D;&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  {% raw %}{% include _header.html %}{% endraw %}
  
  &lt;table width="100%" cellpadding="0" cellspacing="0"&gt;
    &lt;tr&gt;
      &lt;td&gt;
        {% raw %}{% include _text_block.html text="Don't Miss This Amazing Offer!" %}{% endraw %}
      &lt;/td&gt;
    &lt;/tr&gt;
    &lt;tr&gt;
      &lt;td&gt;
        {% raw %}{% include _cta_button.html button_text="View Now" button_url="#" %}{% endraw %}
      &lt;/td&gt;
    &lt;/tr&gt;
  &lt;/table&gt;
  
  {% raw %}{% include _footer.html %}{% endraw %}
&lt;/body&gt;
&lt;/html&gt;
</code></pre>

#### Template for Newsletter
Create a new file named `newsletter.html` in the _layouts directory. This file will be the template for a newsletter:

<pre><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
  &lt;title&gt;&#x7B;&#x7B; page.title &#x7D;&#x7D;&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  {% raw %}{% include _header.html %}{% endraw %}
  
  &lt;table width="100%" cellpadding="0" cellspacing="0"&gt;
    &lt;tr&gt;
      &lt;td&gt;
        {% raw %}{% include _text_block.html text="News and Updates for This Month:" %}{% endraw %}
      &lt;/td&gt;
    &lt;/tr&gt;
    &lt;tr&gt;
      &lt;td&gt;
        {% raw %}{% include _text_block.html text="1. New Product Launch" %}{% endraw %}
        {% raw %}{% include _image.html image_url="image1.jpg" image_alt="New Product" %}{% endraw %}
      &lt;/td&gt;
    &lt;/tr&gt;
    &lt;tr&gt;
      &lt;td&gt;
        {% raw %}{% include _text_block.html text="2. Our Recommendation of the Month" %}{% endraw %}
        {% raw %}{% include _cta_button.html button_text="Read More" button_url="#" %}{% endraw %}
      &lt;/td&gt;
    &lt;/tr&gt;
  &lt;/table&gt;
  
  {% raw %}{% include _footer.html %}{% endraw %}
&lt;/body&gt;
&lt;/html&gt;</code></pre>

### 4. Generating Emails
#### Using YAML Front Matter
In each email template (e.g., promotion_email.html and newsletter.html), use YAML Front Matter to set the email's title:


```yaml
---
layout: promotion_email
title: Amazing Offer!
---
```
#### Utilizing Includes
Use the previously created includes to compose emails within the templates. Include the appropriate variables for dynamic content.

### 5. Testing and Sending
#### Testing Across Email Clients
Before sending the emails, test them across various email clients to ensure proper rendering. Use services like Litmus or Email on Acid for comprehensive testing.

#### Sending the Emails
To send the emails, you can use an email marketing service such as DeployTeq, Selligent, or Salesforce Marketing Cloud. These services provide tools to send your emails to subscribers and track statistics.

With this tutorial, you've set up a modular email system using Jekyll. You can now easily create reusable email components and assemble them into professional email templates. Remember to test and optimize your emails for different email clients before sending them to your subscribers.
