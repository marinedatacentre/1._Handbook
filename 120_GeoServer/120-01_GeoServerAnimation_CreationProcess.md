---
last_reviewed: '2025-06-26'
---

**Purpose:**

To create an animation using GeoServer that employs the time dimension capability of a layer, while pulling data from a PostGIS database. The final result is a gif created through a get map request, showing the change of a selected attribute over time.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 49%" />
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
<td style="text-align: center;"><strong>1</strong></td>
<td>In GeoServer create an appropriately named <em>workspace</em> with WMS services enabled.</td>
<td><p>-Documentation on GeoServer processes, such as creating workspaces, can be found at the official GeoServer website:</p>
<ul>
<li><p>http://docs.geoserver.org/latest/en/user/index.html</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>2</strong></td>
<td><p>Create a new <em>store</em> from a PostGIS data source in GeoServer and call it the same thing as the PostGIS table from which it is pulling. (If you do not have a PostGIS table with a time enabled date column follow steps 2a and 2b, otherwise proceed to step 3.)</p>
<p>*Alternatively a <em>store</em> can be created from a shapefile instead of a PostGIS table, as long as there is a column of type ‘date’.</p></td>
<td><ul>
<li><p>Mandatory fields to fill for the new <em>store</em> are:</p>
<ul>
<li><p>Workspace</p></li>
<li><p>dbtype</p></li>
<li><p>host</p></li>
<li><p>port</p></li>
<li><p>database</p></li>
<li><p>schema</p></li>
<li><p>user</p></li>
<li><p>passwd</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>2.a</strong></td>
<td>If you are starting from a points shapefile with date information, the date column must be of type ‘date’.</td>
<td><ul>
<li><p>This is necessary information for GeoServer’s WMS Animator .</p></li>
<li><p>A ‘date’ field can be created using the field calculator in ArcGIS and QGIS.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>2.b</strong></td>
<td>Your shapefile can be then be imported into a spatially enabled PostGIS database through the command line.</td>
<td><p>-View the following website to see the necessary command:</p>
<ul>
<li><p>http://suite.opengeo.org/docs/latest/dataadmin/pgGettingStarted/shp2pgsql.html</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>3</strong></td>
<td>If the PostGIS table was successfully connected through the new store, the option to publish the desired table will become an option. Publish the layer, name it something appropriate and set the Declared SRS to EPSG:4326. For the bounding box select ‘compute from data’ and ‘compute from native bounds’. Under the <em>Dimensions</em> tab of the layer, enable Time, set the <em>Attribute</em> to the date column and the <em>Presentation</em> to List.</td>
<td><ul>
<li><p>The time dimension will only be allowed to be enabled as long as the PostGIS table or shapefile has a column of type ‘date’.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>4</strong></td>
<td>Test that your layer is working by selecting it in <em>layer preview</em>. Select a point to see its attributes. If the layer is not showing refer back to the previous steps, using the GeoServer website for more in depth information.</td>
<td><p>-Official GeoServer website:</p>
<ul>
<li><p>http://docs.geoserver.org/latest/en/user/index.html</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>5</strong></td>
<td>Create a store and layer for the raster or vector layer you wish to use as a basemap in the animation. Follow the same procedure for the coordinate system and bounding box.</td>
<td><ul>
<li><p>Rather than a PostGIS table it may be a shapefile.</p></li>
<li><p>Dimensions do not have to be set.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>6</strong></td>
<td>In GeoServer, create the <em>style</em> you wish to use for the animation. The style should be selected based on what you think the best way to represent the data is. The GeoServer website provides a range of examples. Set the format to SLD (or download the YSLD extension for simplified coding), and alter the selected styles color ramp and attributes as needed.</td>
<td><ul>
<li><p>Examples of styles include rendering transformations (Barnes Surface, Heatmaps) and categorize.</p></li>
<li><p>Rendering transformations - <a href="http://docs.geoserver.org/2.2.0/user/styling/sld-extensions/rendering-transform.html">http://docs.geoserver.org/2.2.0/user/styling/sld-extensions/rendering-transform.html</a></p></li>
<li><p>Categorize - http://docs.geoserver.org/2.3.2/user/styling/sld-tipstricks/transformation-func.html</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>7</strong></td>
<td>Create an appropriately named <em>Layer Group</em>. Add the layer with the attributes of interest and set its style to the one you have created. Add the basemap layer and compute the bounding box as with the individual layers.</td>
<td><ul>
<li><p>If you want the styled layer to appear below the basemap, ensure the basemap is at the bottom of the drawing order.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>8</strong></td>
<td>Use <em>layer preview</em> to test that your layer group is rendered effectively.</td>
<td><p>-The time dimension can be tested by adding ‘&amp;time=’ with a date, year or month at the end of the layer preview url.</p>
<ul>
<li><p>Ex/ &amp;time=1989</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>9</strong></td>
<td>In order to add layout elements such as a title, legend and scale to the animation, a layout xml file has to be created. If using an independent version of GeoServer, the layout xml folder goes in the ‘layouts’ sub-directory. If using a version of GeoServer bundled with GeoNetwork, create a layouts folder in the ‘data’ sub-directory of GeoServer.</td>
<td><p>-For a detailed description of all <em>WMS Decorations</em> for layouts see:</p>
<ul>
<li><p><a href="http://docs.geoserver.org/latest/en/user/services/wms/decoration.html">http://docs.geoserver.org/latest/en/user/services/wms/decoration.html</a></p></li>
</ul>
<p>-In order to display the year, month or date each frame represents include the text decoration:</p>
<ul>
<li><p>value="${avalue}"</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>9.a</strong></td>
<td>In order to render a legend that doesn’t also include the basemap, it may be best to include a GetLegend Graphic call as an image decoration in the xml file.</td>
<td><p>-Instructions on how to format a get legend graphic:</p>
<ul>
<li><p>http://docs.geoserver.org/2.7.0/user/services/wms/get_legend_graphic/legendgraphic.html</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>10</strong></td>
<td><p>Now that all the necessary elements are completed, the WMS Animator get map request can be composed. Through the get map request, the layer group is called, the bounding box, width and height are set, the dates of interest are specified and the layout xml file is referred to.</p>
<p>Depending on the style chosen and the number of frames requested, the load time can be lengthy. By altering certain attributes of the style, load time can be shorted.</p></td>
<td><p>-For a detailed overview of the WMS Animator function:</p>
<ul>
<li><p>http://docs.geoserver.org/stable/en/user/tutorials/animreflector.html</p></li>
</ul>
<p>-Example of a completed request:</p>
<ul>
<li><p>http://localhost:8080/geoserver/lighthouse/wms/animate?layers=lighthouse:BC_Coastal_lighthouses&amp;styles=&amp;bbox=-137.05,46.7,-117,55.8&amp;width=750&amp;height=500&amp;aparam=time&amp;avalues=1936, 1946,1956,1966,1976,1986,1996,2006,2012&amp;format=image/gif;subtype=animated&amp;format_options=layout:lighthouse_layout;gif_loop_continuosly:true</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>11</strong></td>
<td>If your animation displays, your get map request is composed correctly. If not make adjustments as necessary, referring to the GeoServer WMS Animator page for help. Make adjustments to the layout and style as needed.</td>
<td></td>
</tr>
</tbody>
</table>