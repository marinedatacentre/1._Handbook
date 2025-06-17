**Purpose:**

This document is meant to outline the procedure for creating or
modifying a layer in QGIS though the process of digitization.
Digitization in this context refers to the usage of a GIS to create new
point, line, or polygon features meant to serve as a representation of
some real-world geographic feature.

+------------+-----------------------------------+-------------------------------------------------+
| **Step**   | **Major Activity**                | **References, Forms and Details**               |
+:==========:+===================================+=================================================+
| 1          | Download and install the latest   | A QGIS Standalone Installer is available at the |
|            | version of QGIS if you do not     | following link at the time this document is     |
|            | already have it on your machine.  | being written -                                 |
|            |                                   | https://qgis.org/en/site/forusers/download.html |
+------------+-----------------------------------+-------------------------------------------------+
| 2          | Open QGIS and start a new project |                                                 |
|            | or open one that you have         |                                                 |
|            | previously been working on.       |                                                 |
+------------+-----------------------------------+-------------------------------------------------+
| 3          | If this is the first time using   | Note: Basemaps are the background maps that let |
| (optional) | QGIS on your machine, you will    | you know what part of the world you are         |
|            | want to install a plugin that     | viewing.                                        |
|            | allows you to view basemaps. To   |                                                 |
|            | install the Quick Map Services    |                                                 |
|            | plugin:                           |                                                 |
|            |                                   |                                                 |
|            | - Open QGIS. Go to Plugins Menu   |                                                 |
|            |   -\> Manage and Install Plugins, |                                                 |
|            |                                   |                                                 |
|            | - In the Plugins Window, search   |                                                 |
|            |   for QuickMapServices then click |                                                 |
|            |   the Install button,             |                                                 |
|            |                                   |                                                 |
|            | - After it installs, you should   |                                                 |
|            |   be able to find                 |                                                 |
|            |   QuickMapServices button in the  |                                                 |
|            |   Web Toolbar.                    |                                                 |
+------------+-----------------------------------+-------------------------------------------------+
| 4          | Create a new layer (or use a      | Recommended method:                             |
|            | pre-existing layer that you have  |                                                 |
|            | been digitizing from)             | 'Layer' menu - \> 'Create Layer' -\> 'New       |
|            |                                   | Shapefile Layer'                                |
|            | When creating for the first time, |                                                 |
|            | in the 'New Layer' parameters     |                                                 |
|            | box:                              |                                                 |
|            |                                   |                                                 |
|            | - Select a File name.             |                                                 |
|            |                                   |                                                 |
|            | - Select a Geometry type.         |                                                 |
|            |                                   |                                                 |
|            | The rest can be left as default.  |                                                 |
+------------+-----------------------------------+-------------------------------------------------+
| 5          | Turn on editor mode for the layer | Recommended method:                             |
|            | you wish to perform digitizing    |                                                 |
|            | with.                             | Right-click the Layer name for the newly        |
|            |                                   | created layer and select 'Toggle Editing'.      |
+------------+-----------------------------------+-------------------------------------------------+
| 6          | Set the desired Fields you wish   | Note: There are a few attribute types to select |
|            | to have within the dataset.       | from when adding a field:                       |
|            |                                   |                                                 |
|            | Recommended method:               | **Type Name E.g.**                              |
|            |                                   |                                                 |
|            | - Right click the layer name in   | Whole number Integer 4                          |
|            |   the Layers List, selecting      |                                                 |
|            |   'Properties' in the dropdown,   | Decimal number Real 3.456                       |
|            |                                   |                                                 |
|            | - Select the 'Fields' pane,       | Text String Hello                               |
|            |                                   |                                                 |
|            | - In the top-left of the box,     | Date Date 2016-07-28                            |
|            |   select 'New field',             |                                                 |
|            |                                   |                                                 |
|            | - Fill out the 'Add Field' popup  |                                                 |
|            |   parameters.                     |                                                 |
+------------+-----------------------------------+-------------------------------------------------+
| 7          | Add a feature to the layer of     |                                                 |
|            | interest:                         |                                                 |
+------------+-----------------------------------+-------------------------------------------------+
| 7a         | In the row of buttons in the      | Note: It could be Line, Point, or Polygon       |
|            | toolbar near the top, click the   | depending on what geom type was selected when   |
|            | one labeled 'Add ... Feature'     | the layer was created.                          |
|            | (e.g. Add Line Feature)           |                                                 |
+------------+-----------------------------------+-------------------------------------------------+
| 7b         | Using the basemap added in step 3 | Note: vertexes are used to define unique        |
|            | as reference, hover your mouse    | segments of a feature, e.g. a multi-line would  |
|            | within the map to where you would | be composed of different segments with vertexes |
|            | like a vertex and click to add    | at each end.                                    |
|            | it.                               |                                                 |
|            |                                   |                                                 |
|            | ... If you are creating a point   |                                                 |
|            | feature, you can move on to step  |                                                 |
|            | 7e, if creating a line or polygon |                                                 |
|            | see step 7c.                      |                                                 |
+------------+-----------------------------------+-------------------------------------------------+
| 7c         | If creating a line or polygon,    |                                                 |
|            | following the placement of the    |                                                 |
|            | first vertex, place the second    |                                                 |
|            | vertex at the desired location,   |                                                 |
|            | keeping in mind necessary         |                                                 |
|            | orientation.                      |                                                 |
+------------+-----------------------------------+-------------------------------------------------+
| 7d         | Repeat step 7c until you are      |                                                 |
|            | satisfied with the shape of your  |                                                 |
|            | feature.                          |                                                 |
|            |                                   |                                                 |
|            | When you are ready to complete    |                                                 |
|            | the feature, press the            |                                                 |
|            | right-mouse button.               |                                                 |
+------------+-----------------------------------+-------------------------------------------------+
| 7e         | When the geometry for the feature | Note: An id is required for each unique         |
|            | has been drawn, a popup will      | feature. The id allows the GIS to distinguish   |
|            | appear asking you to fill in      | these features. Assigning sequential numerical  |
|            | 'Feature Attributes'.             | values is standard (E.g. 1, 2, 3).              |
|            |                                   |                                                 |
|            | Assign the appropriate related    |                                                 |
|            | information to the field(s).      |                                                 |
+------------+-----------------------------------+-------------------------------------------------+
| 8          | If the placement of a feature     |                                                 |
| (optional) | needs to be adjusted after it has |                                                 |
|            | been set, the 'Vertex Tool' can   |                                                 |
|            | be used to:                       |                                                 |
|            |                                   |                                                 |
|            | - Click on the vertex of          |                                                 |
|            |   interest,                       |                                                 |
|            |                                   |                                                 |
|            | - Move it to a new desired        |                                                 |
|            |   location.                       |                                                 |
+------------+-----------------------------------+-------------------------------------------------+
| 9          | If the attributes of a feature    |                                                 |
| (optional) | need to be adjusted after the     |                                                 |
|            | have been set, right click the    |                                                 |
|            | layer name in the layer list to   |                                                 |
|            | 'Open Attribute Table':           |                                                 |
|            |                                   |                                                 |
|            | - Within the attribute table,     |                                                 |
|            |   find the correct feature,       |                                                 |
|            |                                   |                                                 |
|            | - Double click the cell that      |                                                 |
|            |   holds the value you wish to     |                                                 |
|            |   change,                         |                                                 |
|            |                                   |                                                 |
|            | - Enter a new value.              |                                                 |
+------------+-----------------------------------+-------------------------------------------------+
| 10         | Click the 'Save Layer Edits'      | Saving often is recommended.                    |
|            | button to register your           |                                                 |
|            | changes/additions.                |                                                 |
+------------+-----------------------------------+-------------------------------------------------+
| 11         | When done editing, select 'Toggle |                                                 |
|            | Editing' to turn editor mode off. |                                                 |
+------------+-----------------------------------+-------------------------------------------------+
