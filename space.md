---
layout: home
title: "Space"
category: space
---

{% assign topic = site.topics | where: "slug", page.category | first %}

<!-- Hero Section -->
<div class="relative h-64 bg-cover bg-center" style="background-image: url('{{ topic.image_url | relative_url }}');">
  <div class="absolute inset-0 bg-black/60"></div>
  <div class="relative max-w-4xl mx-auto px-4 h-full flex items-center justify-center">
    <h1 class="text-5xl font-bold text-white text-center">{{ topic.emoji }} {{ topic.name }}</h1>
  </div>
</div>

<!-- Post Listing -->
<section class="max-w-4xl mx-auto my-12 px-4">
  <ul class="list-none p-0 m-0">
    {% for post in site.categories[page.category] %}
    <li class="border-l-4 border-violet-600 p-4 mb-3 bg-slate-800/20 rounded-r-md hover:bg-slate-800/40 transition-colors">
      <a href="{{ post.url | relative_url }}" class="font-semibold text-lg text-slate-200 no-underline hover:text-violet-400">{{ post.title }}</a>
      <div class="text-sm text-slate-400 mt-1">{{ post.date | date: "%b %d, %Y" }}</div>
      <p class="mt-2 mb-0 text-slate-300">{{ post.excerpt | strip_html | truncate: 160 }}</p>
    </li>
    {% endfor %}
  </ul>
</section>

<!-- Latest Space News -->
<section class="max-w-4xl mx-auto my-12 px-4">
  <h2 class="text-2xl mb-2">Latest Space News</h2>
  <ul class="list-none p-0 m-0">
    {% for item in site.data.space_news %}
    <li class="border-l-4 border-violet-600 p-4 mb-3 bg-slate-800/20 rounded-r-md hover:bg-slate-800/40 transition-colors">
      <a href="{{ item.link }}" class="font-semibold text-lg text-slate-200 no-underline hover:text-violet-400" target="_blank" rel="noopener noreferrer">{{ item.title }}</a>
      <div class="text-sm text-slate-400 mt-1">{{ item.published | date: "%b %d, %Y" }} - {{ item.source }}</div>
    </li>
    {% endfor %}
  </ul>
</section>