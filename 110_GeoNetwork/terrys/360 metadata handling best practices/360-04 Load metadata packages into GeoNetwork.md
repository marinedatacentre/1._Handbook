---
author: Peter
created: 2014-05-10
last_reviewed: '2025-07-08'
modified: 2019-09-10
process_number: 360-04
review_period: 3 years
title: Load metadata packages into GeoNetwork
---

**Purpose:**

This document describes how to load metadata into a GeoNetwork server.

The general description is thoroughly described in the GeoNetwork User’s Manual (search web for the latest version: “GeoNetwork User Manual”). This process is to provide an abbreviated step-by-step.

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
<td>Use a browser to connect to GeoNetwork</td>
<td><ul>
<li><p>Path must be known</p></li>
</ul></td>
</tr>
<tr>
<td>2</td>
<td><ul>
<li><p>Provide ID and password</p></li>
<li><p>The <strong>Administration</strong> tab should appear next to the <strong>Home</strong> tab</p></li>
</ul></td>
<td><ul>
<li><p>The ID and PW is required to access administrative functions</p></li>
</ul></td>
</tr>
<tr>
<td>3</td>
<td><ul>
<li><p>Click the <strong>Administration</strong> tab</p></li>
<li><p>Click on the <strong>Metadata insert</strong> tab</p></li>
</ul></td>
<td><ul>
<li><p>The metadata insert section allows insertion of</p>
<ul>
<li><p>an individual metadata record in xml format, or</p></li>
<li><p>one or more metadata records (optionally plus thumbnails and data files) in a batch load.</p></li>
</ul></li>
<li><p>This latter format is called <strong>metadata exchange format</strong> (mef), and is a structured zip file. This is a recommended input format.</p></li>
</ul></td>
</tr>
<tr>
<td>4</td>
<td><ul>
<li><p>Select the mode:</p>
<ul>
<li><p>File or</p></li>
<li><p>Copy/Paste</p></li>
</ul></li>
</ul></td>
<td></td>
</tr>
<tr>
<td>5</td>
<td><ul>
<li><p>If File, select</p>
<ul>
<li><p>Single File, or</p></li>
<li><p>MEF</p></li>
</ul></li>
<li><p>Browse local storage for desired file, and select</p></li>
</ul></td>
<td></td>
</tr>
<tr>
<td>6</td>
<td><ul>
<li><p>Select desired Import action:</p>
<ol type="1">
<li><p>No action on import</p></li>
<li><p>Overwrite metadata with same UUID</p></li>
<li><p>Generate UUID for inserted metadata</p></li>
</ol></li>
</ul></td>
<td><ol type="1">
<li><p>Normal situation</p></li>
<li><p>Used if replacing metadata after some changes</p></li>
<li><p>Used if for some reason there is an existing record with the same UUID and a different metadata record is desired to be loaded. This can happen if a metadata record is being cloned, then slightly modified. This is not a preferred action, but can occur.</p></li>
</ol></td>
</tr>
<tr>
<td>7</td>
<td><ul>
<li><p>If a single metadata record is being added, then select</p>
<ol type="1">
<li><p>Stylesheet</p></li>
<li><p>Validate</p></li>
<li><p>kind</p></li>
<li><p>group</p></li>
<li><p>category</p></li>
</ol></li>
<li><p>if MEF, these choices are already determined in the MEF info.xml</p></li>
</ul></td>
<td><ol type="1">
<li><p>Normally <strong>none</strong></p></li>
<li><p>Useful to <strong>check</strong> to thoroughly determine metadata validity. The server applies schematron checks that are in addition to the schema validation.</p></li>
<li><p>Normally <strong>metadata</strong></p></li>
<li><p>As desired, from the choices previously established</p></li>
<li><p>Normally <strong>dataset</strong>, although many choices are possible</p></li>
</ol></td>
</tr>
<tr>
<td>8</td>
<td><ul>
<li><p><strong>Insert</strong> record</p></li>
</ul></td>
<td><ul>
<li><p>Often this can take seconds to many minutes. You should look for a subtle “beeble” indicator indicating the application is actively working.</p></li>
</ul></td>
</tr>
<tr>
<td>9</td>
<td><ul>
<li><p>If error, change</p>
<ul>
<li><p>metadata record, or</p></li>
<li><p>change the choices</p></li>
</ul></li>
<li><p>re-enter</p></li>
</ul></td>
<td></td>
</tr>
</tbody>
</table>