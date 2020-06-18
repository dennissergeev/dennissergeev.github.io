---
title: "Atmospheric convection plays a key role in the climate of tidally-locked terrestrial exoplanets: insights from high-resolution simulations"
collection: publications
permalink: /publications/2020-05-08-exoconvection
excerpt: 'This paper is about the impact of the representation of atmospheric convection on the climate of Earth-like exoplanets, specifically those that are tidally-locked to their host M-dwarf stars.'
date: 2020-05-08
venue: Astrophysical Journal
paperurl: 'https://doi.org/10.3847/1538-4357/ab8882'
repository: dennissergeev/exoconvection-apj-2020
citation: 'Sergeev, D.E., F.H. Lambert, N.J. Mayne, I.A. Boutle, J. Manners and K. Kohary. 2020. Atmospheric convection plays a key role in the climate of tidally-locked terrestrial exoplanets: insights from high-resolution simulations. Astrophysical Journal, 894, 84.'
---

# About
This is my "hello-world" paper in the extremely exciting and new to me topic of modelling exoplanet atmospheres.

My co-authors and I were interested how important the representation of the atmospheric convection is for the climate of Earth-like planets, specifically those that are tidally-locked to their host M-dwarf stars.
Tidally-locked terrestrial planets have a permanent day-side, where the atmospheric regime is expected to be largely determined by moist convection, akin to the tropics on Earth.

Individual convective cells are too small to be resolved by most 3D general circulation models (GCMs), and their overall effect is *parameterised* by approximate schemes, or parameterisations.
For Earth, convection is treated by parameterisations, which are "tuned" to the abundant observations available.
Even then, it remains one of the major causes of uncertainty in future climate projections.
For exoplanets, measurements of convective activity are available yet, so their atmospheres are usually modelled using simple approaches to convection, adopted from early generations
of terrestrial GCMs.
While a handful of previous studies hinted at the importance of convection parameters in exoplanet simulations, none have focused on this problem specifically.

Using the Met Office Unified Model, we first perform a series of coarse-resolution simulations with three different representations of convection.
We show that the circulation regime and the global cloud cover is substantially affected.
Importantly, the climate state of the whole planet and not just the substellar hemisphere (where convection occurs) is sensitive to the convection parameterization.
By modelling two different planets, Trappist-1e and Proxima Centauri b, we show that this effect is also planet-dependent.
We then use the same 3D GCM in a convection-permitting mode to obtain a fine-scale picture of atmospheric convection for a portion of the substellar hemisphere and to further explore the differences between the parameterized and explicit convection.
Using an estimate of convection intensity on the day side, we hypothesise that a potential global high-resolution simulation would enhance the day-night surface temperature contrast for a tidally-locked Earth-like planet.
In other words, models with parameterized convection may overestimate the inter-hemispheric heat redistribution efficiency.


**The paper is supplemented by an [interactive 3D visualisation](/exoconvection-apj-2020).**

# Relevant talks

* [NASA GISS seminar](/talks/2020-04-21-nasagiss)
* [Exoclimes V](/talks/2019-08-13-exoclimes)

# Bibtex

    @article{SergeevEtAl2020,
        archivePrefix = {arXiv},
        arxivId = {2004.03007},
        author = {Sergeev, Denis E. and Lambert, F. Hugo and Mayne, Nathan J. and Boutle, Ian A. and Manners, James and Kohary, Krisztian},
        doi = {10.3847/1538-4357/ab8882},
        eprint = {2004.03007},
        issn = {1538-4357},
        journal = {The Astrophysical Journal},
        number = {2},
        pages = {84},
        publisher = {IOP Publishing},
        title = {Atmospheric convection plays a key role in the climate of tidally-locked terrestrial exoplanets: insights from high-resolution simulations},
        url = {https://iopscience.iop.org/article/10.3847/1538-4357/ab8882},
        volume = {894},
        year = {2020}
    }
