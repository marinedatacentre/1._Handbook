---
process_number: 350-01
title: Adding thumbnail links to metadata
author: Peter
created: 2015-02-24
modified: 2024-04-10
review_period: 3 years
---

**Purpose:**



This document describes how to add thumbnail links to metadata for use in GeoServer. Often one would use this approach when doing batches of metadata. For single metadata entries, the included GeoNetwork authoring tool or an external authoring tool (like jNAP) would be simpler to use.



The process uses the Kernow graphical user interface. A Kernow licence (about 10 UK pounds) needs to be purchased after exceeding the 100 execution evaluation limit.



To perform batch operations, a rigid folder structure is needed. The expected seven-folder structure is:



Drive E:\-- all_metadata_work



\|\--specific_metadata_folder



\|\-- 'metadata' folder



\| \|- \<unique_name\>.xml (1 of more metadata files)



\|\-- 'metaGraphics' folder



\| \|- \<unique_name\>.xml (contents to be overwritten)



\|\-- 'metaGraphicsData' folder



\| \|- \<unique_name\>.xml (contents to be overwritten)



\|\--'thumbnails' folder



\| \|- \<unique_name\>.png (0 or more pairs of graphics files)



\| \|- \<unique_name\>\_s.png



\|\--'data' folder



\| \|- \<unique_name\>.zip (0 or more data files)



\| \|- \<unique_name\>.csv (0 or more)



\| \|- \<unique_name\>.pdf (0 or more)



\| \|- \<unique_name\>.xlsx (0 or more)



\|\-- 'tmp' folder



\|\-- 'mef' folder



| **Step** | **Major Activity** | **References, Forms and Details** |
| -------- | ------------------ | --------------------------------- |
| 1 | Install KernowForSaxon, or something equivalent to run XSLTs. http://kernowforsaxon.sourceforge.net/ | - Kernow is a Graphical User Interface for XSLTs |
|  |  |  |
|  |  | - The trial version is free, and permits 100 executions. After that, one needs to purchase a basic licence. |
| 2 | Point the input at the folder containing the metadata file(s) | - The application can process one or many metadata records in batch mode |
|  |  |  |
|  |  | - Metadata names need to have a \<unique_name\>.xml |
|  |  |  |
|  |  | - Input folder is usually named "metadata" |
| 3 | Point at the XSLT to add the graphics links | - Graphics Xslt is in 305-F02 |
| 4 | Point the output at the result folder | - Output metadata will be augmented with links to the graphics files |
|  |  |  |
|  | - the graphics XSLT [expects]{.underline} the ../thumbnails folder for the graphics files to contain \<unique_name\>.png and \<unique_name\>\_s.png | - The Output folder could be named "metaGraphics" |
|  |  |  |
|  | - the XSLT adds the linking code |  |
| 5 | Check the resulting metadata is valid |  |
|  |  |  |
|  | - Choose the validation tab in Kernow |  |
|  |  |  |
|  | - Point the input folder at the translated folder (e.g. metaGraphics) |  |
|  |  |  |
|  | - Point at the NAP schema (often located at C:\\DFO-MPO\\jMW2 NAP\\schema\\schema.xsd) |  |
| 6 | If the results are not valid, examine the records with a xml editor and fix | A free xml editor that can be downloaded is notepad++ |

