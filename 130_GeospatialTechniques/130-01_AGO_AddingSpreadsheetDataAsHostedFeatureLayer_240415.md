---
author: Paulina Salinas Ruiz
created: 2024-04-15
last_reviewed: '2025-07-08'
modified: 2024-11-26
process_number: 130-01
review_period: 3 years
title: AGO_AddingSpreadsheetDataAsHostedFeatureLayer_240415
---

**Purpose:**

To allow for the addition of spatial data (i.e. includes latitude and longitude fields) available through a spreadsheet to ArcGIS Online, in order for the use of the data in interactive maps.

Note - this process only works for spreadsheets that you wish to convert to a Vector Point format layer (i.e. non-compatible with other Vector formats such as Polygon or Polyline, or Raster format).

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
<td><p>Perform any necessary steps to prepare a spreadsheet document:</p>
<ul>
<li><p>Ensure the data is formatted as desired.</p></li>
<li><p>Ensure the sheet has no extraneous. information (e.g. title at top of spreadsheet). It should contain only data listed in rows and columns, with each column marked with a unique column header that contains no spaces.</p></li>
</ul></td>
<td>Recommended format - <em>A comma-separated values (CSV) file is a delimited text file that uses a comma to separate values. To convert an Excel Spreadsheet (.xlsx) to CSV format, open the sheet of interest within Excel and Save As Comma-delimited (.csv).</em></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td>Log into your assigned ArcGIS Online (AGO) organizational account.</td>
<td>A Username &amp; Password are required</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td>Once signed in, access the Content section by clicking <strong>Content</strong> in the AGO header bar.</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td>Select <strong>New Item</strong> on the left side of the Content section page. A pop-up should appear with the option to <strong>Drag and Drop</strong> your file of interest onto the screen. Perform this action by finding the CSV document on your computer and dragging and dropping the file into AGO. Alternatively, the file can be uploaded using a number of options (e.g. from <strong>Your device, Google Drive</strong>, <strong>Dropbox</strong>, <strong>OneDrive).</strong></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td><p>Go through the following steps in the pop-up once the file has been selected:</p>
<ul>
<li><p>Select <strong>Add CSV and create a hosted feature layer</strong></p></li>
<li><p>Unselect any fields you do not want to include and change the <strong>Display name</strong> and data <strong>Type</strong> as needed.</p></li>
<li><p>Ensure the correct fields are selected for <strong>Latitude</strong> and <strong>Longitude</strong></p></li>
<li><p>Enter contextual information for the CSV such as <strong>Title</strong>, <strong>Categories</strong>, <strong>Tags,</strong> and <strong>Summary</strong>. This information should be clear, concise, and understandable by all users.</p></li>
</ul></td>
<td><p>- Data <strong>Types</strong> include String, Date, Integer, etc.</p>
<p>- If you are unsure of the coordinate fields, first experiment adding the CSV in a GIS (e.g. QGIS)</p>
<p>- There should be pre-defined categories for you to choose from.</p></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td>The CSV should now appear in the <strong>Content</strong> page within your organizational ArcGIS Online account as a <strong>Feature Layer (Hosted)</strong>.</td>
<td>Hosted Feature Layers support vector feature querying, visualization, and editing. Hosted feature layers are most appropriate for visualizing data on top of your basemaps.</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td><p>Click the layer name in the list of layers on the Content page to open the details page for the CSV item.</p>
<p>Fill in the following sections with the necessary information:</p>
<ul>
<li><p><strong>Description</strong> (good practice to include all details you think are of importance to the public)</p></li>
<li><p><strong>Terms of Use</strong> (e.g. Intellectual Property Rights)</p></li>
<li><p><strong>Credits</strong> (e.g. Pacific Salmon Foundation – Citizen Science Program)</p></li>
</ul></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td>When you are ready for this layer to be shared with the public, change the <strong>Share</strong> settings of the CSV Hosted Feature layer from <strong>Owner</strong> to <strong>Everyone (public)</strong>. This will be a necessary step if displaying the layer in a public-facing map.</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td>Bonus Step: If you want to set default symbology and pop-up configuration for the layer, this can be done from the <strong>Visualization</strong> tab of the item’s details page.</td>
<td>This can save time if using the layer repeatedly with the same symbology.</td>
</tr>
<tr>
<td style="text-align: center;">10</td>
<td>The CSV Hosted Feature Layer is now ready for use in an ArcGIS Online Interactive Map.</td>
<td></td>
</tr>
</tbody>
</table>