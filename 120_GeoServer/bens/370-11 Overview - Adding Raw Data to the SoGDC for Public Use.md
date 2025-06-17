**Purpose:** If a dataset is acquired that is not available as a REST
service elsewhere, and has been approved for public distribution through
the Strait of Georgia Data Centre by the data source, please follow the
procedure below to add the dataset to the Strait of Georgia Data Centre
architecture.

+-----------+-----------------------------------+---------------------+
| **Step**  | **Major Activity**                | **References, Forms |
|           |                                   | and Details**       |
+:=========:+:==================================+=====================+
| 1         | Perform any necessary preliminary | e.g. Convert XLSX   |
|           | processing on dataset.            | to CSV              |
|           |                                   |                     |
|           |                                   | \- see process      |
|           |                                   | 370-01 for best     |
|           |                                   | practices on data   |
|           |                                   | processing          |
+-----------+-----------------------------------+---------------------+
| 2         | Coordinate with database          | If database         |
|           | administration to add dataset to  | administrator see,  |
|           | appropriate SoGDC PostgreSQL      | for example;        |
|           | database.                         |                     |
|           |                                   | -process 370-03     |
|           |                                   | Loading SHAPEFILE   |
|           |                                   | data into PostGIS   |
|           |                                   |                     |
|           |                                   | -process 370-05     |
|           |                                   | Loading CSV data    |
|           |                                   | into PostGIS        |
+-----------+-----------------------------------+---------------------+
| 3         | Once the dataset is in the        | -see process 370-07 |
|           | database, create and style a      | 'Creating and       |
|           | layer in GeoServer.               | Styling a GeoServer |
|           |                                   | layer'              |
+-----------+-----------------------------------+---------------------+
| 4         | Create or harvest metadata for    | -if creating new    |
|           | the record.                       | metadata see        |
|           |                                   | process 360-03      |
|           |                                   |                     |
|           |                                   | -note --            |
|           |                                   | pre-existing        |
|           |                                   | metadata can        |
|           |                                   | oftentimes be       |
|           |                                   | harvested and       |
|           |                                   | reused (e.g. from   |
|           |                                   | Government of       |
|           |                                   | Canada Open Data    |
|           |                                   | portal)             |
+-----------+-----------------------------------+---------------------+
| 5         | Add the metadata file to the      | -see process 360-04 |
|           | SoGDC GeoNetwork.                 | Load metadata       |
|           |                                   | packages into       |
|           |                                   | GeoNetwork          |
+-----------+-----------------------------------+---------------------+
| 6         | Add a WFS link within the         | -this WFS layer     |
|           | GeoNetwork record to the          | service will serve  |
|           | GeoServer data layer service      | as the data         |
|           | created in step 3.                | download.           |
+-----------+-----------------------------------+---------------------+
| 7         | Add any additional necessary      | e.g. Associated     |
|           | links within the GeoNetwork       | webpages,           |
|           | record.                           | associated reports. |
+-----------+-----------------------------------+---------------------+
| 8         | (optional) Add the layer to the   |                     |
|           | Strait of Georgia Marine          |                     |
|           | Reference Guide (SOG MRG) by      |                     |
|           | working with the SOG MRG          |                     |
|           | administrator.                    |                     |
+-----------+-----------------------------------+---------------------+
