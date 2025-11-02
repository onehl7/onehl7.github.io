---
layout: post
title: "Quantum Updates"
date: 2025-11-02 13:00:00 +0000
categories: [quantum]
excerpt: "A dynamically updated list of recent quantum computing news from various sources."
---

Stay up-to-date with the latest breakthroughs and developments in the world of quantum computing. This page is automatically updated daily with news from leading sources like ScienceDaily and The Quantum Insider.

<div class="news-feed">
{% for item in site.data.quantum_news %}
  <article>
    <h3><a href="{{ item.link }}" target="_blank" rel="noopener">{{ item.title }}</a></h3>
    <p><em>Source: {{ item.source }} | Published: {{ item.published }}</em></p>
  </article>
  <hr>
{% endfor %}
</div>
