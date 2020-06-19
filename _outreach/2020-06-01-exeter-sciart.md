---
title: Science as Art Exhibition
excerpt: 'My submission for the "Science as Art" exhibition at the Exeter Science Centre'
date: 2020-06-01
permalink: /outreach/2020-06-01-exeter-sciart
venue: Exeter Science Centre
collection: outreach
type: "Graphics"
header:
  teaser: exescicen2020.png
---

[![Science as Art exhibition](/images/exescicen2020.png)](https://exetersciencecentre.org/gallery/denis_sergeev_uoe_exoplanets)

> Exoplanets are planets that exist outside of our solar system, orbiting distant stars. Scientists at the University of Exeter and the Met Office use state-of-the-art 3D climate models to understand the key physical processes which control the atmospheres of these exoplanets. Exoplanetary atmospheres are diverse, and many of them behave in a completely unfamiliar way, compared to Earth. This image shows results of several computer simulations given various planetary and stellar parameters. Astrophysicists and climate scientists work together to analyse these simulated atmospheres by looking at temperatures, winds, cloudiness and other meteorological variables – testing and developing theories of climate processes.

# Technical details

I used the Python package called [pyvista](https://docs.pyvista.org/) to create the 3D renderings and [GIMP](https://www.gimp.org/) to assemble the picture together.
3D visualisation is constructed from the output of an idealised simulation of two planetary atmospheres, performed using the UK Met Office Unified Model.
The two planets are both aquaplanets (i.e. there is no land in the simulation) and exemplify planets with Earth-like atmospheric regimes (in front), as well as tidally-locked planets, with permanent day and night sides (at the back).
