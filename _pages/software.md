---
title: "Software"
permalink: /software/
author_profile: true
redirect_from: 
  - /software.html
---

{% include base_path %}

My research involves processing a model data output.
This requires writing code, some of which I develop as open-source packages.
I also have a few fun side projects.
Most of my code can be found on <a href="https://github.com/{{ site.author.github }}"><i class="fab fa-fw fa-github" aria-hidden="true"></i> Github</a>.

{% for post in site.software %}
  {% include archive-single.html %}
{% endfor %}

## My toolbox 

Here is a list of tools that I use in my research
### Generic code editing
* [Vim](http://www.vim.org/)

### Word processing and presentations
* Markdown
* Online: [Overleaf](http://overleaf.com)
* Locally: [Texmaker](http://xm1math.net/texmaker/)
* Google Docs, reveal.js, beamer

### Vector graphics and poster preparation
* [LaTeX](http://latextemplates.com/cat/conference-posters)
* [InkScape](http://inkscape.org/)
* [draw.io](https://app.diagrams.net/)

### Bibliography management
* [Mendeley](http://mendeley.com/dashboard/)

### Scientific data analysis and visualisation 
#### Data IO
* Earth sciences data formats: [netCDF](http://unidata.github.io/netcdf4-python/), [h5py](http://docs.h5py.org/en/latest/), [xarray](http://xarray.pydata.org), [iris](http://scitools.org.uk/iris/index.html), [metpy](https://unidata.github.io/MetPy/latest/)
* Tabular data: [pandas](http://pandas.pydata.org/)
#### Data analysis
* [numpy](http://numpy.org/), [scipy](http://scipy.org/), [iris](http://scitools.org.uk/iris/index.html)
* heavy computations: Fortran, [Cython](https://cython.org/), [dask](https://dask.org), [numba](https://numba.pydata.org)
#### Visualisation
* Generic: [matplotlib](http://matplotlib.org/)
* Geospatial data: [cartopy](http://scitools.org.uk/cartopy/index.html)
* 3D visualisation: [pyvista](https://www.pyvista.org/)

### Python code development
* [Jupyter Lab](http://jupyter.org)

### Workflow automation
* [GNU Make](http://gnu.org/software/make/)
