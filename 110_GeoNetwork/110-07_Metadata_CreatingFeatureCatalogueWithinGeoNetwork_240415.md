---
process_number: 110-07
title: Metadata_CreatingFeatureCatalogueWithinGeoNetwork_240415
author: Paulina Salinas Ruiz
created: 2024-04-15
modified: 2024-11-26
review_period: 3 years
---

**Purpose:**



This document describes how to create a feature catalogue metadata record within the GeoNetwork server. Any desired GeoNetwork metadata records for the dataset associated with the feature catalogue should already be available. 



| **Step** | **Major Activity** | **References, Forms and Details** |
| -------- | ------------------ | --------------------------------- |
| 1 | > Use a browser to connect to GeoNetwork | - If on the local computer, the address is usually [[http://localhost:8080/geonetwork]{.underline}](http://localhost:8080/geonetwork) |
| 2 | - Provide ID and password | - The ID and PW is required to access administrative functions, and specifically the \<edit\> tab at the bottom of each metadata search result. |
|  |  |  |
|  | - The **Administration** tab should appear next to the **Home** tab | - The default ID/PW is admin/admin |
| 3. | - Click the 'Admin console' button at the top of the screen | - The newly created record should initially be called 'Feature catalogue template in ISO19110' |
|  |  |  |
|  | - Select 'Metadata & templates' | - The feature catalogue metadata record will open in 'Default View' |
|  |  |  |
|  | - Check the box for 'Geographic information -- Methodology for feature cataloguing (iso19110) |  |
|  |  |  |
|  | - Choose to 'Load templates for selected standards' |  |
|  |  |  |
|  | - Access the newly created template through the list of records that appear when the 'Contribute' button is clicked at the top of the screen |  |
|  |  |  |
|  | - Click the blue 'Edit' button to switch to edit mode |  |
| 4 | > Complete the 'Feature Catalogue description' section | > |
|  |  |  |
|  | - Enter as many responses as possible |  |
|  |  |  |
|  | - Fields with small red stars require a response |  |
| 5 | > Complete the 'Catalogue producer' section | > |
| 6 | > Begin work on the 'Elements' section of the catalogue | - 'Definition' is optional |
|  |  |  |
|  | - Fill in 'member name' with the name of the attribute |  |
|  |  |  |
|  | - Assign an attribute definition |  |
|  |  |  |
|  | - For 'gco:lower' use a value of 0 |  |
|  |  |  |
|  | - Fill in 'Type name' with the data type the attribute falls under |  |
|  |  |  |
|  | - Once this information has been completed, if necessary, add a new attribute and repeat step 6 |  |
| 7 | > If codes are used in the dataset you are cataloguing, perform the following | - This step is optional, however If codes are present it is highly desirable |
|  |  |  |
|  | - Save the GeoNetwork feature catalogue record |  |
|  |  |  |
|  | - Switch to 'Full' view by clicking the eye symbol in the top right corner of the page |  |
|  |  |  |
|  | - You should now have the option to add a CodeList to any of the attributes you have previously added to the record |  |
|  |  |  |
|  | - For each attribute that contains codes add a CodeList, filling in 'Label' with the meaning of the code and 'Code' with the abbreviation used |  |
| 8 | > To add definitions for the codes, perform the following | - Despite already being in 'Full' view mode, certain elements of the page will not display unless 'Full' view mode is selected again |
|  |  |  |
|  | - Save the GeoNetwork feature catalogue record | - The step to add code definitions is optional but desirable if codes are present in the catalogue |
|  |  |  |
|  | - Select 'Full' view in the top right corner of the page |  |
|  |  |  |
|  | - You should now have the option to add a definition for the codes you have previously added to the record |  |
| 9 | > Validate the record and fix any errors that are present | - If the error *" is not a valid value for 'integer'. (Element: gco:UnlimitedInteger with parent element: gco: upper)* is present, correct it by performing the following: |
|  |  |  |
|  |  | <!-- --> |
|  |  |  |
|  |  | - Switch to 'XML' view and copy the code into a text editor. |
|  |  |  |
|  |  | - Manually replace all occurrences of *\<gco:UnlimitedInteger/\>* with *\<gco:UnlimitedInteger xsi:nil=\"false\" isInfinite=\"false\"\>1\</gco:UnlimitedInteger\>* |
|  |  |  |
|  |  | - Import the updated XML file to GeoNetwork and validate again |
| 10 | > Save the record | > |
| 11 | > If a GeoNetwork metadata record is present for the dataset associated with the feature catalogue, link the newly created feature catalogue record to it as a resource | > |

