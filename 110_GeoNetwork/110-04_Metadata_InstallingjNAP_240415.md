---
process_number: 110-04
title: Metadata_InstallingjNAP_240415
author: Paulina Salinas Ruiz
created: 2024-04-15
modified: 2024-11-26
review_period: 3 years
---

**Purpose:**



This document describes one way to create a metadata record to be later stored on the GeoNetwork server, using the java application jNAP. Creating metadata outside GeoNetwork is useful if many metadata records of a somewhat similar type or series are to be created, because all such records with their associated data files, links and thumbnails can be loaded in one later step.



Some of the jNAP features are:



- Machine independent (java application)



- Graphical interface



- Bilingual -- English, French



- Creates metadata compliant with the North American profile (but using gml, not gml/3.2)



- Extensive help appears during hover over field label



- Built-in thesauri for theme (GCMD v6 and Gov of Canada keywords) and place (Canada locations)



- Automatically builds a contact list (contact.xml) that can be moved to other application installations, reducing manual data entry



- Performs metadata record generation for dataset or service applications



- Graphics overview links and data online links can be added within jNAP.



- Data Quality Reports and Lineage implemented



Other possible editing tools are listed in the document "Common Metadata Editing Tools" (X).



| **Step** | **Major Activity** | **References, Forms and Details** |
| -------- | ------------------ | --------------------------------- |
| 1 | Download jNAP |  |
|  |  |  |
|  | - freely available from: |  |
|  |  |  |
|  | > <ftp://ftp.dfo-mpo.gc.ca/BIOWebmaster/jMW2/> |  |
|  |  |  |
|  | Choose the plain NAP version (no extension, so most current) so as to be operating system independent |  |
| 2 | If a repeat installation, save the previous contact file: | - The jNAP is often installed in folder c:\\DFO-MPO |
|  |  |  |
|  | Copy the Contact.xml file outside of the jNAP installation folder | - Move the Contact.xml file to preserve previous entries |
| 3 | Unzip jNAP to desired folder location | - jNAP application will be at |
|  |  |  |
|  |  | \<desired location\>\\jNAP |
| 4 | Copy (Overwrite) Contact.xml in jNAP folder with saved version | - Right-click the item, and then click Create shortcut |
|  |  |  |
|  |  | - Browse to the location of jMW_NAP.jar |
|  |  |  |
|  |  | - Change name to that desired |
|  |  |  |
|  |  | - Right-click created icon and select properties |
|  |  |  |
|  |  | - Change "start in" to a convenient location where you will be editing metadata |
|  |  |  |
|  |  | Browse and change icon to jNAP icon. The jNAP icon is available from ......... |
| 5 | Create a shortcut icon | - Right-click the item, and then click Create shortcut |
|  |  |  |
|  |  | - Browse to the location of jMW_NAP.jar |
|  |  |  |
|  |  | - Change name to that desired |
|  |  |  |
|  |  | - Right-click created icon and select properties |
|  |  |  |
|  |  | - Change "start in" to a convenient location where you will be editing metadata |
|  |  |  |
|  |  | - Browse and change icon to jNAP icon. The jNAP icon is available from ......... |
| 6 | Move the icon to where you wish |  |
|  |  |  |
|  | - Start menu/Desktop |  |
| 7 | Validate that jNAP opens when icon chosen, and start location correct | - If not valid, fix the errors/omissions |

