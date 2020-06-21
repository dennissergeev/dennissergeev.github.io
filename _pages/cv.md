---
layout: archive
title: "Curricilum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<a href="/files/cv-sergeev-full.pdf"><i class="ai ai-cv-square ai-fw"></i>Download my full CV in PDF</a>

## Education
* PhD in Meteorology, 2018
  - Location: University of East Anglia, Norwich, UK
  - Thesis title: "Characteristics of polar lows in the Nordic Seas and the impact of orography and sea ice on their development"
  - Supervisors:
     - Prof. Ian A. Renfrew
     - Prof. Thomas Spengler
     - Prof. Stephen Dorling
  - Download a copy: [UEA repository](https://ueaeprints.uea.ac.uk/68204/)
* Specialist Diploma in Meteorology (With Honours) 2014
  - Location: Lomonosov Moscow State University, Moscow, Russia
  - Thesis title: "Idealised numerical modelling of polar mesocyclone dynamics"
  - Supervisor: Dr. Victor M. Stepanenko
  - Download a copy (in Russian): [10.6084/m9.figshare.5326846.v1](https://doi.org/10.6084/m9.figshare.5326846.v1)

## Lead-author publications
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
## Selected talks
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
## Teaching
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

## Outreach
  <ul>{% for post in site.outreach reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

## Software
  <ul>{% for post in site.software reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
