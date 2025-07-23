---
author: Paulina Salinas Ruiz
created: 2024-04-15
last_reviewed: '2025-07-08'
modified: 2024-12-17
process_number: 130-81
review_period: 3 years
title: S123_EnableOfflineUsability_240415
---

**Purpose:**

To allow for the creation of an ArcGIS Survey123 Survey that can be used by the public to collect field data offline.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 50%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Step</strong></th>
<th><strong>Major Activity</strong></th>
<th><strong>References, Forms and Details</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1</td>
<td>Set up and ArcGIS Survey 123 &amp; download the ArcGIS Survey 123 field app if you have not already done so.</td>
<td><ul>
<li><p>See process number <a href="https://pacificsalmonfoundation-my.sharepoint.com/:w:/g/personal/psalinasruiz_psf_ca/EVs9rLPj2cBLi-AF3UBzc14BMuvtA4tSBNcKj-Aqpou7mA?e=WNTc3N">130-80</a></p></li>
<li><p>Note – offline functionality is only available in the field app not the web app.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td><p>Prepare basemap for offline use by creating a tile package using Tile Package Kreator</p>
<p>Tile Package Kreator is a desktop app for raster tile package creation and discovery. This app allows you to do the following:</p>
<ul>
<li><p>Create a raster tile package for offline use.</p></li>
<li><p>Browse and download organizational raster tile packages.</p></li>
<li><p>Upload existing raster tile packages to ArcGIS for sharing in your organization.</p></li>
</ul>
<p>Tile Package Kreator provides an alternative method to create and manage the basemap files you need to use Survey123 offline.</p></td>
<td><ul>
<li><p>This is just one option for creating a tile package, various other options exist (e.g. creating a map packing in a browser).</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">2a</td>
<td>Download and install Tile Package Kreator if you have not already done so.</td>
<td><ul>
<li><p><a href="https://links.esri.com/esrilabs/tile-package-kreator-mac">macOS</a></p></li>
<li><p><a href="https://links.esri.com/esrilabs/tile-package-kreator-windows">Windows</a></p></li>
<li><p><a href="https://links.esri.com/esrilabs/tile-package-kreator-ubuntu">Ubuntu</a></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">2b</td>
<td>Create a Tile Package Kreator project with the basemap you are interested in exporting.</td>
<td><ul>
<li><p>E.g. World Imagery (for Export)</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">2c</td>
<td>Draw a polygon, rectangle or path for the area of the basemap you are interested in exporting</td>
<td><ul>
<li><p>If using path, specify a buffer radius.</p></li>
<li><p>You can save the specified area of interest as a bookmark, then export to GeoJson if so desired.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">2b</td>
<td>Select the desired number of zoom levels and enter a title.</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">2c</td>
<td>Select to export the tile package either locally or to upload to ArcGIS Online.</td>
<td><ul>
<li><p>Fill in a description as well as choose sharing settings if uploading to ArcGIS Online.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td>Link the shared tile package to you your survey</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">3a</td>
<td><ol type="1">
<li><p>Open your survey in Survey123 Connect.</p></li>
</ol></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">3b</td>
<td>Open the <strong>Linked Content</strong> tab.</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">3c</td>
<td>Select <strong>Add Map Link</strong>.</td>
<td><ul>
<li><p>A window appears with all map services and packages shared to your named user account. Not all of these items can be used offline.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">3d</td>
<td><ol type="1">
<li><p>Select your preferred shared tile package, and select <strong>OK</strong>.</p></li>
</ol></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td><ol start="2" type="1">
<li><p>Add the offline basemap to ArcGIS Survey123 field app.</p></li>
</ol></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">4a</td>
<td><ol start="3" type="1">
<li><p>Open the ArcGIS Survey123 field app within range or Wifi or cellular data.</p></li>
</ol></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">4b</td>
<td><ol start="4" type="1">
<li><p>Open the survey form you have previously created using web designer for which you would like to download an offline basemap.</p></li>
</ol></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">4c</td>
<td><ol start="5" type="1">
<li><p>Click the settings button in the top-right of the survey, then Offline Maps.</p></li>
</ol>
<p>Download the map package(s) you have previously linked to the survey.</p></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td><ol start="6" type="1">
<li><p>You can now open the ArcGIS Survey 123 app outside of internet access. When a map is needed within the form, change the map basemap to the downloaded map package.</p></li>
</ol></td>
<td></td>
</tr>
</tbody>
</table>