**Purpose:**



This is occasionally required if the resource cannot be removed using the GeoNetwork Administration access. Extreme caution is cautioned, because it is easy to disable GeoNetwork.



| **Step** | **Major Activity** | > **References, Forms and Details** |
| -------- | ------------------ | ----------------------------------- |
| **1** | Obtain the location of the store for the problem metadata record. In the Geonetwork main page, | - e.g. record 02439 |
|  |  |  |
|  | - access the metadata record (search) |  |
|  |  |  |
|  | - download the zip file |  |
|  |  |  |
|  | - open the zip and select "index" |  |
|  |  |  |
|  | - the record number should be available |  |
| **2** | If required, enable a VPN connection to the server. | - For UBC, this means using a connection to myvpn.ubc.ca |
|  |  |  |
|  |  | - This requires a campus-wide logon and password. |
| **3** | Switch to superuser | - Usually the webserver is run by a dedicated user (tomcat or jetty is common), and superuser allows access to all files. |
|  |  |  |
|  | > sudo -i |  |
| **4** | Navigate to the geonetwork store | - For PSF, this is |
|  |  |  |
|  |  | > cd /data/gn_dir/data/metadata_data |
| **5** | And to the desired record group and record | - e.g. |
|  |  |  |
|  |  | group 02400-02499 |
|  |  |  |
|  |  | record 02439 |
| **6** | Open the 'public' folder and perform duties | - this contains the files associated with the metadata |
|  |  |  |
|  |  | - normally this is to delete (Linux 'rm') files |
| **7** | Exit the server |  |
| **8** | In GeoNetwork, check that all references to deleted files have been removed. | - be very careful not to remove valid links |
|  |  |  |
|  | If not, delete links |  |

