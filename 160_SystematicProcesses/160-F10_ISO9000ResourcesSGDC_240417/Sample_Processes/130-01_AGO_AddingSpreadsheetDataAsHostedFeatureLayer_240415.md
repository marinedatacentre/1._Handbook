**Purpose:**

To allow for the addition of spatial data (i.e. includes latitude and
longitude fields) available through a spreadsheet to ArcGIS Online, in
order for the use of the data in interactive maps.

Note - this process only works for spreadsheets that you wish to convert
to a Vector Point format layer (i.e. non-compatible with other Vector
formats such as Polygon or Polyline, or Raster format).

+-----------+-----------------------------------+---------------------+
| **Step**  | **Major Activity**                | **References, Forms |
|           |                                   | and Details**       |
+:=========:+===================================+=====================+
| 1         | Perform any necessary steps to    | Recommended         |
|           | prepare a spreadsheet document:   | format - *A         |
|           |                                   | comma-separated     |
|           | - Ensure the data is formatted as | values (CSV) file   |
|           |   desired.                        | is a delimited text |
|           |                                   | file that uses a    |
|           | - Ensure the sheet has no         | comma to separate   |
|           |   extraneous. information (e.g.   | values. To convert  |
|           |   title at top of spreadsheet).   | an Excel            |
|           |   It should contain only data     | Spreadsheet (.xlsx) |
|           |   listed in rows and columns,     | to CSV format, open |
|           |   with each column marked with a  | the sheet of        |
|           |   unique column header that       | interest within     |
|           |   contains no spaces.             | Excel and Save As   |
|           |                                   | Comma-delimited     |
|           |                                   | (.csv).*            |
+-----------+-----------------------------------+---------------------+
| 2         | Log into your assigned ArcGIS     | A Username &        |
|           | Online (AGO) organizational       | Password are        |
|           | account.                          | required            |
+-----------+-----------------------------------+---------------------+
| 3         | Once signed in, access the        |                     |
|           | Content section by clicking       |                     |
|           | **Content** in the AGO header     |                     |
|           | bar.                              |                     |
+-----------+-----------------------------------+---------------------+
| 4         | Select **New Item** on the left   |                     |
|           | side of the Content section page. |                     |
|           | A pop-up should appear with the   |                     |
|           | option to **Drag and Drop** your  |                     |
|           | file of interest onto the screen. |                     |
|           | Perform this action by finding    |                     |
|           | the CSV document on your computer |                     |
|           | and dragging and dropping the     |                     |
|           | file into AGO. Alternatively, the |                     |
|           | file can be uploaded using a      |                     |
|           | number of options (e.g. from      |                     |
|           | **Your device, Google Drive**,    |                     |
|           | **Dropbox**, **OneDrive).**       |                     |
+-----------+-----------------------------------+---------------------+
| 5         | Go through the following steps in | \- Data **Types**   |
|           | the pop-up once the file has been | include String,     |
|           | selected:                         | Date, Integer, etc. |
|           |                                   |                     |
|           | - Select **Add CSV and create a   | \- If you are       |
|           |   hosted feature layer**          | unsure of the       |
|           |                                   | coordinate fields,  |
|           | - Unselect any fields you do not  | first experiment    |
|           |   want to include and change the  | adding the CSV in a |
|           |   **Display name** and data       | GIS (e.g. QGIS)     |
|           |   **Type** as needed.             |                     |
|           |                                   | \- There should be  |
|           | - Ensure the correct fields are   | pre-defined         |
|           |   selected for **Latitude** and   | categories for you  |
|           |   **Longitude**                   | to choose from.     |
|           |                                   |                     |
|           | - Enter contextual information    |                     |
|           |   for the CSV such as **Title**,  |                     |
|           |   **Categories**, **Tags,** and   |                     |
|           |   **Summary**. This information   |                     |
|           |   should be clear, concise, and   |                     |
|           |   understandable by all users.    |                     |
+-----------+-----------------------------------+---------------------+
| 6         | The CSV should now appear in the  | Hosted Feature      |
|           | **Content** page within your      | Layers support      |
|           | organizational ArcGIS Online      | vector feature      |
|           | account as a **Feature Layer      | querying,           |
|           | (Hosted)**.                       | visualization, and  |
|           |                                   | editing. Hosted     |
|           |                                   | feature layers are  |
|           |                                   | most appropriate    |
|           |                                   | for visualizing     |
|           |                                   | data on top of your |
|           |                                   | basemaps.           |
+-----------+-----------------------------------+---------------------+
| 7         | Click the layer name in the list  |                     |
|           | of layers on the Content page to  |                     |
|           | open the details page for the CSV |                     |
|           | item.                             |                     |
|           |                                   |                     |
|           | Fill in the following sections    |                     |
|           | with the necessary information:   |                     |
|           |                                   |                     |
|           | - **Description** (good practice  |                     |
|           |   to include all details you      |                     |
|           |   think are of importance to the  |                     |
|           |   public)                         |                     |
|           |                                   |                     |
|           | - **Terms of Use** (e.g.          |                     |
|           |   Intellectual Property Rights)   |                     |
|           |                                   |                     |
|           | - **Credits** (e.g. Pacific       |                     |
|           |   Salmon Foundation -- Citizen    |                     |
|           |   Science Program)                |                     |
+-----------+-----------------------------------+---------------------+
| 8         | When you are ready for this layer |                     |
|           | to be shared with the public,     |                     |
|           | change the **Share** settings of  |                     |
|           | the CSV Hosted Feature layer from |                     |
|           | **Owner** to **Everyone           |                     |
|           | (public)**. This will be a        |                     |
|           | necessary step if displaying the  |                     |
|           | layer in a public-facing map.     |                     |
+-----------+-----------------------------------+---------------------+
| 9         | Bonus Step: If you want to set    | This can save time  |
|           | default symbology and pop-up      | if using the layer  |
|           | configuration for the layer, this | repeatedly with the |
|           | can be done from the              | same symbology.     |
|           | **Visualization** tab of the      |                     |
|           | item's details page.              |                     |
+-----------+-----------------------------------+---------------------+
| 10        | The CSV Hosted Feature Layer is   |                     |
|           | now ready for use in an ArcGIS    |                     |
|           | Online Interactive Map.           |                     |
+-----------+-----------------------------------+---------------------+
