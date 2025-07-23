---
author: Peter
created: 2021-11-10
last_reviewed: '2025-07-08'
modified: 2021-11-10
process_number: 360-40
review_period: 3 years
title: Remove a metadata resource directly on the GeoNetwork server
---

**Purpose:**

This is occasionally required if the resource cannot be removed using the GeoNetwork Administration access. Extreme caution is cautioned, because it is easy to disable GeoNetwork.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 49%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Step</strong></th>
<th><strong>Major Activity</strong></th>
<th><blockquote>
<p><strong>References, Forms and Details</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>1</strong></td>
<td><p>Obtain the location of the store for the problem metadata record. In the Geonetwork main page,</p>
<ul>
<li><p>access the metadata record (search)</p></li>
<li><p>download the zip file</p></li>
<li><p>open the zip and select “index”</p></li>
<li><p>the record number should be available</p></li>
</ul></td>
<td><ul>
<li><p>e.g. record 02439</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>2</strong></td>
<td>If required, enable a VPN connection to the server.</td>
<td><ul>
<li><p>For UBC, this means using a connection to myvpn.ubc.ca</p></li>
<li><p>This requires a campus-wide logon and password.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>3</strong></td>
<td><p>Switch to superuser</p>
<blockquote>
<p>sudo -i</p>
</blockquote></td>
<td><ul>
<li><p>Usually the webserver is run by a dedicated user (tomcat or jetty is common), and superuser allows access to all files.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>4</strong></td>
<td>Navigate to the geonetwork store</td>
<td><ul>
<li><p>For PSF, this is</p></li>
</ul>
<blockquote>
<p>cd /data/gn_dir/data/metadata_data</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><strong>5</strong></td>
<td>And to the desired record group and record</td>
<td><ul>
<li><p>e.g.</p></li>
</ul>
<p>group 02400-02499</p>
<p>record 02439</p></td>
</tr>
<tr>
<td style="text-align: center;"><strong>6</strong></td>
<td>Open the ‘public’ folder and perform duties</td>
<td><ul>
<li><p>this contains the files associated with the metadata</p></li>
<li><p>normally this is to delete (Linux ‘rm’) files</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>7</strong></td>
<td>Exit the server</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;"><strong>8</strong></td>
<td><p>In GeoNetwork, check that all references to deleted files have been removed.</p>
<p>If not, delete links</p></td>
<td><ul>
<li><p>be very careful not to remove valid links</p></li>
</ul></td>
</tr>
</tbody>
</table>