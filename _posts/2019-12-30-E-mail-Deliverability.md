---
layout: post
title: "Ultimate e-mail deliverability guide"
date: 2019-02-05
label: e-mail
tags: marketing, tips, e-mail, free
published: true
thumbnail: "images/blog/deliverability.jpg"
description: "Uren gewerkt aan de perfecte e-mail, maar hij komt niet aan? Check hier hoe dat komt en hoe je dit oplost. Krijg grip op email deliverability."
---

Email Deliverability is lastig. Echt echt heel lastig. Een e-mail gaat langs heel veel poortjes voordat deze eindelijk in de inbox van de ontvanger belandt. Gelukkig maar, want dit houdt heel wat spam tegen! 

Het is de verzameling factoren die bepalen of je e-mail in de inbox van je ontvanger terecht komt of niet.

Naast de <b>content</b> van je e-mail heb je ook nog de maken met <b>authenticatie</b> (DKIM, SPF, TLS, DMARC ) en reputatie (blacklists, aantal bounces, engagement).

Het is dus ook mogelijk dat een mailserver een succesvolle ‘handshake’ heeft met Selligent of een andere ESP waardoor je ESP rapportage een email als “sent successfully” markeert, maar de email uiteindelijk niet in de inbox van de klant terecht komt.

#### Reputatie
Een goede domein en zender reputatie is essentieel om ervoor te zorgen dat e-mails succesvol in de inbox belandt. Sites waar je reputatie getest kan worden:
1. <a href="https://returnpath.com/solutions/email-deliverability-optimization/deliverability/" target="_BLANK">Returnpath</a>
1. <a href="https://talosintelligence.com/" target="_BLANK"> Talos Intelligence</a>
1. <a href="http://www.reputationauthority.org/" target="_BLANK">Reputation Authority</a>

##### Spam Traps
Spam traps is een methode van Internet Service Providers (ISP's) om spammers te herkennen en te blokkeren

Een spamtrap is een fake e-mailadres met een valide syntax. Het emailadres is verder niet gekoppeld aan een persoon ofzo.

Zorg voor een goede ‘hygiëne’ van je data door gebruik te maken van een double optin. Ook is het verstandig om inactieve e mailadressen niet te benaderen. Je kan bijvoorbeeld een filter instellen die emailadressen die de laatste 6 maanden geen enkele email hebben geopend filteren.

Tools om spam traps te detecteren:
- [DeBounce](https://debounce.io)
- [zero bounce](https://www.zerobounce.net/)
- [proofy](https://proofy.io/)
- [Brite Verify](https://www.briteverify.com/) (Wordt door Clang gebruikt)

##### Blacklists
Een blacklist is database waarmee wordt bepaald welke e-mails als spam gemarkeerd moeten worden.
Je kan op basis van een domein of op IP-adres opgenomen worden op een blacklist. Hieronder een paar veel gebruikte blacklists:
- [Return Path Reputation Network Blacklist (RNBL)](http://www.returnpath.com/partner-content/reputation-network-blacklist/)
- [Sbl.spamhaus.org (SBL)](http://www.spamhaus.org/sbl/)
- [URIB](http://www.uribl.com/)

Met onderstaande link kan je checken of je op een blacklist voorkomt:
[MX Toolbox](https://mxtoolbox.com/domain/)

#### Bounces (Nope, geen bouncer :))
[Volgens Oracle](http://digitalmarketingdepot.com/whitepaper/new-school-marketers-guide-email-deliverability) zorgt een hoge hardbounce rate voor een trigger om je IP-adres te blacklisten. Zorg er met filters of slimme inleesprocessen voor dat je deze ‘deadweight’ verliest voordat je je e-mails gaat versturen. Bounces kan je verdelen in een hard en softbounce.

##### Hard bounce
Hier vallen bounces onder waarvan het e-mailadres ongeldig of niet meer in gebruik is. Het e-mailadres kan ook ongeldig zijn vanwege typefouten, bijvoorbeeld hotmal in plaats van hotmail of het ontbreken van een '@'.

##### Soft bounce
Een soft bounce is wat vager en vaak ook tijdelijk, denk bijvoorbeeld aan een mailbox dat vol is, de e-mailserver van de ontvanger niet bereikbaar is, etc..

Het opnieuw proberen van de bezorging van berichten na een tijdje kan werken. Als de fout echter vaker optreedt, is het verstandig om ‘m als hard bounce te markeren.

Sites om hard bounces te filteren:
- [https://www.zerobounce.net/](https://www.zerobounce.net/)
- [https://hunter.io/email-verifier](https://hunter.io/email-verifier)
- [https://www.briteverify.com/](https://www.briteverify.com/)

##### ‘Markeer als spam’ klachten
Wanneer de ontvangers van je e-mail op de ‘Markeeren als spam’-optie klikken, wordt er een klacht geregistreerd door de betreffende emailclient zoals Gmail of Outlook. zij sturen dit door naar de ESP. Het is daarom belangrijk om een toegankelijke en werkende afmeldproces te hebben, anders zal een gebruiker sneller van deze functie gebruik maken.

##### IP-reputatie
Spammers zijn sluw. Ze proberen SPAM-filters altijd te omzijlenn, bijvoorbeeld door nieuwe IP-adressen te gebruiken en te rouleren. Hierdoor is het belangrijk dat je een IP-adres opwarmt. Je kan niet van de één op andere dag op dagelijkse basis een miljoen e-mails versturen. Dit zal je in een periode langzaam moeten uitbouwen.

##### Subscriber Engagement
Veel emailclients zoals Gmail zoeken naar de engagement van je ontvangers en gebruiken dit steeds meer als èèn van de belangrijkste deliverability metrics.

Wanneer je ontvangers je e-mails openen of klikken, je e-mailadres toevoegen aan hun contacten of e-mails verplaatsen van promoties naar de primaire inbox, laat dit zien dat ze je e-mails waarderen.

#### Authenticatie
Het is natuurlijk makkelijk om je online voor te doen als iemand anders. Je kan heel makkelijk een e-mail versturen uit naam van een andere e-mailadres. Hierdoor is malware- en phishingaanval relatief makkelijk uit te voeren.

Gelukkig zijn er verschillende methodes zoals DKIM. SPF, TLS en DMARC die ervoor zorgen dat het niet meer zo makkelijk is. Die methodes zorgen er namelijk voor dat we de identiteit van de afzender van de e-mail kunnen authenticeren en te verifiëren.

##### DKIM
DomainKeys Identified Mail (DKIM) is een manier om ESP's te autoriseren e-mail voor je te verzenden. Met DKIM-verificatie kan een verzender de verantwoordelijkheid voor zijn e-mail opnemen en wordt het gebruikt om echte e-mail te scheiden van spam- en phishing-campagnes.

##### SPF
Met SPF kan een ontvangende mailserver controleren of een e-mail afkomstig is van een verzendend IP-adres dat is toegestaan om e-mails te verzenden uit naam van een bepaald domein. Wanneer je een SPF-record maakt, plaats je een lijst met IP's / verzendende hosts die gemachtigd zijn om e-mail namens jouw domein te verzenden.

Via deze [link](https://toolbox.googleapps.com/apps/checkmx) kan je SPF records controleren.

##### TLS
Transport Layer Security (TLS) is een protocol dat wordt gebruikt om informatie te versleutelen. TLS gebruikt certificaten om sessies te coderen om de vertrouwelijkheid van informatie te behouden. SendGrid gebruikt TLS om sessies met zijn toepassing via HTTPS en API te versleutelen. Gmail heeft TLS inmiddels in gebruik genomen. Het zal vast niet lang meer duren voordat ook de e-mailclients dit ook gaan doen.

##### DMARC
DMARC is een afkorting van "Domain-based Message Authentication, Reporting & Conformance", een nieuwe standaard die het voor ISP's eenvoudiger maakt om misbruik van e-mails te voorkomen. Het is een proces om te bepalen of een e-mail legitiem is.

#### Content
Wanneer een bericht wordt ontvangen door je provider, voert het eerst reputatie en authenticatie controles uit. Op basis daarvan kan een e-mailbericht worden toegestaan, gefilterd of geblokkeerd.

Als de e-mail bij het volgende poortje komt, start de antispamsoftware om een analyse uit te voeren op je content en besluit vervolgens om je e-mail als spam te markeren of af te leveren. Hieronder een aantal thema's over e-mail content.

##### Goede HTML
De meeste e-mails die via ESP's worden verzonden, zijn HTML-e-mails. Een kapotte HTML kan leiden tot een onleesbare e-mail. Zorg ervoor dat je HTML on point is.

##### Responsive HTML
Een onderwerp dat tegenwoordig eigenlijk voor iedereen wel commen sense is: Zorg ervoor dat je e-mails mooi weergeven op mobiele apparaten.

##### Gebruik geen short-url tools
URL-shorteners zijn superhandig om gemakkelijk een lange url te delen. Hierdoor wordt dit ook door spammers gebruikt. Het gebruik van short-url wordt steeds vaker door e-mailclients daarom als spam gemarkeerd.

##### From e-mailadres.
Wanneer je zowel transactionele als promotionele e-mails verstuurd dan is het raadzaam om hier aparte emailadressen voor te gebruiken.
Classificatie van e-mails waarop tabbladen (promoties, updates, sociale etc.) plaatsvinden op basis van e-mailinhoud en het e-mailadres van de afzender. Daarnaast zal een promotie e-mail sneller als spam gemarkeerd worden dan een transactionele email.

##### Segmentatie
Segmenteer je doelgroep op basis van interessegebieden zodat de juiste content bij de juiste persoon binnenkomt. Naast dat dit beter is voor converise, zorgt dit ook voor meer interactie in je e-mails. Vermijd ook inactieve aanmelders omdat zij ook een negatief effect hebben op je reputatie.

##### Gemakkelijk unsubscriben
UHet afmeldproces moet eenvoudig en duidelijk zijn. Het zou niet zo moeten zijn dat ze eerst verplicht een formulier moeten invullen om verolgens een week te moeten wachten voordat de afmelding is verwijderd.

##### From & Reply adressen
Het e-mailadres dat je gebruikt, moet wel ergens in een inbox komen. Gebruik dus geen no-reply emaldressen,
Als blijkt dat ze niet via e-mail kunnen reageren, zullen ze sneller de "markeer als spam"-optie gebruiken.

#### Andere methodes

##### Feedback loop
Wanneer een ontvanger heeft besloten om op dit e-mailadres op 'Dit is spam' te klikken, wordt dit beschouwd als een 'klacht'. Sommige providers maken dit voor de versturen inzichtelijk door een feedbackloop te maken. Feedbackloops, of FBL's, stellen afzenders in staat berichten te ontvangen van ontvangers die hebben geklaagd. De provider stuurt het bericht waarover wordt geklaagd door naar de afzender op een afgesproken e-mailadres, zodat de afzender deze gebruiker in zijn database kan kenmerken. 
[Meer info van Returhpath.com](https://blog.returnpath.com/what-is-a-feedback-loop/)

##### Suppression list
De suppressionlist is een speciale tabel en bevat alle e-mailadressen die je **altijd** wilt uitsluiten. E-mailadressen op de suppressionlist kunnen daardoor niet per ongeluk alsnog ingelezen en gemailed worden.

#### Tools
[MX Toolbox](https://mxtoolbox.com/dkim.aspx)
SPF, DKIM en blacklist controleren

[Mail-tester](https://www.mail-tester.com/)
Checken wat je spam-score is

[Senderscore](https://www.senderscore.org/)
Reputatie van afzenderscores

[NeverBounce](https://neverbounce.com/)
Kwaliteit van een e-mailadres controleren.

#### Sources
- litmus.com
- campaignmonitor.com
- sendgrid.com
- returnpath.com
- selligent.com