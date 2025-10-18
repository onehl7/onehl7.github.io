---
layout: home
title: "Home"
---

<div class="text-center py-12 px-4">
  <h1 class="text-5xl font-bold mb-1">A Curious Mind</h1>
  <p class="mx-auto mb-4 max-w-3xl text-slate-400">
    Exploring technology, science, and the cosmos — thoughts, tutorials and interactive dashboards.
  </p>

  <div class="mt-4 space-x-4">
    <a href="{{ '/quantum.html' | relative_url }}" class="inline-block m-1 px-4 py-2 bg-blue-600 text-white rounded-md no-underline hover:bg-blue-700 transition-colors">Quantum</a>
    <a href="{{ '/technology.html' | relative_url }}" class="inline-block m-1 px-4 py-2 bg-teal-500 text-white rounded-md no-underline hover:bg-teal-600 transition-colors">Technology</a>
    <a href="{{ '/space.html' | relative_url }}" class="inline-block m-1 px-4 py-2 bg-violet-600 text-white rounded-md no-underline hover:bg-violet-700 transition-colors">Space</a>
  </div>
</div>

<!-- Topic cards -->
<div class="flex gap-4 justify-center flex-wrap px-4 pb-8">
  <a href="{{ '/space.html' | relative_url }}" class="w-full sm:w-72 no-underline text-inherit">
    <div class="rounded-lg overflow-hidden shadow-lg bg-slate-900 hover:scale-105 transition-transform duration-300">
      <img src="https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1200&q=60&auto=format&fit=crop" alt="Space" class="w-full h-36 object-cover">
      <div class="p-3">
        <h3 class="mb-1 text-lg text-slate-200">Space</h3>
        <p class="m-0 text-sm text-slate-400">Launches, exploration and the cosmos.</p>
      </div>
    </div>
  </a>

  <a href="{{ '/technology.html' | relative_url }}" class="w-full sm:w-72 no-underline text-inherit">
    <div class="rounded-lg overflow-hidden shadow-lg bg-slate-900 hover:scale-105 transition-transform duration-300">
      <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&q=60&auto-format&fit=crop" alt="Technology" class="w-full h-36 object-cover">
      <div class="p-3">
        <h3 class="mb-1 text-lg text-slate-200">Technology</h3>
        <p class="m-0 text-sm text-slate-400">Tools, systems and trends.</p>
      </div>
    </div>
  </a>

  <a href="{{ '/quantum.html' | relative_url }}" class="w-full sm:w-72 no-underline text-inherit">
    <div class="rounded-lg overflow-hidden shadow-lg bg-slate-900 hover:scale-105 transition-transform duration-300">
      <img src="https://images.unsplash.com/photo-1555949963-aa79dcee981d?w=1200&q=60&auto=format&fit=crop" alt="Quantum" class="w-full h-36 object-cover">
      <div class="p-3">
        <h3 class="mb-1 text-lg text-slate-200">Quantum</h3>
        <p class="m-0 text-sm text-slate-400">Quantum computing, sensing and theory.</p>
      </div>
    </div>
  </a>
</div>

<!-- Latest posts -->
<section class="max-w-4xl mx-auto mb-12 px-4">
  <h2 class="text-2xl mb-2">Latest posts</h2>

  <ul class="list-none p-0 m-0">
    {% for post in site.posts limit:5 %}
    <li class="border-l-4 border-blue-700 p-4 mb-3 bg-slate-800/20 rounded-r-md hover:bg-slate-800/40 transition-colors">
      <a href="{{ post.url | relative_url }}" class="font-semibold text-lg text-slate-200 no-underline hover:text-blue-400">{{ post.title }}</a>
      <div class="text-sm text-slate-400 mt-1">
        {{ post.date | date: "%b %d, %Y" }} •
        {% for c in post.categories %}{{ c }}{% unless forloop.last %}, {% endunless %}{% endfor %}
      </div>
      <p class="mt-2 mb-0 text-slate-300">{{ post.excerpt | strip_html | truncate: 160 }}</p>
    </li>
    {% endfor %}
  </ul>
</section>
