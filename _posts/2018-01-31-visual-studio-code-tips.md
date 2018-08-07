---
layout: post
title: "Visual Studio Code - Tips and Tricks"
date: 2018-01-31
label: learning
tags: webdevelopment, tips, visual studio code
published: true
thumbnail: "images/blog/vsc.gif"
description: "Er zijn veel goede editors. Het kiezen van een editor die bij jou past kan daarom best lastig zijn. Zelf vind ik VS Code écht nice! Het werkt gemakkelijk en is gratis, open-source en zowel op OS X als op Windows beschikbaar."
---

#### GIT integratie
VS Code heeft een *[ingebouwde source control](https://code.visualstudio.com/docs/introvideos/versioncontrol "Visual Studio code")*. Het biedt simpele acties zoals het wisselen van branches of het vergelijken van de wijzigingen.
Met de extensie *[Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory "Git History extension")* wordt de integratie nog krachtiger en kan je eenvoudig de log, geschiedenis bekijken of branches en commits vergelijken.


![Open Command Palette](https://github.com/Microsoft/vscode-tips-and-tricks/raw/master/media/OpenCommandPalatte.gif "Open Command Palette")


#### Command Palette
De belangrijkste toetsencombinatie is <kbd>⇧⌘P</kbd> of <kbd>Ctrl+Shift+P</kbd> voor Windows. Hiermee open je het Command Palette waarmee je toegang hebt tot alle beschikbaar functies. Zo kan je hiermee in een paar simpele stappen een repository clonen, een extra branche aanmaken of een file opzoeken.


#### Emmet
Emmet is een snippet toolt waarmee je veel tijd bespaart in je HTML & CSS workflow door met afkortingen te werken. Deze tool is geïntegreerd in VS Code waardoor dit superlekker werkt!

#### Voorbeeld Emmet syntax:
<pre><code class="language-html" data-lang="html">div>ul>li</code></pre>

###### Resultaat

<pre><code class="language-html" data-lang="html">&lt;div&gt;
    &lt;ul&gt;
        &lt;li&gt;&lt;/li&gt;
    &lt;/ul&gt;
&lt;/div&gt;</code></pre>



#### Voorbeeld Emmet snippet:

<pre><code class="language-html" data-lang="html">&lt;!</code></pre>


###### Resultaat

<pre><code class="language-html" data-lang="html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;meta http-equiv=&quot;X-UA-Compatible&quot; content=&quot;ie=edge&quot;&gt;
    &lt;title&gt;Document&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;   
&lt;/body&gt;
&lt;/html&gt;</code></pre>

#### IntelliSense (auto complete)
IntelliSense gaat verder dan syntax markering. Het automatiseert het afronden van een syntax!

<blockquote>
Go beyond syntax highlighting and autocomplete with IntelliSense, which provides smart completions based on variable types, function definitions, and imported modules.
<a href="https://www.microsoft.com" target="_BLANK">- Microsoft</a>
</blockquote>




#### Extensies
Extensies zijn extra functies of thema’s die gedownload kunnen worden in de marketplace. Hierbij een aantal vette extensies die ik gebruik.
<dl>
   <dt><a href="https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-close-tag" target="_BLANK">Auto close tag</a></dt>
   <dd>Voeg automatisch een HTML / XML-close-tag toe, hetzelfde als Visual Studio IDE of Sublime Text
</dd>


   <dt><a href="https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag" target="_BLANK">Auto rename tag</a></dt>
   <dd>Hernoemt automatisch gepaarde HTML / XML-tags
</dd>


   <dt><a href="https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify" target="_BLANK">Beautify</a></dt>
   <dd>Verfraait code in Visual Studio Code 
</dd>


   <dt><a href="https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory" target="_BLANK">Git History</a></dt>
   <dd>Bekijk git log,
bestandsgeschiedenis, vergelijk branches of commits
</dd>

   <dt><a href="https://marketplace.visualstudio.com/items?itemName=zhuangtongfa.Material-theme" target="_BLANK">One Dark Pro theme</a></dt>
   <dd>Atom's iconic One Dark thema voor Visual Studio Code
</dd>



  <dt><a href="https://marketplace.visualstudio.com/items?itemName=robertohuertasm.vscode-icons" target="_BLANK">vscode-icons</a></dt>
   <dd>Icons voor Visual Studio Code
</dd>


</dl>

 

Bekijk zeker ook de [tips](https://github.com/Microsoft/vscode-tips-and-tricks) die Microsoft zelf aanbiedt!


