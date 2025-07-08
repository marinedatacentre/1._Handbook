---
process_number: 140-01
title: FME_DynamicallyRead&WriteADataset_240416
author: Paulina Salinas Ruiz
created: 2024-04-16
modified: 2024-11-26
review_period: 3 years
---

**Purpose:**

This document describes how to read a generic dataset and write it out without prior knowledge of the schema. In particular, an example situation where esri rest layer services are read from a spreadhseet list and out put to PostgreSQL database tables is documented in this process.

Note: A dataset can not be dynamically read into an FME workspace and undergo automated data transformation operations, due to it’s attributes being unexposed. Dynamic read / write functionalities only can be automated.

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
<td>Create or acquire a dynamic source dataset.</td>
<td>In this case, a spreadsheet with a list of esri REST layer service URLS was created.</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td>Open FME Desktop and create a new workspace.</td>
<td><p>A license is required to operate.</p>
<p>- Software download - https://www.safe.com/support/downloads/</p></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td>Add a reader to the workspace for the spreadsheet containing the URL list.</td>
<td>Note – there are likely other alternatives for dynamically reading sources. Search the FME Community forums for additional insight on ‘Dynamic Readers’.</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td><p>Add a FeatureReader transformer to the workspace, connect the CSV reader output port to the FeatureReader Initiator port, and set parameters of the FeatureReader. Parameters were set as:</p>
<ul>
<li><p>Format: Esri-JSON</p></li>
<li><p>Dataset: [url column name]</p></li>
<li><p>Features to Read: Schema and Data Features</p></li>
<li><p>Output Ports: Single Output Port</p></li>
<li><p>Attribute and Geometry Handling:</p>
<ul>
<li><p>Merge Initiator and Result</p></li>
<li><p>Use Result</p></li>
<li><p>No</p></li>
<li><p>Use Result</p></li>
</ul></li>
</ul></td>
<td>Note – parameters may need to be altered depending on input feature type and desired output.</td>
</tr>
<tr>
<td style="text-align: center;">5a</td>
<td>Add a PostGIS Writer to the workspace. Connect to the database where you wish for the table to be created or updated.</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">5b</td>
<td><p>Under the User Attributes tab of the Feature Type window, set Attribute Definition to ‘Dynamic’.</p>
<p>When setting the Feature Type Parameters of the writer, the following were used.</p>
<ul>
<li><p>Table Name: [layer name column from list]</p></li>
<li><p>Schema Sources: “Schema From Schema Feature”</p></li>
<li><p>Schema Definition Name: fme_feature_type</p></li>
<li><p>Feature Operation: Insert</p></li>
<li><p>Table Handling: Drop and Create</p></li>
</ul></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td>Run the workflow &amp; ensure it operates without error.</td>
<td>Note – there is the possibility to automate this workflow by uploading it to FME Server.</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td>Check that the table has been created as desired using PSQL from the command line of PGadmin4 GUI.</td>
<td>Further validation can be completed by viewing the database table in a desktop GIS.</td>
</tr>
</tbody>
</table>
