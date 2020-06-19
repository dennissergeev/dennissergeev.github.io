---
title: "Python packages to calculate wind field quantities"
date: 2014-12-16
permalink: /blog/2014/12/16/wind-field-calculations-in-python
tags:
  - python
  - meteorology
---

_This post is merely sort of my own "lab notes", and I have to test the packages on a common simple example with known result. So I hope to rewrite it sooner or later._
Anyway, below are the links to some of the Python packages that have functions for calculating such wind field quantities as divergence and vorticity (curl, rotor). I am not yet sure what I'm going to use in my research, maybe it's better to write my own Python function. Or write it in Fortran and wrap it with f2py. Or simply use **Iris** package (see update below!). 

## [Windspharm](http://ajdawson.github.io/windspharm/)

At first the most promising package seemed to be windspharm, which is a "Python package for performing computations on global wind fields in spherical geometry". For computations it uses spherical harmonics and depends on a NCAR's SPHEREPACK library, access to which is provided by a wrapper [pyspharm](https://code.google.com/p/pyspharm/). This dependency is for some reason never mentioned on the winspharm's website (two possible reasons: I'm blind or it is too obvious). A very good step-by-step example of using the package can be found [here](https://ocefpaf.github.io/python4oceanographers/blog/2014/04/28/windspharm/).

### Pros:

  * Well-written and makes the code more readable
  * Consists of several tools that make it easy to prepare data for the processing
  * The working object VectorWind has 3 interfaces: "standard" - to work with NumPy arrays, "iris" - to work with Iris cubes, and "cdms" - to work with cdms2 variables. "The only differences are that the windspharm.iris and windspharm.cdms interfaces also use the meta-data stored in input variables to construct outputs with meta-data".
  * Capable of computation of such quantities as: divergence, vorticity, streamfunction, velocity potential, irrotational, and non-divergent components of the wind, vector gradient of a scalar function, magnitude (wind speed).

### Cons:

  * Can be applied only for global fields (spherical harmonics!)
  * Computes only a vertical component of vorticity (dv/dx - du/dy)
  * Does not accept missing values (NaN) nor masked array (solution from the site above - fill the missing values with zeros and then reapply the mask to the result)
  * Rather strange requirements to the input arrays - the leading dimension has to be latitude, and the latitude dimension has to be north-to-south. This can be a source of mistakes in the code, but the bundled tools make it very easy to arrange the data correctly.

## [AtmQty library](http://www.johnny-lin.com/py_pkgs/atmqty/doc/manual.html)

This package offers a wide set of various meteorology-related functions, so you don't need to invent a wheel every time you write a programme in Python. As the website claims, the package "contains methods to calculate atmospheric quantities that are directly derivative (i.e. not requiring time integration or modeling) from standard state variables".

Among the multitude of functions there is a method that provides a method to calculate the relative vorticity and even the isentropic potential vorticity. Just skimming through the source code, I can say that the vorticity calculation is done by using a [curl](http://www.johnny-lin.com/py_pkgs/gemath/doc/curl_2d.html) operator from [gemath](http://www.johnny-lin.com/py_pkgs/gemath/doc/index.html) package. The curl operator offers different algorithms of calculation, default being set to the first-order finite-differencing (back-ward and forward differencing used at the endpoints, and centered differencing used everywhere else). For calculations on a sphere it can use SPHEREPACK, if available. However, there can be no missing values in the input data.

### Pros:

  * Has several calculation algorithms
  * Allows computations on a limited area domain (default is spherical)
  * Has an extensive documentation and examples, including an [example](http://www.johnny-lin.com/py_pkgs/atmqty/doc/test_vort.html) of calculating relative vorticity and comparing the result with ERA-40 reanalysis

### Cons:

  * Is dependent on gemath package and/or SPHEREPACK library
  * When using finite differences on a spherical grid, values north of 88N or south of 88S latitude are set to missing automatically (because of singularities in the algorithm near the poles)
  * Computes only a vertical component of vorticity (dv/dx - du/dy)
  * Seems to be abandoned since 2004 (instead see PyAOS below)

## [PyAOS library](https://github.com/PyAOS/aoslib)

According to the disclaimer, it is "a Python library of standard atmospheric and oceanic sciences calculation routines. It exists mainly so we're all not writing our own routines to calculate potential temperature, isentropic potential vorticity, etc". It is basically a Python wrapper around a library written in Fortran-77. It is most likely a successor of the AtmQty library. This is probably good for speeding up the calculations, though I'm not a fan of the 77 version of Fortran. The subroutine that calculates vorticity is in g2gkinematics.f file and simply employs a centred differences method.

### Pros:

  * The library itself is a pretty large collection of AOS-related methods
  * Presumably fast enough due to code written in Fortran

### Cons:

  * Limited functionality, at least in the vorticity calculations
  * Computes only a vertical component of vorticity (dv/dx - du/dy)
  * Requires compilation that makes it difficult to change the source code "on-the-go"
  * Perhaps not the most dynamically developing project

## [Dynlib](https://wiki.uib.no/gfi/index.php/Dynlib)

The Dynlib library is developed at Geophysical Institute, University of Bergen. The project has a beautiful wiki page (the link in the header). The code is written in Fortran-95, mostly by C. Spensberger.

The subroutine that calculates relative vorticity uses centred differences, but returns zeros at the edges for a non-cyclic grid.

### Pros:

  * The library itself offers an impressive collection of functions that are used in geophysical fluid dynamics, including geostrophic quantities, wind field deformation, etc.
  * Presumably fast enough due to code written in Fortran
  * The source code is well-written and very readable

### Cons:

  * Limited functionality, at least in the vorticity calculations
  * Computes only a vertical component of vorticity (dv/dx - du/dy)
  * Requires compilation

## [Vector field parameters](http://www.malg.eu/vector_field_params.php)

Looking for a ready solution to the wind field processing, a while ago I run across this script. Since it is posted in a blog dedicated to GIS programming, "input data must be provided as two Arc/Info ASCII grids, storing the x- and y-components of the vector field". The results are also stored in ASCII grids.

Vorticity (and couple of other field quantities) are computed simply by using NumPy gradient, which by default uses centred differences in the interior points.

### Pros:

  * Good for GIS-users
  * Pure Python

### Cons:

  * Computes only a vertical component of vorticity (dv/dx - du/dy)
  * ASCII grids I/O

## [Geoscience Australia repository](https://github.com/GeoscienceAustralia/tcrm/tree/master/Utilities)
Another trivial example of vorticity calculation (again only z-component) is embedded in TCRM model (A statistical-parametric model for assessing wind hazard from tropical cyclones). The code is in pure Python, though the vorticity function depends on another function that converts lon/lat grid step to distance in meters.

### Pros:

  * Simple code, can be a starting point to write something more
  * Pure Python

### Cons:

  * Computes only a vertical component of vorticity (dv/dx – du/dy)
  * The computation is done by using explicit differentiation in two loops, which is probably quite slow
  * The returned array is reduced in size by 2 elements in each dimension (so they do not use a forward/backward scheme at the boundaries)

I didn’t find out if CDAT has functions to calculate vorticity, but I tend to think that it uses spherical harmonics and hence allows the computations only on a global grid and only of a vertical component of vorticity.

## Update:

### Iris

I discovered that Iris package actually has functions to calculate the finite differences and curl operator in Cartesian or spherical coordinates. It has some limitations and is being developed to work with Iris cubes, but it is the closest solution to what I had in mind writing this post. Here is the link to Iris’ calculus functions:

[Iris Calculus](http://scitools.org.uk/iris/docs/latest/iris/iris/analysis/calculus.html)

I hope that Iris team will continue to develop the calculus submodule and will make it as awesome as the rest of the package.
