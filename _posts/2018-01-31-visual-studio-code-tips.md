---
layout: post
title: "Visual Studio Code tips"
date: 2018-01-31
category: learning
tags: webdevelopment, tips, visual studio code
published: true
thumbnail: "images/blog/vsc.gif"
description: "Visual Studio Code is mijn favoriete editor. "
---

Dit komt vooral door de vele extensies die worden aangeboden en de geïntegreerde koppeling met Git.

#### Koppeling met Git
Zoals hierboven al aangegeven heeft VSC een [ingebouwde source control](https://code.visualstudio.com/docs/introvideos/versioncontrol "Visual Studio code"). Deze wordt nog krachtiger in combinatie met de extensie *[Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory "Git History extension")*.

#### Command Palette
De belangrijkste toetsencombinatie is <kbd>⇧⌘P</kbd> of <kbd>Ctrl+Shift+P</kbd> voor Windows. Hiermee open je het Command Palette waarmee je toegang hebt tot alle beschikbaar functies. Zo kan je hiermee in een paar simpele stappen een repository clonen, een extra branche aanmaken of een file opzoeken.

![Open Command Palette](https://github.com/Microsoft/vscode-tips-and-tricks/raw/master/media/OpenCommandPalatte.gif "Open Command Palette")

#### Emmet
Emmet is een snippet toolkit waarmee je veel tijd bespaart in je HTML & CSS workflow door met afkortingen te werken.
Deze toolkit is ingebouwd in VSC waardoor dit nog makkelijker is te gebruiken.

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


#### Mijn geinstalleerde extensies
- [Beautify](https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify)
- [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory)
- [HTML Snippets](https://marketplace.visualstudio.com/items?itemName=abusaidm.html-snippets)
- [One Dark Pro theme](https://marketplace.visualstudio.com/items?itemName=zhuangtongfa.Material-theme)
- [Visual Studio team services](https://marketplace.visualstudio.com/items?itemName=ms-vsts.team)
- [vscode-icons](hhttps://marketplace.visualstudio.com/items?itemName=robertohuertasm.vscode-icons)

Bekijk [hier een aantal tips](https://github.com/Microsoft/vscode-tips-and-tricks) die Microsoft zelf aanbiedt!