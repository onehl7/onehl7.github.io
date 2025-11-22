---
layout: post
title: "Space Updates"
date: 2025-11-22 13:00:00 +0000
categories: [space]
excerpt: "A dynamically updated list of recent space news from various sources."
---

Stay up-to-date with the latest breakthroughs and developments in the world of space exploration. This page is automatically updated daily with news from leading sources like NASA and ESA.

<div class="news-feed">
{% for item in site.data.space_news %}
  <article>
    <h3><a href="{{ item.link }}" target="_blank" rel="noopener">{{ item.title }}</a></h3>
    <p><em>Source: {{ item.source }} | Published: {{ item.published }}</em></p>
  </article>
  <hr>
{% endfor %}
</div>
