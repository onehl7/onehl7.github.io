---
layout: home
title: "Home"
---

<main class="home-shell">
  <section class="home-topics motion-in" aria-labelledby="topics-heading">
    <div class="section-heading">
      <p class="eyebrow">Browse by interest</p>
      <h2 id="topics-heading">Explore the topics</h2>
      <p class="home-tagline">Exploring technology, space, and quantum frontiers.</p>
    </div>
    <div class="topic-card-grid">
      {% for topic in site.topics %}
      <a href="{{ '/' | append: topic.slug | append: '.html' | relative_url }}" class="topic-card">
        <span class="topic-card-image">
          <img src="{{ topic.image_url | relative_url }}" alt="" loading="lazy">
        </span>
        <span class="topic-card-title">{{ topic.name }}</span>
      </a>
      {% endfor %}
    </div>
  </section>

  {% assign featured_post = site.posts | first %}
  {% if featured_post %}
  <section class="home-feature motion-in" aria-labelledby="featured-heading">
    <div class="section-heading">
      <p class="eyebrow">Start exploring</p>
      <h2 id="featured-heading">Featured article</h2>
    </div>
    <article class="featured-post">
      {% if featured_post.image %}
      <a class="featured-image-link" href="{{ featured_post.url | relative_url }}" tabindex="-1" aria-hidden="true">
        <img src="{{ featured_post.image | relative_url }}" alt="" class="featured-image">
      </a>
      {% endif %}
      <div class="featured-copy">
        <p class="post-meta">{{ featured_post.date | date: "%b %d, %Y" }}{% if featured_post.categories.size > 0 %} · {{ featured_post.categories | join: ", " }}{% endif %}</p>
        <h3><a href="{{ featured_post.url | relative_url }}">{{ featured_post.title }}</a></h3>
        <p>{{ featured_post.excerpt | strip_html | truncate: 220 }}</p>
        <a class="text-link" href="{{ featured_post.url | relative_url }}">Read the article <span aria-hidden="true">→</span></a>
      </div>
    </article>
  </section>
  {% endif %}

  <section class="home-latest motion-in" aria-labelledby="latest-heading">
    <div class="section-heading">
      <p class="eyebrow">Keep reading</p>
      <h2 id="latest-heading">Latest posts</h2>
    </div>
    <ul class="post-list">
      {% for post in site.posts offset:1 limit:5 %}
      <li class="post-list-item">
        <div>
          <p class="post-meta">{{ post.date | date: "%b %d, %Y" }}{% if post.categories.size > 0 %} · {{ post.categories | join: ", " }}{% endif %}</p>
          <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
          <p>{{ post.excerpt | strip_html | truncate: 180 }}</p>
        </div>
        <a class="post-list-arrow" href="{{ post.url | relative_url }}" aria-label="Read {{ post.title }}">→</a>
      </li>
      {% endfor %}
    </ul>
  </section>
</main>
