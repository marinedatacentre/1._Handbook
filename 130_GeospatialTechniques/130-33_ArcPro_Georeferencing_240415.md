**Purpose:**

Scanned maps and historical data usually do not contain spatial
reference information. In these cases, we need to use accurate location
data to align or georeference our raster data to a map coordinate
system. A map coordinate system is defined using a map projection-a
method by which the curved surface of the earth is portrayed on a flat
surface.

When georeferencing raster data, we define its location using map
coordinates and assign the coordinate system of the map frame.
Georeferencing raster data allows it to be viewed, queried, and analyzed
with your other geographic data.

+-----------+-------------------------+-------------------------------+
| **Step**  | **Major Activity**      | **References, Forms and       |
|           |                         | Details**                     |
+:=========:+=========================+===============================+
| 1         | Launch ArcGIS Pro and   | - Navigate to the "Map" tab   |
|           | import the image        |                               |
|           |                         | - Select the "Add Data" drop  |
|           |                         |   down menu and choose "Data" |
|           |                         |                               |
|           |                         | - Select the image you'd like |
|           |                         |   to georeference             |
|           |                         |                               |
|           |                         | - If you're presented with    |
|           |                         |   multiple band choices,      |
|           |                         |   select band 1               |
+-----------+-------------------------+-------------------------------+
| 2         | Find the image on the   | - Right click the image name  |
|           | map and overlay it on   |   on the Table of Contents    |
|           | region of choice        |   and select "Zoom to Layer"  |
|           |                         |                               |
|           |                         | - Select the "Imagery" tab    |
|           |                         |   and then "Georeference"     |
|           |                         |                               |
|           |                         | - Increase size of image      |
|           |                         |   using "scale" and drag over |
|           |                         |   the region you wish to      |
|           |                         |   georeference.               |
|           |                         |                               |
|           |                         | - Save                        |
+-----------+-------------------------+-------------------------------+
| 3         | Increase transparency   | - Select "Raster layer"       |
|           | of image                |                               |
|           |                         | - Set the transparency of the |
|           |                         |   image to \~50% so you can   |
|           |                         |   see the map underneath the  |
|           |                         |   image (you can adjust this  |
|           |                         |   to your needs)              |
+-----------+-------------------------+-------------------------------+
| 4         | Scale the image         | - Navigate back to the        |
|           |                         |   "Georeference" menu         |
|           |                         |                               |
|           |                         | - Use the "scale" tool to     |
|           |                         |   roughly match the size of   |
|           |                         |   the features in the image   |
|           |                         |   to the features in the      |
|           |                         |   map's baselayer             |
+-----------+-------------------------+-------------------------------+
| 5         | Add control points to   | - Select "add control points" |
|           | adjust dimensions       |                               |
|           |                         | - Find a distinct geographic  |
|           |                         |   features that you can use   |
|           |                         |   to match the image to the   |
|           |                         |   map                         |
|           |                         |                               |
|           |                         | - The "source" is the mage,   |
|           |                         |   and the "target" is the     |
|           |                         |   basemap. Make sure to stay  |
|           |                         |   consistent                  |
|           |                         |                               |
|           |                         | - Click on the source first,  |
|           |                         |   and then on the same        |
|           |                         |   feature of the target. Do   |
|           |                         |   this with several features  |
|           |                         |   all around the image, so    |
|           |                         |   ArcGIS will slowly adjust   |
|           |                         |   the image so it better fits |
|           |                         |   the dimensions and          |
|           |                         |   proportions of the basemap. |
+-----------+-------------------------+-------------------------------+
| 6         | Save map                |                               |
+-----------+-------------------------+-------------------------------+
