---
author: Paulina Salinas Ruiz
created: 2024-04-15
last_reviewed: '2025-07-08'
modified: 2024-11-26
process_number: 130-60
review_period: 3 years
title: QGIS_PerformingBasicOperations_240415
---

**Purpose:**

To provide introductory instructions on how to perform basic actions in QGIS such as adding and viewing vector data.

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
<td>Download and install the latest version of QGIS if you do not already have it on your machine.</td>
<td>QGIS Standalone Installer Version 3.30 is available at the following link at the time this document is being written - https://qgis.org/en/site/forusers/download.html</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td>Open QGIS and start a new project or open one that has previously been worked on.</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td><p>(optional) If this is the first time using QGIS on your machine, you will want to install a plugin that allows you to <strong>view basemaps</strong>. To install the Quick Map Services plugin:</p>
<ul>
<li><p>Open QGIS. Go to Plugins Menu &gt;&gt; Manage and Install Plugins</p></li>
<li><p>In the Plugins Window, search for QuickMapServices then click Install button</p></li>
<li><p>After it installs, you should be able to find QuickMapServices button in the Web Toolbar.</p></li>
</ul></td>
<td>Basemaps are the background maps that let you know what part of the world you are viewing.</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td><strong>Add data to the map</strong>. The formats that can be added are various, a unanimous characteristic for spatial data is that coordinate information must be available (e.g. longitude, latitude). This information will be present as lat/lon columns in a point file, or geom column in a line/polygon file.</td>
<td><p>Some common Vector formats include:</p>
<ul>
<li><p>CSV (Delimited Text Layer)</p></li>
<li><p>Shapefile</p></li>
<li><p>File Geodatabase</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td>Select the hand symbol from the toolbar, move it over the canvas, hold down your mouse clicker and move your mouse to <strong>pan around the map</strong>.</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td><p><strong>Zoom into the map</strong> by selecting the magnifying glass symbol with the plus sign, moving your mouse over the map extent, and click your mouse.</p>
<p>The process is the same for zooming out, expect you select the magnifying glass symbol with the minus sign.</p>
<p>Alternatively, you can use the wheel in the middle of your mouse.</p></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td><p>The layer name of the data you added should be visible in the panel on the left side of your map.</p>
<p>Turn <strong>layer visibility on and off</strong> by clicking the checkbox beside the layer name.</p>
<p>Reveal the layer legend by clicking the arrow beside the layer name.</p></td>
<td>Right clicking the layer name reveals a number of other possible functionalities you can explore such as revealing Layer Properties, which is where you can change symbology.</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td>Click the icon with a little ‘i’ in a blue circle with a mouse pointer touching it in the map toolbar to select the Identify tool. Hover over a data feature in the map and click it to <strong>reveal its attributes</strong> in the panel on the right side of the map.</td>
<td>Sometimes if features exist close to each other, multiple features will be selected, click the arrow beside the bolded text within the panel to reveal attributes for other selected features.</td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td>Many other possible actions exist, to learn more please visit the official QGIS training documentation discoverable via Google search engine.</td>
<td></td>
</tr>
</tbody>
</table>