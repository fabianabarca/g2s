.. gtfs2series documentation master file, created by
   sphinx-quickstart on Tue Jan 3 10:22:43 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

gtfs2series Documentation
=========================

This is an utility tool to retrieve and transform GTFS Schedule and Realtime data into multivariate time series, which is better suited for data analysis in several platforms. 

``gtfs2series`` imports and manages GTFS data, and provides a set of functions to transform the data into multivariate time series. The output is a pandas DataFrame, which can be easily exported to CSV or other formats.

``gtfs2series`` outputs a multivariate time series with variables that are selected by the user. The available variables are the following:


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   about
   installation
   guide
   gtfs
   series

Index
-----

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
