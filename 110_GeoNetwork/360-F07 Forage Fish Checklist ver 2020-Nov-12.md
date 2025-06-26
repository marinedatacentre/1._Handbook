***Notes:***

1.  *Prior to submitting the Forage Fish Monitoring data to Pacific Salmon Foundation’s Strait of Georgia (SOG) Data Centre, please complete the checklist to minimize possible entry errors within the dataset.*

2.  *The following steps may require clarification or assistance from Pacific Salmon Foundation. Please feel free to contact Terry Curran (250-656-4098, <terry.curran@shaw.ca>) at any time.*

<table>
<colgroup>
<col style="width: 64%" />
<col style="width: 20%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p><strong>Item</strong></p>
</blockquote></th>
<th><strong>Date Confirmed</strong></th>
<th><strong>Initials</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><ol type="1">
<li><p>Title of data submission</p></li>
</ol></td>
<td></td>
<td></td>
</tr>
<tr>
<td><ol start="2" type="1">
<li><p>GPS coordinates to ensure monitoring sites are in the correct location for the surveyed beach station(s) (e.g., plot coordinates on Google Earth)</p></li>
</ol></td>
<td></td>
<td></td>
</tr>
<tr>
<td><ol start="3" type="1">
<li><p>latitude/longitude in format xx.xxxxx/-xxx.xxxxx (five decimals)</p></li>
</ol></td>
<td></td>
<td></td>
</tr>
<tr>
<td><ol start="4" type="1">
<li><p>Site has an associated ShoreZone Phyident value “xx/xx/xxxx/xx” (e.g., Mapleguard Point’s associated Phyident value is 01/10/0137/00). If it is a new monitoring site, see below to determine how to generate phyident from the points.</p></li>
</ol></td>
<td></td>
<td></td>
</tr>
<tr>
<td><ol start="5" type="1">
<li><p>Date/time columns (sampling) is in format: yyyy‑mm‑dd hh:mm with24 hour time.</p></li>
</ol></td>
<td></td>
<td></td>
</tr>
<tr>
<td><ol start="6" type="1">
<li><p>Date/time columns (both tidal values) in format: yyyy‑mm‑dd hh:mm with24 hour time</p></li>
</ol></td>
<td></td>
<td></td>
</tr>
<tr>
<td><ol start="7" type="1">
<li><p>Beach name/station properly aligns with your site sample ID</p></li>
</ol></td>
<td></td>
<td></td>
</tr>
<tr>
<td><ol start="8" type="1">
<li><p>Data entered aligns with the appropriate columns</p></li>
</ol></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<u>Steps to generate phyident from points for new sample sites</u>:

1.  Do a dump of the observations into a CSV file.

2.  Open a GPS app (e.g., QGIS) and access a mapserver (e.g. <http://soggy.zoology.ubc.ca:8080/geoserver/wms>).

3.  Select the “**unit lines**”, which is part of the ShoreZone dataset.

4.  Input the CSV data file and use the latitude and longitude for positioning. This should display the points on the unit lines.

5.  Label the points with station ID.

6.  Identify the unit line segment where there is a sampling point, and thus get the phyident

7.  Build a file for future reference (station ID, lat/long, and phyident)
