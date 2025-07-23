---
author: Paulina Salinas Ruiz
created: 2024-04-15
last_reviewed: '2025-07-08'
modified: 2024-11-26
process_number: 110-05
review_period: 3 years
title: Metadata_GeneratingMetadataRecordsGeoNetwork_240415
---

**Purpose:**

The goal of this process is to provide a guide to standardize metadata records in the SGDC. The desired thumbnail and any desired data files should already be available.  If a link to a GeoServer WMS map is desired, this should also be in place. 

<table style="width:100%;">
<colgroup>
<col style="width: 17%" />
<col style="width: 31%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Step</strong> </th>
<th style="text-align: left;"><strong>Major Activity</strong> </th>
<th style="text-align: left;"><strong>References, Forms and Details</strong> </th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1 </td>
<td><blockquote>
<p>Navigate to SGDC website 🡪 Data 🡪 Marine Data BC Portal</p>
</blockquote></td>
<td><ul>
<li><p>Make sure to sign-in using your SGDC credentials</p></li>
<li><p>Navigate to metadata record and select “Edit”</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">2 </td>
<td><blockquote>
<p>Navigate to “Contribute” 🡪 “Add new record”</p>
</blockquote></td>
<td><ul>
<li><p>Select your template of choice, generally an ISO 19139 variant</p></li>
<li><p>Choose a usually “OpenData”</p></li>
<li><p>The metadata record will open in edit mode, click the “eye” drop down at the top-right corner and select “full” view.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td><blockquote>
<p>Complete the “Identification” section – fields with small red stars require a response</p>
</blockquote></td>
<td><ul>
<li><p>Enter as much information as possible</p></li>
<li><p>Defer the “graphic overview” response to step 7 below as it will be done separately.</p></li>
<li><p>Theme and place keywords should follow the ICAN recommendations (<mark>xx</mark>) if it is desired to connect to the ICAN network.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td><blockquote>
<p>Complete the “Distribution” Section</p>
</blockquote></td>
<td><ul>
<li><p>Link to data files if available</p></li>
<li><p>Link to external websites when appropriate</p></li>
<li><p>Link to external map server when available</p></li>
</ul>
<blockquote>
<p>** Make sure to adhere to naming convention in steps 10 and 11 **</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td><blockquote>
<p>Complete the “Reference System Information” and “Metadata” sections</p>
</blockquote></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">7 </td>
<td><blockquote>
<p>Add thumbnail</p>
</blockquote></td>
<td><ul>
<li><p>Always add a thumbnail.</p></li>
<li><p>Refer to process <a href="https://pacificsalmonfoundation-my.sharepoint.com/:w:/g/personal/psalinasruiz_psf_ca/EQdIk9uxw4dLhZiYUZNMFgkBGcktBKNOGNw0tCPr_BFmhg?e=6hiQao">110-06</a></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td><p>Data transfer option section is optional but desirable.  Best to do this after loading into GeoNetwork.  As protocols, use: </p>
<ul>
<li><p>For web address:</p></li>
</ul>
<p>WWW:LINK-1.0-http—link  </p>
<ul>
<li><p>For file download:</p></li>
</ul>
<p>WWW:DOWNLOAD-1.0-http—download </p>
<ul>
<li><p>For OGC Web Map Service (ver 1.1.1):</p></li>
</ul>
<p>OGC:WMS-1.1.1-http-get-map </p></td>
<td><p>There are many other protocols.  These three options are very common: </p>
<ul>
<li><p>Use an external web hyperlink to provide more information, or to link to a data provider site for added acknowledgement </p></li>
<li><p>Use the download link to provide dataset(s) </p></li>
<li><p>Use the map protocol for local map display of data features  and for Google Map display </p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td>Spatial Extent and Temporal Extent </td>
<td><ul>
<li><p>Add a “Geographic bounding box” and draw the spatial extent that best fits the metadata record</p></li>
<li><p>Make sure to include “Temporal Extent” with date range or date of documents/project. Make sure publication date is there too.  </p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">10</td>
<td>Add files to record following this naming convention: “Year_Site_Title”</td>
<td><ul>
<li><p>If the file is internal to PSF:</p>
<ul>
<li><p>Spreadsheet: protect and read only</p></li>
<li><p>Word document: convert to PDF</p></li>
</ul></li>
<li><p>If the file is NOT internal to PSF, maintain original formatting and upload following standard naming convention.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">11</td>
<td><p>Add links to record following this naming convention:</p>
<p>“Topic_WebsiteName”</p></td>
<td><ul>
<li><p>Include a short description if appropriate.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">12</td>
<td>Save record</td>
<td><ul>
<li><p>Click “Save Metadata” record and publish</p></li>
</ul></td>
</tr>
</tbody>
</table>