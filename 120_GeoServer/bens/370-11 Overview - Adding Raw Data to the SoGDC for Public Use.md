**Purpose:** If a dataset is acquired that is not available as a REST service elsewhere, and has been approved for public distribution through the Strait of Georgia Data Centre by the data source, please follow the procedure below to add the dataset to the Strait of Georgia Data Centre architecture.



| **Step** | **Major Activity** | **References, Forms and Details** |
| -------- | ------------------ | --------------------------------- |
| 1 | Perform any necessary preliminary processing on dataset. | e.g. Convert XLSX to CSV |
|  |  |  |
|  |  | \- see process 370-01 for best practices on data processing |
| 2 | Coordinate with database administration to add dataset to appropriate SoGDC PostgreSQL database. | If database administrator see, for example; |
|  |  |  |
|  |  | -process 370-03 Loading SHAPEFILE data into PostGIS |
|  |  |  |
|  |  | -process 370-05 Loading CSV data into PostGIS |
| 3 | Once the dataset is in the database, create and style a layer in GeoServer. | -see process 370-07 'Creating and Styling a GeoServer layer' |
| 4 | Create or harvest metadata for the record. | -if creating new metadata see process 360-03 |
|  |  |  |
|  |  | -note -- pre-existing metadata can oftentimes be harvested and reused (e.g. from Government of Canada Open Data portal) |
| 5 | Add the metadata file to the SoGDC GeoNetwork. | -see process 360-04 Load metadata packages into GeoNetwork |
| 6 | Add a WFS link within the GeoNetwork record to the GeoServer data layer service created in step 3. | -this WFS layer service will serve as the data download. |
| 7 | Add any additional necessary links within the GeoNetwork record. | e.g. Associated webpages, associated reports. |
| 8 | (optional) Add the layer to the Strait of Georgia Marine Reference Guide (SOG MRG) by working with the SOG MRG administrator. |  |

