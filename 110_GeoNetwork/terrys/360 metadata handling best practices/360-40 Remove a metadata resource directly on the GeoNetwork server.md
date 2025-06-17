**Purpose:**

This is occasionally required if the resource cannot be removed using
the GeoNetwork Administration access. Extreme caution is cautioned,
because it is easy to disable GeoNetwork.

+----------+----------------------------------+-----------------------------------+
| **Step** | **Major Activity**               | > **References, Forms and         |
|          |                                  | > Details**                       |
+:========:+==================================+===================================+
| **1**    | Obtain the location of the store | - e.g. record 02439               |
|          | for the problem metadata record. |                                   |
|          | In the Geonetwork main page,     |                                   |
|          |                                  |                                   |
|          | - access the metadata record     |                                   |
|          |   (search)                       |                                   |
|          |                                  |                                   |
|          | - download the zip file          |                                   |
|          |                                  |                                   |
|          | - open the zip and select        |                                   |
|          |   "index"                        |                                   |
|          |                                  |                                   |
|          | - the record number should be    |                                   |
|          |   available                      |                                   |
+----------+----------------------------------+-----------------------------------+
| **2**    | If required, enable a VPN        | - For UBC, this means using a     |
|          | connection to the server.        |   connection to myvpn.ubc.ca      |
|          |                                  |                                   |
|          |                                  | - This requires a campus-wide     |
|          |                                  |   logon and password.             |
+----------+----------------------------------+-----------------------------------+
| **3**    | Switch to superuser              | - Usually the webserver is run by |
|          |                                  |   a dedicated user (tomcat or     |
|          | > sudo -i                        |   jetty is common), and superuser |
|          |                                  |   allows access to all files.     |
+----------+----------------------------------+-----------------------------------+
| **4**    | Navigate to the geonetwork store | - For PSF, this is                |
|          |                                  |                                   |
|          |                                  | > cd                              |
|          |                                  | > /data/gn_dir/data/metadata_data |
+----------+----------------------------------+-----------------------------------+
| **5**    | And to the desired record group  | - e.g.                            |
|          | and record                       |                                   |
|          |                                  | group 02400-02499                 |
|          |                                  |                                   |
|          |                                  | record 02439                      |
+----------+----------------------------------+-----------------------------------+
| **6**    | Open the 'public' folder and     | - this contains the files         |
|          | perform duties                   |   associated with the metadata    |
|          |                                  |                                   |
|          |                                  | - normally this is to delete      |
|          |                                  |   (Linux 'rm') files              |
+----------+----------------------------------+-----------------------------------+
| **7**    | Exit the server                  |                                   |
+----------+----------------------------------+-----------------------------------+
| **8**    | In GeoNetwork, check that all    | - be very careful not to remove   |
|          | references to deleted files have |   valid links                     |
|          | been removed.                    |                                   |
|          |                                  |                                   |
|          | If not, delete links             |                                   |
+----------+----------------------------------+-----------------------------------+
