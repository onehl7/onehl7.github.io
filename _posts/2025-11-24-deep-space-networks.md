---
layout: post
title: "Deep Space Networks"
date: 2025-11-24 10:00:00 +0000
categories: [space]
excerpt: "An overview of NASA's Deep Space Network and the latest news on deep space exploration."
---

Explore NASA's Deep Space Network (DSN), the international network of antennas that supports interplanetary spacecraft missions, plus radio and radar astronomy observations for the exploration of the solar system and the universe.

<div class="dsn-container" style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://eyes.nasa.gov/apps/dsn-now/dsn.html" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div>

## Latest Deep Space News

This section is automatically updated with the latest news related to deep space exploration.

<div class="news-feed">
{% for item in site.data.deep_space_news %}
  <article>
    <h3><a href="{{ item.link }}" target="_blank" rel="noopener">{{ item.title }}</a></h3>
    <p><em>Source: {{ item.source }} | Published: {{ item.published }}</em></p>
  </article>
  <hr>
{% endfor %}
</div>
