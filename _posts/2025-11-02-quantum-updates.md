---
layout: post
title: "Quantum Updates"
date: 2025-11-02 13:00:00 +0000
categories: [quantum]
excerpt: "A dynamically updated list of recent quantum computing news from various sources."
---

This page provides a list of recent quantum computing news, automatically updated daily from the following sources: Quantum Computing Report, ScienceDaily, MIT News, and The Quantum Insider.

<div class="news-feed">
{% for item in site.data.quantum_news %}
  <article>
    <h3><a href="{{ item.link }}" target="_blank" rel="noopener">{{ item.title }}</a></h3>
    <p><em>Source: {{ item.source }} | Published: {{ item.published }}</em></p>
  </article>
  <hr>
{% endfor %}
</div>
