***Notes:***

1.  *Prior to submitting the Forage Fish Monitoring data to Pacific Salmon Foundation's Strait of Georgia (SOG) Data Centre, please complete the checklist to minimize possible entry errors within the dataset.*

2.  *The following steps may require clarification or assistance from Pacific Salmon Foundation. Please feel free to contact Terry Curran (250-656-4098, <terry.curran@shaw.ca>) at any time.*

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+-----------------+
| > **Item**                                                                                                                                                                                                                                  | **Date Confirmed**    | **Initials**    |
+=============================================================================================================================================================================================================================================+=======================+=================+
| 1.  Title of data submission                                                                                                                                                                                                                |                       |                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+-----------------+
| 2.  GPS coordinates to ensure monitoring sites are in the correct location for the surveyed beach station(s) (e.g., plot coordinates on Google Earth)                                                                                       |                       |                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+-----------------+
| 3.  latitude/longitude in format xx.xxxxx/-xxx.xxxxx (five decimals)                                                                                                                                                                        |                       |                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+-----------------+
| 4.  Site has an associated ShoreZone Phyident value "xx/xx/xxxx/xx" (e.g., Mapleguard Point's associated Phyident value is 01/10/0137/00). If it is a new monitoring site, see below to determine how to generate phyident from the points. |                       |                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+-----------------+
| 5.  Date/time columns (sampling) is in format: yyyy‑mm‑dd hh:mm with24 hour time.                                                                                                                                                           |                       |                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+-----------------+
| 6.  Date/time columns (both tidal values) in format: yyyy‑mm‑dd hh:mm with24 hour time                                                                                                                                                      |                       |                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+-----------------+
| 7.  Beach name/station properly aligns with your site sample ID                                                                                                                                                                             |                       |                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+-----------------+
| 8.  Data entered aligns with the appropriate columns                                                                                                                                                                                        |                       |                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+-----------------+

[Steps to generate phyident from points for new sample sites]{.underline}:

1.  Do a dump of the observations into a CSV file.

2.  Open a GPS app (e.g., QGIS) and access a mapserver (e.g. <http://soggy.zoology.ubc.ca:8080/geoserver/wms>).

3.  Select the "**unit lines**", which is part of the ShoreZone dataset.

4.  Input the CSV data file and use the latitude and longitude for positioning. This should display the points on the unit lines.

5.  Label the points with station ID.

6.  Identify the unit line segment where there is a sampling point, and thus get the phyident

7.  Build a file for future reference (station ID, lat/long, and phyident)
