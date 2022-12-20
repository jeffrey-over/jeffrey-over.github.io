---
layout: post
title: "Track conversions from your email campaign"
date: 2022-12-18
label: email
permalink: /track-conversion-from-your-email
tags: email marketing, email, marketing
yearreview: false
author: Jeffrey Overmeer
published: true
thumbnail: "/images/emailconversions.jpg"
description: "How to track conversions from your email campaign using UTMs and Google Analytics"
---

<b>This article was created with the help of AI.</b>

Are you running an email campaign and want to know how it's performing? One way to track its effectiveness is by using UTMs (Urchin Tracking Module) and Google Analytics.

UTMs are little pieces of code that you can add to the links in your emails. They allow you to track where traffic is coming from and see how many conversions (e.g., purchases, sign-ups, etc.) are coming from your email campaign.

Here's how to set it up:

<ol>
<li>First, make sure you have a Google Analytics account and have added the tracking code to your website. This will allow you to track traffic to your site and see how visitors are interacting with it.</li>
<li>Next, create unique UTMs for your email campaign. UTMs are made up of three parts: <b>utm_source</b>, <b>utm_medium</b>, and <b>utm_campaign</b>.<Br /><br />
utm_source tells Google Analytics where the traffic is coming from (e.g., "email").<br>
utm_medium specifies the type of email (e.g., "newsletter").<br>
utm_campaign lets you know which specific campaign the traffic is coming from (e.g., "summer_sale").<br>
Here's an example of what a UTM might look like:<br>
<br>
http://www.example.com/?utm_source=email&utm_medium=newsletter&utm_campaign=summer_sale
<br><br></li>
<li>Add these UTMs to the links in your email. For example, if you have a link in your email that says "Shop now," you would change it to something like this:<br>
<pre>&lt;a href="http://www.example.com/?utm_source=email&utm_medium=newsletter&utm_campaign=summer_sale">Shop now&lt;/a&gt;</pre></li>
<li>Now, when someone clicks on that link and visits your website, Google Analytics will track that traffic and attribute it to your email campaign. To see how many conversions came from your email campaign, go to the "Conversions" section of your Google Analytics account and set the "Primary Dimension" to "Campaign."</li>
</ol>

And that's it! With UTMs and Google Analytics, you can easily track the performance of your email campaigns and see how they're driving conversions on your website.