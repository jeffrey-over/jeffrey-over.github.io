---
layout: post
title: "Visual Studio Code - Best practices"
date: 2018-01-31
label: learning
permalink: /vscode-tips
tags: webdevelopment, tips, visual studio code
yearreview: false
published: true
thumbnail: "images/blog/vsc.gif"
description: "There are many good editors. Choosing an editor that suits you can be quite tricky. I really like VS Code! It works easily and is free, open-source, and available on both OS X and Windows."
---

### GIT integration
VS Code has a *[built-in source control](https://code.visualstudio.com/docs/introvideos/versioncontrol "Visual Studio code")*. It offers simple actions such as switching branches or comparing changes.
With the extension *[Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory "Git History extension")* the integration becomes even more powerful and you can easily view the log, history or branches and compare commits.

<img src="https://github.com/Microsoft/vscode-tips-and-tricks/raw/master/media/OpenCommandPalatte.gif" class="fullscreen" alt="Open Command Palette">

### Command Palette
The most important key combination you should know is <kbd> ⇧ + ⌘ + P </kbd> or <kbd> Ctrl + Shift + P </kbd> for Windows. This will open the Command Palette that gives you access to all available functions. This way you can clone a repository, create an extra branch or search for a file in a few simple steps.


### Emmet
Emmet is a snippet tool that saves a lot of time in your HTML & CSS workflow by working with abbreviations. This tool is integrated into VS Code, making it super tasty!

### Example Emmet input:
<pre><code>   div&gt;ul&gt;li
</code></pre>

### Output result
<pre><code class="language-html" data-lang="html">&lt;div&gt;
    &lt;ul&gt;
        &lt;li&gt;&lt;/li&gt;
    &lt;/ul&gt;
&lt;/div&gt;</code></pre>


### Emmet snippet:
<pre><code>&lt;!</code></pre>

### Output result
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

### IntelliSense (auto complete)
IntelliSense goes beyond syntax highlighting. It automates the completion of a syntax!
<blockquote>
Go beyond syntax highlighting and autocomplete with IntelliSense, which provides smart completions based on variable types, function definitions, and imported modules.
<a href="https://www.microsoft.com" target="_BLANK">- Microsoft</a>
</blockquote>

### Extensions
Extensions are additional features or themes that can be downloaded from the marketplace. Here are some cool extensions that I use.
<dl>
   
<dt> <a href="https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-close-tag" target="_BLANK"> Auto close tag </a> </dt>
   
<dd> Automatically add an HTML / XML close tag, the same as Visual Studio IDE or Sublime Text</dd>
   
<dt> <a href="https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag" target="_BLANK"> Auto rename tag </a> </dt>
   
<dd> Automatically renames paired HTML / XML tags</dd>
   
<dt> <a href="https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify" target="_BLANK"> Beautify </a> </dt>
   
<dd> Beautifies code in Visual Studio Code</dd>
   
<dt> <a href="https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory" target="_BLANK"> Git History </a> </dt>
   
<dd> View git log,
   file history, compare branches or commits
</dd>
   
<dt> <a href="https://marketplace.visualstudio.com/items?itemName=zhuangtongfa.Material-theme" target="_BLANK"> One Dark Pro theme </a> </dt>
   
<dd> Atom's iconic One Dark theme for Visual Studio Code</dd>
  
<dt> <a href="https://marketplace.visualstudio.com/items?itemName=robertohuertasm.vcode-icons" target="_BLANK"> vcode icons </a> </dt>
   
<dd> Icons for Visual Studio Code</dd>

</dl>

 
Be sure to check the [tips](https://github.com/Microsoft/vcode-tips-and-tricks) that Microsoft itself offers!