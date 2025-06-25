---
process_number: 330-10
title: Finding and fixing metadata record errors
author: Peter
created: 2019-12-12
modified: 2020-06-03
review_period: 3 years
---

**Purpose:**



How to find and fix metadata errors



| **Step** | **Major Activity** | **References, Forms and Details** |
| -------- | ------------------ | --------------------------------- |
| 1 | Sign in to GeoNetwork |  |
| 2 | Search for a desired record with one or more words from the title | Depending on specificity, more than one record may appear |
|  |  |  |
|  | - Desired record should be listed |  |
| 3 | Enter 'edit' mode. Either |  |
|  |  |  |
|  | - Using the search results, click on the 'pencil' icon at the bottom of the record, OR |  |
|  |  |  |
|  | - Click on the record title to open the record, then click on the 'edit' tab at the top of the record |  |
| 4 | In metadata edit mode, click on \"validate\".  When the process continues, you will see a success summary for each of the four main categories. | Four main categories |
|  |  |  |
|  |  | - (Schema validation |
|  |  |  |
|  |  | - Schematron validation / GeoNetwork recommendations, |
|  |  |  |
|  |  | - Schematron validation for ISO 19115(19139), |
|  |  |  |
|  |  | - URL Validation). |
|  |  |  |
|  |  | Hopefully, all green or blue. |
| 5 | If errors, click on the \"thumbs-down\" (see \"orig\" png).  The errors will be revealed in red. | This location is in xpath, so a number like \[2\] means the second occurrence of the preceeding path. |
|  |  |  |
|  | If you hover over each error description, the location will appear in black text. |  |
| 6 | Switch to xml display and make a copy of the record: | Creates a backup copy just in case something goes amiss when editing |
|  |  |  |
|  | - Highlight the xml |  |
|  |  |  |
|  | - Copy |  |
|  |  |  |
|  | - Paste into a text editor |  |
|  |  |  |
|  | - save |  |
| 7 | Move to the troublesome location. | Often, need reference to ISO standards to resolve errors. |
|  |  |  |
|  | If possible do a compare and contrast with sections that pass validation to determine how to fix. | - 19115 Metadata |
|  |  |  |
|  | - Do the correction | - 19157 Data Quality |
|  |  |  |
|  | - save the record in GeoNetwork |  |
|  |  |  |
|  | - do another validation |  |
| 8 | Repeat step 7 until no errors |  |

