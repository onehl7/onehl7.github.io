---
layout: home
title: "Home"
---

<div style="text-align:center; padding:3rem 1rem;">
  <h1 style="font-size:3.2rem; margin:0 0 .25rem;">A Curious Mind</h1>
  <p style="margin:0 auto 1rem; max-width:740px; color:#9fb0d6;">
    Exploring technology, science, and the cosmos — thoughts, tutorials and interactive dashboards.
  </p>

  <div style="margin-top:1rem;">
    <a href="{{ '/quantum.html' | relative_url }}" style="display:inline-block; margin:.25rem .5rem; padding:.6rem 1rem; background:#2563eb; color:#fff; border-radius:6px; text-decoration:none;">Quantum</a>
    <a href="{{ '/technology.html' | relative_url }}" style="display:inline-block; margin:.25rem .5rem; padding:.6rem 1rem; background:#0ea5a4; color:#fff; border-radius:6px; text-decoration:none;">Technology</a>
    <a href="{{ '/space.html' | relative_url }}" style="display:inline-block; margin:.25rem .5rem; padding:.6rem 1rem; background:#7c3aed; color:#fff; border-radius:6px; text-decoration:none;">Space</a>
  </div>
</div>

<!-- Topic cards -->
<div style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap; padding:0 1rem 2rem;">
  <a href="{{ '/space.html' | relative_url }}" style="width:300px; text-decoration:none; color:inherit;">
    <div style="border-radius:10px; overflow:hidden; box-shadow:0 6px 18px rgba(2,6,23,.35);">
      <img src="https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1200&q=60&auto=format&fit=crop" alt="Space" style="width:100%; height:140px; object-fit:cover;">
      <div style="padding:12px; background:#071025;">
        <h3 style="margin:0 0 .25rem; font-size:1.1rem; color:#e6eef8;">Space</h3>
        <p style="margin:0; font-size:.9rem; color:#9fb0d6;">Launches, exploration and the cosmos.</p>
      </div>
    </div>
  </a>

  <a href="{{ '/technology.html' | relative_url }}" style="width:300px; text-decoration:none; color:inherit;">
    <div style="border-radius:10px; overflow:hidden; box-shadow:0 6px 18px rgba(2,6,23,.35);">
      <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&q=60&auto=format&fit=crop" alt="Technology" style="width:100%; height:140px; object-fit:cover;">
      <div style="padding:12px; background:#071025;">
        <h3 style="margin:0 0 .25rem; font-size:1.1rem; color:#e6eef8;">Technology</h3>
        <p style="margin:0; font-size:.9rem; color:#9fb0d6;">Tools, systems and trends.</p>
      </div>
    </div>
  </a>

  <a href="{{ '/quantum.html' | relative_url }}" style="width:300px; text-decoration:none; color:inherit;">
    <div style="border-radius:10px; overflow:hidden; box-shadow:0 6px 18px rgba(2,6,23,.35);">
      <img src="https://images.unsplash.com/photo-1555949963-aa79dcee981d?w=1200&q=60&auto=format&fit=crop" alt="Quantum" style="width:100%; height:140px; object-fit:cover;">
      <div style="padding:12px; background:#071025;">
        <h3 style="margin:0 0 .25rem; font-size:1.1rem; color:#e6eef8;">Quantum</h3>
        <p style="margin:0; font-size:.9rem; color:#9fb0d6;">Quantum computing, sensing and theory.</p>
      </div>
    </div>
  </a>
</div>

<!-- Latest posts -->
<section style="max-width:900px; margin:0 auto 3rem; padding:0 1rem;">
  <h2 style="font-size:1.4rem; margin-bottom:.5rem;">Latest posts</h2>

  <ul style="list-style:none; padding:0; margin:0;">
    {% for post in site.posts limit:5 %}
    <li style="border-left:3px solid #2b6cb0; padding:12px 16px; margin-bottom:12px; background:linear-gradient(180deg, rgba(7,16,37,0.02), transparent); border-radius:6px;">
      <a href="{{ post.url | relative_url }}" style="font-weight:600; font-size:1.05rem; color:#e6eef8; text-decoration:none;">{{ post.title }}</a>
      <div style="font-size:.85rem; color:#9fb0d6; margin-top:4px;">
        {{ post.date | date: "%b %d, %Y" }} •
        {% for c in post.categories %}{{ c }}{% unless forloop.last %}, {% endunless %}{% endfor %}
      </div>
      <p style="margin:.5rem 0 0; color:#b7c7e2;">{{ post.excerpt | strip_html | truncate: 160 }}</p>
    </li>
    {% endfor %}
  </ul>
</section>

<!-- Footer CTA -->
<div style="text-align:center; padding-bottom:3rem;">
  <p style="color:#9fb0d6;">Subscribe for updates (you can add a form or link here)</p>
</div>


