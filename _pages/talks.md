---
layout: archive
title: "Talks and presentations"
permalink: /talks/
author_profile: true
---

Some of the talks and posters that I have presented over the years at various conferences and workshops.
All have links to download or view the slides.

The full list of my talks can be found in my [<i class="ai ai-cv-square ai-fw"></i>CV (.pdf)](/files/cv-sergeev-full.pdf).

{% for post in site.talks reversed %}
  {% include archive-single-talk.html %}
{% endfor %}
