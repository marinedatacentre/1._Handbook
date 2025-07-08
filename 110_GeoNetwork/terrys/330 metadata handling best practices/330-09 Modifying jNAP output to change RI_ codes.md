---
process_number: 330-09
title: Modifying jNAP output to change RI_ codes
author: Peter
created: 2017-02-26
modified: 2024-04-15
review_period: 3 years
---

**Purpose:**

This document describes how to alter a metadata record that contains “RI_nnn” codes to more-standard English. This normally occurs with records created by jNAP. This is an optional step.

To do so uses a custom XSLT and can be run in the free text editor Notepad++ (NPP) with the XML Tools plugin installed.

The following process describes the one-time complete installation of NPP and XML Tools. Subsequent transformations only require steps 4 and 5.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 47%" />
<col style="width: 41%" />
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
<td>Download and install NPP, if necessary. Choose the <strong>32-bit version</strong>, because the 64 bit version does not presently support the plugin manager</td>
<td><ul>
<li><p><a href="https://notepad-plus-plus.org/">https://notepad-plus-plus.org/</a></p></li>
<li><p>The latest downloads include plugin manager</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td><p>Download and install “XML Tools” using plugin manager</p>
<ul>
<li><p>Open NPP</p></li>
<li><p>Select Plugins, Show Plugin Manager</p></li>
<li><p>Choose and install XML Tools</p></li>
<li><p>Accept all prompts and reboots</p></li>
<li><p>XML Tools should now be present on the dropdown Plugins tab</p></li>
</ul></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td>Using NPP, open the xml file to be translated</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: left;"><p>In NPP, click on</p>
<ul>
<li><p>Plugins</p></li>
<li><p>XML Tools / XSL Transformation</p></li>
</ul></td>
<td><ul>
<li><p>The XSLT to translate the RI codes is “<strong>RI_Code_to_English.xsl</strong>”</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td><p>A “XSL Transformation Settings” will open</p>
<ul>
<li><p>Browse to and select the desired XSL</p></li>
<li><p>Click on the “Transform” button</p></li>
<li><p>The transformed xml will appear in a new window</p></li>
<li><p>Save the result</p></li>
</ul></td>
<td>Metadata record is now ready for uploading to a metadata server.</td>
</tr>
</tbody>
</table>
