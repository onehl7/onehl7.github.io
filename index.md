---
layout: home
title: "Home"
---

<div class="text-center py-12 px-4">
  <h1 class="text-5xl font-bold mb-1">A Curious Mind</h1>
  <p class="mx-auto mb-4 max-w-3xl text-muted">
    Exploring Technology, Space, and Quantum Frontiers -Views, Learnings, and Findings
  </p>

  <div class="mt-4 space-x-4">
    {% for topic in site.topics %}
      <a href="{{ '/' | append: topic.slug | append: '.html' | relative_url }}" class="btn-topic">{{ topic.name }}</a>
    {% endfor %}
  </div>
</div>

<!-- Topic cards -->
<div class="flex gap-4 justify-center flex-wrap px-4 pb-8">
  {% for topic in site.topics %}
  <a href="{{ '/' | append: topic.slug | append: '.html' | relative_url }}" class="w-full sm:w-72 no-underline text-inherit">
    <div class="rounded-lg overflow-hidden shadow-lg card hover:scale-105 transition-transform duration-300">
      <img src="{{ topic.image_url | relative_url }}" alt="{{ topic.name }}" class="w-full h-36 object-cover">
      <div class="p-3">
        <h3 class="mb-1 text-lg card-heading">{{ topic.name }}</h3>
      </div>
    </div>
  </a>
  {% endfor %}
</div>

<!-- Latest posts -->
<section class="max-w-4xl mx-auto mb-12 px-4">
  <h2 class="text-2xl mb-2">Latest posts</h2>

  <ul class="list-none p-0 m-0">
    {% for post in site.posts limit:5 %}
    <li class="border-l-4 border-blue-700 p-4 mb-3 rounded-r-md transition-colors topic-item">
      <a href="{{ post.url | relative_url }}" class="font-semibold text-lg text-primary no-underline hover:text-blue-400">{{ post.title }}</a>
      <div class="text-sm text-muted mt-1">
        {{ post.date | date: "%b %d, %Y" }} •
        {% for c in post.categories %}{{ c }}{% unless forloop.last %}, {% endunless %}{% endfor %}
      </div>
      <p class="mt-2 mb-0 text-muted">{{ post.excerpt | strip_html | truncate: 160 }}</p>
    </li>
    {% endfor %}
  </ul>
</section>
