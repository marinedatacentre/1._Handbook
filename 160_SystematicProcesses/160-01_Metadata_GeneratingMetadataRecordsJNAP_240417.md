**Purpose:**

This document serves as a guide to creating metadata records using jNAP.
This approach is useful when creating one or a few records at a time, as
it has a much more user-friendly interface than other metadata generator
software.

Also, creating metadata outside GeoNetwork is convenient if many
metadata records of similar type (or series) are created because all
such records with their associated data files, links and thumbnails can
be loaded in one later step (xx). 

+-----------+------------------+------------------------------------------------------------+
| **Step**  | **Major          | **References, Forms and Details**                          |
|           | Activity**       |                                                            |
+:=========:+==================+============================================================+
| 1         | > Install jNAP   | - jNAP is a metadata software that implements the North    |
|           | > if not already |   American Profile and follows the ISO standard very       |
|           | > installed. To  |   closely.                                                 |
|           | > do so, refer   |                                                            |
|           | > to process     |                                                            |
|           | > 110-40.        |                                                            |
+-----------+------------------+------------------------------------------------------------+
| 2         | > Generate new   | - Do so by clicking the green "+" sign at the top-right    |
|           | > File           |   corner of the file identifier text box.                  |
|           | > Identifier     |                                                            |
+-----------+------------------+------------------------------------------------------------+
| 3         | > Populate       | - Date Stamp: automatically assigned                       |
|           | > Metadata       |                                                            |
|           | > Record         | - Language: usually English although it could be French    |
|           | > Information    |                                                            |
|           | > mandatory      | - Character Set: utf8 (default)                            |
|           | >                |                                                            |
|           | > fields (red)   | - Hierarchy Level: type of data the metadata represents.   |
|           |                  |   Can select more than one.                                |
|           |                  |                                                            |
|           |                  | - Contact: make sure to include name, organization,        |
|           |                  |   position, and email when possible.                       |
+-----------+------------------+------------------------------------------------------------+
| 4         | Populate         | - Language will usually be English. There are datasets     |
|           | Identification   |   that contain more than one language though and it is     |
|           | Information      |   important to include that information.                   |
|           |  mandatory       |                                                            |
|           | fields (red)-    | - Status: if unsure, inquire with data owner.              |
|           | Data             |                                                            |
|           | Identification   | - Maintenance: default to "Quarterly" unless otherwise     |
|           |                  |   specified.                                               |
+-----------+------------------+------------------------------------------------------------+
| 5         | > Populate       | - Date: make sure to inquire and include all known dates   |
|           | > Identification |                                                            |
|           | > Information    | - Responsible Party: make sure to include name,            |
|           | >  mandatory     |   organization, position, and email when possible.         |
|           | > fields (red)-  |                                                            |
|           | > Citation       |                                                            |
+-----------+------------------+------------------------------------------------------------+
| 6         | > Populate       | - Include short abstract describing information included   |
|           | > Identification |   in abstract. At least 3 sentences long. Refer to owner   |
|           | > Information    |   of data if unsure.                                       |
|           | >  mandatory     |                                                            |
|           | > fields (red)-  |                                                            |
|           | > Description    |                                                            |
+-----------+------------------+------------------------------------------------------------+
| 7         | > Validate       | - Choose "Edit- Validate_xml"                              |
|           |                  |                                                            |
|           |                  | - If not valid, address the errors/omissions               |
+-----------+------------------+------------------------------------------------------------+
| 8         | > Save to avoid  | - Save as xml file with the naming convention:             |
|           | > from losing    |   "YearfromDateStamp_GeographicRegion_Topic_SourceofData", |
|           | > your work      |   for example "2014_Clayoquot_ChinookSalmon_DFO"           |
+-----------+------------------+------------------------------------------------------------+
