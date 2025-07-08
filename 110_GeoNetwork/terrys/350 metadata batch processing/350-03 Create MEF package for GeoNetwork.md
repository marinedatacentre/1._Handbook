---
process_number: 350-03
title: Create MEF package for GeoNetwork
author: Peter
created: 2015-02-22
modified: 2015-03-23
review_period: 3 years
---

**Purpose:**

This document describes how to create a metadata exchange format (mef) package for loading groups of metadata with accompanying files into GeoNetwork. There is sufficient detail required for the graphic overview and data files being added into the mef that it is best constructed programmatically.

Each metadata set in the mef package consists of a metadata record, optional graphics files, optional data files, and an “info.xml” document describing the package contents. It uses a custom python application (305-F05).

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 53%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr>
<th><strong>Step</strong></th>
<th><strong>Major Activity</strong></th>
<th><strong>References, Forms and Details</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Open a python shell</td>
<td>ActivePython is one example of a suitable shell. It has a graphical user interface</td>
</tr>
<tr>
<td>2</td>
<td><p>Navigate to the python application</p>
<ul>
<li><p>File – open - …</p></li>
</ul></td>
<td>Application is listed in 307-F03</td>
</tr>
<tr>
<td>3</td>
<td>Modify the paths, following the expected folder structure mentioned in processes 307-01 and 307-02.</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Modify the site name convention and the site UUID</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td><p>Run the application. Outputs are:</p>
<ul>
<li><p>real time feedback on-screen</p></li>
<li><p>each metadata package will be formed in tmp, consecutively</p></li>
<li><p>a log file and the final mef package (called &lt;something&gt;.zip) will be placed in the mef folder</p></li>
</ul></td>
<td></td>
</tr>
<tr>
<td>6</td>
<td><p>Errors may be noted on-screen or in the log:</p>
<ul>
<li><p>path errors</p></li>
<li><p>missing thumbnails when expected</p></li>
<li><p>missing data when expected</p></li>
</ul>
<p>Identify and correct</p></td>
<td></td>
</tr>
<tr>
<td>7</td>
<td><p>Ensure the resulting mef is less than 100 MB</p>
<ul>
<li><p>if not, split into one or more packages using the partial results from the tmp folder</p></li>
</ul></td>
<td>The 100MB limit can be changed, but it is probably a reasonable size for upload.</td>
</tr>
<tr>
<td>8</td>
<td>Upload MEF to GeoNetwork</td>
<td>Follow process 305-06</td>
</tr>
</tbody>
</table>
