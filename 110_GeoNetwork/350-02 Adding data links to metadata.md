**Purpose:**

This document describes how to add data links to metadata for use in GeoServer. Often one would use this approach when doing batches of metadata. For single metadata entries, the included GeoNetwork authoring tool or an external authoring tool (like jNAP) would be simpler to use.

The process uses the Kernow graphical user interface. A Kernow licence (about 10 UK pounds) needs to be purchased after 100 executions. It also requires the use of an included java file, and this \*may\* require a Saxon-PE licence (untested with the free Kernow and Saxon versions).

To perform batch operations, a rigid folder structure is needed. The expected seven-folder structure is:

Drive E:-- all_metadata_work

\|--specific_metadata_folder

\|-- ‘metadata’ folder

\| \|- \<unique_name\>.xml (1 of more metadata files)

\|-- ‘metaGraphics’ folder

\| \|- \<unique_name\>.xml (contents to be overwritten)

\|-- ‘metaGraphicsData’ folder

\| \|- \<unique_name\>.xml (contents to be overwritten)

\|--‘thumbnails’ folder

\| \|- \<unique_name\>.png (0 or more pairs of graphics files)

\| \|- \<unique_name\>\_s.png

\|--‘data’ folder

\| \|- \<unique_name\>.zip (0 or more data files)

\| \|- \<unique_name\>.csv (0 or more)

\| \|- \<unique_name\>.pdf (0 or more)

\| \|- \<unique_name\>.xlsx (0 or more)

\|-- ‘tmp’ folder

\|-- ‘mef’ folder

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 50%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Step</strong></th>
<th style="text-align: left;"><strong>Major Activity</strong></th>
<th><strong>References, Forms and Details</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: left;">Install KernowForSaxon, or something equivalent to run XSLTs</td>
<td><ul>
<li><p>Kernow is a Graphical User Interface for XSLTs</p></li>
<li><p>The trial version is free, and permits 100 executions. After that, one needs to purchase a basic licence.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: left;"><p>Point the input at the folder containing the metadata file(s)</p>
<ul>
<li><p>The application can process one or many metadata records in batch mode</p></li>
<li><p>Metadata names need to have a &lt;unique_name&gt;.xml</p></li>
<li><p>Input folder is usually “metaGraphics”</p></li>
</ul></td>
<td><ul>
<li><p>This process is normally run after the graphics links have been added (305-06).</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: left;"><p>The Xslt will need some customization for each end-user application</p>
<ul>
<li><p>Drive, path</p></li>
</ul></td>
<td><ul>
<li><p>A sample Xslt is in 305-F03</p></li>
<li><p>This *may* require Saxon-PE, at a cost of about 50 UK pounds</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: left;"><p>Point at the XSLT to add the data links:</p>
<ul>
<li><p>Data as flat files (one or more)</p></li>
<li><p>External website</p></li>
<li><p>Web map server files</p></li>
</ul></td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: left;"><p>Point the output at the result folder</p>
<ul>
<li><p>Output folder is usually “metaGraphicsData”</p></li>
<li><p>the data XSLT <u>expects</u> the ../data folder for the data files to contain zero or more files with extension zip, csv, xlsx or pdf.</p></li>
</ul>
<ul>
<li><p>the XSLT adds the linking code</p></li>
</ul></td>
<td><ul>
<li><p>Output metadata will be augmented with links to any and all data files</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: left;"><p>Check the resulting metadata is valid</p>
<ul>
<li><p>Choose the validation tab in Kernow</p></li>
<li><p>Point the input folder at the translated folder (e.g. metaGraphics)</p></li>
</ul>
<p>Point at the NAP schema (often located at C:\DFO-MPO\jMW2 NAP\schema\schema.xsd)</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: left;">If the results are not valid, examine the records with a xml editor and fix</td>
<td style="text-align: left;">A free xml editor that can be downloaded is notepad++</td>
</tr>
</tbody>
</table>
