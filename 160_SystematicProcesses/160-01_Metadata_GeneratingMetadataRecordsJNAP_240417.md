---
process_number: 160-01
title: Metadata_GeneratingMetadataRecordsJNAP_240417
author: Paulina Salinas Ruiz
created: 2024-04-10
modified: 2024-04-16
review_period: 3 years
---

**Purpose:**

This document serves as a guide to creating metadata records using jNAP. This approach is useful when creating one or a few records at a time, as it has a much more user-friendly interface than other metadata generator software.

Also, creating metadata outside GeoNetwork is convenient if many metadata records of similar type (or series) are created because all such records with their associated data files, links and thumbnails can be loaded in one later step (xx). 

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 68%" />
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
<p>Install jNAP if not already installed. To do so, refer to process 110-40.</p>
</blockquote></td>
<td><ul>
<li><p>jNAP is a metadata software that implements the North American Profile and follows the ISO standard very closely.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">2 </td>
<td><blockquote>
<p>Generate new File Identifier </p>
</blockquote></td>
<td><ul>
<li><p>Do so by clicking the green “+” sign at the top-right corner of the file identifier text box.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">3 </td>
<td><blockquote>
<p>Populate Metadata Record Information mandatory</p>
<p>fields (red)</p>
</blockquote></td>
<td><ul>
<li><p>Date Stamp: automatically assigned</p></li>
<li><p>Language: usually English although it could be French</p></li>
<li><p>Character Set: utf8 (default)</p></li>
<li><p>Hierarchy Level: type of data the metadata represents. Can select more than one.</p></li>
<li><p>Contact: make sure to include name, organization, position, and email when possible.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td>Populate Identification Information  mandatory fields (red)- Data Identification</td>
<td><ul>
<li><p>Language will usually be English. There are datasets that contain more than one language though and it is important to include that information.</p></li>
<li><p>Status: if unsure, inquire with data owner.</p></li>
<li><p>Maintenance: default to “Quarterly” unless otherwise specified.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td><blockquote>
<p>Populate Identification Information  mandatory fields (red)- Citation</p>
</blockquote></td>
<td><ul>
<li><p>Date: make sure to inquire and include all known dates</p></li>
<li><p>Responsible Party: make sure to include name, organization, position, and email when possible.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td><blockquote>
<p>Populate Identification Information  mandatory fields (red)- Description</p>
</blockquote></td>
<td><ul>
<li><p>Include short abstract describing information included in abstract. At least 3 sentences long. Refer to owner of data if unsure.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td><blockquote>
<p>Validate</p>
</blockquote></td>
<td><ul>
<li><p>Choose “Edit- Validate_xml”</p></li>
<li><p>If not valid, address the errors/omissions</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td><blockquote>
<p>Save to avoid from losing your work</p>
</blockquote></td>
<td><ul>
<li><p>Save as xml file with the naming convention: “YearfromDateStamp_GeographicRegion_Topic_SourceofData”, for example “2014_Clayoquot_ChinookSalmon_DFO”</p></li>
</ul></td>
</tr>
</tbody>
</table>
