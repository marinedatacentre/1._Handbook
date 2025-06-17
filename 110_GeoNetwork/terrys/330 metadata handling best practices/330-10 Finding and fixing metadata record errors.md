**Purpose:**

How to find and fix metadata errors

+----------+---------------------------------+----------------------------+
| **Step** | **Major Activity**              | **References, Forms and    |
|          |                                 | Details**                  |
+:========:+=================================+:===========================+
| 1        | Sign in to GeoNetwork           |                            |
+----------+---------------------------------+----------------------------+
| 2        | Search for a desired record     | Depending on specificity,  |
|          | with one or more words from the | more than one record may   |
|          | title                           | appear                     |
|          |                                 |                            |
|          | - Desired record should be      |                            |
|          |   listed                        |                            |
+----------+---------------------------------+----------------------------+
| 3        | Enter 'edit' mode. Either       |                            |
|          |                                 |                            |
|          | - Using the search results,     |                            |
|          |   click on the 'pencil' icon at |                            |
|          |   the bottom of the record, OR  |                            |
|          |                                 |                            |
|          | - Click on the record title to  |                            |
|          |   open the record, then click   |                            |
|          |   on the 'edit' tab at the top  |                            |
|          |   of the record                 |                            |
+----------+---------------------------------+----------------------------+
| 4        | In metadata edit mode, click on | Four main categories       |
|          | \"validate\".  When the process |                            |
|          | continues, you will see a       | - (Schema validation       |
|          | success summary for each of the |                            |
|          | four main categories.           | - Schematron validation /  |
|          |                                 |   GeoNetwork               |
|          |                                 |   recommendations,         |
|          |                                 |                            |
|          |                                 | - Schematron validation    |
|          |                                 |   for ISO 19115(19139),    |
|          |                                 |                            |
|          |                                 | - URL Validation).         |
|          |                                 |                            |
|          |                                 | Hopefully, all green or    |
|          |                                 | blue.                      |
+----------+---------------------------------+----------------------------+
| 5        | If errors, click on the         | This location is in xpath, |
|          | \"thumbs-down\" (see \"orig\"   | so a number like \[2\]     |
|          | png).  The errors will be       | means the second           |
|          | revealed in red.                | occurrence of the          |
|          |                                 | preceeding path.           |
|          | If you hover over each error    |                            |
|          | description, the location will  |                            |
|          | appear in black text.           |                            |
+----------+---------------------------------+----------------------------+
| 6        | Switch to xml display and make  | Creates a backup copy just |
|          | a copy of the record:           | in case something goes     |
|          |                                 | amiss when editing         |
|          | - Highlight the xml             |                            |
|          |                                 |                            |
|          | - Copy                          |                            |
|          |                                 |                            |
|          | - Paste into a text editor      |                            |
|          |                                 |                            |
|          | - save                          |                            |
+----------+---------------------------------+----------------------------+
| 7        | Move to the troublesome         | Often, need reference to   |
|          | location.                       | ISO standards to resolve   |
|          |                                 | errors.                    |
|          | If possible do a compare and    |                            |
|          | contrast with sections that     | - 19115 Metadata           |
|          | pass validation to determine    |                            |
|          | how to fix.                     | - 19157 Data Quality       |
|          |                                 |                            |
|          | - Do the correction             |                            |
|          |                                 |                            |
|          | - save the record in GeoNetwork |                            |
|          |                                 |                            |
|          | - do another validation         |                            |
+----------+---------------------------------+----------------------------+
| 8        | Repeat step 7 until no errors   |                            |
+----------+---------------------------------+----------------------------+
