---
title: "octant: Objective Cyclone Tracking ANalysis Tools"
collection: software
permalink: /software/octant
language: Python
repository: dennissergeev/octant
---

[![Python 3.6 | 3.7](https://img.shields.io/badge/python-3.6%20%7C%203.7-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Conda](https://img.shields.io/conda/v/dennissergeev/octant?color=dark-green&logo=anaconda)](https://anaconda.org/dennissergeev/octant)
[![Documentation](https://img.shields.io/badge/docs-latest-green?logo=read-the-docs)](https://octant-docs.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/license-MIT-black.svg)](https://github.com/dennissergeev/octant/blob/master/LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1313078.svg)](https://doi.org/10.5281/zenodo.1313078)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A small Python/Cython library to process and visualise cyclone tracks. Based on such packages as `pandas`, `matplotlib`, `xarray`, `cython`. Testing is done with `pytest`.

Functionality includes:
* generation of derived fields such as cyclone density
* matching tracks to each other or to an external dataset
* convenient plotting functions.
