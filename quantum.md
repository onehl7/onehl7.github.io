---
layout: home
title: "Quantum"
category: quantum
---

<!-- Hero Section -->
<div class="relative h-64 bg-cover bg-center" style="background-image: url('https://images.unsplash.com/photo-1555949963-aa79dcee981d?w=1200&q=60&auto-format&fit=crop');">
  <div class="absolute inset-0 bg-black/60"></div>
  <div class="relative max-w-4xl mx-auto px-4 h-full flex items-center justify-center">
    <h1 class="text-5xl font-bold text-white text-center">🧬 Quantum</h1>
  </div>
</div>

<!-- Post Listing -->
<section class="max-w-4xl mx-auto my-12 px-4">
  <ul class="list-none p-0 m-0">
    {% for post in site.categories.quantum %}
    <li class="border-l-4 border-blue-700 p-4 mb-3 bg-slate-800/20 rounded-r-md hover:bg-slate-800/40 transition-colors">
      <a href="{{ post.url | relative_url }}" class="font-semibold text-lg text-slate-200 no-underline hover:text-blue-400">{{ post.title }}</a>
      <div class="text-sm text-slate-400 mt-1">{{ post.date | date: "%b %d, %Y" }}</div>
      <p class="mt-2 mb-0 text-slate-300">{{ post.excerpt | strip_html | truncate: 160 }}</p>
    </li>
    {% endfor %}
  </ul>
</section>