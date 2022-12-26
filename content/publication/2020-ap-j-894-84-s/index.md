---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Atmospheric Convection Plays a Key Role in the Climate of Tidally Locked Terrestrial
  Exoplanets: Insights from High-resolution Simulations'
subtitle: ''
summary: ''
authors:
- admin
- F. Hugo Lambert
- Nathan J. Mayne
- Ian A. Boutle
- James Manners
- Krisztian Kohary
tags:
- Exoplanet atmospheres
- Planetary atmospheres
- Habitable planets
- Habitable zone
- Water vapor
- Atmospheric circulation
categories: []
date: '2020-05-01'
lastmod: 2022-12-26T12:56:57Z
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-12-26T12:56:57.123153Z'
publication_types:
- '2'
abstract: ''
publication: '*apj*'
doi: 10.3847/1538-4357/ab8882
links:
- name: arXiv
  url: https://arxiv.org/abs/2004.03007
url_pdf: ''
url_code: 'https://github.com/dennissergeev/exoconvection-apj-2020'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: 'https://slides.com/denissergeev/2020-04-21-nasa-giss'
url_source: ''
url_video: 'https://youtu.be/9nGIpQiPwDs'
---
This is my "hello-world" paper in the extremely exciting and new to me topic of modelling exoplanet atmospheres.

My co-authors and I were interested how important the representation of the atmospheric convection is for the climate of Earth-like planets, specifically those that are tidally-locked to their host M-dwarf stars. Tidally-locked terrestrial planets have a permanent day-side, where the atmospheric regime is expected to be largely determined by moist convection, akin to the tropics on Earth.

Individual convective cells are too small to be resolved by most 3D general circulation models (GCMs), and their overall effect is parameterised by approximate schemes, or parameterisations. For Earth, convection is treated by parameterisations, which are “tuned” to the abundant observations available. Even then, it remains one of the major causes of uncertainty in future climate projections. For exoplanets, measurements of convective activity are available yet, so their atmospheres are usually modelled using simple approaches to convection, adopted from early generations of terrestrial GCMs. While a handful of previous studies hinted at the importance of convection parameters in exoplanet simulations, none have focused on this problem specifically.

Using the Met Office Unified Model, we first perform a series of coarse-resolution simulations with three different representations of convection. We show that the circulation regime and the global cloud cover is substantially affected. Importantly, the climate state of the whole planet and not just the substellar hemisphere (where convection occurs) is sensitive to the convection parameterization. By modelling two different planets, Trappist-1e and Proxima Centauri b, we show that this effect is also planet-dependent. We then use the same 3D GCM in a convection-permitting mode to obtain a fine-scale picture of atmospheric convection for a portion of the substellar hemisphere and to further explore the differences between the parameterized and explicit convection. Using an estimate of convection intensity on the day side, we hypothesise that a potential global high-resolution simulation would enhance the day-night surface temperature contrast for a tidally-locked Earth-like planet. In other words, models with parameterized convection may overestimate the inter-hemispheric heat redistribution efficiency.

The paper is supplemented by an [interactive 3D visualisation](https://dennissergeev.github.io/exoconvection-apj-2020).
