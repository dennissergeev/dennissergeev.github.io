---
title: "Exercise in converting a CSV file to netCDF using xarray"
date: 2015-09-08
permalink: /blog/2015/09/08/csv-to-xarray
tags:
  - python
  - xarray
---

The story begins with a text file that I got from my supervisor. That file contains many lines (time dimension) and many columns (variables) of numeric data that were the result of postprocessing of [ACCACIA](http://arcticaccacia.wordpress.com/) aircraft measurements. The file itself didn't contain any metadata, but it came with a matlab script, which loads the data and has comments to each column, e.g.:

`...`

`flux_data = load(file_name);`

`...`

`pressure    = flux_data(:,11);      % Air pressure (hPa)`

`wind_speed  = flux_data(:,12);      % Horisontal wind speed (m s-1)`

`wind_dir    = flux_data(:,13);      % Wind direction (deg)`

`...`

Converting this script to Python was pretty trivial, and I had used this interface for some tim. It was already more convenient to use than the original matlab: once the script was imported, all the variables could be accessed as its keys:

`import read_flux_data as flx`

`print(flx.wind_speed) # 1D array of wind speed values`

But then I got tired of only the values being accessible, but not the description and units that resided in the comments inside the script. The obvious way to was to convert two files: data and reading script into a NetCDF file. Plus, the `xarray` package had been gaining popularity. So below is my little exercise in data I/O using the modern NetCDF handler.

To begin with, I load necessary modules

```python
from collections import OrderedDict
import numpy as np
import os
import pandas as pd
import xarray
```

Instead of `numpy.genfromtxt()` as my original Python script did I use a `pandas` function to read the .csv file. TIL the `read_csv` function has an awesome feature to parse date-time strings automatically...

```python
flux_data = pd.read_csv('../data/flux_data.txt', delim_whitespace=True, parse_dates=[1], header=None)
```

Then, being a lazy bastard I am, I just copied the contents of my Python script and literally wrapped them with necessary syntax to divide data input and the comments, organising all this in an `OrderedDict` of dictionaries. Useful thing is this dictionary class...

```python
values_and_names = OrderedDict([
('time         ' , dict(data=flux_data[1 ].values, long_name='Time')),
('BXXX         ' , dict(data=flux_data[2 ].values, long_name='Mission identifier')),
('lat          ' , dict(data=flux_data[3 ].values, long_name='Latitude (deg)')),
('lon          ' , dict(data=flux_data[4 ].values, long_name='Longitude (deg)')),
('flag         ' , dict(data=flux_data[5 ].values, long_name='1: sea, 2: MIZ/ice')),
('dist         ' , dict(data=flux_data[6 ].values, long_name='Length of run (km)')),
('altitude     ' , dict(data=flux_data[7 ].values, long_name='Radar altitude (m)')),
('altitude_std ' , dict(data=flux_data[8 ].values, long_name='Stdev radar altitude (m)')),
('heading      ' , dict(data=flux_data[9 ].values, long_name='Heading (deg)')),
('pressure     ' , dict(data=flux_data[10].values, long_name='Air pressure (hPa)')),
('wind_speed   ' , dict(data=flux_data[11].values, long_name='Horisontal wind speed (m s-1)')),
('wind_dir     ' , dict(data=flux_data[12].values, long_name='Wind direction (deg)')),
('vert_wind    ' , dict(data=flux_data[13].values, long_name='Vertical wind velocity (m s-1)')),
('temp         ' , dict(data=flux_data[14].values, long_name='Air temperature (K)')),
('temp_dew     ' , dict(data=flux_data[15].values, long_name='Dew point (K)')),
('q            ' , dict(data=flux_data[16].values, long_name='Air specific humidity (g/kg)')),
('theta        ' , dict(data=flux_data[17].values, long_name='Pot. temp., 1.order approximation: theta = T+gamma.z  (K)  ')),
('theta_v      ' , dict(data=flux_data[18].values, long_name='Virtual pot. temperature (K)')),
('rho          ' , dict(data=flux_data[19].values, long_name='Density (kg m-3)')),
('mslp         ' , dict(data=flux_data[20].values, long_name='Mean sea level pressure')),
('temp_sfc     ' , dict(data=flux_data[21].values, long_name='Surface temperature (Upwell. brightn. temp.) (K)')),
('q_sfc        ' , dict(data=flux_data[22].values, long_name='Surface air specific humidity (g kg-1)')),
('sw_up        ' , dict(data=flux_data[23].values, long_name='Short wave upward (W m-2) ')),
('sw_down      ' , dict(data=flux_data[24].values, long_name='Short wave downward (W m-2)')),
('lw_up        ' , dict(data=flux_data[25].values, long_name='Long wave upward (W m-2) ')),
('lw_down      ' , dict(data=flux_data[26].values, long_name='Long wave downward (W m-2) ')),
('u_10m        ' , dict(data=flux_data[27].values, long_name='Wind speed adjusted to 10 m (m s-1)')),
('t_2m         ' , dict(data=flux_data[28].values, long_name='Temperature adjusted to 2 m (K)')),
('q_2m         ' , dict(data=flux_data[29].values, long_name='Specific humidity adjusted to 2 m (g kg-1)')),
('rh_2m        ' , dict(data=flux_data[30].values, long_name='Relative humidity at 2 m (%)')),
('u_10N        ' , dict(data=flux_data[31].values, long_name='10-m neutral wind speed (m s-1)')),
('L            ' , dict(data=flux_data[32].values, long_name='Monin-Obukhov length (m)')),
('tau          ' , dict(data=flux_data[33].values, long_name='Wind stress (N m-2)')),
('ustar        ' , dict(data=flux_data[34].values, long_name='Friction velocity (m s-1)')),
('z0           ' , dict(data=flux_data[35].values, long_name='Surface roughness length (m)')),
('Cdn          ' , dict(data=flux_data[36].values, long_name='10-m neutral drag coefficient')),
('SH           ' , dict(data=flux_data[37].values, long_name='Sensible heat flux (W m-2)')),
('thetastar    ' , dict(data=flux_data[38].values, long_name='Friction potential temperature (K)')),
('tstar        ' , dict(data=flux_data[39].values, long_name='Friction temperature (K)')),
('z0_t         ' , dict(data=flux_data[40].values, long_name='Surface roughness lenght wrt heat based on theta (m)')),
('Chn          ' , dict(data=flux_data[41].values, long_name='10-m neutral heat exchange coefficient ')),
('LH           ' , dict(data=flux_data[42].values, long_name='Latent heat flux (W m-2)')),
('qstar        ' , dict(data=flux_data[43].values, long_name='Friction moisture (g kg-1)')),
('z0_q         ' , dict(data=flux_data[44].values, long_name='Surface roughness lenght wrt moisture (m)')),
('Cen          ' , dict(data=flux_data[45].values, long_name='10-m neutral moisture exchange coefficient')),
('tau_bulk     ' , dict(data=flux_data[46].values, long_name='[Smith, 1988] wind stress (N m-2)')),
('SH_bulk      ' , dict(data=flux_data[47].values, long_name='[Smith, 1988] sensible heat flux (W m-2)')),
('LH_bulk      ' , dict(data=flux_data[48].values, long_name='[Smith, 1988] latent heat flux (W m-2)')),
('u_10N_coare  ' , dict(data=flux_data[49].values, long_name='Coare3.0: 10-m neutral wind speed (m s-1)')),
('u_10m_coare  ' , dict(data=flux_data[50].values, long_name='Coare3.0: 10-m wind speed (m s-1)')),
('t_2m_coare   ' , dict(data=flux_data[51].values, long_name='Coare3.0: 2-m temperature (K)')),
('q_2m_coare   ' , dict(data=flux_data[52].values, long_name='Coare3.0: 2-m specific humidity (g kg-1)')),
('rh_2m_coare  ' , dict(data=flux_data[53].values, long_name='Coare3.0: 2-m relative humidity (%)')),
('tau_coare    ' , dict(data=flux_data[54].values, long_name='Coare3.0: wind stress (W m-2)')),
('z0_coare     ' , dict(data=flux_data[55].values, long_name='Coare3.0: surface roughness length (m)')),
('Cdn_coare    ' , dict(data=flux_data[56].values, long_name='Coare3.0: 10-m neutral drag coefficient')),
('SH_coare     ' , dict(data=flux_data[57].values, long_name='Coare3.0: sensible heat flux (W m-2)')),
('z0_t_coare   ' , dict(data=flux_data[58].values, long_name='Coare3.0: surface roughness length wrt heat (m)')),
('Chn_coare    ' , dict(data=flux_data[59].values, long_name='Coare3.0: 10-m neutral heat exchange coefficient')),
('LH_coare     ' , dict(data=flux_data[60].values, long_name='Coare3.0: latent heat flux (W m-2)')),
('z0_q_coare   ' , dict(data=flux_data[61].values, long_name='Coare3.0: surface roughness length wrt moisture (m)')),
('Cen_coare    ' , dict(data=flux_data[62].values, long_name='Coare3.0: 10-m neutral moisture exchange coefficient')),
('tau_bulk_gfd ' , dict(data=flux_data[63].values, long_name='[Smith, 1988] w/GFD coeffs: Cdn = 2.04e-03')),
('SH_bulk_gfd  ' , dict(data=flux_data[64].values, long_name='[Smith, 1988] Chn = 1.63e-03')),
('LH_bulk_gfd  ' , dict(data=flux_data[65].values, long_name='[Smith, 1988] Cen = 1.57e-03')),
('TKE          ' , dict(data=flux_data[66].values, long_name='turbulence kinetic energy (m+2 s-2)')),
('u_10N_err    ' , dict(data=flux_data[67].values, long_name='error on 10-m neutral wind speed (m s-1)')),
('Cdn_err      ' , dict(data=flux_data[68].values, long_name='error on 10-m neutral drag coefficient')),
('d_theta      ' , dict(data=flux_data[69].values, long_name='theta difference (theta - temp_sfc) (K)')),
('d_theta_err  ' , dict(data=flux_data[70].values, long_name='error on theta difference (K)')),
('Chn_err      ' , dict(data=flux_data[71].values, long_name='error on 10-m neutral heat exchange coefficient')),
('d_q          ' , dict(data=flux_data[72].values, long_name='specific humidity difference (q - q_sfc) (g kg-1)')),
('d_q_err      ' , dict(data=flux_data[73].values, long_name='error on specific humidity difference (g kg-1)')),
('Cen_err      ' , dict(data=flux_data[74].values, long_name='error on 10-m neutral moisture exchange coefficient')),
('u_d_theta    ' , dict(data=flux_data[75].values, long_name='10-m neutral wind speed x theta difference (m s-1 K)')),
('u_d_theta_err' , dict(data=flux_data[76].values, long_name='error on 10-m neutral wind speed x theta difference (m s-1 K)')),
('u_d_q        ' , dict(data=flux_data[77].values, long_name='10-m neutral wind speed x specific humidity difference (m s-1 g kg-1)')),
('u_d_q_err    ' , dict(data=flux_data[78].values, long_name='error on 10-m neutral wind speed x specific humidity difference (m s-1 g kg-1)'))
])
```

Since I was even lazy to put a quote after each variable name and just added a column of quotes in vim editor, I had to remove white spaces from the dictionary keys.

```python
values_and_names = OrderedDict((k.split()[0], v) for k, v in values_and_names.viewitems())
```

The next step was to parse the comments inherited from the original matlab script. Looping over the dictionary, I use few simple tricks to get a string inside parenthesis at the end of each `long_name` string. The obtained string I then assign to a `unit` key in the corresponding dictionary. Note I also expand 'deg' to 'degrees' just in case I want to transform it later to [`iris.units.Unit()`](http://scitools.org.uk/iris/docs/latest/iris/iris/unit.html) object later (which accepts only 'degrees' as the name for degrees).

```python
for i in values_and_names:
    s = values_and_names[i]['long_name']
    ibeg = s[::-1].find(")")
    ibeg = ibeg+1 if ibeg>=0 else -1
    iend = s[::-1].find("(")
    unit_str = s[::-1][ibeg:iend][::-1]
    if unit_str == 'deg':
        unit_str = 'degrees'
    values_and_names[i]['units'] = unit_str
    values_and_names[i]['long_name'] = s[:len(s)-iend-1]
```

With the help of `xarray` package documentation, I rearranged the dictionary into another dictionary of tuples.

```python
variables = dict()
for i in values_and_names:
    if i != 'time':
        variables[i] = ('time', 
                    values_and_names[i]['data'], 
                    dict(units=values_and_names[i]['units'], long_name=values_and_names[i]['long_name']))
```

Why did I do that? Now the data and metadata is packed in a structure that is digestible for `xarray.Dataset`. The only coordinate is time, and is defined by the same keyword. The great thing is that `pandas` parsed the time strings for me and already converted them to a `datetime64` object.

```python
ds = xarray.Dataset(variables=variables,
                    coords={'time': ('time', values_and_names['time']['data'])})
```

And voil&agrave;, we have everything packed in the NetCDF file.

```python
ds.to_netcdf('flux_data.nc')
```

If you are interested in the data, you should check out this paper:

Cook, P. A. and I. A. Renfrew, 2015: Aircraft-based observations of air-sea turbulent fluxes around the British Isles, *Quarterly J. Royal Meteorol. Soc.*,**141**, 139-152. doi: [10.1002/qj.2345](http://www.uea.ac.uk/~e046/reprints/cook_renfrew_diamet_fluxes_qj2345_QJRMS_2014.pdf)

This post was written as an Jupyter Notebook. You can view or download it using [nbviewer](http://nbviewer.ipython.org/github/dennissergeev/dennissergeev.github.io/blob/master/_blog/_notebooks/2015-09-08-csv-to-xarray.ipynb)
