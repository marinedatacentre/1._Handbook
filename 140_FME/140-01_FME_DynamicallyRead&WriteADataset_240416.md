**Purpose:**

This document describes how to read a generic dataset and write it out
without prior knowledge of the schema. In particular, an example
situation where esri rest layer services are read from a spreadhseet
list and out put to PostgreSQL database tables is documented in this
process.

Note: A dataset can not be dynamically read into an FME workspace and
undergo automated data transformation operations, due to it's attributes
being unexposed. Dynamic read / write functionalities only can be
automated.

+-----------+-----------------------------------+-----------------------------------------+
| **Step**  | **Major Activity**                | **References, Forms and Details**       |
+:=========:+===================================+=========================================+
| 1         | Create or acquire a dynamic       | In this case, a spreadsheet with a list |
|           | source dataset.                   | of esri REST layer service URLS was     |
|           |                                   | created.                                |
+-----------+-----------------------------------+-----------------------------------------+
| 2         | Open FME Desktop and create a new | A license is required to operate.       |
|           | workspace.                        |                                         |
|           |                                   | \- Software download -                  |
|           |                                   | https://www.safe.com/support/downloads/ |
+-----------+-----------------------------------+-----------------------------------------+
| 3         | Add a reader to the workspace for | Note -- there are likely other          |
|           | the spreadsheet containing the    | alternatives for dynamically reading    |
|           | URL list.                         | sources. Search the FME Community       |
|           |                                   | forums for additional insight on        |
|           |                                   | 'Dynamic Readers'.                      |
+-----------+-----------------------------------+-----------------------------------------+
| 4         | Add a FeatureReader transformer   | Note -- parameters may need to be       |
|           | to the workspace, connect the CSV | altered depending on input feature type |
|           | reader output port to the         | and desired output.                     |
|           | FeatureReader Initiator port, and |                                         |
|           | set parameters of the             |                                         |
|           | FeatureReader. Parameters were    |                                         |
|           | set as:                           |                                         |
|           |                                   |                                         |
|           | - Format: Esri-JSON               |                                         |
|           |                                   |                                         |
|           | - Dataset: \[url column name\]    |                                         |
|           |                                   |                                         |
|           | - Features to Read: Schema and    |                                         |
|           |   Data Features                   |                                         |
|           |                                   |                                         |
|           | - Output Ports: Single Output     |                                         |
|           |   Port                            |                                         |
|           |                                   |                                         |
|           | - Attribute and Geometry          |                                         |
|           |   Handling:                       |                                         |
|           |                                   |                                         |
|           |   - Merge Initiator and Result    |                                         |
|           |                                   |                                         |
|           |   - Use Result                    |                                         |
|           |                                   |                                         |
|           |   - No                            |                                         |
|           |                                   |                                         |
|           |   - Use Result                    |                                         |
+-----------+-----------------------------------+-----------------------------------------+
| 5a        | Add a PostGIS Writer to the       |                                         |
|           | workspace. Connect to the         |                                         |
|           | database where you wish for the   |                                         |
|           | table to be created or updated.   |                                         |
+-----------+-----------------------------------+-----------------------------------------+
| 5b        | Under the User Attributes tab of  |                                         |
|           | the Feature Type window, set      |                                         |
|           | Attribute Definition to           |                                         |
|           | 'Dynamic'.                        |                                         |
|           |                                   |                                         |
|           | When setting the Feature Type     |                                         |
|           | Parameters of the writer, the     |                                         |
|           | following were used.              |                                         |
|           |                                   |                                         |
|           | - Table Name: \[layer name column |                                         |
|           |   from list\]                     |                                         |
|           |                                   |                                         |
|           | - Schema Sources: "Schema From    |                                         |
|           |   Schema Feature"                 |                                         |
|           |                                   |                                         |
|           | - Schema Definition Name:         |                                         |
|           |   fme_feature_type                |                                         |
|           |                                   |                                         |
|           | - Feature Operation: Insert       |                                         |
|           |                                   |                                         |
|           | - Table Handling: Drop and Create |                                         |
+-----------+-----------------------------------+-----------------------------------------+
| 6         | Run the workflow & ensure it      | Note -- there is the possibility to     |
|           | operates without error.           | automate this workflow by uploading it  |
|           |                                   | to FME Server.                          |
+-----------+-----------------------------------+-----------------------------------------+
| 7         | Check that the table has been     | Further validation can be completed by  |
|           | created as desired using PSQL     | viewing the database table in a desktop |
|           | from the command line of PGadmin4 | GIS.                                    |
|           | GUI.                              |                                         |
+-----------+-----------------------------------+-----------------------------------------+
