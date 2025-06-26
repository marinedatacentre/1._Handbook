**Purpose:**

This document is meant to outline the procedure for creating or modifying a layer in QGIS though the process of digitization. Digitization in this context refers to the usage of a GIS to create new point, line, or polygon features meant to serve as a representation of some real-world geographic feature.

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
<td>A QGIS Standalone Installer is available at the following link at the time this document is being written - https://qgis.org/en/site/forusers/download.html</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td>Open QGIS and start a new project or open one that you have previously been working on.</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">3 (optional)</td>
<td><p>If this is the first time using QGIS on your machine, you will want to install a plugin that allows you to view basemaps. To install the Quick Map Services plugin:</p>
<ul>
<li><p>Open QGIS. Go to Plugins Menu -&gt; Manage and Install Plugins,</p></li>
<li><p>In the Plugins Window, search for QuickMapServices then click the Install button,</p></li>
<li><p>After it installs, you should be able to find QuickMapServices button in the Web Toolbar.</p></li>
</ul></td>
<td>Note: Basemaps are the background maps that let you know what part of the world you are viewing.</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td><p>Create a new layer (or use a pre-existing layer that you have been digitizing from)</p>
<p>When creating for the first time, in the ‘New Layer’ parameters box:</p>
<ul>
<li><p>Select a File name.</p></li>
<li><p>Select a Geometry type.</p></li>
</ul>
<p>The rest can be left as default.</p></td>
<td><p>Recommended method:</p>
<p>‘Layer’ menu - &gt; ‘Create Layer’ -&gt; ‘New Shapefile Layer’</p></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td>Turn on editor mode for the layer you wish to perform digitizing with.</td>
<td><p>Recommended method:</p>
<p>Right-click the Layer name for the newly created layer and select ‘Toggle Editing’.</p></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td><p>Set the desired Fields you wish to have within the dataset.</p>
<p>Recommended method:</p>
<ul>
<li><p>Right click the layer name in the Layers List, selecting ‘Properties’ in the dropdown,</p></li>
<li><p>Select the ‘Fields’ pane,</p></li>
<li><p>In the top-left of the box, select ‘New field’,</p></li>
<li><p>Fill out the ‘Add Field’ popup parameters.</p></li>
</ul></td>
<td><p>Note: There are a few attribute types to select from when adding a field:</p>
<p><strong>Type Name E.g.</strong></p>
<p>Whole number Integer 4</p>
<p>Decimal number Real 3.456</p>
<p>Text String Hello</p>
<p>Date Date 2016-07-28</p></td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td>Add a feature to the layer of interest:</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">7a</td>
<td>In the row of buttons in the toolbar near the top, click the one labeled ‘Add … Feature’ (e.g. Add Line Feature)</td>
<td>Note: It could be Line, Point, or Polygon depending on what geom type was selected when the layer was created.</td>
</tr>
<tr>
<td style="text-align: center;">7b</td>
<td><p>Using the basemap added in step 3 as reference, hover your mouse within the map to where you would like a vertex and click to add it.</p>
<p>… If you are creating a point feature, you can move on to step 7e, if creating a line or polygon see step 7c.</p></td>
<td>Note: vertexes are used to define unique segments of a feature, e.g. a multi-line would be composed of different segments with vertexes at each end.</td>
</tr>
<tr>
<td style="text-align: center;">7c</td>
<td>If creating a line or polygon, following the placement of the first vertex, place the second vertex at the desired location, keeping in mind necessary orientation.</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">7d</td>
<td><p>Repeat step 7c until you are satisfied with the shape of your feature.</p>
<p>When you are ready to complete the feature, press the right-mouse button.</p></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">7e</td>
<td><p>When the geometry for the feature has been drawn, a popup will appear asking you to fill in ‘Feature Attributes’.</p>
<p>Assign the appropriate related information to the field(s).</p></td>
<td>Note: An id is required for each unique feature. The id allows the GIS to distinguish these features. Assigning sequential numerical values is standard (E.g. 1, 2, 3).</td>
</tr>
<tr>
<td style="text-align: center;">8 (optional)</td>
<td><p>If the placement of a feature needs to be adjusted after it has been set, the ‘Vertex Tool’ can be used to:</p>
<ul>
<li><p>Click on the vertex of interest,</p></li>
<li><p>Move it to a new desired location.</p></li>
</ul></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">9 (optional)</td>
<td><p>If the attributes of a feature need to be adjusted after the have been set, right click the layer name in the layer list to ‘Open Attribute Table’:</p>
<ul>
<li><p>Within the attribute table, find the correct feature,</p></li>
<li><p>Double click the cell that holds the value you wish to change,</p></li>
<li><p>Enter a new value.</p></li>
</ul></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">10</td>
<td>Click the ‘Save Layer Edits’ button to register your changes/additions.</td>
<td>Saving often is recommended.</td>
</tr>
<tr>
<td style="text-align: center;">11</td>
<td>When done editing, select ‘Toggle Editing’ to turn editor mode off.</td>
<td></td>
</tr>
</tbody>
</table>
