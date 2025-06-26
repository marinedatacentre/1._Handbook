**Purpose:**

Scanned maps and historical data usually do not contain spatial reference information. In these cases, we need to use accurate location data to align or georeference our raster data to a map coordinate system. A map coordinate system is defined using a map projection-a method by which the curved surface of the earth is portrayed on a flat surface.

When georeferencing raster data, we define its location using map coordinates and assign the coordinate system of the map frame. Georeferencing raster data allows it to be viewed, queried, and analyzed with your other geographic data.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 37%" />
<col style="width: 45%" />
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
<td>Launch ArcGIS Pro and import the image</td>
<td><ul>
<li><p>Navigate to the “Map” tab</p></li>
<li><p>Select the “Add Data” drop down menu and choose “Data”</p></li>
<li><p>Select the image you’d like to georeference</p></li>
<li><p>If you’re presented with multiple band choices, select band 1</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td>Find the image on the map and overlay it on region of choice</td>
<td><ul>
<li><p>Right click the image name on the Table of Contents and select “Zoom to Layer”</p></li>
<li><p>Select the “Imagery” tab and then “Georeference”</p></li>
<li><p>Increase size of image using “scale” and drag over the region you wish to georeference.</p></li>
<li><p>Save</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td>Increase transparency of image</td>
<td><ul>
<li><p>Select “Raster layer”</p></li>
<li><p>Set the transparency of the image to ~50% so you can see the map underneath the image (you can adjust this to your needs)</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td>Scale the image</td>
<td><ul>
<li><p>Navigate back to the “Georeference” menu</p></li>
<li><p>Use the “scale” tool to roughly match the size of the features in the image to the features in the map’s baselayer</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td>Add control points to adjust dimensions</td>
<td><ul>
<li><p>Select “add control points”</p></li>
<li><p>Find a distinct geographic features that you can use to match the image to the map</p></li>
<li><p>The “source” is the mage, and the “target” is the basemap. Make sure to stay consistent</p></li>
<li><p>Click on the source first, and then on the same feature of the target. Do this with several features all around the image, so ArcGIS will slowly adjust the image so it better fits the dimensions and proportions of the basemap.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td>Save map</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>
