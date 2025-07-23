---
author: Paulina Salinas Ruiz
created: 2024-04-15
last_reviewed: '2025-07-08'
modified: 2024-11-26
process_number: 110-04
review_period: 3 years
title: Metadata_InstallingjNAP_240415
---

**Purpose:**

This document describes one way to create a metadata record to be later stored on the GeoNetwork server, using the java application jNAP. Creating metadata outside GeoNetwork is useful if many metadata records of a somewhat similar type or series are to be created, because all such records with their associated data files, links and thumbnails can be loaded in one later step.

Some of the jNAP features are:

- Machine independent (java application)

- Graphical interface

- Bilingual – English, French

- Creates metadata compliant with the North American profile (but using gml, not gml/3.2)

- Extensive help appears during hover over field label

- Built-in thesauri for theme (GCMD v6 and Gov of Canada keywords) and place (Canada locations)

- Automatically builds a contact list (contact.xml) that can be moved to other application installations, reducing manual data entry

- Performs metadata record generation for dataset or service applications

- Graphics overview links and data online links can be added within jNAP.

- Data Quality Reports and Lineage implemented

Other possible editing tools are listed in the document “Common Metadata Editing Tools” (X).

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 28%" />
<col style="width: 59%" />
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
<td><p>Download jNAP</p>
<ul>
<li><p>freely available from:</p></li>
</ul>
<blockquote>
<p><a href="ftp://ftp.dfo-mpo.gc.ca/BIOWebmaster/jMW2/">ftp://ftp.dfo-mpo.gc.ca/BIOWebmaster/jMW2/</a></p>
</blockquote>
<p>Choose the plain NAP version (no extension, so most current) so as to be operating system independent</p></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">2 </td>
<td><p>If a repeat installation, save the previous contact file:</p>
<p>Copy the Contact.xml file outside of the jNAP installation folder</p></td>
<td><ul>
<li><p>The jNAP is often installed in folder c:\DFO-MPO</p></li>
<li><p>Move the Contact.xml file to preserve previous entries</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">3 </td>
<td>Unzip jNAP to desired folder location</td>
<td><ul>
<li><p>jNAP application will be at</p></li>
</ul>
<p>&lt;desired location&gt;\jNAP</p></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td>Copy (Overwrite) Contact.xml in jNAP folder with saved version</td>
<td><ul>
<li><p>Right-click the item, and then click Create shortcut</p></li>
<li><p>Browse to the location of jMW_NAP.jar</p></li>
<li><p>Change name to that desired</p></li>
<li><p>Right-click created icon and select properties</p></li>
<li><p>Change “start in” to a convenient location where you will be editing metadata</p></li>
</ul>
<p>Browse and change icon to jNAP icon. The jNAP icon is available from ………</p></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td>Create a shortcut icon</td>
<td><ul>
<li><p>Right-click the item, and then click Create shortcut</p></li>
<li><p>Browse to the location of jMW_NAP.jar</p></li>
<li><p>Change name to that desired</p></li>
<li><p>Right-click created icon and select properties</p></li>
<li><p>Change “start in” to a convenient location where you will be editing metadata</p></li>
<li><p>Browse and change icon to jNAP icon. The jNAP icon is available from ………</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td><p>Move the icon to where you wish</p>
<ul>
<li><p>Start menu/Desktop</p></li>
</ul></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td>Validate that jNAP opens when icon chosen, and start location correct</td>
<td><ul>
<li><p>If not valid, fix the errors/omissions</p></li>
</ul></td>
</tr>
</tbody>
</table>