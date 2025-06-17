**Purpose:**

To use jNAP (java metadata authoring tool for North American Profile
responses) for creation of a typical iso-19115 metadata record, and for
inclusion into GeoNetwork. It is assumed that jNAP has been installed on
the computer
([110-04](https://pacificsalmonfoundation-my.sharepoint.com/:w:/g/personal/psalinasruiz_psf_ca/EWbWp7hx93FNnGXgBlV46OQBhwrUztMWwM6eVcd1n0wAWw?e=BgpgNv)).
jNAP is written in java, and should be operating system independent. It
is known to work on Windows, Mac and Linux computers.

There are many different versions of jNAP, but the recommended version
for PSF is 8.00.

Most required metadata entries are highlighted in red and starred.
Hovering the cursor over an item provides a definition of that item.

Upon import into GeoNetwork, the record needs to be completed with a
notional thumbnail and the dataset itself (or hyperlinks).

+----------+----------------------------------------------+---------------------------------------------------------+
| **Step** | **Major Activity**                           | **References, Forms and Details**                       |
+:========:+==============================================+=========================================================+
| **1**    | Open jNAP                                    | The opening screen should display file-edit-help tabs   |
|          |                                              | horizontally, and four or five tabs vertically:         |
|          | - click on the icon                          |                                                         |
|          |                                              | - Metadata Record Information                           |
|          |                                              |                                                         |
|          |                                              | - Identification Information                            |
|          |                                              |                                                         |
|          |                                              | - Distribution Information                              |
|          |                                              |                                                         |
|          |                                              | - Data Quality Information                              |
|          |                                              |                                                         |
|          |                                              | - Reference System Information (optional)               |
+----------+----------------------------------------------+---------------------------------------------------------+
| **2**    | Select the preference (Edit tab, and         | - Expert mode enables the Reference System Information  |
|          | Preference):                                 |   section                                               |
|          |                                              |                                                         |
|          | - English/French language entry              | - Tool Tips enables the hover-for-definition mode, and  |
|          |                                              |   time delay                                            |
|          | - Standard/Expert mode                       |                                                         |
|          |                                              | - Schema location could be important if wish for some   |
|          | - Tool Tips                                  |   different one.                                        |
|          |                                              |                                                         |
|          | - Default jNAP Directory location            |                                                         |
|          |                                              |                                                         |
|          | - Schema location                            |                                                         |
|          |                                              |                                                         |
|          | <!-- -->                                     |                                                         |
|          |                                              |                                                         |
|          | - Then start entering information, starting  |                                                         |
|          |   with "Metadata Record Information"         |                                                         |
+----------+----------------------------------------------+---------------------------------------------------------+
| **3**    | File Identifier                              | - Also called the UUID. The Universally Unique          |
|          |                                              |   Identifier (UUID) is a                                |
|          | - Click on the green '+' to generate a       |   [128-bit](https://en.wikipedia.org/wiki/128-bit)      |
|          |   different one.                             |   [label](https://en.wikipedia.org/wiki/Nominal_number) |
|          |                                              |   used for information in computer systems. It is       |
|          | - If generating a new record from a          |   unique for all practical purposes.                    |
|          |   convenient copy, be certain to create a    |                                                         |
|          |   new UUID.                                  |                                                         |
+----------+----------------------------------------------+---------------------------------------------------------+
| **4**    | Date Stamp                                   | - Automatically generated metadata creation date.       |
+----------+----------------------------------------------+---------------------------------------------------------+
| **5**    | Language -\> English                         | - Language of the metadata record, not the dataset.     |
|          |                                              |   Default is English.                                   |
+----------+----------------------------------------------+---------------------------------------------------------+
| **6**    | Country -\> Canada                           | - Location of the dataset -- Canada or USA. Default is  |
|          |                                              |   Canada.                                               |
+----------+----------------------------------------------+---------------------------------------------------------+
| **7**    | Character Set -\> utf8                       | - The metadata record can be encoded in many different  |
|          |                                              |   versions. The Internet mainly uses UTF-8, and it is   |
|          |                                              |   recommended to use that default.                      |
+----------+----------------------------------------------+---------------------------------------------------------+
| **8**    | Locale -\> blank                             | - There is provision for record entries in multiple     |
|          |                                              |   languages. Recommended default is blank.              |
+----------+----------------------------------------------+---------------------------------------------------------+
| **9**    | Hierarchy Level -\> Dataset                  | - A metadata record can describe many types of objects, |
|          |                                              |   including data, software, models, physical items,     |
|          |                                              |   etc. The normal default is Dataset.                   |
|          |                                              |                                                         |
|          |                                              | - Clicking on the green'+' allows one to add hierarchy  |
|          |                                              |   classifications, the red '-' deletes the selected     |
|          |                                              |   items, and the central 'edit' icon opens the list of  |
|          |                                              |   choices.                                              |
+----------+----------------------------------------------+---------------------------------------------------------+
| **10**   | Contact -. Author                            | A metadata record uses a combination of individuals and |
|          |                                              | roles.                                                  |
|          | - Select the individual from the list, or    |                                                         |
|          |   create a new entry (process 305-20, and    | jNAP maintains a list of individuals to allow entry of  |
|          |   save it when done).                        | details just once, and then makes that information for  |
|          |                                              | future use in this or subsequent metadata records.      |
|          | - Click "OK", and window will close and      |                                                         |
|          |   request a "role"                           | The list is held on the computer but can be shared with |
|          |                                              | others by explicitly transferring the file. Sometimes   |
|          |                                              | it can be convenient to establish the same individual   |
|          |                                              | with less detail, using a similar but                   |
|          |                                              | distinguishingly-different name.                        |
|          |                                              |                                                         |
|          |                                              | It is possible but unusual to have multiple metadata    |
|          |                                              | authors.                                                |
+----------+----------------------------------------------+---------------------------------------------------------+
| **11**   | Add "role"                                   | In a metadata record, an individual can typically have  |
|          |                                              | four or more roles (of a possible 15 or so). The role   |
|          |                                              | will be requested via a right-click request. At this    |
|          |                                              | location in the metadata record, the proper role to     |
|          |                                              | choose is (metadata) author.                            |
+----------+----------------------------------------------+---------------------------------------------------------+
| **12**   | Select "Identification Information" tab.     | - The "Identification Information" is the only          |
|          |                                              |   absolutely required information.                      |
|          | - For the first time entering data for this  |                                                         |
|          |   record, it will offer a choice of two      | - There are nine cascading templates. Start with "Data  |
|          |   templates. Choose the data option          |   Identification"                                       |
|          |   (default).                                 |                                                         |
+----------+----------------------------------------------+---------------------------------------------------------+
| **13**   | Language --select "English"                  | - Required entry, and often initially missed            |
+----------+----------------------------------------------+---------------------------------------------------------+
| **14**   | Character Set -- leave blank                 |                                                         |
+----------+----------------------------------------------+---------------------------------------------------------+
| **15**   | Supplemental Info                            | This is one of the few free text sections, and can be   |
|          |                                              | very useful to provide information not easily entered   |
|          |                                              | elsewhere.                                              |
+----------+----------------------------------------------+---------------------------------------------------------+
| **16**   | Extent:                                      | This should always be completed.                        |
|          |                                              |                                                         |
|          | - Description                                | Description (required) -- text description of the       |
|          |                                              | physical and temporal extent of the dataset.            |
|          | - Temporal Extent                            |                                                         |
|          |                                              | Temporal Extent -- the start and end dates in the       |
|          | - Geographic Extent                          | format yyyy-mm-dd. Actually, the metadata standard      |
|          |                                              | permits other options for temporal extent, such as a    |
|          | - Vertical Extent                            | series of specific dates, or a single date. If this is  |
|          |                                              | required, it will be necessary to edit the resulting    |
|          |                                              | xml record.                                             |
|          |                                              |                                                         |
|          |                                              | Geographic Extent -- this will be used to display the   |
|          |                                              | general area for the dataset, and does not need to be   |
|          |                                              | precise. Select the square bounding box, for which      |
|          |                                              | (N,S,W,E) is required. A bounding polygon is also an    |
|          |                                              | option, especially for the Strait of Georgia. However,  |
|          |                                              | this requires adding a set of coordinates describing    |
|          |                                              | the polygon exterior (and possibly interior).           |
|          |                                              |                                                         |
|          |                                              | Vertical Extent -- this can get very complex and        |
|          |                                              | technical quickly (geodesy), and is seldom used. Don't  |
|          |                                              | complete this one unless absolutely required.           |
+----------+----------------------------------------------+---------------------------------------------------------+
| **17**   | Spatial Representation Type                  | Not generally needed                                    |
+----------+----------------------------------------------+---------------------------------------------------------+
| **18**   | Spatial Resolution                           | Denominator for maps. Not generally needed              |
+----------+----------------------------------------------+---------------------------------------------------------+
| **19**   | Topic Category                               | This is required (should be red, but isn't).            |
|          |                                              |                                                         |
|          |                                              | Often, several topic words are included, such as        |
|          |                                              | oceans, biota, etc.                                     |
|          |                                              |                                                         |
|          |                                              | Hover over the listed words to raise the definitions,   |
|          |                                              | because the definitions of the words may not be what    |
|          |                                              | one expects.                                            |
+----------+----------------------------------------------+---------------------------------------------------------+
| **20**   | Environment Description                      | This is a description of the Informatics Technology     |
|          |                                              | used in processing the dataset, not the geospatial      |
|          |                                              | environment.                                            |
|          |                                              |                                                         |
|          |                                              | It is normally left blank.                              |
+----------+----------------------------------------------+---------------------------------------------------------+
| **21**   | Status                                       | This is required, but not hugely important. Of the      |
|          |                                              | eight choices, the "Completed" term is often chosen.    |
+----------+----------------------------------------------+---------------------------------------------------------+
| **22**   | Select the "Citation" tab                    | There are three sections under this tab that are        |
|          |                                              | normally completed                                      |
+----------+----------------------------------------------+---------------------------------------------------------+
| **23**   | Title -- for the metadata record             | Try to create a metadata title of about ten words. Use  |
|          |                                              |                                                         |
|          |                                              | - 'object' words (e.g. "phytoplankton")                 |
|          |                                              |                                                         |
|          |                                              | - a very brief description of area (e.g. Nanaimo, or    |
|          |                                              |   "Central Strait of Georgia")                          |
|          |                                              |                                                         |
|          |                                              | - a year, or date range                                 |
|          |                                              |                                                         |
|          |                                              | The result might be "Nanoplankton sampled near Tofino   |
|          |                                              | BC, 2017-present"                                       |
|          |                                              |                                                         |
|          |                                              | Usually do not use the title of a research paper, or    |
|          |                                              | describe processes or purpose. That can be done         |
|          |                                              | elsewhere.                                              |
+----------+----------------------------------------------+---------------------------------------------------------+
| **24**   | Date -- for the metadata record              | There are three main date types (there are others).     |
|          |                                              | Dates should not be removed -- only appended.           |
|          |                                              |                                                         |
|          |                                              | - Creation -- date of metadata creation                 |
|          |                                              |                                                         |
|          |                                              | - Publication -- date the record is published. A record |
|          |                                              |   always needs a Publication date.                      |
|          |                                              |                                                         |
|          |                                              | - Revision -- date when the record is revised. There    |
|          |                                              |   can be many revision dates.                           |
+----------+----------------------------------------------+---------------------------------------------------------+
| **25**   | Responsible Party                            | The associated definition via "hover" is misleading.    |
|          |                                              | This is the principal investigator -- often there is    |
|          |                                              | more than one.                                          |
+----------+----------------------------------------------+---------------------------------------------------------+
| **26**   | Presentation Form                            | Can be omitted. If included, as an example: a           |
|          |                                              | spreadsheet format is "Document Digital".               |
+----------+----------------------------------------------+---------------------------------------------------------+
| **27**   | Series                                       | A way of documenting data gathered periodically over    |
|          |                                              | years, with separate metadata. The "Series" links these |
|          |                                              | grammatically (but not technically).                    |
+----------+----------------------------------------------+---------------------------------------------------------+
| **28**   | Other Citation Details                       | Normally blank                                          |
+----------+----------------------------------------------+---------------------------------------------------------+
| **29**   | Select the "Description" tab                 |                                                         |
+----------+----------------------------------------------+---------------------------------------------------------+
| **30**   | Abstract                                     | Required. It describes the "what". It generally does    |
|          |                                              | NOT include the full abstract of a paper, but should    |
|          |                                              | include essential details. Typically less that 100      |
|          |                                              | words.                                                  |
+----------+----------------------------------------------+---------------------------------------------------------+
| **31**   | Purpose                                      | Optional. It describes the "why". Often a research      |
|          |                                              | paper abstract mixes the what and why                   |
+----------+----------------------------------------------+---------------------------------------------------------+
| **32**   | Optionally select the "Resource Constraints" | Optional section. Provides information about            |
|          | tab                                          | constraints which apply to the resources, but good idea |
|          |                                              | to complete.                                            |
+----------+----------------------------------------------+---------------------------------------------------------+
| **33**   | Use Limitations                              | Optional. Free text block. Limitation affecting the     |
|          |                                              | fitness for use o the resource. Example: "not to be     |
|          |                                              | used for navigation"                                    |
+----------+----------------------------------------------+---------------------------------------------------------+
| **34**   | Legal Constraints                            | Access, Use, Other                                      |
+----------+----------------------------------------------+---------------------------------------------------------+
| **35**   | Access                                       | Optional. Drop-down list. To assure the protection of   |
|          |                                              | privacy or intellecetual property.                      |
+----------+----------------------------------------------+---------------------------------------------------------+
| **36**   | Use                                          | Optional. Drop-down list. To assure the protection of   |
|          |                                              | privacy or intellectual property                        |
+----------+----------------------------------------------+---------------------------------------------------------+
| **37**   | Other                                        | Free text. Require if Access or Use =                   |
|          |                                              | "otherRestrictions"                                     |
+----------+----------------------------------------------+---------------------------------------------------------+
| **38**   | Optionally select the "Credit" tab           | Free text block. Good place to acknowledge funding      |
|          |                                              | sources, and team members.                              |
+----------+----------------------------------------------+---------------------------------------------------------+
| **39**   | Graphic Overview                             | Provide a actual or notional graphic suggesting the     |
|          |                                              | dataset content.                                        |
|          |                                              |                                                         |
|          |                                              | Often, this is obtained from Open Sources on the web.   |
|          |                                              | The file size should be less than 300K.                 |
|          |                                              |                                                         |
|          |                                              | Usually this is left blank, because it is easier to add |
|          |                                              | when the record is loaded into GeoNetwork.              |
+----------+----------------------------------------------+---------------------------------------------------------+
| **40**   | Select the "Keywords" tab                    | Two types of keywords are available -- Theme and Place. |
|          |                                              | Words in this section are selected from thesauri that   |
|          |                                              | have formal attribution. One cannot invent keywords.    |
|          |                                              |                                                         |
|          |                                              | It is redundant to add words that already occur in      |
|          |                                              | title or abstract; they are automatically included in   |
|          |                                              | searches and indexed.                                   |
+----------+----------------------------------------------+---------------------------------------------------------+
| **41**   | In the theme section, click on the green +   | Choose keywords from the drop-down lists, at your       |
|          | and sequentially select                      | discretion.                                             |
|          |                                              |                                                         |
|          | - NASA GCMD thesaurus                        | Always choose some words from the GCMD list.            |
|          |                                              |                                                         |
|          | - GoC thesaurus                              | For the GoC thesaurus, many words are in the "Nature    |
|          |                                              | and Environment" section                                |
|          |                                              |                                                         |
|          |                                              | When selecting a number of words, hold the CNTL key     |
|          |                                              | down and select.                                        |
+----------+----------------------------------------------+---------------------------------------------------------+
| **42**   | In the Place section, choose appropriate     |                                                         |
|          | words                                        |                                                         |
+----------+----------------------------------------------+---------------------------------------------------------+
| **43**   | Select the "Contact" tab and select a        | This entry should be red (essential).                   |
|          | contact                                      |                                                         |
|          |                                              | This contact role is the "Point Of Contact"             |
+----------+----------------------------------------------+---------------------------------------------------------+
| **44**   | Aggregation Information                      | Normally blank                                          |
+----------+----------------------------------------------+---------------------------------------------------------+
| **45**   | Select the "Distribution Information"        | Although the whole section is optional according to the |
|          | section                                      | standard, it is always completed by PSF.                |
|          |                                              |                                                         |
|          | - Select "Distributor"                       |                                                         |
|          |                                              |                                                         |
|          |   - add a contact -- usually PSF             |                                                         |
|          |                                              |                                                         |
|          |   - choose "Distributor" as role             |                                                         |
|          |                                              |                                                         |
|          | - Optionally complete "Distribution Order    |                                                         |
|          |   process"                                   |                                                         |
|          |                                              |                                                         |
|          |   - Ordering instructions are usually        |                                                         |
|          |     "Download"                               |                                                         |
|          |                                              |                                                         |
|          |   - Fees are usually "free"                  |                                                         |
+----------+----------------------------------------------+---------------------------------------------------------+
| **46**   | Optionally complete "Distribution Format"    | Version is required. Often "Unknown" is used for CSV,   |
|          |                                              | and "xlsx" for Excel.                                   |
|          | - Name is often "CSV" or "Excel", but should |                                                         |
|          |   match dataset format                       |                                                         |
|          |                                              |                                                         |
|          | - Version is anything reasonable             |                                                         |
|          |                                              |                                                         |
|          | <!-- -->                                     |                                                         |
|          |                                              |                                                         |
|          | - File Decompression Technique is optional   |                                                         |
|          |   and never completed                        |                                                         |
+----------+----------------------------------------------+---------------------------------------------------------+
| **47**   | The "Digital Transfer Options" is not        | It is easier to complete this section in GeoNetwork.    |
|          | usually completed                            |                                                         |
+----------+----------------------------------------------+---------------------------------------------------------+
| **48**   | Optionally select "Data Quality Information" | There are two main components -- Report(s) and Lineage. |
|          |                                              | We do not usually complete Reports.                     |
|          | - Scope Level -- usually "dataset"           |                                                         |
|          |                                              | Experience has shown that Users do not have an          |
|          | - Report - blank                             | automatic high level of trust in data from Non-Profit   |
|          |                                              | sources (like PSF). Documenting this section can        |
|          | - Lineage                                    | provide clarity as to data handling.                    |
|          |                                              |                                                         |
|          |   - Statement -- not completed               |                                                         |
|          |                                              |                                                         |
|          |   - Step                                     |                                                         |
|          |                                              |                                                         |
|          |     - Description                            |                                                         |
|          |                                              |                                                         |
|          |     - Rationale                              |                                                         |
|          |                                              |                                                         |
|          |     - Date                                   |                                                         |
|          |                                              |                                                         |
|          |     - Processor                              |                                                         |
|          |                                              |                                                         |
|          |   - Source                                   |                                                         |
+----------+----------------------------------------------+---------------------------------------------------------+
| **49**   | Select "Reference System Information"        | Optional --only displayed if Edit/Preference is set to  |
|          |                                              | "Expert"                                                |
+----------+----------------------------------------------+---------------------------------------------------------+
| **50**   | Save the record, with ".xml" extension       |                                                         |
+----------+----------------------------------------------+---------------------------------------------------------+
| **51**   | Use Edit/Validate to confirm valid entries   | If errors, remedy the errors                            |
+----------+----------------------------------------------+---------------------------------------------------------+
| **52**   | Open the record with a text or xml editor.   | Add a trailing "/3.2" to fix a schema incompatibility   |
|          | In the (typically) 3^rd^ line, change        |                                                         |
|          |                                              |                                                         |
|          | - xmlns:gml=<http://www.opengis.net/gml>     |                                                         |
|          |                                              |                                                         |
|          | - TO                                         |                                                         |
|          |                                              |                                                         |
|          | - xmlns:gml=<http://www.opengis.net/gml>/3.2 |                                                         |
+----------+----------------------------------------------+---------------------------------------------------------+
| **53**   | Save the record for import into GeoNetwork   |                                                         |
+----------+----------------------------------------------+---------------------------------------------------------+
