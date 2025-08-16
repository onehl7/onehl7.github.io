---
layout: home
title: "Technology"
category: technology
---

## 💻 Technology Posts

{% for post in site.categories.technology %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}