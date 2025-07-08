---
process_number: 110-07
title: Metadata_CreatingFeatureCatalogueWithinGeoNetwork_240415
author: Paulina Salinas Ruiz
created: 2024-04-15
modified: 2024-11-26
review_period: 3 years
---

**Purpose:**

This document describes how to create a feature catalogue metadata record within the GeoNetwork server. Any desired GeoNetwork metadata records for the dataset associated with the feature catalogue should already be available. 

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 60%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr>
<th><strong>Step</strong> </th>
<th><strong>Major Activity</strong> </th>
<th><strong>References, Forms and Details</strong> </th>
</tr>
</thead>
<tbody>
<tr>
<td>1 </td>
<td><blockquote>
<p>Use a browser to connect to GeoNetwork </p>
</blockquote></td>
<td><ul>
<li><p>If on the local computer, the address is usually <a href="http://localhost:8080/geonetwork"><u>http://localhost:8080/geonetwork</u></a> </p></li>
</ul></td>
</tr>
<tr>
<td>2 </td>
<td><ul>
<li><p>Provide ID and password </p></li>
<li><p>The <strong>Administration</strong> tab should appear next to the <strong>Home</strong> tab </p></li>
</ul></td>
<td><ul>
<li><p>The ID and PW is required to access administrative functions, and specifically the &lt;edit&gt; tab at the bottom of each metadata search result. </p></li>
<li><p>The default ID/PW is admin/admin </p></li>
</ul></td>
</tr>
<tr>
<td><ol start="3" type="1">
<li></li>
</ol></td>
<td><ul>
<li><p>Click the ‘Admin console’ button at the top of the screen </p></li>
<li><p>Select ‘Metadata &amp; templates’  </p></li>
<li><p>Check the box for ‘Geographic information – Methodology for feature cataloguing (iso19110) </p></li>
<li><p>Choose to ‘Load templates for selected standards’ </p></li>
<li><p>Access the newly created template through the list of records that appear when the ‘Contribute’ button is clicked at the top of the screen </p></li>
<li><p>Click the blue ‘Edit’ button to switch to edit mode </p></li>
</ul></td>
<td><ul>
<li><p>The newly created record should initially be called ‘Feature catalogue template in ISO19110’ </p></li>
<li><p>The feature catalogue metadata record will open in ‘Default View’  </p></li>
</ul></td>
</tr>
<tr>
<td>4 </td>
<td><blockquote>
<p>Complete the ‘Feature Catalogue description’ section </p>
</blockquote>
<ul>
<li><p>Enter as many responses as possible </p></li>
<li><p>Fields with small red stars require a response </p></li>
</ul></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr>
<td>5 </td>
<td><blockquote>
<p>Complete the ‘Catalogue producer’ section </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr>
<td>6 </td>
<td><blockquote>
<p>Begin work on the ‘Elements’ section of the catalogue </p>
</blockquote>
<ul>
<li><p>Fill in ‘member name’ with the name of the attribute </p></li>
<li><p>Assign an attribute definition </p></li>
<li><p>For ‘gco:lower’ use a value of 0 </p></li>
<li><p>Fill in ‘Type name’ with the data type the attribute falls under </p></li>
<li><p>Once this information has been completed, if necessary, add a new attribute and repeat step 6 </p></li>
</ul></td>
<td><ul>
<li><p>‘Definition’ is optional </p></li>
</ul></td>
</tr>
<tr>
<td>7 </td>
<td><blockquote>
<p>If codes are used in the dataset you are cataloguing, perform the following </p>
</blockquote>
<ul>
<li><p>Save the GeoNetwork feature catalogue record </p></li>
<li><p>Switch to ‘Full’ view by clicking the eye symbol in the top right corner of the page </p></li>
<li><p>You should now have the option to add a CodeList to any of the attributes you have previously added to the record </p></li>
<li><p>For each attribute that contains codes add a CodeList, filling in ‘Label’ with the meaning of the code and ‘Code’ with the abbreviation used </p></li>
</ul></td>
<td><ul>
<li><p>This step is optional, however If codes are present it is highly desirable </p></li>
</ul></td>
</tr>
<tr>
<td>8 </td>
<td><blockquote>
<p>To add definitions for the codes, perform the following </p>
</blockquote>
<ul>
<li><p>Save the GeoNetwork feature catalogue record </p></li>
<li><p>Select ‘Full’ view in the top right corner of the page  </p></li>
<li><p>You should now have the option to add a definition for the codes you have previously added to the record </p></li>
</ul></td>
<td><ul>
<li><p>Despite already being in ‘Full’ view mode, certain elements of the page will not display unless ‘Full’ view mode is selected again </p></li>
<li><p>The step to add code definitions is optional but desirable if codes are present in the catalogue </p></li>
</ul></td>
</tr>
<tr>
<td>9 </td>
<td><blockquote>
<p>Validate the record and fix any errors that are present </p>
</blockquote></td>
<td><ul>
<li><p>If the error <em>“ is not a valid value for ‘integer’. (Element: gco:UnlimitedInteger with parent element: gco: upper)</em> is present, correct it by performing the following: </p></li>
</ul>
<ul>
<li><p>Switch to ‘XML’ view and copy the code into a text editor.  </p></li>
<li><p>Manually replace all occurrences of <em>&lt;gco:UnlimitedInteger/&gt;</em> with <em>&lt;gco:UnlimitedInteger xsi:nil="false" isInfinite="false"&gt;1&lt;/gco:UnlimitedInteger&gt;</em> </p></li>
<li><p>Import the updated XML file to GeoNetwork and validate again </p></li>
</ul></td>
</tr>
<tr>
<td>10 </td>
<td><blockquote>
<p>Save the record </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr>
<td>11 </td>
<td><blockquote>
<p>If a GeoNetwork metadata record is present for the dataset associated with the feature catalogue, link the newly created feature catalogue record to it as a resource </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
</tbody>
</table>
