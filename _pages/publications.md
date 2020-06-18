---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

Here only my first-author publications are listed.
{% if site.author.googlescholar %}
The full list of my publications is available on 
<a href="{{ site.author.googlescholar }}"><i class="ai ai-google-scholar ai-fw"></i>Google Scholar</a>.
{% endif %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
