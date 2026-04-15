---
layout: home
title: "AI"
category: ai
---

{% assign topic = site.topics | where: "slug", page.category | first %}

<!-- Hero Section -->
<div class="topic-hero relative h-64 bg-cover bg-center" style="background-image: url('{{ topic.image_url | relative_url }}');">
  <div class="absolute inset-0 bg-black/30"></div>
  <div class="relative max-w-4xl mx-auto px-4 h-full flex items-center justify-center">
    <h1 class="text-5xl font-bold hero-title text-center">{{ topic.emoji }} {{ topic.name }}</h1>
  </div>
</div>

<!-- Post Listing -->
<section class="max-w-4xl mx-auto my-12 px-4">
  <ul class="list-none p-0 m-0">
    {% for post in site.categories[page.category] %}
    <li class="border-l-4 border-purple-500 p-4 mb-3 rounded-r-md transition-colors topic-item">
      <a href="{{ post.url | relative_url }}" class="font-semibold text-lg text-primary no-underline hover:text-purple-400">{{ post.title }}</a>
      <div class="text-sm text-muted mt-1">{{ post.date | date: "%b %d, %Y" }}</div>
      <p class="mt-2 mb-0 text-muted">{{ post.excerpt | strip_html | truncate: 160 }}</p>
    </li>
    {% endfor %}
  </ul>
</section>