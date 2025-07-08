---
process_number: 110-01
title: Metadata_GeneratingMetadataRecordsJNAP_240410
author: Paulina Salinas Ruiz
created: 2024-04-10
modified: 2024-11-26
review_period: 3 years
---

**Purpose:**

To use jNAP (java metadata authoring tool for North American Profile responses) for creation of a typical iso-19115 metadata record, and for inclusion into GeoNetwork. It is assumed that jNAP has been installed on the computer ([110-04](https://pacificsalmonfoundation-my.sharepoint.com/:w:/g/personal/psalinasruiz_psf_ca/EWbWp7hx93FNnGXgBlV46OQBhwrUztMWwM6eVcd1n0wAWw?e=BgpgNv)). jNAP is written in java, and should be operating system independent. It is known to work on Windows, Mac and Linux computers.

There are many different versions of jNAP, but the recommended version for PSF is 8.00.

Most required metadata entries are highlighted in red and starred. Hovering the cursor over an item provides a definition of that item.

Upon import into GeoNetwork, the record needs to be completed with a notional thumbnail and the dataset itself (or hyperlinks).

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 41%" />
<col style="width: 47%" />
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
<td style="text-align: center;"><strong>1</strong></td>
<td><p>Open jNAP</p>
<ul>
<li><p>click on the icon</p></li>
</ul></td>
<td><p>The opening screen should display file-edit-help tabs horizontally, and four or five tabs vertically:</p>
<ul>
<li><p>Metadata Record Information</p></li>
<li><p>Identification Information</p></li>
<li><p>Distribution Information</p></li>
<li><p>Data Quality Information</p></li>
<li><p>Reference System Information (optional)</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>2</strong></td>
<td><p>Select the preference (Edit tab, and Preference):</p>
<ul>
<li><p>English/French language entry</p></li>
<li><p>Standard/Expert mode</p></li>
<li><p>Tool Tips</p></li>
<li><p>Default jNAP Directory location</p></li>
<li><p>Schema location</p></li>
</ul>
<ul>
<li><p>Then start entering information, starting with “Metadata Record Information”</p></li>
</ul></td>
<td><ul>
<li><p>Expert mode enables the Reference System Information section</p></li>
<li><p>Tool Tips enables the hover-for-definition mode, and time delay</p></li>
<li><p>Schema location could be important if wish for some different one.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>3</strong></td>
<td><p>File Identifier</p>
<ul>
<li><p>Click on the green ‘+’ to generate a different one.</p></li>
<li><p>If generating a new record from a convenient copy, be certain to create a new UUID.</p></li>
</ul></td>
<td><ul>
<li><p>Also called the UUID. The Universally Unique Identifier (UUID) is a <a href="https://en.wikipedia.org/wiki/128-bit">128-bit</a> <a href="https://en.wikipedia.org/wiki/Nominal_number">label</a> used for information in computer systems. It is unique for all practical purposes.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>4</strong></td>
<td>Date Stamp</td>
<td><ul>
<li><p>Automatically generated metadata creation date.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>5</strong></td>
<td>Language -&gt; English</td>
<td><ul>
<li><p>Language of the metadata record, not the dataset. Default is English.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>6</strong></td>
<td>Country -&gt; Canada</td>
<td><ul>
<li><p>Location of the dataset – Canada or USA. Default is Canada.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>7</strong></td>
<td>Character Set -&gt; utf8</td>
<td><ul>
<li><p>The metadata record can be encoded in many different versions. The Internet mainly uses UTF-8, and it is recommended to use that default.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>8</strong></td>
<td>Locale -&gt; blank</td>
<td><ul>
<li><p>There is provision for record entries in multiple languages. Recommended default is blank.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>9</strong></td>
<td>Hierarchy Level -&gt; Dataset</td>
<td><ul>
<li><p>A metadata record can describe many types of objects, including data, software, models, physical items, etc. The normal default is Dataset.</p></li>
<li><p>Clicking on the green’+’ allows one to add hierarchy classifications, the red ‘-‘ deletes the selected items, and the central ‘edit’ icon opens the list of choices.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>10</strong></td>
<td><p>Contact -. Author</p>
<ul>
<li><p>Select the individual from the list, or create a new entry (process 305-20, and save it when done).</p></li>
<li><p>Click “OK”, and window will close and request a “role”</p></li>
</ul></td>
<td><p>A metadata record uses a combination of individuals and roles.</p>
<p>jNAP maintains a list of individuals to allow entry of details just once, and then makes that information for future use in this or subsequent metadata records.</p>
<p>The list is held on the computer but can be shared with others by explicitly transferring the file. Sometimes it can be convenient to establish the same individual with less detail, using a similar but distinguishingly-different name.</p>
<p>It is possible but unusual to have multiple metadata authors.</p></td>
</tr>
<tr>
<td style="text-align: center;"><strong>11</strong></td>
<td>Add “role”</td>
<td>In a metadata record, an individual can typically have four or more roles (of a possible 15 or so). The role will be requested via a right-click request. At this location in the metadata record, the proper role to choose is (metadata) author.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>12</strong></td>
<td><p>Select “Identification Information” tab.</p>
<ul>
<li><p>For the first time entering data for this record, it will offer a choice of two templates. Choose the data option (default).</p></li>
</ul></td>
<td><ul>
<li><p>The “Identification Information” is the only absolutely required information.</p></li>
<li><p>There are nine cascading templates. Start with “Data Identification”</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>13</strong></td>
<td>Language –select “English”</td>
<td><ul>
<li><p>Required entry, and often initially missed</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>14</strong></td>
<td>Character Set – leave blank</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;"><strong>15</strong></td>
<td>Supplemental Info</td>
<td>This is one of the few free text sections, and can be very useful to provide information not easily entered elsewhere.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>16</strong></td>
<td><p>Extent:</p>
<ul>
<li><p>Description</p></li>
<li><p>Temporal Extent</p></li>
<li><p>Geographic Extent</p></li>
<li><p>Vertical Extent</p></li>
</ul></td>
<td><p>This should always be completed.</p>
<p>Description (required) – text description of the physical and temporal extent of the dataset.</p>
<p>Temporal Extent – the start and end dates in the format yyyy-mm-dd. Actually, the metadata standard permits other options for temporal extent, such as a series of specific dates, or a single date. If this is required, it will be necessary to edit the resulting xml record.</p>
<p>Geographic Extent – this will be used to display the general area for the dataset, and does not need to be precise. Select the square bounding box, for which (N,S,W,E) is required. A bounding polygon is also an option, especially for the Strait of Georgia. However, this requires adding a set of coordinates describing the polygon exterior (and possibly interior).</p>
<p>Vertical Extent – this can get very complex and technical quickly (geodesy), and is seldom used. Don’t complete this one unless absolutely required.</p></td>
</tr>
<tr>
<td style="text-align: center;"><strong>17</strong></td>
<td>Spatial Representation Type</td>
<td>Not generally needed</td>
</tr>
<tr>
<td style="text-align: center;"><strong>18</strong></td>
<td>Spatial Resolution</td>
<td>Denominator for maps. Not generally needed</td>
</tr>
<tr>
<td style="text-align: center;"><strong>19</strong></td>
<td>Topic Category</td>
<td><p>This is required (should be red, but isn’t).</p>
<p>Often, several topic words are included, such as oceans, biota, etc.</p>
<p>Hover over the listed words to raise the definitions, because the definitions of the words may not be what one expects.</p></td>
</tr>
<tr>
<td style="text-align: center;"><strong>20</strong></td>
<td>Environment Description</td>
<td><p>This is a description of the Informatics Technology used in processing the dataset, not the geospatial environment.</p>
<p>It is normally left blank.</p></td>
</tr>
<tr>
<td style="text-align: center;"><strong>21</strong></td>
<td>Status</td>
<td>This is required, but not hugely important. Of the eight choices, the “Completed” term is often chosen.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>22</strong></td>
<td>Select the “Citation” tab</td>
<td>There are three sections under this tab that are normally completed</td>
</tr>
<tr>
<td style="text-align: center;"><strong>23</strong></td>
<td>Title – for the metadata record</td>
<td><p>Try to create a metadata title of about ten words. Use</p>
<ul>
<li><p>‘object’ words (e.g. “phytoplankton”)</p></li>
<li><p>a very brief description of area (e.g. Nanaimo, or “Central Strait of Georgia”)</p></li>
<li><p>a year, or date range</p></li>
</ul>
<p>The result might be “Nanoplankton sampled near Tofino BC, 2017-present”</p>
<p>Usually do not use the title of a research paper, or describe processes or purpose. That can be done elsewhere.</p></td>
</tr>
<tr>
<td style="text-align: center;"><strong>24</strong></td>
<td>Date – for the metadata record</td>
<td><p>There are three main date types (there are others). Dates should not be removed – only appended.</p>
<ul>
<li><p>Creation – date of metadata creation</p></li>
<li><p>Publication – date the record is published. A record always needs a Publication date.</p></li>
<li><p>Revision – date when the record is revised. There can be many revision dates.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><strong>25</strong></td>
<td>Responsible Party</td>
<td>The associated definition via “hover” is misleading. This is the principal investigator – often there is more than one.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>26</strong></td>
<td>Presentation Form</td>
<td>Can be omitted. If included, as an example: a spreadsheet format is “Document Digital”.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>27</strong></td>
<td>Series</td>
<td>A way of documenting data gathered periodically over years, with separate metadata. The “Series” links these grammatically (but not technically).</td>
</tr>
<tr>
<td style="text-align: center;"><strong>28</strong></td>
<td>Other Citation Details</td>
<td>Normally blank</td>
</tr>
<tr>
<td style="text-align: center;"><strong>29</strong></td>
<td>Select the “Description” tab</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;"><strong>30</strong></td>
<td>Abstract</td>
<td>Required. It describes the “what”. It generally does NOT include the full abstract of a paper, but should include essential details. Typically less that 100 words.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>31</strong></td>
<td>Purpose</td>
<td>Optional. It describes the “why”. Often a research paper abstract mixes the what and why</td>
</tr>
<tr>
<td style="text-align: center;"><strong>32</strong></td>
<td>Optionally select the “Resource Constraints” tab</td>
<td>Optional section. Provides information about constraints which apply to the resources, but good idea to complete.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>33</strong></td>
<td>Use Limitations</td>
<td>Optional. Free text block. Limitation affecting the fitness for use o the resource. Example: “not to be used for navigation”</td>
</tr>
<tr>
<td style="text-align: center;"><strong>34</strong></td>
<td>Legal Constraints</td>
<td>Access, Use, Other</td>
</tr>
<tr>
<td style="text-align: center;"><strong>35</strong></td>
<td>Access</td>
<td>Optional. Drop-down list. To assure the protection of privacy or intellecetual property.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>36</strong></td>
<td>Use</td>
<td>Optional. Drop-down list. To assure the protection of privacy or intellectual property</td>
</tr>
<tr>
<td style="text-align: center;"><strong>37</strong></td>
<td>Other</td>
<td>Free text. Require if Access or Use = “otherRestrictions”</td>
</tr>
<tr>
<td style="text-align: center;"><strong>38</strong></td>
<td>Optionally select the “Credit” tab</td>
<td>Free text block. Good place to acknowledge funding sources, and team members.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>39</strong></td>
<td>Graphic Overview</td>
<td><p>Provide a actual or notional graphic suggesting the dataset content.</p>
<p>Often, this is obtained from Open Sources on the web. The file size should be less than 300K.</p>
<p>Usually this is left blank, because it is easier to add when the record is loaded into GeoNetwork.</p></td>
</tr>
<tr>
<td style="text-align: center;"><strong>40</strong></td>
<td>Select the “Keywords” tab</td>
<td><p>Two types of keywords are available – Theme and Place. Words in this section are selected from thesauri that have formal attribution. One cannot invent keywords.</p>
<p>It is redundant to add words that already occur in title or abstract; they are automatically included in searches and indexed.</p></td>
</tr>
<tr>
<td style="text-align: center;"><strong>41</strong></td>
<td><p>In the theme section, click on the green + and sequentially select</p>
<ul>
<li><p>NASA GCMD thesaurus</p></li>
<li><p>GoC thesaurus</p></li>
</ul></td>
<td><p>Choose keywords from the drop-down lists, at your discretion.</p>
<p>Always choose some words from the GCMD list.</p>
<p>For the GoC thesaurus, many words are in the “Nature and Environment” section</p>
<p>When selecting a number of words, hold the CNTL key down and select.</p></td>
</tr>
<tr>
<td style="text-align: center;"><strong>42</strong></td>
<td>In the Place section, choose appropriate words</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;"><strong>43</strong></td>
<td>Select the “Contact” tab and select a contact</td>
<td><p>This entry should be red (essential).</p>
<p>This contact role is the “Point Of Contact”</p></td>
</tr>
<tr>
<td style="text-align: center;"><strong>44</strong></td>
<td>Aggregation Information</td>
<td>Normally blank</td>
</tr>
<tr>
<td style="text-align: center;"><strong>45</strong></td>
<td><p>Select the “Distribution Information” section</p>
<ul>
<li><p>Select “Distributor”</p>
<ul>
<li><p>add a contact – usually PSF</p></li>
<li><p>choose “Distributor” as role</p></li>
</ul></li>
<li><p>Optionally complete “Distribution Order process”</p>
<ul>
<li><p>Ordering instructions are usually “Download”</p></li>
<li><p>Fees are usually “free”</p></li>
</ul></li>
</ul></td>
<td>Although the whole section is optional according to the standard, it is always completed by PSF.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>46</strong></td>
<td><p>Optionally complete “Distribution Format”</p>
<ul>
<li><p>Name is often “CSV” or “Excel”, but should match dataset format</p></li>
<li><p>Version is anything reasonable</p></li>
</ul>
<ul>
<li><p>File Decompression Technique is optional and never completed</p></li>
</ul></td>
<td>Version is required. Often “Unknown” is used for CSV, and “xlsx” for Excel.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>47</strong></td>
<td>The “Digital Transfer Options” is not usually completed</td>
<td>It is easier to complete this section in GeoNetwork.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>48</strong></td>
<td><p>Optionally select “Data Quality Information”</p>
<ul>
<li><p>Scope Level – usually “dataset”</p></li>
<li><p>Report - blank</p></li>
<li><p>Lineage</p>
<ul>
<li><p>Statement – not completed</p></li>
<li><p>Step</p>
<ul>
<li><p>Description</p></li>
<li><p>Rationale</p></li>
<li><p>Date</p></li>
<li><p>Processor</p></li>
</ul></li>
<li><p>Source</p></li>
</ul></li>
</ul></td>
<td><p>There are two main components – Report(s) and Lineage. We do not usually complete Reports.</p>
<p>Experience has shown that Users do not have an automatic high level of trust in data from Non-Profit sources (like PSF). Documenting this section can provide clarity as to data handling.</p></td>
</tr>
<tr>
<td style="text-align: center;"><strong>49</strong></td>
<td>Select “Reference System Information”</td>
<td>Optional –only displayed if Edit/Preference is set to “Expert”</td>
</tr>
<tr>
<td style="text-align: center;"><strong>50</strong></td>
<td>Save the record, with “.xml” extension</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;"><strong>51</strong></td>
<td>Use Edit/Validate to confirm valid entries</td>
<td>If errors, remedy the errors</td>
</tr>
<tr>
<td style="text-align: center;"><strong>52</strong></td>
<td><p>Open the record with a text or xml editor. In the (typically) 3<sup>rd</sup> line, change</p>
<ul>
<li><p>xmlns:gml=<a href="http://www.opengis.net/gml">http://www.opengis.net/gml</a></p></li>
<li><p>TO</p></li>
<li><p>xmlns:gml=<a href="http://www.opengis.net/gml">http://www.opengis.net/gml</a>/3.2</p></li>
</ul></td>
<td>Add a trailing “/3.2” to fix a schema incompatibility</td>
</tr>
<tr>
<td style="text-align: center;"><strong>53</strong></td>
<td>Save the record for import into GeoNetwork</td>
<td></td>
</tr>
</tbody>
</table>
