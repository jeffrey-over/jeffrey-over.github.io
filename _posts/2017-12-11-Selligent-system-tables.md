---
layout: post
title: "Selligent backbone tables - use all the data you have at your disposal."
date: 2020-06-01
label: learning
tags: Selligent Marketing Cloud, Data
yearreview: false
published: true
thumbnail: "images/blog/sim-tables.jpg"
description: "There is a lot of information to be gained from the underlying system tables of Selligent Marketing Cloud. For example, you could further automate your workflow with triggers or use custom queries to generate reports. "
---

Fortunately, for me most of us, the days when hail is randomly shot are far behind us. Nowadays, the end customer receives so many emails that you no longer get away with generic information. This will quickly be perceived as negative, which will not benefit your brand. You must be of added value with your expressions. To achieve this, you must use all available data from the end customer to send the right message at the right time.

<img src="/images/blog/addvalueformula.png" alt="Added value = Right content * Right moment" class="" >


Therefore, use all the data you have at your disposal to get the best possible picture of your customers and their interests. The Selligent system tables can also be useful here.

### Examples
*Business intelligence / dashboarding sync*
By using aggregated data you can develop a process that links Selligent interaction data to business intelligence systems such as Tableau.

*Incident dashboard*
By linking to the correct system tables, it is possible to set up an incident monitoring dashboard. Classify the incidents to allow critical errors to surface and resolve even faster, before the customer is affected.

*Delivery failure*
Use a self-developed export to track which domains often cause delivery failures to avoid blacklisting and improve your email quality.

### Selligent system tables
| Table        | Description  | 
| ------------- |-------------| 
|*Flags*| Storage of all user interactions. |
|*Actionqueue*| This table serves as the queue for emails. Each record contains the definition for one email to be sent. |
|*Campaigns*| Table with all campaign definitions. |
|*Lists*| Table with information of all lists. |
|*Mails*| Table with information all emails / pages. |
|*Gates*| Table with gate definitions. Gates can be triggered with APIs.|
|*Probes*| Table containing custom reportable links. |
|*Incidents*| Table tracking all incidents with relevant information.|

This overview is a selection from the system tables. The Selligent backbone data model consists of more tables than those listed above. These tables form the heart of Selligent. So always be careful when approaching these tables! Create processes that do not affect the performance of the system.