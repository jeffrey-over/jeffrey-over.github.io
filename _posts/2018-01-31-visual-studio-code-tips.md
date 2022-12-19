---
layout: post
author: Jeffrey Overmeer
title: "Visual Studio Code - Best practices"
date: 2018-01-31
label: development
permalink: /vscode-tips
tags: <span>webdevelopment</span> <span>visual studio code</span>
yearreview: false
published: true
thumbnail: "/images/blog/vsc.gif"
description: "There are many good text editors to choose from, and it can be tough to decide which one is right for you. Personally, I really like VS Code! It's easy to use, free, open-source, and available on both MacOS and Windows."
---

### GIT integration
VS Code has *[built-in source control](https://code.visualstudio.com/docs/introvideos/versioncontrol "Visual Studio code")*, which makes it easy to switch branches or compare changes. With the *[Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory "Git History extension") extension, the integration becomes even more powerful, allowing you to view the log, history, branches, and compare commits.

<img src="https://github.com/Microsoft/vscode-tips-and-tricks/raw/master/media/OpenCommandPalatte.gif" class="fullscreen" alt="Open Command Palette">

### Command Palette
The most important key combination to know is <kbd> ⇧ + ⌘ + P </kbd> (or <kbd> Ctrl + Shift + P </kbd> on Windows). This will open the Command Palette, which gives you access to all available functions. You can use it to clone a repository, create a new branch, or search for a file in just a few simple steps.




### Emmet
Emmet is a snippet tool that saves a lot of time in your HTML & CSS workflow by working with abbreviations. This tool is integrated into VS Code, making it super convenient!

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
IntelliSense is a feature that goes beyond just syntax highlighting. It helps automate the completion of syntax by providing smart suggestions based on variable types, function definitions, and imported modules.
<blockquote>
Go beyond syntax highlighting and autocomplete with IntelliSense, which provides smart completions based on variable types, function definitions, and imported modules.
<a href="https://www.microsoft.com" target="_BLANK">- Microsoft</a>
</blockquote>

### Extensions
EExtensions are additional features or themes that can be downloaded from the marketplace. Here are some of the extensions I use and recommend:
<dl>
<dt> <a href="https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-close-tag" target="_BLANK"> Auto close tag </a> </dt>
<dd> This extension automatically adds an HTML / XML close tag, similar to the functionality in Visual Studio IDE or Sublime Text</dd>
<dt> <a href="https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag" target="_BLANK"> Auto rename tag </a> </dt>
<dd> This extension automatically renames paired HTML / XML tags</dd>
<dt> <a href="https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify" target="_BLANK"> Beautify </a> </dt>
<dd> This extension beautifies code in Visual Studio Code</dd>
<dt> <a href="https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory" target="_BLANK"> Git History </a> </dt>
<dd> This extension allows you to view the git log, file history, compare branches or commits
</dd>

   
<dt> <a href="https://marketplace.visualstudio.com/items?itemName=zhuangtongfa.Material-theme" target="_BLANK"> One Dark Pro theme </a> </dt>
   
<dd> One Dark Pro theme is a Visual Studio Code extension that brings the iconic Atom One Dark theme to Visual Studio Code</dd>
  
<dt> <a href="https://marketplace.visualstudio.com/items?itemName=robertohuertasm.vcode-icons" target="_BLANK"> vcode icons </a> </dt>
   
<dd> Icons for Visual Studio Code</dd>

</dl>

 
Be sure to check the [tips](https://github.com/Microsoft/vcode-tips-and-tricks) that Microsoft itself offers for additional information and resources.