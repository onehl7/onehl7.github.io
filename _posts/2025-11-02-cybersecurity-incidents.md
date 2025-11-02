---
layout: post
title: "Cybersecurity Incidents"
date: 2025-11-02 12:00:00 +0000
categories: [technology]
excerpt: "A dynamically updated list of recent cybersecurity incidents from various sources."
---

This page provides a list of recent cybersecurity incidents, automatically updated every hour from the following sources: The Hacker News and Bleeping Computer.

<div class="news-feed">
{% for item in site.data.news %}
  <article>
    <h3><a href="{{ item.link }}" target="_blank" rel="noopener">{{ item.title }}</a></h3>
    <p><em>Source: {{ item.source }} | Published: {{ item.published }}</em></p>
  </article>
  <hr>
{% endfor %}
</div>
