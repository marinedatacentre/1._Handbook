---
process_number: 360-09
title: Modifying jNAP output to change RI_ codes
author: Peter
created: 2017-02-26
modified: 2019-09-10
review_period: 3 years
---

**Purpose:**



This documents describes how to alter a metadata record that contains "RI_nnn" codes to more-standard English. This normally occurs with records created by jNAP. This is an optional step.



To do so uses a custom XSLT and can be run in the free text editor Notepad++ (NPP) with the XML Tools plugin installed.



The following process describes the one-time complete installation of NPP and XML Tools. Subsequent transformations only require steps 4 and 5.



| **Step** | **Major Activity** | **References, Forms and Details** |
| -------- | ------------------ | --------------------------------- |
| 1 | Download and install NPP, if necessary. Choose the **32-bit version**, because the 64 bit version does not presently support the plugin manager | - <https://notepad-plus-plus.org/> |
|  |  |  |
|  |  | - The latest downloads include plugin manager |
| 2 | Download and install "XML Tools" using plugin manager |  |
|  |  |  |
|  | - Open NPP |  |
|  |  |  |
|  | - Select Plugins, Show Plugin Manager |  |
|  |  |  |
|  | - Choose and install XML Tools |  |
|  |  |  |
|  | - Accept all prompts and reboots |  |
|  |  |  |
|  | - XML Tools should now be present on the dropdown Plugins tab |  |
| 3 | Using NPP, open the xml file to be translated |  |
| 4 | In NPP, click on | - The XSLT to translate the RI codes is "**RI_Code_to_English.xsl**" |
|  |  |  |
|  | - Plugins |  |
|  |  |  |
|  | - XML Tools / XSL Transformation |  |
| 5 | A "XSL Transformation Settings" will open | Metadata record is now ready for uploading to a metadata server. |
|  |  |  |
|  | - Browse to and select the desired XSL |  |
|  |  |  |
|  | - Click on the "Transform" button |  |
|  |  |  |
|  | - The transformed xml will appear in a new window |  |
|  |  |  |
|  | - Save the result |  |

