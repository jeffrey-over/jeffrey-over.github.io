---
layout: post
title: "Ultimate email deliverability guide"
date: 2020-02-05
label: e-mail
tags: marketing, tips, e-mail, free
published: true
yearreview: false
thumbnail: "images/blog/deliverability.jpg"
description: "Worked hours on the perfect email, but it bounces? Check out why and how to solve this. Get control over email deliverability."
---

Email Deliverability is difficult. Really really difficult. An email goes through a lot of gates before it finally ends up in the recipient's inbox. Fortunately, because this stops a lot of spam!

It is the collection of factors that determine whether or not your email ends up in your recipient's inbox.

In addition to the <b>content </b> of your email, you also have to deal with <b> authentication </b> (DKIM, SPF, TLS, DMARC) and reputation (blacklists, number of bounces, engagement).

It is therefore also possible that a mail server has a successful "handshake" with Selligent (or another ESP), but the email does not end up in the customer's inbox.

### Reputation
A good domain and sender reputation are essential to ensure that emails end up in the inbox successfully. Sites where your reputation can be tested:
1. <a href="https://returnpath.com/solutions/email-deliverability-optimization/deliverability/" target="_BLANK"> Returnpath </a>
1. <a href="https://talosintelligence.com/" target="_BLANK"> Talos Intelligence </a>
1. <a href="http://www.reputationauthority.org/" target="_BLANK"> Reputation Authority </a>

#### Spam Traps
Spam trap is a method of Internet Service Providers (ISPs) to recognize and block spammers

A spam trap is a fake email address with valid syntax. The email address is otherwise not linked to a person or something.

Ensure good "hygiene" of your data by using a double opt-in. It is also wise not to approach inactive e-mail addresses. For example, you can set a filter that filters email addresses that haven't opened any emails in the last 6 months.

Tools to detect spam traps:
- [DeBounce](https://debounce.io)
- [zero bounce](https://www.zerobounce.net/)
- [proofy](https://proofy.io/)
- [Brite Verify](https://www.briteverify.com/) (Used by Clang)

#### Blacklists
A blacklist is a database that determines which emails should be marked as spam.
You can be blacklisted based on a domain or IP address. Below are some commonly used blacklists:
- [Return Path Reputation Network Blacklist (RNBL)](http://www.returnpath.com/partner-content/reputation-network-blacklist/)
- [Sbl.spamhaus.org (SBL)](http://www.spamhaus.org/sbl/)
- [URIB](http://www.uribl.com/)

With the link below you can check whether you are on a blacklist:
[MX Toolbox](https://mxtoolbox.com/domain/)

### Bounces
[According to Oracle](http://digitalmarketingdepot.com/whitepaper/new-school-marketers-guide-email-deliverability) a high hard bounce rate triggers to blacklist your IP address. With filters or smart read-in processes, make sure you lose this deadweight before sending your emails. Bounces can be divided into a hard and soft bounce.

#### Hard bounce
This includes bounces whose email address is invalid or no longer in use. The email address can also be invalid due to typos, for example hotmal instead of hotmail or the absence of an '@'.

#### Soft bounce
A soft bounce is somewhat vaguer and often temporary, such as a mailbox that is full, the e-mail server of the recipient is not available, etc.

Retrying message delivery after a while can work. However, if the error occurs more often, it is wise to mark it as a hard bounce.

Hard bounces filtering sites:
- [https://www.zerobounce.net/](https://www.zerobounce.net/)
- [https://hunter.io/email-verifier](https://hunter.io/email-verifier)
- [https://www.briteverify.com/](https://www.briteverify.com/)

#### "Mark as spam" complaints
When the recipients of your email click on the "Mark as spam" option, a complaint is registered by the relevant email client such as Gmail or Outlook. they forward this to the ESP. It is therefore important to have an accessible and working logout process. Otherwise, a user will use this feature faster.

#### IP reputation
Spammers are cunning. They always try to bypass SPAM filters, for example by using and rotating new IP addresses. This makes it important that you heat up an IP address. You cannot send a million emails on a daily basis overnight. You will have to expand this slowly over a period of time.

#### Subscriber Engagement
Many email clients such as Gmail are looking for the engagement of your recipients and increasingly use it as one of the most important deliverability metrics.

When your recipients open or click your emails, add your email address to their contacts, or move emails from promotions to the primary inbox, it shows that they appreciate your emails.

### Authentication
Of course, it is easy to pretend to be someone else online. You can easily send an email on behalf of another email address. This makes malware and phishing attacks relatively easy to carry out.

Fortunately, there are several methods such as DKIM. SPF, TLS, and DMARC that make it not so easy anymore. These methods ensure that we can authenticate and verify the identity of the sender of the email.

#### DKIM
DomainKeys Identified Mail (DKIM) is a way to authorize ESPs to send emails for you. DKIM authentication allows a sender to take responsibility for their email and it is used to separate real emails from spam and phishing campaigns.

#### SPF
With SPF, a receiving mail server can check whether an email is from a sending IP address that is allowed to send emails on behalf of a particular domain. When you create an SPF record, you place a list of IPs / sending hosts that are authorized to send an email on behalf of your domain.

You can check SPF records via this [link](https://toolbox.googleapps.com/apps/checkmx).

#### TLS
Transport Layer Security (TLS) is a protocol used to encrypt information. TLS uses certificates to encrypt sessions to maintain the confidentiality of information. SendGrid uses TLS to encrypt sessions with its application over HTTPS and API. Gmail has now started using TLS. It will probably not be long before the email clients do the same.

#### DMARC
DMARC is an abbreviation for "Domain-based Message Authentication, Reporting & Conformance", a new standard that makes it easier for ISPs to prevent e-mail abuse. It is a process of determining whether an email is legitimate.

### Content
When a message is received by your provider it first performs reputation and authentication checks. Based on that an email can be allowed, filtered, or blocked.

When the email arrives at the next gate, the anti-spam software starts to analyze your content and then decides to mark or deliver your email as spam. Below a number of themes about e-mail content.

#### Good HTML
Most emails sent via ESPs are HTML emails. A broken HTML can lead to an unreadable email. Make sure your HTML is on point.

#### Responsive HTML
A topic that nowadays is common for everyone: Make sure that your emails are displayed nicely on mobile devices.

#### Don't use short-url tools
URL shorteners are super handy for easily sharing a long URL. This is also used by spammers. The use of short-URL is therefore increasingly marked by email clients as spam.

#### From email address.
If you send both transactional and promotional emails, it is advisable to use separate email addresses.
Classification of emails with tabs (promotions, updates, social, etc.) based on email content and the sender's email address. In addition, a promotional email will be marked as spam faster than a transactional email.

#### Segmentation
Segment your target group based on areas of interest so that the right content arrives at the right person. In addition to being better for conversion, it also allows for more interaction in your emails. Also avoid inactive applicants because they also have a negative effect on your reputation.

#### Easy unsubscribe process
The logout process should be simple and straightforward. It shouldn't be that they are required to fill out a form first and then wait a week before the opt-out is removed.

#### From & Reply addresses
The email address you use has to go to an inbox somewhere. So don't use no-reply email addresses,
If it turns out that they cannot respond by email, they will use the "mark as spam" option more quickly.

### Other methods

#### Feedback loop
When a recipient has decided to click 'This is spam' on this email address, it is considered a 'complaint'. Some providers make this clear before sending by making a feedback loop. Feedback loops, or FBLs, allow senders to receive messages from recipients who have complained. The provider forwards the complained message to the sender at an agreed e-mail address so that the sender can identify this user in his database.
[More info from Returhpath.com] (https://blog.returnpath.com/what-is-a-feedback-loop/)

#### Suppression list
The suppression list is a special table and contains all email addresses that you **always** want to exclude. E-mail addresses on the suppression list cannot, therefore, be accidentally read and emailed.

### Tools
[MX Toolbox](https://mxtoolbox.com/dkim.aspx)
<br />Check SPF, DKIM and blacklist

[Mail tester](https://www.mail-tester.com/)
<br />Check what your spam score is

[Senderscore](https://www.senderscore.org/)
<br />The reputation of sender scores

[NeverBounce](https://neverbounce.com/)
<br />Check the quality of an email address.
<div class="sources">
<h3>Sources</h3>
- litmus.com<br />
- campaignmonitor.com<br />
- sendgrid.com<br />
- returnpath.com<br />
- selligent.com<br />
</div>
