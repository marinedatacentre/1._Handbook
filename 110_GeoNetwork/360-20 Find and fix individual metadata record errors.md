**Purpose:**

How to find and fix metadata errors

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
<th style="text-align: left;"><strong>References, Forms and Details</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1</td>
<td>Sign in to GeoNetwork</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td><p>Search for a desired record with one or more words from the title</p>
<ul>
<li><p>Desired record should be listed</p></li>
</ul></td>
<td style="text-align: left;">Depending on specificity, more than one record may appear</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td><p>Enter ‘edit’ mode. Either</p>
<ul>
<li><p>Using the search results, click on the ‘pencil’ icon at the bottom of the record, OR</p></li>
<li><p>Click on the record title to open the record, then click on the ‘edit’ tab at the top of the record</p></li>
</ul></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td>In metadata edit mode, click on "validate".  When the process continues, you will see a success summary for each of the four main categories.</td>
<td style="text-align: left;"><p>Four main categories</p>
<ul>
<li><p>(Schema validation</p></li>
<li><p>Schematron validation / GeoNetwork recommendations,</p></li>
<li><p>Schematron validation for ISO 19115(19139),</p></li>
<li><p>URL Validation). </p></li>
</ul>
<p>Hopefully, all green or blue.</p></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td><p>If errors, click on the "thumbs-down" (see "orig" png).  The errors will be revealed in red. </p>
<p>If you hover over each error description, the location will appear in black text. </p></td>
<td style="text-align: left;">This location is in xpath, so a number like [2] means the second occurrence of the preceeding path.</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td><p>Switch to xml display and make a copy of the record:</p>
<ul>
<li><p>Highlight the xml</p></li>
<li><p>Copy</p></li>
<li><p>Paste into a text editor</p></li>
<li><p>save</p></li>
</ul></td>
<td style="text-align: left;">Creates a backup copy just in case something goes amiss when editing</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td><p>Move to the troublesome location.</p>
<p>If possible do a compare and contrast with sections that pass validation to determine how to fix.</p>
<ul>
<li><p>Do the correction</p></li>
<li><p>save the record in GeoNetwork</p></li>
<li><p>do another validation</p></li>
</ul></td>
<td style="text-align: left;"><p>Often, need reference to ISO standards to resolve errors.</p>
<ul>
<li><p>19115 Metadata</p></li>
<li><p>19157 Data Quality</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: left;">Repeat step 7 until no errors</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>
