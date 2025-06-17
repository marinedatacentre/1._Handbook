**Purpose:**

This document describes how to load metadata into a GeoNetwork server.

The general description is thoroughly described in the GeoNetwork User's
Manual (search web for the latest version: "GeoNetwork User Manual").
This process is to provide an abbreviated step-by-step.

+----------+-------------------------------------+------------------------+
| **Step** | **Major Activity**                  | **References, Forms    |
|          |                                     | and Details**          |
+==========+=====================================+========================+
| 1        | Use a browser to connect to         | - Path must be known   |
|          | GeoNetwork                          |                        |
+----------+-------------------------------------+------------------------+
| 2        | - Provide ID and password           | - The ID and PW is     |
|          |                                     |   required to access   |
|          | - The **Administration** tab should |   administrative       |
|          |   appear next to the **Home** tab   |   functions            |
+----------+-------------------------------------+------------------------+
| 3        | - Click the **Administration** tab  | - The metadata insert  |
|          |                                     |   section allows       |
|          | - Click on the **Metadata insert**  |   insertion of         |
|          |   tab                               |                        |
|          |                                     |   - an individual      |
|          |                                     |     metadata record in |
|          |                                     |     xml format, or     |
|          |                                     |                        |
|          |                                     |   - one or more        |
|          |                                     |     metadata records   |
|          |                                     |     (optionally plus   |
|          |                                     |     thumbnails and     |
|          |                                     |     data files) in a   |
|          |                                     |     batch load.        |
|          |                                     |                        |
|          |                                     | - This latter format   |
|          |                                     |   is called **metadata |
|          |                                     |   exchange format**    |
|          |                                     |   (mef), and is a      |
|          |                                     |   structured zip file. |
|          |                                     |   This is a            |
|          |                                     |   recommended input    |
|          |                                     |   format.              |
+----------+-------------------------------------+------------------------+
| 4        | - Select the mode:                  |                        |
|          |                                     |                        |
|          |   - File or                         |                        |
|          |                                     |                        |
|          |   - Copy/Paste                      |                        |
+----------+-------------------------------------+------------------------+
| 5        | - If File, select                   |                        |
|          |                                     |                        |
|          |   - Single File, or                 |                        |
|          |                                     |                        |
|          |   - MEF                             |                        |
|          |                                     |                        |
|          | - Browse local storage for desired  |                        |
|          |   file, and select                  |                        |
+----------+-------------------------------------+------------------------+
| 6        | - Select desired Import action:     | 1.  Normal situation   |
|          |                                     |                        |
|          |   1.  No action on import           | 2.  Used if replacing  |
|          |                                     |     metadata after     |
|          |   2.  Overwrite metadata with same  |     some changes       |
|          |       UUID                          |                        |
|          |                                     | 3.  Used if for some   |
|          |   3.  Generate UUID for inserted    |     reason there is an |
|          |       metadata                      |     existing record    |
|          |                                     |     with the same UUID |
|          |                                     |     and a different    |
|          |                                     |     metadata record is |
|          |                                     |     desired to be      |
|          |                                     |     loaded. This can   |
|          |                                     |     happen if a        |
|          |                                     |     metadata record is |
|          |                                     |     being cloned, then |
|          |                                     |     slightly modified. |
|          |                                     |     This is not a      |
|          |                                     |     preferred action,  |
|          |                                     |     but can occur.     |
+----------+-------------------------------------+------------------------+
| 7        | - If a single metadata record is    | 1.  Normally **none**  |
|          |   being added, then select          |                        |
|          |                                     | 2.  Useful to          |
|          |   1.  Stylesheet                    |     **check** to       |
|          |                                     |     thoroughly         |
|          |   2.  Validate                      |     determine metadata |
|          |                                     |     validity. The      |
|          |   3.  kind                          |     server applies     |
|          |                                     |     schematron checks  |
|          |   4.  group                         |     that are in        |
|          |                                     |     addition to the    |
|          |   5.  category                      |     schema validation. |
|          |                                     |                        |
|          | - if MEF, these choices are already | 3.  Normally           |
|          |   determined in the MEF info.xml    |     **metadata**       |
|          |                                     |                        |
|          |                                     | 4.  As desired, from   |
|          |                                     |     the choices        |
|          |                                     |     previously         |
|          |                                     |     established        |
|          |                                     |                        |
|          |                                     | 5.  Normally           |
|          |                                     |     **dataset**,       |
|          |                                     |     although many      |
|          |                                     |     choices are        |
|          |                                     |     possible           |
+----------+-------------------------------------+------------------------+
| 8        | - **Insert** record                 | - Often this can take  |
|          |                                     |   seconds to many      |
|          |                                     |   minutes. You should  |
|          |                                     |   look for a subtle    |
|          |                                     |   "beeble" indicator   |
|          |                                     |   indicating the       |
|          |                                     |   application is       |
|          |                                     |   actively working.    |
+----------+-------------------------------------+------------------------+
| 9        | - If error, change                  |                        |
|          |                                     |                        |
|          |   - metadata record, or             |                        |
|          |                                     |                        |
|          |   - change the choices              |                        |
|          |                                     |                        |
|          | - re-enter                          |                        |
+----------+-------------------------------------+------------------------+
