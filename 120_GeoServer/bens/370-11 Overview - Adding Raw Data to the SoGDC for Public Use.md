---
process_number: 370-11
title: Overview - Adding Raw Data to the SoGDC for Public Use
author: Peter
created: 2022-10-27
modified: 2024-02-29
review_period: 3 years
---

**Purpose:** If a dataset is acquired that is not available as a REST service elsewhere, and has been approved for public distribution through the Strait of Georgia Data Centre by the data source, please follow the procedure below to add the dataset to the Strait of Georgia Data Centre architecture.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 50%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Step</strong></th>
<th style="text-align: left;"><strong>Major Activity</strong></th>
<th><strong>References, Forms and Details</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: left;">Perform any necessary preliminary processing on dataset.</td>
<td><p>e.g. Convert XLSX to CSV</p>
<p>- see process 370-01 for best practices on data processing</p></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: left;">Coordinate with database administration to add dataset to appropriate SoGDC PostgreSQL database.</td>
<td><p>If database administrator see, for example;</p>
<p>-process 370-03 Loading SHAPEFILE data into PostGIS</p>
<p>-process 370-05 Loading CSV data into PostGIS</p></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: left;">Once the dataset is in the database, create and style a layer in GeoServer.</td>
<td>-see process 370-07 ‘Creating and Styling a GeoServer layer’</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: left;">Create or harvest metadata for the record.</td>
<td><p>-if creating new metadata see process 360-03</p>
<p>-note – pre-existing metadata can oftentimes be harvested and reused (e.g. from Government of Canada Open Data portal)</p></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: left;">Add the metadata file to the SoGDC GeoNetwork.</td>
<td>-see process 360-04 Load metadata packages into GeoNetwork</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: left;">Add a WFS link within the GeoNetwork record to the GeoServer data layer service created in step 3.</td>
<td>-this WFS layer service will serve as the data download.</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: left;">Add any additional necessary links within the GeoNetwork record.</td>
<td>e.g. Associated webpages, associated reports.</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: left;">(optional) Add the layer to the Strait of Georgia Marine Reference Guide (SOG MRG) by working with the SOG MRG administrator.</td>
<td></td>
</tr>
</tbody>
</table>
