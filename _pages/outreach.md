---
title: "Outreach"
permalink: /outreach/
author_profile: true
redirect_from: 
  - /outreach.html
---

{% include base_path %}

My outreach and science communication activities.

{% for post in site.outreach reversed %}
  {% include archive-single.html type="grid" %}
{% endfor %}
